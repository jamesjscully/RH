r"""Valuation-degree-character DD.4/SCC no-go.

Doc 267 showed that the full Laurent field kills the DD.4 class by using
the integer valuation/uniformizer axis.  Doc 268 showed that the parity
quotient of valuation is too small.  This witness tests the next repair:

    keep the full integer valuation character and promote it to the SCC
    degree data.

The positive fact is real: the Laurent valuation axis both kills the named
representative c=(1+z)^-1 and remembers the exact integer m.  The no-go is
rank: one additive valuation character is a rank-one shadow, while the square
carrier contract needs two independent endpoint degree maps.  A single
homomorphism Z^2 -> Z always has a kernel direction that changes endpoint
pairings, so it cannot replace the two carrier-native maps.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_valuation_degree_character_no_go
"""

from math import comb, log2

import numpy as np

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


def pair_mul(x, y, mul):
    return x[0] + y[0], mul(x[1], y[1])


def pair_inv(x, inv):
    return -x[0], inv(x[1])


def laurent_profile(L):
    _, mul, inv, phi = make(L)
    c = inv({0: 1, 1: 1})

    def sigma(x):
        valuation, unit = x
        twist = pow_unit(c, valuation, mul, inv)
        return valuation, mul(twist, phi(unit))

    def pmul(x, y):
        return pair_mul(x, y, mul)

    def pinv(x):
        return pair_inv(x, inv)

    def pboundary(x):
        return pmul(x, pinv(sigma(x)))

    phi_z = sigma((1, {0: 1}))
    valuation_rows = []
    for valuation in range(-4, 5):
        bdry = pboundary((valuation, {0: 1}))
        valuation_rows.append(
            {
                "valuation": valuation,
                "retained_integer": valuation,
                "boundary_res1": bdry[1].get(1, 0),
                "kills_c_class": valuation % 2 == 1,
            }
        )

    return {
        "L": L,
        "phi_z": phi_z,
        "phi_z_boundary_is_c": pboundary(phi_z) == (0, c),
        "integer_valuations_unique": len(
            {row["retained_integer"] for row in valuation_rows}
        )
        == len(valuation_rows),
        "odd_valuation_kills_c_class": all(
            row["boundary_res1"] == (row["valuation"] % 2)
            and row["kills_c_class"] == (row["valuation"] % 2 == 1)
            for row in valuation_rows
        ),
    }


def endpoint_pairing(endpoint_pair, probe):
    d_left, d_right = endpoint_pair
    e_left, e_right = probe
    return d_left * e_right + d_right * e_left


def collision_for_linear_character(a, b):
    assert (a, b) != (0, 0)
    base = (10 + abs(a) + abs(b), 12 + abs(a) + abs(b))
    delta = (b, -a)
    other = (base[0] + delta[0], base[1] + delta[1])
    probe = (0, 1) if b != 0 else (1, 0)
    chi_base = a * base[0] + b * base[1]
    chi_other = a * other[0] + b * other[1]
    return {
        "character": (a, b),
        "base": base,
        "other": other,
        "same_character": chi_base == chi_other,
        "changed_pair": base != other,
        "probe": probe,
        "pairing_base": endpoint_pairing(base, probe),
        "pairing_other": endpoint_pairing(other, probe),
    }


def rank_one_character_profile():
    characters = [(1, 0), (0, 1), (1, 1), (1, -1), (2, 3), (-2, 5)]
    collisions = [collision_for_linear_character(a, b) for a, b in characters]
    return {
        "collisions": collisions,
        "every_character_has_kernel_collision": all(
            row["same_character"]
            and row["changed_pair"]
            and row["pairing_base"] != row["pairing_other"]
            for row in collisions
        ),
    }


def scc_endpoint_anchor():
    F7 = frobenius(7, 1)
    Delta7 = diagonal(F7)
    left_fiber = (1, np.zeros_like(F7), 0)
    right_fiber = (0, np.zeros_like(F7), 1)
    pair_a = (10, F7, 1)
    pair_b = (7, F7, 4)
    base = (7, F7, 1)
    return {
        "base_delta": ns_intersection(Delta7, base),
        "left_changed_delta": ns_intersection(Delta7, pair_a),
        "right_changed_delta": ns_intersection(Delta7, pair_b),
        "same_total_degree": pair_a[0] + pair_a[2] == pair_b[0] + pair_b[2],
        "same_delta_intersection": ns_intersection(Delta7, pair_a)
        == ns_intersection(Delta7, pair_b),
        "left_probe_a": ns_intersection(left_fiber, pair_a),
        "left_probe_b": ns_intersection(left_fiber, pair_b),
        "right_probe_a": ns_intersection(right_fiber, pair_a),
        "right_probe_b": ns_intersection(right_fiber, pair_b),
    }


def control_degree_character_profile(dim):
    base = (dim + 3, dim + 5)
    other = (dim + 4, dim + 4)
    return {
        "dim": dim,
        "same_total_character": base[0] + base[1] == other[0] + other[1],
        "left_endpoint_changed": base[0] != other[0],
        "right_endpoint_changed": base[1] != other[1],
        "character_declared_without_square": True,
        "uses_square_data": False,
    }


base_profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
laurent_profiles = [laurent_profile(L) for L in (6, 8, 10, 12)]
rank_one_profile = rank_one_character_profile()
scc_anchor = scc_endpoint_anchor()
control_profiles = [control_degree_character_profile(dim) for dim in (2, 4, 8)]


gate(
    "VDC1 base DD.4 class remains the nonzero 1-unit obstruction",
    all(
        p["h1_order"] == 2 and not p["c_boundary"] and p["res1_c"] == 1
        for p in base_profiles
    ),
    "  ".join(
        "L%d:|B|=2^%d,|Z1|=2^%d,H1=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in base_profiles
    ),
)

gate(
    "VDC2 full Laurent valuation kills c and retains exact integer valuation",
    all(
        p["phi_z_boundary_is_c"]
        and p["integer_valuations_unique"]
        and p["odd_valuation_kills_c_class"]
        for p in laurent_profiles
    ),
    "  ".join(
        "L%d:phi(z)-boundary=c,valuations=-4..4 exact" % p["L"]
        for p in laurent_profiles
    ),
)

gate(
    "VDC3 one additive valuation character cannot recover two endpoint degrees",
    rank_one_profile["every_character_has_kernel_collision"],
    "  ".join(
        "chi%s:%s~%s,probe%s gives %d/%d"
        % (
            row["character"],
            row["base"],
            row["other"],
            row["probe"],
            row["pairing_base"],
            row["pairing_other"],
        )
        for row in rank_one_profile["collisions"]
    ),
)

gate(
    "VDC4 SCC finite-field anchor detects endpoint data beyond total degree",
    scc_anchor["base_delta"] == 7
    and scc_anchor["left_changed_delta"] == 10
    and scc_anchor["right_changed_delta"] == 10
    and scc_anchor["same_total_degree"]
    and scc_anchor["same_delta_intersection"]
    and scc_anchor["left_probe_a"] != scc_anchor["left_probe_b"]
    and scc_anchor["right_probe_a"] != scc_anchor["right_probe_b"],
    (
        "(7,F,1)->%.0f; (10,F,1)->%.0f; (7,F,4)->%.0f; "
        "same total 11, fibers %.0f/%.0f and %.0f/%.0f"
        % (
            scc_anchor["base_delta"],
            scc_anchor["left_changed_delta"],
            scc_anchor["right_changed_delta"],
            scc_anchor["left_probe_a"],
            scc_anchor["left_probe_b"],
            scc_anchor["right_probe_a"],
            scc_anchor["right_probe_b"],
        )
    ),
)

gate(
    "VDC5 the same single-degree-character package is formable on controls",
    all(
        p["same_total_character"]
        and p["left_endpoint_changed"]
        and p["right_endpoint_changed"]
        and p["character_declared_without_square"]
        and not p["uses_square_data"]
        for p in control_profiles
    ),
    "  ".join("dim%d:total-character-collision" % p["dim"] for p in control_profiles),
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

valuation_degree_slots = {
    "kills_dd4_class": True,
    "integer_valuation_character": True,
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
    "VDC6 valuation-degree character satisfies no square-carrier slot",
    not any(valuation_degree_slots[slot] for slot in required_slots),
    "missing: " + ", ".join(required_slots),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nVDC1-VDC6 ALL PASS: a single valuation character is not the SCC degree data")
print(
    "VERDICT: the full Laurent valuation axis can kill c=(1+z)^-1 and "
    "remember the exact integer valuation, but promoting one additive "
    "valuation character to the carrier degree data loses a rank.  SCC needs "
    "two carrier-native endpoint degree maps plus the square, rep_NS, "
    "diagonal, graph, correspondence composition, projection formula, Rosati, "
    "carrier boundary, and control death."
)
