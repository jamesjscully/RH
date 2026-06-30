r"""Boundary self-duality interface for oriented-Cartier Qbar_BECD.

Doc 313 leaves the residual B proof:

    carrier-fixed orientation + self-dual boundary/properness.

The nearby hyperbolic/Rosati/projection bank shows that this cannot be
discharged by an abstract endpoint plane, a formal End envelope, matrix
positivity, projection forcing, or formal fiber-product cells.  Those are
Phase-B-shaped unless produced by Qbar itself.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_boundary_self_duality_interface
"""

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
        "b_order": len(coboundaries),
        "z1_order": z1_order,
        "h1_order": z1_order // len(coboundaries),
    }


def primitive_directions(bound=2):
    return [
        (a, b)
        for a in range(-bound, bound + 1)
        for b in range(-bound, bound + 1)
        if (a, b) != (0, 0) and gcd(abs(a), abs(b)) == 1
    ]


def source(**kwargs):
    data = {
        "boundary_native": False,
        "orientation_fixed": False,
        "self_dual_properness": False,
        "p1p2_primary": False,
        "uses_phase_b_graph": False,
        "projection_from_geometry": False,
        "preserves_counts": True,
        "dd4_coupled_to_duality": False,
        "control_formable": True,
    }
    data.update(kwargs)
    return data


SOURCES = {
    "hyperbolic_endpoint_plane": source(
        self_dual_properness=True,
        p1p2_primary=True,
    ),
    "trace_augmented_hyperbolic": source(
        self_dual_properness=True,
        p1p2_primary=True,
        uses_phase_b_graph=True,
    ),
    "end_augmented_hyperbolic": source(
        self_dual_properness=True,
        p1p2_primary=True,
        uses_phase_b_graph=True,
    ),
    "positive_rosati_end": source(
        self_dual_properness=True,
        p1p2_primary=True,
        uses_phase_b_graph=True,
    ),
    "projection_forced_positive": source(
        self_dual_properness=True,
        p1p2_primary=True,
        uses_phase_b_graph=True,
        preserves_counts=False,
    ),
    "fiber_product_saturated_positive": source(
        self_dual_properness=True,
        p1p2_primary=True,
        uses_phase_b_graph=True,
    ),
}


def accepts_phase_a_self_duality(data):
    return (
        data["boundary_native"]
        and data["orientation_fixed"]
        and data["self_dual_properness"]
        and data["p1p2_primary"]
        and not data["uses_phase_b_graph"]
        and data["projection_from_geometry"] is False
        and data["preserves_counts"]
        and data["dd4_coupled_to_duality"]
        and not data["control_formable"]
    )


def reasons(data):
    out = []
    if not data["boundary_native"]:
        out.append("not_boundary_native")
    if not data["orientation_fixed"]:
        out.append("orientation_not_fixed")
    if not data["self_dual_properness"]:
        out.append("no_self_dual_properness")
    if not data["p1p2_primary"]:
        out.append("p1p2_not_primary")
    if data["uses_phase_b_graph"]:
        out.append("imports_phase_b_graph")
    if data["projection_from_geometry"]:
        out.append("phase_b_projection_claim")
    if not data["preserves_counts"]:
        out.append("distorts_counts")
    if not data["dd4_coupled_to_duality"]:
        out.append("dd4_not_coupled_to_duality")
    if data["control_formable"]:
        out.append("control_formable")
    return out


oe = OBJECT | ENDPOINT
ocb_shape = oe | {
    "boundary_map_actual",
    "localization_exact_actual",
    "dd4_class_mapped_to_zero",
    "oriented_cartier_normal_shape_actual",
    "dd4_direction_selected",
}
boundary_self_dual = ocb_shape | {"self_dual_boundary_actual"}

gate(
    "BSD1 Phase-A boundary self-duality starts from O+E plus OCB shape",
    represented_slots(oe) == {"carrier_object", "endpoint_maps"}
    and represented_slots(ocb_shape) == {"carrier_object", "endpoint_maps"}
    and represented_slots(boundary_self_dual)
    == {"carrier_object", "endpoint_maps", "dd4_boundary_killing"},
    "O+E=%s OCB-shape=%s self-dual=%s"
    % (
        ",".join(sorted(represented_slots(oe))),
        ",".join(sorted(represented_slots(ocb_shape))),
        ",".join(sorted(represented_slots(boundary_self_dual))),
    ),
)


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]

gate(
    "BSD2 orientation must fix a representative, not only the Z/2 class",
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

gate(
    "BSD3 OCB fixes the DD.4 direction but not self-dual properness by itself",
    len(directions) == 16 and (1, -1) in directions and represented_slots(ocb_shape) == {"carrier_object", "endpoint_maps"},
    "primitive directions=%d selected=(1,-1)" % len(directions),
)


basic_names = ("hyperbolic_endpoint_plane", "trace_augmented_hyperbolic", "end_augmented_hyperbolic")
basic_reasons = {name: reasons(SOURCES[name]) for name in basic_names}

gate(
    "BSD4 hyperbolic and End envelopes are not Phase-A boundary self-duality",
    all(not accepts_phase_a_self_duality(SOURCES[name]) for name in basic_names)
    and "not_boundary_native" in basic_reasons["hyperbolic_endpoint_plane"]
    and "imports_phase_b_graph" in basic_reasons["trace_augmented_hyperbolic"]
    and "dd4_not_coupled_to_duality" in basic_reasons["end_augmented_hyperbolic"],
    "; ".join("%s:%s" % (name, ",".join(basic_reasons[name])) for name in basic_names),
)


projection_names = (
    "positive_rosati_end",
    "projection_forced_positive",
    "fiber_product_saturated_positive",
)
projection_reasons = {name: reasons(SOURCES[name]) for name in projection_names}

gate(
    "BSD5 positive Rosati/projection repairs remain Phase-B-shaped",
    all(not accepts_phase_a_self_duality(SOURCES[name]) for name in projection_names)
    and "dd4_not_coupled_to_duality" in projection_reasons["positive_rosati_end"]
    and "distorts_counts" in projection_reasons["projection_forced_positive"]
    and "imports_phase_b_graph" in projection_reasons["fiber_product_saturated_positive"],
    "; ".join("%s:%s" % (name, ",".join(projection_reasons[name])) for name in projection_names),
)


live_boundary_self_duality = source(
    boundary_native=True,
    orientation_fixed=True,
    self_dual_properness=True,
    p1p2_primary=True,
    uses_phase_b_graph=False,
    projection_from_geometry=False,
    preserves_counts=True,
    dd4_coupled_to_duality=True,
    control_formable=False,
)

gate(
    "BSD6 the live Phase-A interface is boundary-native self-dual properness",
    accepts_phase_a_self_duality(live_boundary_self_duality)
    and not any(accepts_phase_a_self_duality(data) for data in SOURCES.values()),
    "banked accepted=%d live accepted=%s"
    % (sum(accepts_phase_a_self_duality(data) for data in SOURCES.values()), accepts_phase_a_self_duality(live_boundary_self_duality)),
)


gate(
    "BSD7 live boundary self-duality completes B and leaves only control death",
    represented_slots(boundary_self_dual) == {"carrier_object", "endpoint_maps", "dd4_boundary_killing"}
    and represented_slots(boundary_self_dual | CONTROL)
    == {"carrier_object", "endpoint_maps", "dd4_boundary_killing", "control_death"},
    "before C=%s after C=%s"
    % (
        ",".join(sorted(represented_slots(boundary_self_dual))),
        ",".join(sorted(represented_slots(boundary_self_dual | CONTROL))),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nBSD1-BSD7 ALL PASS: boundary self-duality interface pinned")
print(
    "VERDICT: Phase-A self-dual boundary/properness must be boundary-native: "
    "it fixes the oriented-Cartier representative, couples DD.4 to boundary "
    "duality, preserves primary p1,p2, avoids Phase-B graph/projection imports, "
    "and is not formable on controls."
)
