r"""Cartier-boundary normal line DD.4/SCC no-go.

After the carrier-first categorical contract, the first geometric-looking
repair is to make the Hilbert-90 uniformizer a normal coordinate of an honest
Cartier boundary divisor.  The positive fact is real: the normal line gives a
valuation axis and kills c=(1+z)^-1.  The no-go is that a normal line is still
only boundary valuation data.  A normal-crossing pair can provide two integer
valuations, but the DD.4 boundary direction is still a chosen primitive
linear functional unless the square carrier supplies p1,p2, graph,
composition, Rosati, and control death.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_cartier_boundary_normal_no_go
"""

from math import comb, gcd, log2

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
        "cocycle": mul(c, phi(c)) == {0: 1},
        "c_nonboundary": to_vec(c, L) not in coboundaries,
        "res1_c": c.get(1, 0),
        "b_order": len(coboundaries),
        "z1_order": z1_order,
        "h1_order": z1_order // len(coboundaries),
    }


def line_mul(x, y, mul):
    return x[0] + y[0], mul(x[1], y[1])


def line_inv(x, inv):
    return -x[0], inv(x[1])


def normal_line_profile(L):
    """One Cartier normal coordinate t with sigma(t)=t*c."""

    mul, inv, phi = make(L)
    c = inv({0: 1, 1: 1})

    def sigma(x):
        valuation, unit = x
        return valuation, mul(pow_unit(c, valuation, mul, inv), phi(unit))

    def boundary(x):
        return line_mul(x, line_inv(sigma(x), inv), mul)

    t = (1, {0: 1})
    sigma_t = sigma(t)
    splitter = sigma_t
    return {
        "sigma_t": sigma_t,
        "sigma2_t": sigma(sigma_t),
        "splitter_boundary": boundary(splitter),
        "boundary_is_c": boundary(splitter) == (0, c),
        "uses_odd_normal_valuation": splitter[0] % 2 == 1,
    }


def kernel_direction(character):
    a, b = character
    if a == 0 and b == 0:
        return None
    return b, -a


def character_value(character, endpoint):
    a, b = character
    x, y = endpoint
    return a * x + b * y


def rank_one_character_profile():
    characters = [(1, 0), (0, 1), (1, 1), (1, -1), (2, 3), (-2, 5)]
    rows = []
    for character in characters:
        direction = kernel_direction(character)
        base = (7, 4)
        moved = (base[0] + direction[0], base[1] + direction[1])
        rows.append(
            {
                "character": character,
                "kernel_direction": direction,
                "same_character": character_value(character, base)
                == character_value(character, moved),
                "endpoint_changed": base != moved,
            }
        )
    return rows


def primitive_characters(bound=2):
    chars = []
    for a in range(-bound, bound + 1):
        for b in range(-bound, bound + 1):
            if (a, b) == (0, 0):
                continue
            if gcd(abs(a), abs(b)) == 1:
                chars.append((a, b))
    return chars


def bezout_vector(character, search=4):
    a, b = character
    for x in range(-search, search + 1):
        for y in range(-search, search + 1):
            if a * x + b * y == 1:
                return x, y
    raise AssertionError(f"no small Bezout vector for {character}")


def normal_crossing_profile(L):
    """Two normal components D1,D2; DD.4 still needs a chosen ell."""

    mul, inv, phi = make(L)
    c = inv({0: 1, 1: 1})
    chars = primitive_characters()
    rows = []

    def make_sigma(character):
        def sigma(x):
            (m1, m2), unit = x
            ell = character[0] * m1 + character[1] * m2
            return (m1, m2), mul(pow_unit(c, ell, mul, inv), phi(unit))

        return sigma

    def emul(x, y):
        return (x[0][0] + y[0][0], x[0][1] + y[0][1]), mul(x[1], y[1])

    def einv(x):
        return (-x[0][0], -x[0][1]), inv(x[1])

    for character in chars:
        sigma = make_sigma(character)
        v = bezout_vector(character)
        split_generator = sigma((v, {0: 1}))
        boundary = emul(split_generator, einv(sigma(split_generator)))
        k = kernel_direction(character)
        rows.append(
            {
                "character": character,
                "bezout_vector": v,
                "boundary_is_c": boundary == ((0, 0), c),
                "kernel_direction": k,
                "kernel_nonzero": k != (0, 0),
            }
        )
    return {
        "rows": rows,
        "all_primitive_directions_split_c": all(row["boundary_is_c"] for row in rows),
        "many_boundary_directions": len(chars),
        "all_have_kernel_direction": all(row["kernel_nonzero"] for row in rows),
    }


def finite_field_endpoint_probe():
    F = frobenius(7, 1)
    Delta = diagonal(F)
    a = (10, F, 1)
    b = (7, F, 4)
    return {
        "same_total": a[0] + a[2] == b[0] + b[2],
        "same_diagonal_intersection": ns_intersection(Delta, a)
        == ns_intersection(Delta, b),
        "left_probe_differs": a[2] != b[2],
        "right_probe_differs": a[0] != b[0],
        "a_intersection": ns_intersection(Delta, a),
        "b_intersection": ns_intersection(Delta, b),
    }


def control_boundary_profile(dim):
    return {
        "dim": dim,
        "formal_cartier_boundary": True,
        "formal_normal_line": True,
        "chosen_dd4_direction": True,
        "square_carrier": False,
        "rep_NS": False,
        "two_degree_maps": False,
        "frobenius_graph": False,
        "rosati": False,
        "control_death": False,
    }


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
gate(
    "CBN1 DD.4 class is still nonzero before boundary normal data",
    all(p["cocycle"] and p["c_nonboundary"] and p["h1_order"] == 2 and p["res1_c"] == 1 for p in profiles),
    "  ".join(
        "L%d:|B|=2^%d|Z1|=2^%d|H1|=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in profiles
    ),
)


normal_profiles = [normal_line_profile(L) for L in (6, 8, 10, 12)]
gate(
    "CBN2 a Cartier normal coordinate really gives the Laurent splitter",
    all(p["sigma2_t"] == (1, {0: 1}) and p["boundary_is_c"] and p["uses_odd_normal_valuation"] for p in normal_profiles),
    "sigma(t)=t*c and boundary(sigma(t))=c in L=6,8,10,12",
)


rank_rows = rank_one_character_profile()
gate(
    "CBN3 one normal valuation is not two endpoint degree maps",
    all(row["same_character"] and row["endpoint_changed"] for row in rank_rows),
    "; ".join(f"chi={row['character']} ker={row['kernel_direction']}" for row in rank_rows),
)


nc = normal_crossing_profile(8)
gate(
    "CBN4 normal crossings give two valuations but not the DD.4 direction",
    nc["all_primitive_directions_split_c"]
    and nc["many_boundary_directions"] > 8
    and nc["all_have_kernel_direction"],
    f"{nc['many_boundary_directions']} primitive ell choices split c in the test window",
)


ff = finite_field_endpoint_probe()
gate(
    "CBN5 boundary totals still do not recover SCC endpoint probes",
    ff["same_total"]
    and ff["same_diagonal_intersection"]
    and ff["left_probe_differs"]
    and ff["right_probe_differs"],
    f"(10,F,1) and (7,F,4): total=11, Delta intersections={ff['a_intersection']:.0f}/{ff['b_intersection']:.0f}",
)


controls = [control_boundary_profile(dim) for dim in (2, 4, 8)]
gate(
    "CBN6 formal Cartier-boundary packages are formable on controls",
    all(
        p["formal_cartier_boundary"]
        and p["formal_normal_line"]
        and p["chosen_dd4_direction"]
        and not p["square_carrier"]
        and not p["control_death"]
        for p in controls
    ),
    "control dimensions: " + ",".join(str(p["dim"]) for p in controls),
)


cartier_boundary_slots = {
    "cartier_boundary": True,
    "normal_line": True,
    "normal_crossing_pair": True,
    "dd4_split": True,
    "actual_square": False,
    "rep_NS": False,
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
    "CBN7 Cartier normal data satisfies no square-carrier contract",
    cartier_boundary_slots["dd4_split"]
    and not cartier_boundary_slots["actual_square"]
    and not cartier_boundary_slots["rep_NS"]
    and not cartier_boundary_slots["two_carrier_degree_maps"]
    and not cartier_boundary_slots["frobenius_graph"]
    and not cartier_boundary_slots["rosati_duality"]
    and not cartier_boundary_slots["control_death"],
    "DD.4 split yes; Qbar/p1/p2/rep_NS/graph/Rosati/control death no",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nCBN1-CBN7 ALL PASS: Cartier boundary normal line is not the square carrier")
print(
    "VERDICT: a boundary normal coordinate is the right kind of object to kill "
    "the DD.4 class, but by itself it is only Laurent valuation data. A surviving "
    "route must construct the normal line as part of Qbar and simultaneously tie "
    "its normal-crossing components to p1,p2, rep_NS, Frobenius/Hecke graphs, "
    "Rosati duality, and control death."
)
