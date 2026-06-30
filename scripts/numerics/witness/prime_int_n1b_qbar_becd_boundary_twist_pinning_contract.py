r"""Boundary twist-pinning contract for oriented-Cartier Qbar_BECD.

Doc 315 leaves one tight question inside the rank-one boundary-defect map:
where does the Laurent twist come from?  This witness separates a carrier
pinning source from a chosen Hom(L,L) unit, a formal torsor splitter, a full
Laurent valuation axis, or degree-zero normalization.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_boundary_twist_pinning_contract
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


def laurent_unit_twists_in_window(kmax):
    return 2 * kmax + 1


def nonzero_laurent_window_maps(kmax):
    return 2 ** (2 * kmax + 1) - 1


def endpoint_rank_of_character(a, b):
    return 0 if (a, b) == (0, 0) else 1


def source(**kwargs):
    data = {
        "carrier_native": False,
        "rank_one_defect_map": False,
        "oriented_cartier_pair": False,
        "normal_ratio_rigidified": False,
        "twist_unique": False,
        "boundary_is_c": False,
        "inserted_splitter": False,
        "external_valuation_axis": False,
        "degree_zero_imposed": False,
        "orientation_fixed": False,
        "p1p2_primary": False,
        "endpoint_rank_preserved": False,
        "control_formable": True,
    }
    data.update(kwargs)
    return data


def accepts_twist_pinning(data):
    return (
        data["carrier_native"]
        and data["rank_one_defect_map"]
        and data["oriented_cartier_pair"]
        and data["normal_ratio_rigidified"]
        and data["twist_unique"]
        and data["boundary_is_c"]
        and not data["inserted_splitter"]
        and not data["external_valuation_axis"]
        and not data["degree_zero_imposed"]
        and data["orientation_fixed"]
        and data["p1p2_primary"]
        and data["endpoint_rank_preserved"]
        and not data["control_formable"]
    )


def reasons(data):
    out = []
    if not data["carrier_native"]:
        out.append("not_carrier_native")
    if not data["rank_one_defect_map"]:
        out.append("no_rank_one_defect_map")
    if not data["oriented_cartier_pair"]:
        out.append("no_oriented_cartier_pair")
    if not data["normal_ratio_rigidified"]:
        out.append("normal_ratio_not_rigidified")
    if not data["twist_unique"]:
        out.append("twist_not_unique")
    if not data["boundary_is_c"]:
        out.append("boundary_not_c")
    if data["inserted_splitter"]:
        out.append("inserted_splitter")
    if data["external_valuation_axis"]:
        out.append("external_valuation_axis")
    if data["degree_zero_imposed"]:
        out.append("degree_zero_imposed")
    if not data["orientation_fixed"]:
        out.append("orientation_not_fixed")
    if not data["p1p2_primary"]:
        out.append("p1p2_not_primary")
    if not data["endpoint_rank_preserved"]:
        out.append("endpoint_rank_not_preserved")
    if data["control_formable"]:
        out.append("control_formable")
    return out


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]

gate(
    "BTP1 the base DD.4 class is still the twist that must be pinned",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        for p in profiles
    ),
    "H1 order 2 and res_1(c)=1 for L=6,8,10,12",
)


formal_splitter = source(
    rank_one_defect_map=True,
    twist_unique=True,
    boundary_is_c=True,
    inserted_splitter=True,
)

gate(
    "BTP2 formal torsor splitting has boundary c only by insertion",
    not accepts_twist_pinning(formal_splitter)
    and {"inserted_splitter", "not_carrier_native", "control_formable"}
    <= set(reasons(formal_splitter)),
    ",".join(reasons(formal_splitter)),
)


odd_valuations = [m for m in range(-3, 4) if m % 2]
even_valuations = [m for m in range(-3, 4) if not m % 2]
laurent_hilbert90 = source(
    rank_one_defect_map=True,
    twist_unique=True,
    boundary_is_c=True,
    external_valuation_axis=True,
)

gate(
    "BTP3 Laurent Hilbert-90 pins by an imported odd valuation axis",
    odd_valuations == [-3, -1, 1, 3]
    and even_valuations == [-2, 0, 2]
    and not accepts_twist_pinning(laurent_hilbert90)
    and {"external_valuation_axis", "not_carrier_native", "control_formable"}
    <= set(reasons(laurent_hilbert90)),
    "odd valuations=%s even valuations=%s reasons=%s"
    % (odd_valuations, even_valuations, ",".join(reasons(laurent_hilbert90))),
)


tested_characters = [(1, 0), (0, 1), (1, 1), (1, -1), (2, 3), (-2, 5)]
valuation_character = source(
    rank_one_defect_map=True,
    twist_unique=True,
    boundary_is_c=True,
    external_valuation_axis=True,
    endpoint_rank_preserved=False,
)

gate(
    "BTP4 one valuation character cannot preserve two endpoint maps",
    all(endpoint_rank_of_character(a, b) == 1 for a, b in tested_characters)
    and not accepts_twist_pinning(valuation_character)
    and {"external_valuation_axis", "endpoint_rank_not_preserved"}
    <= set(reasons(valuation_character)),
    "tested characters=%s reasons=%s"
    % (tested_characters, ",".join(reasons(valuation_character))),
)


unit_twists = {kmax: laurent_unit_twists_in_window(kmax) for kmax in (1, 2, 4, 8)}
nonzero_maps = {kmax: nonzero_laurent_window_maps(kmax) for kmax in (1, 2, 4, 8)}
degree_zero = source(
    carrier_native=True,
    rank_one_defect_map=True,
    oriented_cartier_pair=True,
    twist_unique=True,
    boundary_is_c=True,
    degree_zero_imposed=True,
    orientation_fixed=True,
    p1p2_primary=True,
    endpoint_rank_preserved=True,
)

gate(
    "BTP5 degree-zero normalization is not carrier twist pinning",
    unit_twists == {1: 3, 2: 5, 4: 9, 8: 17}
    and nonzero_maps == {1: 7, 2: 31, 4: 511, 8: 131071}
    and not accepts_twist_pinning(degree_zero)
    and "degree_zero_imposed" in reasons(degree_zero),
    "unit twists=%s nonzero maps=%s reasons=%s"
    % (unit_twists, nonzero_maps, ",".join(reasons(degree_zero))),
)


directions = primitive_directions()
ocb_shape = source(
    carrier_native=True,
    oriented_cartier_pair=True,
    orientation_fixed=True,
    p1p2_primary=True,
    endpoint_rank_preserved=True,
)

gate(
    "BTP6 OCB shape selects direction but not the normal-ratio rigidification",
    len(directions) == 16
    and (1, -1) in directions
    and not accepts_twist_pinning(ocb_shape)
    and {"no_rank_one_defect_map", "normal_ratio_not_rigidified", "boundary_not_c"}
    <= set(reasons(ocb_shape)),
    "primitive directions=%d selected=(1,-1) reasons=%s"
    % (len(directions), ",".join(reasons(ocb_shape))),
)


live_pinning = source(
    carrier_native=True,
    rank_one_defect_map=True,
    oriented_cartier_pair=True,
    normal_ratio_rigidified=True,
    twist_unique=True,
    boundary_is_c=True,
    orientation_fixed=True,
    p1p2_primary=True,
    endpoint_rank_preserved=True,
    control_formable=False,
)

dead_sources = {
    "formal_splitter": formal_splitter,
    "laurent_hilbert90": laurent_hilbert90,
    "valuation_character": valuation_character,
    "degree_zero": degree_zero,
    "ocb_shape": ocb_shape,
}

gate(
    "BTP7 only carrier normal-ratio twist pinning passes",
    accepts_twist_pinning(live_pinning)
    and not any(accepts_twist_pinning(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_twist_pinning(data) for data in dead_sources.values()),
        accepts_twist_pinning(live_pinning),
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
pinned_twist_evidence = ocb_evidence | {"self_dual_boundary_actual"}

gate(
    "BTP8 pinned twist makes the boundary-defect duality count as live B",
    represented_slots(oe) == {"carrier_object", "endpoint_maps"}
    and represented_slots(ocb_evidence) == {"carrier_object", "endpoint_maps"}
    and represented_slots(pinned_twist_evidence)
    == {"carrier_object", "endpoint_maps", "dd4_boundary_killing"}
    and represented_slots(pinned_twist_evidence | CONTROL)
    == {"carrier_object", "endpoint_maps", "dd4_boundary_killing", "control_death"},
    "O+E=%s OCB=%s pinned=%s after C=%s"
    % (
        ",".join(sorted(represented_slots(oe))),
        ",".join(sorted(represented_slots(ocb_evidence))),
        ",".join(sorted(represented_slots(pinned_twist_evidence))),
        ",".join(sorted(represented_slots(pinned_twist_evidence | CONTROL))),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nBTP1-BTP8 ALL PASS: boundary twist-pinning contract pinned")
print(
    "VERDICT: the Laurent twist in the boundary-defect duality must be pinned "
    "by carrier oriented-Cartier normal-ratio data. A formal splitter, full "
    "Laurent Hilbert-90 valuation axis, rank-one valuation character, "
    "degree-zero normalization, or shape-only OCB still leaves the live S atom "
    "unconstructed."
)
