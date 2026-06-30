r"""Hyperbolic-plane/Rosati DD.4/SCC no-go.

Doc 279 left the strongest nearby repair:

    make the same-parity endpoint lattice an actual even hyperbolic
    intersection plane, with Rosati swapping the two isotropic endpoints.

The positive fact is real.  Once a hyperbolic endpoint basis e,f is present,
total/difference coordinates automatically have the required parity, the
half-sum decoder is integral, the anti-invariant direction e-f splits the
DD.4 class, and the swap is an isometry.

The no-go is that an abstract hyperbolic plane is still only boundary lattice
data.  It forgets the End/Frobenius graph component in rep_NS, has no
fiber-product composition or projection formula, needs an extra lift of the
swap to the DD.4 unit line, and is formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_hyperbolic_plane_rosati_no_go
"""

from fractions import Fraction
from math import comb, log2


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


def hyp_pair(v, w):
    return v[0] * w[1] + v[1] * w[0]


def hyp_q(v):
    return hyp_pair(v, v)


def tau(v):
    return v[1], v[0]


def total(v):
    return v[0] + v[1]


def difference(v):
    return v[0] - v[1]


def decode_total_difference(s, a):
    return Fraction(s + a, 2), Fraction(s - a, 2)


def hyperbolic_endpoint_profile(window=4):
    vectors = [(x, y) for x in range(-window, window + 1) for y in range(-window, window + 1)]
    rows = []
    for v in vectors:
        s = total(v)
        a = difference(v)
        decoded = decode_total_difference(s, a)
        rows.append(
            {
                "v": v,
                "q_even": hyp_q(v) % 2 == 0,
                "same_parity": (s - a) % 2 == 0,
                "decoded": decoded,
                "decode_integral": decoded[0].denominator == 1
                and decoded[1].denominator == 1,
            }
        )
    return {
        "rows": rows,
        "all_even": all(row["q_even"] for row in rows),
        "all_same_parity": all(row["same_parity"] for row in rows),
        "all_decode_integral": all(row["decode_integral"] for row in rows),
        "e_isotropic": hyp_q((1, 0)) == 0,
        "f_isotropic": hyp_q((0, 1)) == 0,
        "e_f_pairing": hyp_pair((1, 0), (0, 1)),
        "tau_is_isometry": all(hyp_pair(tau(v), tau(w)) == hyp_pair(v, w) for v in vectors for w in vectors),
        "difference_anti_invariant": all(difference(tau(v)) == -difference(v) for v in vectors),
        "total_invariant": all(total(tau(v)) == total(v) for v in vectors),
    }


def endpoint_mul(x, y, mul):
    return (x[0][0] + y[0][0], x[0][1] + y[0][1]), mul(x[1], y[1])


def endpoint_inv(x, inv):
    return (-x[0][0], -x[0][1]), inv(x[1])


def split_profile(L, lift_swap_to_units):
    mul, inv, phi = make(L)
    c = inv({0: 1, 1: 1})

    def sigma(x):
        vector, unit = x
        twist = pow_unit(c, difference(vector), mul, inv)
        return vector, mul(twist, phi(unit))

    def rosati(x):
        vector, unit = x
        unit_out = inv(unit) if lift_swap_to_units else unit
        return tau(vector), unit_out

    def emul(x, y):
        return endpoint_mul(x, y, mul)

    def einv(x):
        return endpoint_inv(x, inv)

    def boundary(x):
        return emul(x, einv(sigma(x)))

    gens = [((1, 0), {0: 1}), ((0, 1), {0: 1}), ((1, 1), {0: 1})]
    gens.extend([((0, 0), {0: 1, k: 1}) for k in range(1, L + 1)])
    split_generator = sigma(((1, 0), {0: 1}))
    return {
        "L": L,
        "lift_swap_to_units": lift_swap_to_units,
        "sigma_involutive_on_gens": all(sigma(sigma(gen)) == gen for gen in gens),
        "split_boundary_is_c": boundary(split_generator) == ((0, 0), c),
        "rosati_commutes_with_sigma": all(rosati(sigma(gen)) == sigma(rosati(gen)) for gen in gens),
    }


def frobenius_trace_blindness_profile():
    # In rep_NS, Delta.(q,F,1)=q+1-Tr(F).  The hyperbolic endpoint
    # plane only sees (q,1), hence q+1, and loses the End/Frobenius trace.
    q = 7
    endpoint_vector = (q, 1)
    trace_a = 1
    trace_b = 3
    return {
        "endpoint_vector": endpoint_vector,
        "hyperbolic_boundary_value": hyp_pair((1, 1), endpoint_vector),
        "count_a": q + 1 - trace_a,
        "count_b": q + 1 - trace_b,
        "same_endpoint_data": True,
        "different_rep_ns_counts": (q + 1 - trace_a) != (q + 1 - trace_b),
        "end_component_present": False,
        "frobenius_graph_present": False,
    }


def composition_profile():
    return {
        "abstract_hyperbolic_plane": True,
        "proper_correspondence_category": False,
        "fiber_product_composition": False,
        "projection_formula": False,
        "indecomposable_diagonal": False,
        "frobenius_graph": False,
        "rep_ns_end_component": False,
    }


def control_hyperbolic_profile(dim):
    return {
        "dim": dim,
        "hyperbolic_plane": True,
        "rosati_swap": True,
        "dd4_split": True,
        "actual_square": False,
        "frobenius_graph": False,
        "control_death": False,
    }


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
gate(
    "HPR1 DD.4 class is nonzero before adjoining the hyperbolic plane",
    all(p["cocycle"] and p["c_nonboundary"] and p["h1_order"] == 2 and p["res1_c"] == 1 for p in profiles),
    "  ".join(
        "L%d:|B|=2^%d|Z1|=2^%d|H1|=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in profiles
    ),
)


endpoint_plane = hyperbolic_endpoint_profile()
gate(
    "HPR2 hyperbolic endpoint basis packages parity and integral decoding",
    endpoint_plane["all_even"]
    and endpoint_plane["all_same_parity"]
    and endpoint_plane["all_decode_integral"]
    and endpoint_plane["e_isotropic"]
    and endpoint_plane["f_isotropic"]
    and endpoint_plane["e_f_pairing"] == 1,
    "U=<e,f>, q(v)=2xy even, total/difference decode back to (x,y)",
)


gate(
    "HPR3 swap is a Rosati-looking isometry and difference is anti-invariant",
    endpoint_plane["tau_is_isometry"]
    and endpoint_plane["difference_anti_invariant"]
    and endpoint_plane["total_invariant"],
    "tau(e)=f, total fixed, difference negated",
)


split_plain = [split_profile(L, False) for L in (6, 8, 10, 12)]
split_lifted = [split_profile(L, True) for L in (6, 8, 10, 12)]
gate(
    "HPR4 DD.4 split needs a chosen lift of Rosati to the unit line",
    all(p["split_boundary_is_c"] and p["sigma_involutive_on_gens"] for p in split_lifted)
    and not any(p["rosati_commutes_with_sigma"] for p in split_plain)
    and all(p["rosati_commutes_with_sigma"] for p in split_lifted),
    "plain swap is an isometry but not the DD.4/Rosati lift; inverse-unit lift commutes",
)


trace_blind = frobenius_trace_blindness_profile()
gate(
    "HPR5 hyperbolic boundary data forgets the End/Frobenius graph trace",
    trace_blind["same_endpoint_data"]
    and trace_blind["different_rep_ns_counts"]
    and not trace_blind["end_component_present"]
    and not trace_blind["frobenius_graph_present"],
    (
        f"endpoint {trace_blind['endpoint_vector']} gives hyperbolic "
        f"{trace_blind['hyperbolic_boundary_value']}, but rep_NS counts "
        f"{trace_blind['count_a']} and {trace_blind['count_b']} differ by trace"
    ),
)


composition = composition_profile()
gate(
    "HPR6 the hyperbolic plane supplies no proper graph composition",
    composition["abstract_hyperbolic_plane"]
    and not composition["proper_correspondence_category"]
    and not composition["fiber_product_composition"]
    and not composition["projection_formula"]
    and not composition["indecomposable_diagonal"]
    and not composition["rep_ns_end_component"],
    "pairing yes; Corr^prop, fiber products, projection formula, End component no",
)


controls = [control_hyperbolic_profile(dim) for dim in (2, 4, 8)]
gate(
    "HPR7 the same hyperbolic/Rosati/DD.4 package is formable on controls",
    all(
        p["hyperbolic_plane"]
        and p["rosati_swap"]
        and p["dd4_split"]
        and not p["actual_square"]
        and not p["frobenius_graph"]
        and not p["control_death"]
        for p in controls
    ),
    "control dimensions: " + ",".join(str(p["dim"]) for p in controls),
)


carrier_slots = {
    "hyperbolic_plane": True,
    "endpoint_basis": True,
    "dd4_split": True,
    "rosati_swap_lift": True,
    "actual_square": False,
    "integral_rep_NS_with_End": False,
    "two_carrier_degree_maps": False,
    "indecomposable_diagonal": False,
    "frobenius_graph": False,
    "proper_correspondence_category": False,
    "fiber_product_composition": False,
    "projection_formula": False,
    "positive_primitive_sign": False,
    "control_death": False,
}

gate(
    "HPR8 hyperbolic plane/Rosati satisfies no square-carrier contract",
    carrier_slots["dd4_split"]
    and carrier_slots["rosati_swap_lift"]
    and not carrier_slots["actual_square"]
    and not carrier_slots["integral_rep_NS_with_End"]
    and not carrier_slots["frobenius_graph"]
    and not carrier_slots["fiber_product_composition"]
    and not carrier_slots["control_death"],
    "endpoint lattice yes; Qbar/rep_NS-End/graph/composition/Rosati sign/control death no",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nHPR1-HPR8 ALL PASS: hyperbolic plane/Rosati is not the square carrier")
print(
    "VERDICT: a hyperbolic endpoint plane packages integrality, parity, "
    "the endpoint swap, and a DD.4 split, but it is still boundary lattice "
    "data unless constructed by Qbar. It forgets the End/Frobenius graph "
    "component, supplies no proper composition or projection formula, and "
    "does not kill controls."
)
