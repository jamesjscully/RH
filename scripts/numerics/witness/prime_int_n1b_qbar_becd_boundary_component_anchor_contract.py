r"""Endpoint-anchored boundary component contract for Qbar_BECD.

Doc 316 says the Laurent twist must be pinned by carrier oriented-Cartier
normal-ratio data.  This witness sharpens the source of the two boundary
components: the normal ratio must be anchored to the primary endpoint maps
p1,p2.  An oriented boundary pair without endpoint anchoring still has a
swap/inversion ambiguity; product endpoints without live B do not pin the
twist; endpoint-coordinate decoders are only labels.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_boundary_component_anchor_contract
"""

from math import comb, gcd


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
        "h1_order": z1_order // len(coboundaries),
    }


def primitive_directions(bound=2):
    return [
        (a, b)
        for a in range(-bound, bound + 1)
        for b in range(-bound, bound + 1)
        if (a, b) != (0, 0) and gcd(abs(a), abs(b)) == 1
    ]


def rank_of_maps(vectors):
    # Only need ranks for the small integer matrices used below.
    nonzero = [v for v in vectors if v != (0, 0)]
    if not nonzero:
        return 0
    if len(nonzero) == 1:
        return 1
    (a, b), (c, d) = nonzero[:2]
    return 2 if a * d - b * c != 0 else 1


def source(**kwargs):
    data = {
        "carrier_native": False,
        "boundary_components_present": False,
        "component_d1_p1": False,
        "component_d2_p2": False,
        "ordered_by_endpoints": False,
        "normal_ratio_rigidified": False,
        "twist_unique": False,
        "boundary_is_c": False,
        "p1p2_primary": False,
        "endpoint_rank_preserved": False,
        "product_shape_only": False,
        "coordinate_decoder": False,
        "control_formable": True,
    }
    data.update(kwargs)
    return data


def accepts_anchor(data):
    return (
        data["carrier_native"]
        and data["boundary_components_present"]
        and data["component_d1_p1"]
        and data["component_d2_p2"]
        and data["ordered_by_endpoints"]
        and data["normal_ratio_rigidified"]
        and data["twist_unique"]
        and data["boundary_is_c"]
        and data["p1p2_primary"]
        and data["endpoint_rank_preserved"]
        and not data["product_shape_only"]
        and not data["coordinate_decoder"]
        and not data["control_formable"]
    )


def reasons(data):
    out = []
    if not data["carrier_native"]:
        out.append("not_carrier_native")
    if not data["boundary_components_present"]:
        out.append("no_boundary_components")
    if not data["component_d1_p1"]:
        out.append("D1_not_anchored_to_p1")
    if not data["component_d2_p2"]:
        out.append("D2_not_anchored_to_p2")
    if not data["ordered_by_endpoints"]:
        out.append("not_ordered_by_endpoints")
    if not data["normal_ratio_rigidified"]:
        out.append("normal_ratio_not_rigidified")
    if not data["twist_unique"]:
        out.append("twist_not_unique")
    if not data["boundary_is_c"]:
        out.append("boundary_not_c")
    if not data["p1p2_primary"]:
        out.append("p1p2_not_primary")
    if not data["endpoint_rank_preserved"]:
        out.append("endpoint_rank_not_preserved")
    if data["product_shape_only"]:
        out.append("product_shape_only")
    if data["coordinate_decoder"]:
        out.append("coordinate_decoder")
    if data["control_formable"]:
        out.append("control_formable")
    return out


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]

gate(
    "BCA1 swapping boundary components inverts the representative",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and to_vec(p["c"], p["L"]) != to_vec(p["c_inv"], p["L"])
        for p in profiles
    ),
    "c and c^-1 remain distinct representatives for L=6,8,10,12",
)


directions = primitive_directions()
unanchored_oriented_pair = source(
    carrier_native=True,
    boundary_components_present=True,
    normal_ratio_rigidified=True,
    twist_unique=True,
    boundary_is_c=True,
    endpoint_rank_preserved=True,
)

gate(
    "BCA2 oriented pair without p1,p2 anchoring is still a label choice",
    len(directions) == 16
    and (1, -1) in directions
    and not accepts_anchor(unanchored_oriented_pair)
    and {"D1_not_anchored_to_p1", "D2_not_anchored_to_p2", "not_ordered_by_endpoints"}
    <= set(reasons(unanchored_oriented_pair)),
    "primitive directions=%d reasons=%s"
    % (len(directions), ",".join(reasons(unanchored_oriented_pair))),
)


product_endpoint_shape = source(
    carrier_native=True,
    boundary_components_present=True,
    component_d1_p1=True,
    component_d2_p2=True,
    ordered_by_endpoints=True,
    p1p2_primary=True,
    endpoint_rank_preserved=True,
    product_shape_only=True,
)

gate(
    "BCA3 product endpoints anchor labels but do not supply live B",
    not accepts_anchor(product_endpoint_shape)
    and {"normal_ratio_not_rigidified", "twist_not_unique", "boundary_not_c", "product_shape_only"}
    <= set(reasons(product_endpoint_shape)),
    ",".join(reasons(product_endpoint_shape)),
)


coordinate_decoder = source(
    boundary_components_present=True,
    component_d1_p1=True,
    component_d2_p2=True,
    ordered_by_endpoints=True,
    p1p2_primary=False,
    endpoint_rank_preserved=False,
    coordinate_decoder=True,
)
rank_boundary_difference = rank_of_maps([(1, -1)])
rank_primary_endpoints = rank_of_maps([(1, 0), (0, 1)])
rank_total_difference = rank_of_maps([(1, 1), (1, -1)])

gate(
    "BCA4 endpoint-coordinate decoders do not anchor boundary components",
    rank_boundary_difference == 1
    and rank_primary_endpoints == 2
    and rank_total_difference == 2
    and not accepts_anchor(coordinate_decoder)
    and {"not_carrier_native", "normal_ratio_not_rigidified", "coordinate_decoder"}
    <= set(reasons(coordinate_decoder)),
    "ranks difference=%d p1p2=%d total+difference=%d reasons=%s"
    % (
        rank_boundary_difference,
        rank_primary_endpoints,
        rank_total_difference,
        ",".join(reasons(coordinate_decoder)),
    ),
)


parity_decoder_labels = [(11, 9), (11, 3), (11, 8), (0, 1), (10, 1)]
integral = [
    (s, a)
    for s, a in parity_decoder_labels
    if (s + a) % 2 == 0 and (s - a) % 2 == 0
]
half_integral = [pair for pair in parity_decoder_labels if pair not in integral]

gate(
    "BCA5 parity selects endpoint labels but not component anchoring",
    integral == [(11, 9), (11, 3)]
    and half_integral == [(11, 8), (0, 1), (10, 1)],
    "integral=%s half_integral=%s" % (integral, half_integral),
)


control_product_shape = source(
    carrier_native=False,
    boundary_components_present=True,
    component_d1_p1=True,
    component_d2_p2=True,
    ordered_by_endpoints=True,
    normal_ratio_rigidified=True,
    twist_unique=True,
    boundary_is_c=True,
    p1p2_primary=True,
    endpoint_rank_preserved=True,
    product_shape_only=True,
    control_formable=True,
)

gate(
    "BCA6 endpoint-anchored-looking product data remains formable on controls",
    not accepts_anchor(control_product_shape)
    and {"not_carrier_native", "product_shape_only", "control_formable"}
    <= set(reasons(control_product_shape)),
    ",".join(reasons(control_product_shape)),
)


live_anchor = source(
    carrier_native=True,
    boundary_components_present=True,
    component_d1_p1=True,
    component_d2_p2=True,
    ordered_by_endpoints=True,
    normal_ratio_rigidified=True,
    twist_unique=True,
    boundary_is_c=True,
    p1p2_primary=True,
    endpoint_rank_preserved=True,
    control_formable=False,
)

dead_sources = {
    "unanchored_oriented_pair": unanchored_oriented_pair,
    "product_endpoint_shape": product_endpoint_shape,
    "coordinate_decoder": coordinate_decoder,
    "control_product_shape": control_product_shape,
}

gate(
    "BCA7 only endpoint-anchored normal-ratio data passes",
    accepts_anchor(live_anchor)
    and not any(accepts_anchor(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_anchor(data) for data in dead_sources.values()),
        accepts_anchor(live_anchor),
    ),
)


oe = OBJECT | ENDPOINT
ocb_evidence = oe | {
    "boundary_map_actual",
    "localization_exact_actual",
    "dd4_class_mapped_to_zero",
    "oriented_cartier_normal_shape_actual",
    "dd4_direction_selected",
}
anchored_ratio_evidence = ocb_evidence | {"self_dual_boundary_actual"}

gate(
    "BCA8 endpoint-anchored normal-ratio data completes live B",
    represented_slots(oe) == {"carrier_object", "endpoint_maps"}
    and represented_slots(ocb_evidence) == {"carrier_object", "endpoint_maps"}
    and represented_slots(anchored_ratio_evidence)
    == {"carrier_object", "endpoint_maps", "dd4_boundary_killing"}
    and represented_slots(anchored_ratio_evidence | CONTROL)
    == {"carrier_object", "endpoint_maps", "dd4_boundary_killing", "control_death"},
    "O+E=%s OCB=%s anchored=%s after C=%s"
    % (
        ",".join(sorted(represented_slots(oe))),
        ",".join(sorted(represented_slots(ocb_evidence))),
        ",".join(sorted(represented_slots(anchored_ratio_evidence))),
        ",".join(sorted(represented_slots(anchored_ratio_evidence | CONTROL))),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nBCA1-BCA8 ALL PASS: boundary component anchoring contract pinned")
print(
    "VERDICT: the oriented-Cartier normal ratio must be anchored by the "
    "primary endpoint maps: D1 is the p1 boundary component, D2 is the p2 "
    "boundary component, and their ordered ratio produces the twist with "
    "boundary c. Unanchored oriented pairs, product shape, coordinate "
    "decoders, parity labels, and control-formable packages do not meet this "
    "contract."
)
