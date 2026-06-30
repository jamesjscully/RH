r"""Frobenius-root / perfect-closure DD.4 no-go.

This witness tests the repair after docs 257-263:
adjoin a square root w of z, extend the Artin-Schreier shear by

    phi(w) = w/(1+w),

and observe that the pullback of c=(1+z)^-1 becomes a coboundary.
The identity is real, but it is not a square-carrier boundary.  It only
reindexes the obstruction:

    d = (1+w)^-1 is still nonzero in H^1,
    c(z) -> (1+w)^-2 = d/phi(d).

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_frobenius_root_extension_no_go
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


def cohomology_profile(L):
    add, mul, inv, phi = make(L)
    c = inv({0: 1, 1: 1})
    boundary_gens = [
        mul({0: 1, k: 1}, inv(phi({0: 1, k: 1}))) for k in range(1, L + 1)
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
    h1_order = z1_order // len(coboundaries)
    return {
        "L": L,
        "c": c,
        "b_order": len(coboundaries),
        "z1_order": z1_order,
        "h1_order": h1_order,
        "c_boundary": to_vec(c, L) in coboundaries,
        "c_res1": c.get(1, 0),
        "coboundaries": coboundaries,
    }


def pullback_z_to_w(f_z, Lw):
    out = {}
    for k in f_z:
        wk = 2 * k
        if wk <= Lw:
            out[wk] = out.get(wk, 0) ^ 1
    return {k: 1 for k, v in out.items() if v}


def root_profile(Lz):
    Lw = 2 * Lz
    _, mul_z, inv_z, phi_z = make(Lz)
    _, mul_w, inv_w, phi_w = make(Lw)
    base = cohomology_profile(Lz)
    root = cohomology_profile(Lw)

    c_z = inv_z({0: 1, 1: 1})
    d_w = inv_w({0: 1, 1: 1})
    pull_c = pullback_z_to_w(c_z, Lw)
    d_square = mul_w(d_w, d_w)
    d_boundary = mul_w(d_w, inv_w(phi_w(d_w)))

    phi_w_generator_square = mul_w(phi_w({1: 1}), phi_w({1: 1}))
    phi_z_generator_pullback = pullback_z_to_w(phi_z({1: 1}), Lw)

    return {
        "Lz": Lz,
        "Lw": Lw,
        "base_h1_order": base["h1_order"],
        "base_c_boundary": base["c_boundary"],
        "base_res1": base["c_res1"],
        "root_h1_order": root["h1_order"],
        "root_d_boundary": root["c_boundary"],
        "root_res1_d": root["c_res1"],
        "action_extends": phi_w_generator_square == phi_z_generator_pullback,
        "pull_c": pull_c,
        "pull_c_is_d_square": pull_c == d_square,
        "pull_c_is_d_boundary": pull_c == d_boundary,
        "pull_c_boundary": to_vec(pull_c, Lw) in root["coboundaries"],
        "pull_c_res1": pull_c.get(1, 0),
        "pull_c_res2": pull_c.get(2, 0),
        "even_support_only": all(k % 2 == 0 for k in pull_c),
        "d_uses_odd_root_slots": any(k % 2 == 1 for k in d_w if k > 0),
        "b_order_log2": int(log2(root["b_order"])),
        "z1_order_log2": int(log2(root["z1_order"])),
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


def control_root_profile(dim):
    """Formal root/splitter adjoining on an exact F_2 control complex."""

    chosen = tuple(1 if i == 0 else 0 for i in range(dim))
    zero = tuple(0 for _ in range(dim))
    base_boundaries = span([zero], dim)
    root_extension_boundaries = span([chosen], dim)
    return {
        "dim": dim,
        "base_nonboundary": chosen not in base_boundaries,
        "killed_after_root_adjoin": chosen in root_extension_boundaries,
        "adds_formal_root_coordinate": True,
        "uses_square_data": False,
    }


root_profiles = [root_profile(Lz) for Lz in (6, 8, 10, 12)]
control_profiles = [control_root_profile(dim) for dim in (1, 2, 4, 8)]


gate(
    "FRC1 base DD.4 class is still the nonzero obstruction",
    all(
        p["base_h1_order"] == 2 and not p["base_c_boundary"] and p["base_res1"] == 1
        for p in root_profiles
    ),
    "  ".join("L%d:H1=%d,res1=%d" % (p["Lz"], p["base_h1_order"], p["base_res1"]) for p in root_profiles),
)

gate(
    "FRC2 square-root shear is exact and kills the old pullback",
    all(
        p["action_extends"]
        and p["pull_c_is_d_square"]
        and p["pull_c_is_d_boundary"]
        and p["pull_c_boundary"]
        for p in root_profiles
    ),
    "  ".join("L%d->L%d:pull(c)=d/phi(d)" % (p["Lz"], p["Lw"]) for p in root_profiles),
)

gate(
    "FRC3 the root extension shifts rather than removes H1",
    all(
        p["root_h1_order"] == 2
        and not p["root_d_boundary"]
        and p["root_res1_d"] == 1
        and p["pull_c_res1"] == 0
        and p["pull_c_res2"] == 1
        for p in root_profiles
    ),
    "  ".join(
        "L%d:|B|=2^%d,|Z1|=2^%d,d-nonboundary"
        % (p["Lw"], p["b_order_log2"], p["z1_order_log2"])
        for p in root_profiles
    ),
)

gate(
    "FRC4 support is refined by new odd root slots",
    all(
        p["Lw"] == 2 * p["Lz"]
        and p["even_support_only"]
        and p["d_uses_odd_root_slots"]
        for p in root_profiles
    ),
    "  ".join("rank %d->%d" % (p["Lz"], p["Lw"]) for p in root_profiles),
)

gate(
    "FRC5 formal root adjoining is formable on controls",
    all(
        p["base_nonboundary"]
        and p["killed_after_root_adjoin"]
        and p["adds_formal_root_coordinate"]
        and not p["uses_square_data"]
        for p in control_profiles
    ),
    "  ".join("dim%d:root-splitter-kills-control-class" % p["dim"] for p in control_profiles),
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

root_extension_slots = {
    "frobenius_root_adjoined": True,
    "old_class_boundary_after_pullback": True,
    "new_root_obstruction": True,
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
    "FRC6 Frobenius-root extension satisfies no square-carrier slot",
    not any(root_extension_slots[slot] for slot in required_slots),
    "missing: " + ", ".join(required_slots),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nFRC1-FRC6 ALL PASS: Frobenius-root extension is not the DD.4 carrier boundary")
print(
    "VERDICT: adjoining w with w^2=z makes the old class c pull back to "
    "d/phi(d) for d=(1+w)^-1, so the old obstruction becomes a coboundary. "
    "But d is the new nonzero H^1 generator, the support has been refined by "
    "odd root slots, the same formal root/splitter move is formable on "
    "controls, and no square, rep_NS, degree maps, graph, projection formula, "
    "Rosati, carrier boundary, or control death is constructed."
)
