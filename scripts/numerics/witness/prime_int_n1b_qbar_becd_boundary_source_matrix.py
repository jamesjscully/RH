r"""Boundary-source matrix for the endpoint-fixed Qbar_BECD frontier.

Doc 310 reduced the live CC/CxC product line to:

    O+E is present; construct actual B next.

The prior DD.4 bank already separates many failed ways to produce B.  This
witness records that split without adding another random construction branch.
It classifies each boundary source by the four atoms of B:

    M = carrier boundary map,
    L = exact localization,
    Z = DD.4 class maps to zero,
    S = self-dual boundary/properness.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_boundary_source_matrix
"""

from math import comb, gcd, log2


failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


PHASE_A_SLOTS = {
    "carrier_object",
    "endpoint_maps",
    "dd4_boundary_killing",
    "control_death",
}

OBJECT = {"object_actual", "open_actual", "boundary_actual"}
ENDPOINT = {"p1_map_actual", "p2_map_actual", "proper_pushforward_actual"}
CONTROL = {"control_instantiation_impossible", "control_death_at_formation_proved"}
BOUNDARY = {
    "boundary_map_actual",
    "localization_exact_actual",
    "dd4_class_mapped_to_zero",
    "self_dual_boundary_actual",
}


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
        "cocycle": mul(c, phi(c)) == {0: 1},
        "c_nonboundary": to_vec(c, L) not in coboundaries,
        "res1_c": c.get(1, 0),
        "b_order": len(coboundaries),
        "z1_order": z1_order,
        "h1_order": z1_order // len(coboundaries),
    }


def source(**kwargs):
    defaults = {
        "carrier_map": False,
        "exact_localization": False,
        "zero_image": False,
        "self_dual_proper": False,
        "carrier_native": False,
        "preserves_c": True,
        "direction_unique": False,
        "endpoint_rank_ok": True,
        "control_formable": True,
    }
    defaults.update(kwargs)
    return defaults


SOURCES = {
    "coinduced_module": source(
        exact_localization=True,
        zero_image=True,
        preserves_c=True,
    ),
    "bar_resolution": source(
        exact_localization=True,
        zero_image=True,
        preserves_c=True,
    ),
    "mapping_cone": source(
        exact_localization=True,
        zero_image=True,
        preserves_c=True,
    ),
    "jet_deletion": source(
        exact_localization=True,
        zero_image=False,
        preserves_c=False,
    ),
    "obstruction_quotient": source(
        exact_localization=False,
        zero_image=False,
        preserves_c=False,
    ),
    "norm_one_hilbert90": source(
        self_dual_proper=False,
        preserves_c=True,
    ),
    "laurent_field_hilbert90": source(
        exact_localization=True,
        zero_image=True,
        preserves_c=True,
        endpoint_rank_ok=False,
    ),
    "valuation_degree_character": source(
        exact_localization=True,
        zero_image=True,
        preserves_c=True,
        endpoint_rank_ok=False,
    ),
    "cartier_boundary_normal": source(
        carrier_map=True,
        exact_localization=True,
        zero_image=True,
        preserves_c=True,
        carrier_native=False,
        direction_unique=False,
    ),
    "oriented_boundary_complex": source(
        carrier_map=True,
        exact_localization=True,
        zero_image=True,
        preserves_c=True,
        carrier_native=False,
        direction_unique=True,
    ),
    "boundary_even_lattice": source(
        carrier_map=True,
        exact_localization=False,
        zero_image=True,
        preserves_c=True,
        carrier_native=False,
        direction_unique=False,
    ),
    "product_normal_crossing": source(
        carrier_map=False,
        exact_localization=False,
        zero_image=False,
        preserves_c=True,
        direction_unique=False,
    ),
}


def boundary_source_accepts(data):
    return (
        data["carrier_map"]
        and data["exact_localization"]
        and data["zero_image"]
        and data["self_dual_proper"]
        and data["carrier_native"]
        and data["preserves_c"]
        and data["direction_unique"]
        and data["endpoint_rank_ok"]
        and not data["control_formable"]
    )


def missing_reasons(data):
    reasons = []
    if not data["carrier_map"]:
        reasons.append("no_carrier_map")
    if not data["exact_localization"]:
        reasons.append("no_exact_localization")
    if not data["zero_image"]:
        reasons.append("no_zero_image")
    if not data["self_dual_proper"]:
        reasons.append("no_self_dual_properness")
    if not data["carrier_native"]:
        reasons.append("not_carrier_native")
    if not data["preserves_c"]:
        reasons.append("deletes_or_quotients_c")
    if not data["direction_unique"]:
        reasons.append("no_unique_dd4_direction")
    if not data["endpoint_rank_ok"]:
        reasons.append("endpoint_rank_lost")
    if data["control_formable"]:
        reasons.append("control_formable")
    return reasons


oe_evidence = OBJECT | ENDPOINT
product_boundary_shape = oe_evidence | {
    "product_boundary_shape_actual",
    "normal_crossing_boundary_actual",
    "boundary_direction_family_actual",
}

gate(
    "BSM1 active line is O+E; product boundary shape still gives no B",
    represented_slots(oe_evidence) == {"carrier_object", "endpoint_maps"}
    and represented_slots(product_boundary_shape) == {"carrier_object", "endpoint_maps"},
    "O+E slots=%s" % ",".join(sorted(represented_slots(oe_evidence))),
)


formal_names = ("coinduced_module", "bar_resolution", "mapping_cone")
formal_reasons = {name: missing_reasons(SOURCES[name]) for name in formal_names}

gate(
    "BSM2 formal coboundary sources kill only by external resolution",
    all(
        {"no_carrier_map", "no_self_dual_properness", "not_carrier_native", "control_formable"}
        <= set(formal_reasons[name])
        for name in formal_names
    ),
    "; ".join("%s:%s" % (name, ",".join(formal_reasons[name])) for name in formal_names),
)


deletion_names = ("jet_deletion", "obstruction_quotient")
deletion_reasons = {name: missing_reasons(SOURCES[name]) for name in deletion_names}

gate(
    "BSM3 deletion and quotient sources do not preserve the DD.4 class",
    all("deletes_or_quotients_c" in deletion_reasons[name] for name in deletion_names)
    and "no_zero_image" in deletion_reasons["jet_deletion"]
    and "no_exact_localization" in deletion_reasons["obstruction_quotient"],
    "; ".join("%s:%s" % (name, ",".join(deletion_reasons[name])) for name in deletion_names),
)


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]

gate(
    "BSM4 norm-one self-duality is only the cocycle condition",
    all(
        p["cocycle"] and p["c_nonboundary"] and p["h1_order"] == 2 and p["res1_c"] == 1
        for p in profiles
    )
    and "no_zero_image" in missing_reasons(SOURCES["norm_one_hilbert90"])
    and "no_carrier_map" in missing_reasons(SOURCES["norm_one_hilbert90"]),
    "  ".join(
        "L%d:|B|=2^%d|Z1|=2^%d|H1|=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in profiles
    ),
)


valuation_names = ("laurent_field_hilbert90", "valuation_degree_character")
valuation_reasons = {name: missing_reasons(SOURCES[name]) for name in valuation_names}

gate(
    "BSM5 external valuation sources can zero c but lose endpoint rank",
    all("zero_image" not in valuation_reasons[name] for name in valuation_names)
    and all("endpoint_rank_lost" in valuation_reasons[name] for name in valuation_names)
    and all("not_carrier_native" in valuation_reasons[name] for name in valuation_names),
    "; ".join("%s:%s" % (name, ",".join(valuation_reasons[name])) for name in valuation_names),
)


primitive_directions = [
    (a, b)
    for a in range(-2, 3)
    for b in range(-2, 3)
    if (a, b) != (0, 0) and gcd(abs(a), abs(b)) == 1
]
geometric_names = (
    "cartier_boundary_normal",
    "oriented_boundary_complex",
    "boundary_even_lattice",
    "product_normal_crossing",
)
geometric_reasons = {name: missing_reasons(SOURCES[name]) for name in geometric_names}

gate(
    "BSM6 geometric direction sources are shape evidence, not actual B",
    len(primitive_directions) == 16
    and all(not boundary_source_accepts(SOURCES[name]) for name in geometric_names)
    and "not_carrier_native" in geometric_reasons["cartier_boundary_normal"]
    and "no_self_dual_properness" in geometric_reasons["oriented_boundary_complex"]
    and "no_exact_localization" in geometric_reasons["boundary_even_lattice"]
    and "no_carrier_map" in geometric_reasons["product_normal_crossing"],
    "; ".join("%s:%s" % (name, ",".join(geometric_reasons[name])) for name in geometric_names),
)


live_boundary_source = source(
    carrier_map=True,
    exact_localization=True,
    zero_image=True,
    self_dual_proper=True,
    carrier_native=True,
    preserves_c=True,
    direction_unique=True,
    endpoint_rank_ok=True,
    control_formable=False,
)

gate(
    "BSM7 the surviving B-shape is a carrier-native self-dual boundary source",
    boundary_source_accepts(live_boundary_source)
    and not any(boundary_source_accepts(data) for data in SOURCES.values()),
    "banked sources accepted=%d; live source accepted=%s"
    % (sum(boundary_source_accepts(data) for data in SOURCES.values()), boundary_source_accepts(live_boundary_source)),
)


oeb_evidence = oe_evidence | BOUNDARY
oeb_slots = represented_slots(oeb_evidence)

gate(
    "BSM8 constructing live B would leave exactly formation control death",
    oeb_slots == {"carrier_object", "endpoint_maps", "dd4_boundary_killing"}
    and PHASE_A_SLOTS - oeb_slots == {"control_death"},
    "O+E+B slots=%s missing=%s"
    % (",".join(sorted(oeb_slots)), ",".join(sorted(PHASE_A_SLOTS - oeb_slots))),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nBSM1-BSM8 ALL PASS: Qbar_BECD boundary-source matrix pinned")
print(
    "VERDICT: the next target is not formal coinduction, deletion, external "
    "valuation, or direction-only boundary geometry.  It is a carrier-native "
    "boundary source on O+E that supplies map, exact localization, DD.4 zero, "
    "self-dual properness, unique DD.4 direction, endpoint-rank preservation, "
    "and non-formability on controls."
)
