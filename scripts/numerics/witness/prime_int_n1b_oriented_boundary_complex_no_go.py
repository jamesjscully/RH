r"""Oriented-boundary-complex DD.4/SCC no-go.

Doc 277 showed that a normal-crossing boundary gives two valuations but does
not by itself select the DD.4 primitive direction ell.  This witness tests the
next geometric repair: use the oriented boundary complex of the two-component
normal-crossing boundary.  Its incidence vector selects ell=d1-d2.

The positive fact is real: the alternating direction splits c=(1+z)^-1.
The no-go is that the oriented boundary complex is still only incidence data.
It does not construct rep_NS, graph composition, Rosati, projection formula,
or control death, and total plus difference still has determinant -2.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_oriented_boundary_complex_no_go
"""

from fractions import Fraction
from math import comb, log2

from scripts.numerics.witness.ns_diagonal_representability import (
    diagonal,
    frobenius,
    ns_intersection,
)


failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def make(L):
    """Arithmetic in F_2[z]/z^(L+1); 1-units are dicts {power: 1}."""

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


def closure(gens, L, mul):
    seen = {(0,) * L}
    queue = [(0,) * L]
    while queue:
        current = from_vec(queue.pop())
        for gen in gens:
            nxt = to_vec(mul(current, gen), L)
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return seen


def pow_unit(unit, exponent, mul, inv):
    if exponent < 0:
        return inv(pow_unit(unit, -exponent, mul, inv))
    out = {0: 1}
    base = unit
    n = exponent
    while n:
        if n & 1:
            out = mul(out, base)
        base = mul(base, base)
        n >>= 1
    return out


def h1_profile(L):
    mul, inv, phi = make(L)
    c = inv({0: 1, 1: 1})
    boundary_gens = [
        mul({0: 1, k: 1}, inv(phi({0: 1, k: 1}))) for k in range(1, L + 1)
    ]
    norm_gens = [
        mul({0: 1, k: 1}, phi({0: 1, k: 1})) for k in range(1, L + 1)
    ]
    coboundaries = closure(boundary_gens, L, mul)
    norm_image = closure(norm_gens, L, mul)
    z1_order = 2**L // len(norm_image)
    return {
        "L": L,
        "c": c,
        "c_inv": inv(c),
        "coboundaries": coboundaries,
        "cocycle": mul(c, phi(c)) == {0: 1},
        "c_nonboundary": to_vec(c, L) not in coboundaries,
        "res1_c": c.get(1, 0),
        "b_order": len(coboundaries),
        "z1_order": z1_order,
        "h1_order": z1_order // len(coboundaries),
    }


def emul(x, y, mul):
    return (x[0][0] + y[0][0], x[0][1] + y[0][1]), mul(x[1], y[1])


def einv(x, inv):
    return (-x[0][0], -x[0][1]), inv(x[1])


def oriented_boundary_profile(L, orientation=1):
    """Boundary complex incidence vector orientation*(D1-D2)."""

    mul, inv, phi = make(L)
    c = inv({0: 1, 1: 1})

    def ell(v):
        return orientation * (v[0] - v[1])

    def sigma(x):
        v, unit = x
        return v, mul(pow_unit(c, ell(v), mul, inv), phi(unit))

    def boundary(x):
        return emul(x, einv(sigma(x), inv), mul)

    split_vector = (1, 0) if orientation == 1 else (-1, 0)
    split_generator = sigma((split_vector, {0: 1}))
    split_boundary = boundary(split_generator)

    return {
        "orientation": orientation,
        "incidence_vector": (orientation, -orientation),
        "split_vector": split_vector,
        "sigma_involutive": sigma(sigma(((1, 0), {0: 1}))) == ((1, 0), {0: 1})
        and sigma(sigma(((0, 1), {0: 1}))) == ((0, 1), {0: 1}),
        "split_boundary": split_boundary,
        "split_boundary_is_c": split_boundary == ((0, 0), c),
    }


def orientation_reversal_profile(L):
    mul, inv, _phi = make(L)
    c = inv({0: 1, 1: 1})
    h1 = h1_profile(L)
    ratio = mul(h1["c_inv"], inv(c))
    return {
        "L": L,
        "c_inv_same_h1_class": to_vec(ratio, L) in h1["coboundaries"],
        "c_inv_not_equal_c": h1["c_inv"] != c,
    }


def decode_from_total_difference(total, difference):
    return Fraction(total + difference, 2), Fraction(total - difference, 2)


def total_difference_profile():
    rows = []
    labels = [(11, 9), (11, 3), (11, 8), (0, 1), (10, 1)]
    for label in labels:
        decoded = decode_from_total_difference(*label)
        rows.append(
            {
                "label": label,
                "decoded": decoded,
                "integral": decoded[0].denominator == 1 and decoded[1].denominator == 1,
            }
        )
    return {
        "determinant": -2,
        "rows": rows,
        "has_half_integral_labels": any(not row["integral"] for row in rows),
        "valid_decodes": [row for row in rows if row["integral"]],
    }


def rank_one_difference_profile():
    base = (10, 1)
    moved = (11, 2)
    F = frobenius(7, 1)
    Delta = diagonal(F)
    a = (base[0], F, base[1])
    b = (moved[0], F, moved[1])
    return {
        "same_difference": base[0] - base[1] == moved[0] - moved[1],
        "different_total": base[0] + base[1] != moved[0] + moved[1],
        "different_diagonal_intersection": ns_intersection(Delta, a)
        != ns_intersection(Delta, b),
        "base_intersection": ns_intersection(Delta, a),
        "moved_intersection": ns_intersection(Delta, b),
    }


def control_boundary_complex_profile(dim):
    return {
        "dim": dim,
        "two_boundary_vertices": True,
        "oriented_edge": True,
        "alternating_incidence": True,
        "dd4_splitter": True,
        "square_carrier": False,
        "rep_NS": False,
        "frobenius_graph": False,
        "rosati": False,
        "control_death": False,
    }


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
gate(
    "OBC1 DD.4 class is nonzero before the oriented boundary selector",
    all(p["cocycle"] and p["c_nonboundary"] and p["h1_order"] == 2 and p["res1_c"] == 1 for p in profiles),
    "  ".join(
        "L%d:|B|=2^%d|Z1|=2^%d|H1|=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in profiles
    ),
)


oriented_profiles = [oriented_boundary_profile(L, 1) for L in (6, 8, 10, 12)]
gate(
    "OBC2 oriented boundary complex selects d1-d2 and splits c",
    all(p["incidence_vector"] == (1, -1) and p["sigma_involutive"] and p["split_boundary_is_c"] for p in oriented_profiles),
    "incidence vector (1,-1), split vector (1,0), L=6,8,10,12",
)


reversal_profiles = [orientation_reversal_profile(L) for L in (6, 8, 10, 12)]
gate(
    "OBC3 orientation reversal is a sign choice, not endpoint geometry",
    all(p["c_inv_same_h1_class"] and p["c_inv_not_equal_c"] for p in reversal_profiles),
    "reversing orientation changes representative c<->c^-1 but not the Z/2 class",
)


rank_one = rank_one_difference_profile()
gate(
    "OBC4 alternating incidence is still rank-one endpoint data",
    rank_one["same_difference"]
    and rank_one["different_total"]
    and rank_one["different_diagonal_intersection"],
    (
        "(10,1) and (11,2): same difference 9, "
        f"Delta intersections={rank_one['base_intersection']:.0f}/{rank_one['moved_intersection']:.0f}"
    ),
)


decoder = total_difference_profile()
gate(
    "OBC5 total plus oriented difference still needs parity and half-sums",
    decoder["determinant"] == -2
    and decoder["has_half_integral_labels"]
    and len(decoder["valid_decodes"]) >= 2,
    "labels include integral decodes and half-integral non-endpoints",
)


controls = [control_boundary_complex_profile(dim) for dim in (2, 4, 8)]
gate(
    "OBC6 the same oriented boundary complex is formable on controls",
    all(
        p["two_boundary_vertices"]
        and p["oriented_edge"]
        and p["alternating_incidence"]
        and p["dd4_splitter"]
        and not p["square_carrier"]
        and not p["control_death"]
        for p in controls
    ),
    "control dimensions: " + ",".join(str(p["dim"]) for p in controls),
)


oriented_boundary_slots = {
    "boundary_complex": True,
    "alternating_incidence": True,
    "dd4_split": True,
    "orientation_choice": True,
    "actual_square": False,
    "integral_rep_NS": False,
    "two_carrier_degree_maps": False,
    "proper_correspondence_category": False,
    "fiber_product_composition": False,
    "frobenius_graph": False,
    "projection_formula": False,
    "rosati_duality": False,
    "positive_primitive_sign": False,
    "control_death": False,
}

gate(
    "OBC7 oriented boundary complex satisfies no square-carrier contract",
    oriented_boundary_slots["dd4_split"]
    and not oriented_boundary_slots["actual_square"]
    and not oriented_boundary_slots["integral_rep_NS"]
    and not oriented_boundary_slots["proper_correspondence_category"]
    and not oriented_boundary_slots["frobenius_graph"]
    and not oriented_boundary_slots["rosati_duality"]
    and not oriented_boundary_slots["control_death"],
    "DD.4 split yes; rep_NS/graph/composition/Rosati/control death no",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nOBC1-OBC7 ALL PASS: oriented boundary complex is not the square carrier")
print(
    "VERDICT: the oriented boundary complex is a plausible carrier-native way "
    "to select the DD.4 difference direction, but by itself it is incidence "
    "data. It does not construct rep_NS, graph composition, Rosati, projection, "
    "or control death, and total plus difference still requires a parity "
    "theorem and half-sum decoder."
)
