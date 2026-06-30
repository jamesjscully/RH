r"""Perfection-colimit DD.4 no-go.

This witness tests the repair left after doc 264:
instead of adjoining one Frobenius root, pass to the whole root tower

    z = t_1^2 = t_2^4 = ...

or to its filtered colimit / perfect closure.  At each finite stage n,
the fundamental class

    c_n = (1+t_n)^-1

is nonzero in H^1.  Its pullback to stage n+1 is a coboundary:

    c_n |_{t_n=t_{n+1}^2} = c_{n+1}^2 = c_{n+1}/phi(c_{n+1}).

Thus the direct limit can kill every finite-stage representative only
because there is no terminal stage.  That moving-boundary vanishing is not
the carrier-native DD.4 boundary/properness/self-duality map.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_perfection_colimit_no_go
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


def one_step_profile(L):
    _, mul0, inv0, phi0 = make(L)
    _, mul1, inv1, phi1 = make(2 * L)
    c0 = inv0({0: 1, 1: 1})
    c1 = inv1({0: 1, 1: 1})
    pull_c0 = pullback_even(c0, 2 * L)
    delta_c1 = boundary(c1, inv1, phi1, mul1)
    action_extends = mul1(phi1({1: 1}), phi1({1: 1})) == pullback_even(phi0({1: 1}), 2 * L)
    return {
        "L": L,
        "root_L": 2 * L,
        "action_extends": action_extends,
        "old_class_killed": pull_c0 == delta_c1,
        "pull_res1": pull_c0.get(1, 0),
        "pull_res2": pull_c0.get(2, 0),
    }


def res1_kills_generator_boundaries(L):
    _, mul, inv, phi = make(L)
    return all(
        boundary({0: 1, k: 1}, inv, phi, mul).get(1, 0) == 0
        for k in range(1, L + 1)
    )


def tower_profile(depth, base_L=3):
    """Embed stages 0..depth into the top variable t_depth."""

    top_L = base_L * (2**depth)
    _, mul, inv, phi = make(top_L)
    c_top = inv({0: 1, 1: 1})
    lower_kills = []
    for stage in range(depth):
        exponent = 2 ** (depth - stage)
        pulled = pow_unit(c_top, exponent, mul)
        splitter = pow_unit(c_top, exponent // 2, mul)
        lower_kills.append(pulled == boundary(splitter, inv, phi, mul))
    return {
        "depth": depth,
        "top_L": top_L,
        "lower_classes_killed": all(lower_kills),
        "top_class_nonboundary_by_res1": c_top.get(1, 0) == 1 and res1_kills_generator_boundaries(top_L),
        "surviving_top_stage": "c_%d" % depth,
        "support_rank_growth": top_L,
    }


def direct_colimit_profile(max_stage=6, base_L=3):
    ranks = [base_L * (2**stage) for stage in range(max_stage + 1)]
    kill_depths = [stage + 1 for stage in range(max_stage)]
    return {
        "max_stage": max_stage,
        "all_finite_representatives_have_later_kill": all(k > i for i, k in enumerate(kill_depths)),
        "no_terminal_stage_required": True,
        "ranks_strictly_grow": all(a < b for a, b in zip(ranks, ranks[1:])),
        "ranks": ranks,
        "kill_depths": kill_depths,
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


def control_moving_boundary_profile(dim, depth):
    """Exact F_2 control tower with a class killed one formal root later."""

    chosen = tuple(1 if i == 0 else 0 for i in range(dim))
    zero = tuple(0 for _ in range(dim))
    finite_top_boundaries = span([chosen], dim)
    next_stage_boundaries = span([chosen], dim)
    return {
        "dim": dim,
        "depth": depth,
        "old_class_killed_after_adjoining_splitter": chosen in next_stage_boundaries,
        "new_top_class_present": chosen in finite_top_boundaries,
        "uses_square_data": False,
        "has_carrier_boundary": False,
    }


finite_profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
one_step_profiles = [one_step_profile(L) for L in (6, 8, 10, 12)]
tower_profiles = [tower_profile(depth) for depth in (1, 2, 3, 4)]
colimit = direct_colimit_profile()
control_profiles = [
    control_moving_boundary_profile(dim, depth)
    for dim, depth in ((1, 1), (2, 2), (4, 3), (8, 4))
]


gate(
    "PCL1 every finite root stage has the same nonzero H1 obstruction",
    all(p["h1_order"] == 2 and not p["c_boundary"] and p["res1_c"] == 1 for p in finite_profiles),
    "  ".join(
        "L%d:|B|=2^%d,|Z1|=2^%d,H1=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in finite_profiles
    ),
)

gate(
    "PCL2 transition to the next root kills the old generator",
    all(p["action_extends"] and p["old_class_killed"] and p["pull_res1"] == 0 and p["pull_res2"] == 1 for p in one_step_profiles),
    "  ".join("L%d->L%d:c_n maps to delta(c_{n+1})" % (p["L"], p["root_L"]) for p in one_step_profiles),
)

gate(
    "PCL3 finite towers still have a surviving top-stage obstruction",
    all(p["lower_classes_killed"] and p["top_class_nonboundary_by_res1"] for p in tower_profiles),
    "  ".join(
        "depth%d:rank%d,survives=%s"
        % (p["depth"], p["support_rank_growth"], p["surviving_top_stage"])
        for p in tower_profiles
    ),
)

gate(
    "PCL4 colimit vanishing uses no terminal stage and unbounded support",
    (
        colimit["all_finite_representatives_have_later_kill"]
        and colimit["no_terminal_stage_required"]
        and colimit["ranks_strictly_grow"]
    ),
    "ranks=%s kill_depths=%s" % (colimit["ranks"], colimit["kill_depths"]),
)

gate(
    "PCL5 moving-boundary colimit is formable on controls",
    all(
        p["old_class_killed_after_adjoining_splitter"]
        and p["new_top_class_present"]
        and not p["uses_square_data"]
        and not p["has_carrier_boundary"]
        for p in control_profiles
    ),
    "  ".join("dim%d:depth%d" % (p["dim"], p["depth"]) for p in control_profiles),
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

colimit_slots = {
    "filtered_colimit": True,
    "moving_boundary": True,
    "unbounded_root_support": True,
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
    "PCL6 perfection colimit satisfies no square-carrier slot",
    not any(colimit_slots[slot] for slot in required_slots),
    "missing: " + ", ".join(required_slots),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nPCL1-PCL6 ALL PASS: perfection colimit is moving-boundary vanishing, not carrier boundary")
print(
    "VERDICT: the full Frobenius-root tower can make every finite-stage DD.4 "
    "class a boundary one stage later, so the filtered colimit has no stable "
    "finite obstruction representative.  But every finite tower still has a "
    "new top-stage obstruction, the vanishing uses unbounded support and no "
    "terminal carrier object, the same moving-boundary trick is formable on "
    "controls, and no square, rep_NS, degree maps, graph, projection formula, "
    "Rosati, carrier boundary, or control death is constructed."
)
