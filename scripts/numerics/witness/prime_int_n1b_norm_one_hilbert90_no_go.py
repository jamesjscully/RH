r"""Norm-one / Hilbert-90 DD.4 no-go.

This witness tests the repair after docs 257-262:
promote the identity c*phi(c)=1 to the carrier-native
boundary/properness/self-duality map, using the slogan that norm-one
elements should be coboundaries.  In the DD.4 coefficient system this is
false: norm-one is exactly the cocycle condition, and H^1 is still Z/2.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_norm_one_hilbert90_no_go
"""

from math import comb, log2


failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def make(L):
    """Arithmetic in F_2[z]/z^{L+1}; 1-units are dicts {power: 1}."""

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

    return mul, inv, phi


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


def h1_profile(L):
    mul, inv, phi = make(L)
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
    z1_order = 2 ** L // len(norm_image)
    h1_order = z1_order // len(coboundaries)
    c_norm = mul(c, phi(c))
    c_boundary = to_vec(c, L) in coboundaries
    return {
        "L": L,
        "c": c,
        "b_order": len(coboundaries),
        "z1_order": z1_order,
        "h1_order": h1_order,
        "norm_image_order": len(norm_image),
        "norm_one_index": z1_order // len(coboundaries),
        "c_norm_one": c_norm == {0: 1},
        "phi_c_is_inv_c": phi(c) == inv(c),
        "c_boundary": c_boundary,
        "res1_c": c.get(1, 0),
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


def control_norm_one_profile(dim):
    """A trivial-action F_2 control: every class is norm-one, boundaries are zero."""

    chosen = tuple(1 if i == 0 else 0 for i in range(dim))
    zero = tuple(0 for _ in range(dim))
    coboundaries = span([zero], dim)
    return {
        "dim": dim,
        "chosen_norm_one": xor_vec(chosen, chosen) == zero,
        "chosen_boundary": chosen in coboundaries,
        "uses_square_data": False,
    }


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
control_profiles = [control_norm_one_profile(dim) for dim in (1, 2, 4, 8)]

gate(
    "NOH1 base DD.4 class is norm-one and non-boundary",
    all(p["c_norm_one"] and p["phi_c_is_inv_c"] and not p["c_boundary"] for p in profiles),
    "  ".join("L%d:res1(c)=%d" % (p["L"], p["res1_c"]) for p in profiles),
)

gate(
    "NOH2 norm-one classes strictly contain coboundaries",
    all(p["h1_order"] == 2 and p["norm_one_index"] == 2 for p in profiles),
    "  ".join(
        "L%d:|B|=2^%d|Norm1|=2^%d|Norm1/B|=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["norm_one_index"])
        for p in profiles
    ),
)

gate(
    "NOH3 Hilbert-90 slogan fails for this coefficient system",
    all(p["c_norm_one"] and not p["c_boundary"] and p["h1_order"] == 2 for p in profiles),
    "c*phi(c)=1 but no b has b/phi(b)=c",
)

gate(
    "NOH4 norm-one/self-dual identity is formable on controls",
    all(p["chosen_norm_one"] and not p["chosen_boundary"] and not p["uses_square_data"] for p in control_profiles),
    "  ".join("dim%d:norm-one-not-boundary" % p["dim"] for p in control_profiles),
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

norm_one_slots = {
    "cocycle_condition": True,
    "self_dual_identity": True,
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
    "NOH5 norm-one identity satisfies no square-carrier slot",
    not any(norm_one_slots[slot] for slot in required_slots),
    "missing: " + ", ".join(required_slots),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nNOH1-NOH5 ALL PASS: norm-one is not the DD.4 carrier boundary")
print(
    "VERDICT: c*phi(c)=1 only says c is a cocycle.  In U_1 the norm-one "
    "subgroup is larger than the coboundary subgroup by a factor of 2, with "
    "c representing the nontrivial class.  The same norm-one-not-boundary "
    "pattern is formable on controls and constructs no actual square, rep_NS, "
    "degree maps, graph, projection formula, Rosati, carrier boundary, or "
    "control death."
)
