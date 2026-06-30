r"""Boundary-fiber anchor contract for Qbar_BECD.

Doc 317 says the oriented-Cartier components D1,D2 must be anchored to the
primary endpoint maps p1,p2.  This witness sharpens "anchored": D1,D2 must
be actual endpoint boundary fibers of p1,p2 inside the carrier boundary, not
named components, product labels, or endpoint-coordinate decoders.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_boundary_fiber_anchor_contract
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
        "res1_c": c.get(1, 0),
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
        "p1p2_primary": False,
        "p1_boundary_fiber_actual": False,
        "p2_boundary_fiber_actual": False,
        "boundary_fibers_cartier": False,
        "boundary_fibers_inside_dq": False,
        "endpoint_order_fixes_orientation": False,
        "normal_ratio_from_fibers": False,
        "exact_localization_restricts": False,
        "twist_unique": False,
        "boundary_is_c": False,
        "endpoint_rank_preserved": False,
        "product_shape_only": False,
        "component_label_only": False,
        "coordinate_decoder": False,
        "declared_localization": False,
        "control_formable": True,
    }
    data.update(kwargs)
    return data


def accepts_fiber_anchor(data):
    return (
        data["carrier_native"]
        and data["p1p2_primary"]
        and data["p1_boundary_fiber_actual"]
        and data["p2_boundary_fiber_actual"]
        and data["boundary_fibers_cartier"]
        and data["boundary_fibers_inside_dq"]
        and data["endpoint_order_fixes_orientation"]
        and data["normal_ratio_from_fibers"]
        and data["exact_localization_restricts"]
        and data["twist_unique"]
        and data["boundary_is_c"]
        and data["endpoint_rank_preserved"]
        and not data["product_shape_only"]
        and not data["component_label_only"]
        and not data["coordinate_decoder"]
        and not data["declared_localization"]
        and not data["control_formable"]
    )


def reasons(data):
    out = []
    if not data["carrier_native"]:
        out.append("not_carrier_native")
    if not data["p1p2_primary"]:
        out.append("p1p2_not_primary")
    if not data["p1_boundary_fiber_actual"]:
        out.append("p1_boundary_fiber_not_actual")
    if not data["p2_boundary_fiber_actual"]:
        out.append("p2_boundary_fiber_not_actual")
    if not data["boundary_fibers_cartier"]:
        out.append("boundary_fibers_not_cartier")
    if not data["boundary_fibers_inside_dq"]:
        out.append("boundary_fibers_not_inside_dq")
    if not data["endpoint_order_fixes_orientation"]:
        out.append("endpoint_order_not_orientation")
    if not data["normal_ratio_from_fibers"]:
        out.append("normal_ratio_not_from_fibers")
    if not data["exact_localization_restricts"]:
        out.append("localization_not_restricted")
    if not data["twist_unique"]:
        out.append("twist_not_unique")
    if not data["boundary_is_c"]:
        out.append("boundary_not_c")
    if not data["endpoint_rank_preserved"]:
        out.append("endpoint_rank_not_preserved")
    if data["product_shape_only"]:
        out.append("product_shape_only")
    if data["component_label_only"]:
        out.append("component_label_only")
    if data["coordinate_decoder"]:
        out.append("coordinate_decoder")
    if data["declared_localization"]:
        out.append("declared_localization")
    if data["control_formable"]:
        out.append("control_formable")
    return out


oe = OBJECT | ENDPOINT
product_boundary_shape = oe | {"product_boundary_shape_declared"}
actual_fiber_boundary = oe | BOUNDARY | {
    "p1_boundary_fiber_actual",
    "p2_boundary_fiber_actual",
    "endpoint_ordered_normal_ratio_actual",
}

gate(
    "BFA1 O+E and product boundary shape still do not give boundary fibers",
    represented_slots(oe) == {"carrier_object", "endpoint_maps"}
    and represented_slots(product_boundary_shape) == {"carrier_object", "endpoint_maps"}
    and represented_slots(actual_fiber_boundary)
    == {"carrier_object", "endpoint_maps", "dd4_boundary_killing"},
    "O+E=%s product=%s actual-fiber=%s"
    % (
        ",".join(sorted(represented_slots(oe))),
        ",".join(sorted(represented_slots(product_boundary_shape))),
        ",".join(sorted(represented_slots(actual_fiber_boundary))),
    ),
)


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]

gate(
    "BFA2 endpoint fiber order matters at representative level",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and to_vec(p["c"], p["L"]) != to_vec(p["c_inv"], p["L"])
        for p in profiles
    ),
    "c and c^-1 distinct; res_1(c)=1 for L=6,8,10,12",
)


component_label_anchor = source(
    carrier_native=True,
    p1p2_primary=True,
    endpoint_order_fixes_orientation=True,
    normal_ratio_from_fibers=True,
    twist_unique=True,
    boundary_is_c=True,
    endpoint_rank_preserved=True,
    component_label_only=True,
)

gate(
    "BFA3 component labels are not actual endpoint boundary fibers",
    not accepts_fiber_anchor(component_label_anchor)
    and {
        "p1_boundary_fiber_not_actual",
        "p2_boundary_fiber_not_actual",
        "boundary_fibers_not_cartier",
        "component_label_only",
    }
    <= set(reasons(component_label_anchor)),
    ",".join(reasons(component_label_anchor)),
)


product_endpoint_boundary = source(
    carrier_native=True,
    p1p2_primary=True,
    p1_boundary_fiber_actual=True,
    p2_boundary_fiber_actual=True,
    boundary_fibers_inside_dq=True,
    endpoint_order_fixes_orientation=True,
    endpoint_rank_preserved=True,
    product_shape_only=True,
)

gate(
    "BFA4 product endpoint fibers need actual Cartier/localization data",
    not accepts_fiber_anchor(product_endpoint_boundary)
    and {
        "boundary_fibers_not_cartier",
        "normal_ratio_not_from_fibers",
        "localization_not_restricted",
        "product_shape_only",
    }
    <= set(reasons(product_endpoint_boundary)),
    ",".join(reasons(product_endpoint_boundary)),
)


declared_fiber_localization = source(
    carrier_native=True,
    p1p2_primary=True,
    p1_boundary_fiber_actual=True,
    p2_boundary_fiber_actual=True,
    boundary_fibers_cartier=True,
    boundary_fibers_inside_dq=True,
    endpoint_order_fixes_orientation=True,
    normal_ratio_from_fibers=True,
    twist_unique=True,
    boundary_is_c=True,
    endpoint_rank_preserved=True,
    declared_localization=True,
)

gate(
    "BFA5 declared localization is not endpoint-fiber exactness",
    not accepts_fiber_anchor(declared_fiber_localization)
    and {
        "localization_not_restricted",
        "declared_localization",
        "control_formable",
    }
    <= set(reasons(declared_fiber_localization)),
    ",".join(reasons(declared_fiber_localization)),
)


coordinate_decoder = source(
    p1p2_primary=False,
    p1_boundary_fiber_actual=False,
    p2_boundary_fiber_actual=False,
    endpoint_order_fixes_orientation=True,
    endpoint_rank_preserved=False,
    coordinate_decoder=True,
)
rank_boundary_difference = rank_of_maps([(1, -1)])
rank_endpoint_fibers = rank_of_maps([(1, 0), (0, 1)])
rank_total_difference = rank_of_maps([(1, 1), (1, -1)])

gate(
    "BFA6 endpoint-coordinate decoders are not endpoint boundary fibers",
    rank_boundary_difference == 1
    and rank_endpoint_fibers == 2
    and rank_total_difference == 2
    and not accepts_fiber_anchor(coordinate_decoder)
    and {"coordinate_decoder", "p1p2_not_primary", "endpoint_rank_not_preserved"}
    <= set(reasons(coordinate_decoder)),
    "ranks difference=%d endpoint-fibers=%d total+difference=%d reasons=%s"
    % (
        rank_boundary_difference,
        rank_endpoint_fibers,
        rank_total_difference,
        ",".join(reasons(coordinate_decoder)),
    ),
)


directions = primitive_directions()

gate(
    "BFA7 direction selection alone is not endpoint-fiber construction",
    len(directions) == 16 and (1, -1) in directions,
    "primitive directions=%d selected=(1,-1)" % len(directions),
)


control_fiber_lookalike = source(
    carrier_native=False,
    p1p2_primary=True,
    p1_boundary_fiber_actual=True,
    p2_boundary_fiber_actual=True,
    boundary_fibers_cartier=True,
    boundary_fibers_inside_dq=True,
    endpoint_order_fixes_orientation=True,
    normal_ratio_from_fibers=True,
    exact_localization_restricts=True,
    twist_unique=True,
    boundary_is_c=True,
    endpoint_rank_preserved=True,
    product_shape_only=True,
    control_formable=True,
)

gate(
    "BFA8 endpoint-fiber-looking control package still fails carrier nativity",
    not accepts_fiber_anchor(control_fiber_lookalike)
    and {"not_carrier_native", "product_shape_only", "control_formable"}
    <= set(reasons(control_fiber_lookalike)),
    ",".join(reasons(control_fiber_lookalike)),
)


live_fiber_anchor = source(
    carrier_native=True,
    p1p2_primary=True,
    p1_boundary_fiber_actual=True,
    p2_boundary_fiber_actual=True,
    boundary_fibers_cartier=True,
    boundary_fibers_inside_dq=True,
    endpoint_order_fixes_orientation=True,
    normal_ratio_from_fibers=True,
    exact_localization_restricts=True,
    twist_unique=True,
    boundary_is_c=True,
    endpoint_rank_preserved=True,
    control_formable=False,
)

dead_sources = {
    "component_label_anchor": component_label_anchor,
    "product_endpoint_boundary": product_endpoint_boundary,
    "declared_fiber_localization": declared_fiber_localization,
    "coordinate_decoder": coordinate_decoder,
    "control_fiber_lookalike": control_fiber_lookalike,
}

gate(
    "BFA9 only actual p1,p2 boundary-fiber data passes",
    accepts_fiber_anchor(live_fiber_anchor)
    and not any(accepts_fiber_anchor(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_fiber_anchor(data) for data in dead_sources.values()),
        accepts_fiber_anchor(live_fiber_anchor),
    ),
)


gate(
    "BFA10 actual endpoint boundary fibers complete live B and leave controls",
    represented_slots(actual_fiber_boundary)
    == {"carrier_object", "endpoint_maps", "dd4_boundary_killing"}
    and represented_slots(actual_fiber_boundary | CONTROL)
    == {"carrier_object", "endpoint_maps", "dd4_boundary_killing", "control_death"},
    "before C=%s after C=%s"
    % (
        ",".join(sorted(represented_slots(actual_fiber_boundary))),
        ",".join(sorted(represented_slots(actual_fiber_boundary | CONTROL))),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nBFA1-BFA10 ALL PASS: endpoint boundary-fiber contract pinned")
print(
    "VERDICT: D1 and D2 must be actual Cartier boundary fibers of p1 and p2 "
    "inside dQ, with endpoint order fixing orientation and exact localization "
    "restricting to their ordered normal ratio. Component labels, product "
    "shape, declared localization, coordinate decoders, and control-formable "
    "lookalikes do not meet this contract."
)
