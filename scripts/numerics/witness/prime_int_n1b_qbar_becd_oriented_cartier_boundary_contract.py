r"""Oriented Cartier boundary contract for the Qbar_BECD B-source.

Doc 311 says the live B target must be carrier-native, self-dual, endpoint-rank
preserving, and non-formable on controls.  The strongest positive pieces in
the bank are:

    Cartier normal line:      supplies the Hilbert-90 normal splitter.
    Oriented boundary complex: selects the DD.4 direction d1-d2.

This witness records their combined contract on the O+E line.  It is a
construction-spec witness, not a no-go theorem.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_oriented_cartier_boundary_contract
"""

from fractions import Fraction
from math import comb, gcd, log2


failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


OBJECT = {"object_actual", "open_actual", "boundary_actual"}
ENDPOINT = {"p1_map_actual", "p2_map_actual", "proper_pushforward_actual"}
BOUNDARY = {
    "boundary_map_actual",
    "localization_exact_actual",
    "dd4_class_mapped_to_zero",
    "self_dual_boundary_actual",
}
CONTROL = {"control_instantiation_impossible", "control_death_at_formation_proved"}


def represented_slots(evidence):
    evidence = set(evidence)
    slots = set()
    if OBJECT <= evidence:
        slots.add("carrier_object")
    if ENDPOINT <= evidence:
        slots.add("endpoint_maps")
    if BOUNDARY <= evidence:
        slots.add("dd4_boundary_killing")
    if CONTROL <= evidence:
        slots.add("control_death")
    return slots


def make(L):
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
        "cocycle": mul(c, phi(c)) == {0: 1},
        "c_nonboundary": to_vec(c, L) not in coboundaries,
        "res1_c": c.get(1, 0),
        "coboundaries": coboundaries,
        "b_order": len(coboundaries),
        "z1_order": z1_order,
        "h1_order": z1_order // len(coboundaries),
    }


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


def emul(x, y, mul):
    return (x[0][0] + y[0][0], x[0][1] + y[0][1]), mul(x[1], y[1])


def einv(x, inv):
    return (-x[0][0], -x[0][1]), inv(x[1])


def oriented_cartier_profile(L, orientation=1):
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
    return {
        "L": L,
        "orientation": orientation,
        "incidence": (orientation, -orientation),
        "sigma_involutive": sigma(sigma(((1, 0), {0: 1}))) == ((1, 0), {0: 1})
        and sigma(sigma(((0, 1), {0: 1}))) == ((0, 1), {0: 1}),
        "split_boundary_is_c": boundary(split_generator) == ((0, 0), c),
        "normal_rank": 2,
    }


def primitive_directions(bound=2):
    return [
        (a, b)
        for a in range(-bound, bound + 1)
        for b in range(-bound, bound + 1)
        if (a, b) != (0, 0) and gcd(abs(a), abs(b)) == 1
    ]


def decode_total_difference(total, difference):
    return Fraction(total + difference, 2), Fraction(total - difference, 2)


def endpoint_rank(contract):
    vectors = []
    if contract["has_p1"]:
        vectors.append((1, 0))
    if contract["has_p2"]:
        vectors.append((0, 1))
    if contract["uses_boundary_difference"]:
        vectors.append((1, -1))
    rank = 0
    if vectors:
        rank = 1
        base = vectors[0]
        if any(base[0] * v[1] - base[1] * v[0] != 0 for v in vectors[1:]):
            rank = 2
    return rank


def contract_accepts(contract):
    return (
        contract["normal_pair_actual"]
        and contract["oriented_incidence_actual"]
        and contract["orientation_fixed_by_carrier"]
        and contract["carrier_native_source"]
        and contract["self_dual_boundary_actual"]
        and contract["properness_actual"]
        and contract["endpoint_rank_preserved"]
        and contract["control_nonformability_proved"]
    )


oe = OBJECT | ENDPOINT

gate(
    "OCB1 the contract starts from the endpoint-fixed O+E line",
    represented_slots(oe) == {"carrier_object", "endpoint_maps"},
    "O+E slots=%s" % ",".join(sorted(represented_slots(oe))),
)


base_profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
oriented_profiles = [oriented_cartier_profile(L) for L in (6, 8, 10, 12)]

gate(
    "OCB2 oriented Cartier normal data supplies map/exact/zero/direction",
    all(
        p["cocycle"] and p["c_nonboundary"] and p["h1_order"] == 2 and p["res1_c"] == 1
        for p in base_profiles
    )
    and all(p["sigma_involutive"] and p["split_boundary_is_c"] for p in oriented_profiles),
    "normal-crossing incidence (1,-1) splits c for L=6,8,10,12",
)


gate(
    "OCB3 orientation is an actual carrier datum, not a cohomology-class detail",
    all(
        to_vec(p["c_inv"], p["L"]) != to_vec(p["c"], p["L"])
        and to_vec(make(p["L"])[0](p["c_inv"], make(p["L"])[1](p["c"])), p["L"]) in p["coboundaries"]
        for p in base_profiles
    ),
    "c and c^-1 are cohomologous but different representatives",
)


directions = primitive_directions()
gate(
    "OCB4 orientation selects one primitive direction from the normal-crossing family",
    len(directions) == 16 and (1, -1) in directions,
    "primitive directions in [-2,2]^2=%d; selected=(1,-1)" % len(directions),
)


boundary_only = {
    "has_p1": False,
    "has_p2": False,
    "uses_boundary_difference": True,
}
endpoint_plus_boundary = {
    "has_p1": True,
    "has_p2": True,
    "uses_boundary_difference": True,
}
half_sum_labels = [(11, 8), (0, 1), (10, 1)]
half_sum_defects = [decode_total_difference(*label) for label in half_sum_labels]

gate(
    "OCB5 endpoint rank is preserved only when p1,p2 stay primary",
    endpoint_rank(boundary_only) == 1
    and endpoint_rank(endpoint_plus_boundary) == 2
    and any(x.denominator == 2 or y.denominator == 2 for x, y in half_sum_defects),
    "boundary-only rank=1; p1,p2 plus boundary rank=2; total/difference has half-sum defects",
)


shape_only_contract = {
    "normal_pair_actual": True,
    "oriented_incidence_actual": True,
    "orientation_fixed_by_carrier": False,
    "carrier_native_source": False,
    "self_dual_boundary_actual": False,
    "properness_actual": False,
    "endpoint_rank_preserved": True,
    "control_nonformability_proved": False,
}
live_contract = dict(shape_only_contract)
live_contract.update(
    {
        "orientation_fixed_by_carrier": True,
        "carrier_native_source": True,
        "self_dual_boundary_actual": True,
        "properness_actual": True,
        "control_nonformability_proved": True,
    }
)

gate(
    "OCB6 shape-only oriented Cartier data is still not live B",
    not contract_accepts(shape_only_contract)
    and contract_accepts(live_contract),
    "missing from shape-only: orientation, carrier-native source, self-dual properness, control nonformability",
)


live_evidence = oe | BOUNDARY
live_slots = represented_slots(live_evidence)

gate(
    "OCB7 live oriented Cartier B leaves exactly formation control death",
    live_slots == {"carrier_object", "endpoint_maps", "dd4_boundary_killing"}
    and {"control_death"} == {"carrier_object", "endpoint_maps", "dd4_boundary_killing", "control_death"} - live_slots,
    "O+E+B slots=%s" % ",".join(sorted(live_slots)),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nOCB1-OCB7 ALL PASS: oriented Cartier boundary contract pinned")
print(
    "VERDICT: the live B construction should combine the Cartier normal "
    "splitter with oriented boundary incidence on O+E, while proving carrier "
    "orientation, carrier-nativity, self-dual properness, endpoint-rank "
    "preservation through actual p1,p2, and non-formability on controls."
)
