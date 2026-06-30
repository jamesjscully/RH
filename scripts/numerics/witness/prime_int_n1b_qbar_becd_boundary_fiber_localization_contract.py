r"""Endpoint boundary-fiber localization contract for Qbar_BECD.

Doc 318 says D1,D2 must be actual Cartier boundary fibers of p1,p2 inside dQ.
This witness sharpens the exactness requirement: the localization sequence
must be a single carrier sequence on dQ that restricts to both endpoint
fibers and sends the original DD.4 representative to zero. Formal acyclic
replacement, bar/cone boundaries, jet deletion, obstruction quotient, and
declared localization do not count.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_boundary_fiber_localization_contract
"""

from math import comb


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


def source(**kwargs):
    data = {
        "carrier_native": False,
        "p1p2_primary": False,
        "p1_boundary_fiber_actual": False,
        "p2_boundary_fiber_actual": False,
        "boundary_fibers_cartier": False,
        "single_localization_on_dq": False,
        "restricts_to_p1_fiber": False,
        "restricts_to_p2_fiber": False,
        "common_sequence_for_ratio": False,
        "connecting_map_sends_c_to_zero": False,
        "preserves_c_as_class": False,
        "normal_ratio_boundary": False,
        "self_dual_properness": False,
        "endpoint_rank_preserved": False,
        "formal_acyclic_replacement": False,
        "formal_nullhomotopy": False,
        "deletes_obstruction": False,
        "quotients_obstruction": False,
        "declared_localization": False,
        "separate_fiber_sequences": False,
        "control_formable": True,
    }
    data.update(kwargs)
    return data


def accepts_localization(data):
    return (
        data["carrier_native"]
        and data["p1p2_primary"]
        and data["p1_boundary_fiber_actual"]
        and data["p2_boundary_fiber_actual"]
        and data["boundary_fibers_cartier"]
        and data["single_localization_on_dq"]
        and data["restricts_to_p1_fiber"]
        and data["restricts_to_p2_fiber"]
        and data["common_sequence_for_ratio"]
        and data["connecting_map_sends_c_to_zero"]
        and data["preserves_c_as_class"]
        and data["normal_ratio_boundary"]
        and data["self_dual_properness"]
        and data["endpoint_rank_preserved"]
        and not data["formal_acyclic_replacement"]
        and not data["formal_nullhomotopy"]
        and not data["deletes_obstruction"]
        and not data["quotients_obstruction"]
        and not data["declared_localization"]
        and not data["separate_fiber_sequences"]
        and not data["control_formable"]
    )


def reasons(data):
    out = []
    for key, label in (
        ("carrier_native", "not_carrier_native"),
        ("p1p2_primary", "p1p2_not_primary"),
        ("p1_boundary_fiber_actual", "p1_boundary_fiber_not_actual"),
        ("p2_boundary_fiber_actual", "p2_boundary_fiber_not_actual"),
        ("boundary_fibers_cartier", "boundary_fibers_not_cartier"),
        ("single_localization_on_dq", "no_single_localization_on_dq"),
        ("restricts_to_p1_fiber", "does_not_restrict_to_p1"),
        ("restricts_to_p2_fiber", "does_not_restrict_to_p2"),
        ("common_sequence_for_ratio", "no_common_sequence_for_ratio"),
        ("connecting_map_sends_c_to_zero", "c_not_mapped_to_zero"),
        ("preserves_c_as_class", "c_not_preserved_as_class"),
        ("normal_ratio_boundary", "normal_ratio_not_boundary"),
        ("self_dual_properness", "no_self_dual_properness"),
        ("endpoint_rank_preserved", "endpoint_rank_not_preserved"),
    ):
        if not data[key]:
            out.append(label)
    if data["formal_acyclic_replacement"]:
        out.append("formal_acyclic_replacement")
    if data["formal_nullhomotopy"]:
        out.append("formal_nullhomotopy")
    if data["deletes_obstruction"]:
        out.append("deletes_obstruction")
    if data["quotients_obstruction"]:
        out.append("quotients_obstruction")
    if data["declared_localization"]:
        out.append("declared_localization")
    if data["separate_fiber_sequences"]:
        out.append("separate_fiber_sequences")
    if data["control_formable"]:
        out.append("control_formable")
    return out


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]

gate(
    "BFL1 c must be mapped to zero, not deleted or replaced",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        for p in profiles
    ),
    "H1 order 2 and res_1(c)=1 for L=6,8,10,12",
)


oe = OBJECT | ENDPOINT
fiber_shape = oe | {
    "p1_boundary_fiber_actual",
    "p2_boundary_fiber_actual",
    "cartier_fiber_shape",
}
live_localization_evidence = oe | BOUNDARY | {
    "p1_boundary_fiber_actual",
    "p2_boundary_fiber_actual",
    "restricted_localization_actual",
}

gate(
    "BFL2 endpoint fibers without restricted localization are not B",
    represented_slots(oe) == {"carrier_object", "endpoint_maps"}
    and represented_slots(fiber_shape) == {"carrier_object", "endpoint_maps"}
    and represented_slots(live_localization_evidence)
    == {"carrier_object", "endpoint_maps", "dd4_boundary_killing"},
    "O+E=%s fiber-shape=%s live=%s"
    % (
        ",".join(sorted(represented_slots(oe))),
        ",".join(sorted(represented_slots(fiber_shape))),
        ",".join(sorted(represented_slots(live_localization_evidence))),
    ),
)


formal_resolution = source(
    formal_acyclic_replacement=True,
    connecting_map_sends_c_to_zero=True,
)

gate(
    "BFL3 coinduced/bar acyclic replacement is not carrier localization",
    not accepts_localization(formal_resolution)
    and {
        "formal_acyclic_replacement",
        "not_carrier_native",
        "p1_boundary_fiber_not_actual",
        "control_formable",
    }
    <= set(reasons(formal_resolution)),
    ",".join(reasons(formal_resolution)),
)


cone_nullhomotopy = source(
    formal_nullhomotopy=True,
    connecting_map_sends_c_to_zero=True,
    preserves_c_as_class=False,
)

gate(
    "BFL4 cone nullhomotopy declares dh=c instead of restricting localization",
    not accepts_localization(cone_nullhomotopy)
    and {"formal_nullhomotopy", "c_not_preserved_as_class", "control_formable"}
    <= set(reasons(cone_nullhomotopy)),
    ",".join(reasons(cone_nullhomotopy)),
)


jet_deletion = source(
    deletes_obstruction=True,
    connecting_map_sends_c_to_zero=False,
    preserves_c_as_class=False,
)
obstruction_quotient = source(
    quotients_obstruction=True,
    connecting_map_sends_c_to_zero=False,
    preserves_c_as_class=False,
)

gate(
    "BFL5 deletion and quotient do not map the original class to zero",
    not accepts_localization(jet_deletion)
    and not accepts_localization(obstruction_quotient)
    and {"deletes_obstruction", "c_not_mapped_to_zero", "c_not_preserved_as_class"}
    <= set(reasons(jet_deletion))
    and {"quotients_obstruction", "c_not_mapped_to_zero", "c_not_preserved_as_class"}
    <= set(reasons(obstruction_quotient)),
    "jet=%s quotient=%s"
    % (",".join(reasons(jet_deletion)), ",".join(reasons(obstruction_quotient))),
)


declared_localization = source(
    carrier_native=True,
    p1p2_primary=True,
    p1_boundary_fiber_actual=True,
    p2_boundary_fiber_actual=True,
    boundary_fibers_cartier=True,
    connecting_map_sends_c_to_zero=True,
    preserves_c_as_class=True,
    endpoint_rank_preserved=True,
    declared_localization=True,
)

gate(
    "BFL6 declared localization is not exact restriction to endpoint fibers",
    not accepts_localization(declared_localization)
    and {
        "no_single_localization_on_dq",
        "does_not_restrict_to_p1",
        "does_not_restrict_to_p2",
        "declared_localization",
    }
    <= set(reasons(declared_localization)),
    ",".join(reasons(declared_localization)),
)


separate_fiber_sequences = source(
    carrier_native=True,
    p1p2_primary=True,
    p1_boundary_fiber_actual=True,
    p2_boundary_fiber_actual=True,
    boundary_fibers_cartier=True,
    restricts_to_p1_fiber=True,
    restricts_to_p2_fiber=True,
    connecting_map_sends_c_to_zero=True,
    preserves_c_as_class=True,
    endpoint_rank_preserved=True,
    separate_fiber_sequences=True,
)

gate(
    "BFL7 separate fiber exact sequences do not give the ordered normal ratio",
    not accepts_localization(separate_fiber_sequences)
    and {
        "no_single_localization_on_dq",
        "no_common_sequence_for_ratio",
        "normal_ratio_not_boundary",
        "separate_fiber_sequences",
    }
    <= set(reasons(separate_fiber_sequences)),
    ",".join(reasons(separate_fiber_sequences)),
)


control_lookalike = source(
    p1p2_primary=True,
    p1_boundary_fiber_actual=True,
    p2_boundary_fiber_actual=True,
    boundary_fibers_cartier=True,
    single_localization_on_dq=True,
    restricts_to_p1_fiber=True,
    restricts_to_p2_fiber=True,
    common_sequence_for_ratio=True,
    connecting_map_sends_c_to_zero=True,
    preserves_c_as_class=True,
    normal_ratio_boundary=True,
    self_dual_properness=True,
    endpoint_rank_preserved=True,
    control_formable=True,
)

gate(
    "BFL8 localization-looking control package still fails carrier nativity",
    not accepts_localization(control_lookalike)
    and {"not_carrier_native", "control_formable"} <= set(reasons(control_lookalike)),
    ",".join(reasons(control_lookalike)),
)


live_localization = source(
    carrier_native=True,
    p1p2_primary=True,
    p1_boundary_fiber_actual=True,
    p2_boundary_fiber_actual=True,
    boundary_fibers_cartier=True,
    single_localization_on_dq=True,
    restricts_to_p1_fiber=True,
    restricts_to_p2_fiber=True,
    common_sequence_for_ratio=True,
    connecting_map_sends_c_to_zero=True,
    preserves_c_as_class=True,
    normal_ratio_boundary=True,
    self_dual_properness=True,
    endpoint_rank_preserved=True,
    control_formable=False,
)

dead_sources = {
    "formal_resolution": formal_resolution,
    "cone_nullhomotopy": cone_nullhomotopy,
    "jet_deletion": jet_deletion,
    "obstruction_quotient": obstruction_quotient,
    "declared_localization": declared_localization,
    "separate_fiber_sequences": separate_fiber_sequences,
    "control_lookalike": control_lookalike,
}

gate(
    "BFL9 only carrier restricted fiber localization passes",
    accepts_localization(live_localization)
    and not any(accepts_localization(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_localization(data) for data in dead_sources.values()),
        accepts_localization(live_localization),
    ),
)


gate(
    "BFL10 restricted fiber localization completes B and leaves controls",
    represented_slots(live_localization_evidence)
    == {"carrier_object", "endpoint_maps", "dd4_boundary_killing"}
    and represented_slots(live_localization_evidence | CONTROL)
    == {"carrier_object", "endpoint_maps", "dd4_boundary_killing", "control_death"},
    "before C=%s after C=%s"
    % (
        ",".join(sorted(represented_slots(live_localization_evidence))),
        ",".join(sorted(represented_slots(live_localization_evidence | CONTROL))),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nBFL1-BFL10 ALL PASS: boundary-fiber localization contract pinned")
print(
    "VERDICT: exactness must be a carrier localization sequence on dQ that "
    "restricts to both endpoint boundary fibers and maps the original DD.4 "
    "representative to zero through their ordered normal ratio. Formal "
    "acyclic replacement, cone nullhomotopy, deletion, quotient, declared "
    "localization, separate fiber sequences, and control-formable lookalikes "
    "do not meet this contract."
)
