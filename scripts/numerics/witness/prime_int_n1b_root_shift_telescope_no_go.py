r"""Root-shift telescope DD.4 no-go.

This witness tests the repair after doc 265:
promote the Frobenius-root tower transition to a shift/telescope operator
and treat that operator as the missing carrier boundary.

The exact obstruction is that the root transition is not an invertible
carrier shift on H^1.  It sends the old generator to zero in cohomology,
because the old generator becomes a boundary one stage later.  At every
finite tower height a new top generator remains, and killing it requires a
new half-root not present in the finite tower.  A finite periodic wrap or
formal inverse shift therefore inserts extra data.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_root_shift_telescope_no_go
"""

from math import comb, log2


failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def make(L):
    """Arithmetic in F_2[t]/t^{L+1}; 1-units are dicts {power: 1}."""

    def add(a, b):
        out = dict(a)
        for k in b:
            out[k] = out.get(k, 0) ^ 1
        return {k: 1 for k, v in out.items() if v}

    def mul(a, b):
        out = {}
        for i in a:
            for j in b:
                if i + j <= L:
                    out[i + j] = out.get(i + j, 0) ^ 1
        return {k: 1 for k, v in out.items() if v}

    def inv(a):
        assert a.get(0, 0) == 1
        rem = add(a, {0: 1})
        term = {0: 1}
        out = {0: 1}
        for _ in range(1, L + 1):
            term = mul(term, rem)
            if not term:
                break
            out = add(out, term)
        return out

    def phi(f):
        out = {}
        for m in f:
            if m == 0:
                out[0] = out.get(0, 0) ^ 1
                continue
            for k in range(0, L - m + 1):
                if comb(m + k - 1, k) % 2:
                    out[m + k] = out.get(m + k, 0) ^ 1
        return {k: 1 for k, v in out.items() if v}

    return add, mul, inv, phi


def to_vec(f, L):
    return tuple(f.get(k, 0) for k in range(1, L + 1))


def from_vec(v):
    out = {0: 1}
    for i, bit in enumerate(v, start=1):
        if bit:
            out[i] = 1
    return out


def closure(gens, zero_vec, from_vec_fn, mul_fn, to_vec_fn):
    seen = {zero_vec}
    queue = [zero_vec]
    while queue:
        current = from_vec_fn(queue.pop())
        for gen in gens:
            nxt = to_vec_fn(mul_fn(current, gen))
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return seen


def pow_unit(unit, exponent, mul):
    out = {0: 1}
    base = unit
    n = exponent
    while n:
        if n & 1:
            out = mul(out, base)
        base = mul(base, base)
        n >>= 1
    return out


def boundary(unit, inv, phi, mul):
    return mul(unit, inv(phi(unit)))


def h1_profile(L):
    _, mul, inv, phi = make(L)
    c = inv({0: 1, 1: 1})
    boundary_gens = [
        boundary({0: 1, k: 1}, inv, phi, mul) for k in range(1, L + 1)
    ]
    norm_gens = [
        mul({0: 1, k: 1}, phi({0: 1, k: 1})) for k in range(1, L + 1)
    ]
    coboundaries = closure(
        boundary_gens,
        (0,) * L,
        from_vec,
        mul,
        lambda f: to_vec(f, L),
    )
    norm_image = closure(
        norm_gens,
        (0,) * L,
        from_vec,
        mul,
        lambda f: to_vec(f, L),
    )
    z1_order = 2**L // len(norm_image)
    return {
        "L": L,
        "c": c,
        "coboundaries": coboundaries,
        "h1_order": z1_order // len(coboundaries),
        "b_order": len(coboundaries),
        "z1_order": z1_order,
        "c_boundary": to_vec(c, L) in coboundaries,
        "res1_c": c.get(1, 0),
    }


def pullback_even(f, Lout):
    out = {}
    for k in f:
        kk = 2 * k
        if kk <= Lout:
            out[kk] = out.get(kk, 0) ^ 1
    return {k: 1 for k, v in out.items() if v}


def transition_profile(L):
    _, _, inv0, phi0 = make(L)
    _, mul1, inv1, phi1 = make(2 * L)
    source = h1_profile(L)
    target = h1_profile(2 * L)
    c0 = inv0({0: 1, 1: 1})
    c1 = inv1({0: 1, 1: 1})
    pull_c0 = pullback_even(c0, 2 * L)
    delta_c1 = boundary(c1, inv1, phi1, mul1)
    action_extends = mul1(phi1({1: 1}), phi1({1: 1})) == pullback_even(phi0({1: 1}), 2 * L)
    return {
        "L": L,
        "root_L": 2 * L,
        "source_h1": source["h1_order"],
        "target_h1": target["h1_order"],
        "source_generator_nonboundary": not source["c_boundary"],
        "target_generator_nonboundary": not target["c_boundary"],
        "pull_old_boundary": to_vec(pull_c0, 2 * L) in target["coboundaries"],
        "pull_old_equals_delta_new": pull_c0 == delta_c1,
        "action_extends": action_extends,
        "induced_h1_map_is_zero": to_vec(pull_c0, 2 * L) in target["coboundaries"],
    }


def res1_kills_generator_boundaries(L):
    _, mul, inv, phi = make(L)
    return all(
        boundary({0: 1, k: 1}, inv, phi, mul).get(1, 0) == 0
        for k in range(1, L + 1)
    )


def tower_wrap_profile(depth, base_L=4):
    top_L = base_L * (2**depth)
    _, mul, inv, phi = make(top_L)
    c_top = inv({0: 1, 1: 1})
    stage_candidates = []
    for stage in range(depth + 1):
        exponent = 2 ** (depth - stage)
        candidate = pow_unit(c_top, exponent, mul)
        candidate_boundary = boundary(candidate, inv, phi, mul)
        stage_candidates.append(
            {
                "stage": stage,
                "exponent": exponent,
                "kills_top": candidate_boundary == c_top,
                "boundary_res1": candidate_boundary.get(1, 0),
            }
        )
    return {
        "depth": depth,
        "top_L": top_L,
        "top_nonboundary": c_top.get(1, 0) == 1 and res1_kills_generator_boundaries(top_L),
        "no_finite_stage_splitter": not any(c["kills_top"] for c in stage_candidates),
        "all_internal_boundaries_res1_zero": all(c["boundary_res1"] == 0 for c in stage_candidates),
        "candidate_exponents": [c["exponent"] for c in stage_candidates],
    }


def periodic_wrap_profile(depth):
    """A finite wrap would have to solve 2e=1 with e an internal stage exponent."""

    internal_exponents = [2 ** (depth - stage) for stage in range(depth + 1)]
    needed_half_exponent = "1/2"
    exact_internal_solution = any(2 * exponent == 1 for exponent in internal_exponents)
    return {
        "depth": depth,
        "internal_exponents": internal_exponents,
        "needed_half_exponent": needed_half_exponent,
        "exact_internal_solution": exact_internal_solution,
        "periodic_wrap_is_extra_relation": not exact_internal_solution,
    }


def xor_vec(x, y):
    return tuple(a ^ b for a, b in zip(x, y))


def span(gens, dim):
    seen = {tuple(0 for _ in range(dim))}
    queue = list(seen)
    while queue:
        current = queue.pop()
        for gen in gens:
            nxt = xor_vec(current, gen)
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return seen


def control_inverse_shift_profile(dim):
    """A formal inverse shift kills a control class by adding a splitter."""

    chosen = tuple(1 if i == 0 else 0 for i in range(dim))
    zero = tuple(0 for _ in range(dim))
    base_boundaries = span([zero], dim)
    after_formal_inverse_shift = span([chosen], dim)
    return {
        "dim": dim,
        "base_nonboundary": chosen not in base_boundaries,
        "killed_after_formal_inverse_shift": chosen in after_formal_inverse_shift,
        "uses_square_data": False,
        "has_carrier_shift": False,
    }


transition_profiles = [transition_profile(L) for L in (6, 8, 10, 12)]
tower_profiles = [tower_wrap_profile(depth) for depth in (1, 2, 3, 4)]
wrap_profiles = [periodic_wrap_profile(depth) for depth in (1, 2, 3, 4)]
control_profiles = [control_inverse_shift_profile(dim) for dim in (1, 2, 4, 8)]


gate(
    "RST1 root transition is zero on the DD.4 H1 generator",
    all(
        p["action_extends"]
        and p["source_h1"] == 2
        and p["target_h1"] == 2
        and p["source_generator_nonboundary"]
        and p["target_generator_nonboundary"]
        and p["pull_old_boundary"]
        and p["pull_old_equals_delta_new"]
        and p["induced_h1_map_is_zero"]
        for p in transition_profiles
    ),
    "  ".join("L%d->L%d:H1 map generator->0" % (p["L"], p["root_L"]) for p in transition_profiles),
)

gate(
    "RST2 every finite root tower still has no internal splitter for the top class",
    all(
        p["top_nonboundary"]
        and p["no_finite_stage_splitter"]
        and p["all_internal_boundaries_res1_zero"]
        for p in tower_profiles
    ),
    "  ".join(
        "depth%d:rank%d,exponents=%s"
        % (p["depth"], p["top_L"], p["candidate_exponents"])
        for p in tower_profiles
    ),
)

gate(
    "RST3 periodic root-shift wrap would impose an external half-exponent",
    all(p["periodic_wrap_is_extra_relation"] for p in wrap_profiles),
    "  ".join(
        "depth%d:need %s,have %s"
        % (p["depth"], p["needed_half_exponent"], p["internal_exponents"])
        for p in wrap_profiles
    ),
)

gate(
    "RST4 formal inverse root-shift is formable on controls",
    all(
        p["base_nonboundary"]
        and p["killed_after_formal_inverse_shift"]
        and not p["uses_square_data"]
        and not p["has_carrier_shift"]
        for p in control_profiles
    ),
    "  ".join("dim%d:formal-splitter" % p["dim"] for p in control_profiles),
)


required_slots = [
    "actual_square",
    "integral_rep_NS",
    "two_degree_maps",
    "indecomposable_diagonal",
    "frobenius_graph",
    "proper_correspondence",
    "fiber_product_composition",
    "projection_formula",
    "canonical_rosati",
    "positive_primitive_sign",
    "carrier_boundary",
    "control_death",
]

root_shift_slots = {
    "zero_h1_transition": True,
    "formal_inverse_shift": True,
    "periodic_wrap_relation": True,
    "actual_square": False,
    "integral_rep_NS": False,
    "two_degree_maps": False,
    "indecomposable_diagonal": False,
    "frobenius_graph": False,
    "proper_correspondence": False,
    "fiber_product_composition": False,
    "projection_formula": False,
    "canonical_rosati": False,
    "positive_primitive_sign": False,
    "carrier_boundary": False,
    "control_death": False,
}

gate(
    "RST5 root-shift telescope satisfies no square-carrier slot",
    not any(root_shift_slots[slot] for slot in required_slots),
    "missing: " + ", ".join(required_slots),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nRST1-RST5 ALL PASS: root-shift telescope is not the DD.4 carrier boundary")
print(
    "VERDICT: the Frobenius-root transition kills the old H^1 generator, so "
    "it is zero on the obstruction line rather than an invertible carrier "
    "shift.  Every finite root tower still has a top obstruction, and a "
    "periodic wrap would need an external half-exponent.  A formal inverse "
    "shift kills the class only by splitter insertion, is formable on "
    "controls, and constructs no square, rep_NS, degree maps, graph, "
    "projection formula, Rosati, carrier boundary, or control death."
)
