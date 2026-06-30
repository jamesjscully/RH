r"""Boundary pushforward-compatibility contract for Qbar_BECD.

Doc 319 pins exactness: one carrier localization sequence on dQ must restrict
to the actual p1,p2 boundary fibers and send the original DD.4 representative
to zero. This witness sharpens the next interface: that restricted boundary
localization must commute with the primary endpoint proper pushforwards. A
detached boundary null-homotopy, symbolic composition package, formal adjoint
package, projection quotient, or local degree retuning does not count.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_boundary_pushforward_compat_contract
"""

from __future__ import annotations

from math import comb

import numpy as np

from scripts.numerics.witness.ns_diagonal_representability import (
    frobenius,
    ns_intersection,
    rosati,
    weil_pairing,
)


failures: list[str] = []

Corr = tuple[float, np.ndarray, float]


def gate(name: str, ok: bool, detail: str = "") -> None:
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
BE_COMPAT = {
    "p1_boundary_pushforward_commutes",
    "p2_boundary_pushforward_commutes",
    "endpoint_degree_maps_preserved",
    "finite_field_count_anchor_preserved",
}
CONTROL = {"control_instantiation_impossible", "control_death_at_formation_proved"}


def represented_slots(evidence: set[str]) -> set[str]:
    slots = set()
    if OBJECT <= evidence:
        slots.add("carrier_object")
    if ENDPOINT <= evidence:
        slots.add("endpoint_maps")
    if BOUNDARY <= evidence:
        slots.add("dd4_boundary_killing")
    if BE_COMPAT <= evidence:
        slots.add("boundary_endpoint_pushforward_compat")
    if CONTROL <= evidence:
        slots.add("control_death")
    return slots


def make(L: int):
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


def to_vec(f, L: int) -> tuple[int, ...]:
    return tuple(f.get(k, 0) for k in range(1, L + 1))


def from_vec(v):
    out = {0: 1}
    for i, bit in enumerate(v, start=1):
        if bit:
            out[i] = 1
    return out


def closure(gens, L: int, mul) -> set[tuple[int, ...]]:
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


def h1_profile(L: int) -> dict[str, int | bool]:
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
        "h1_order": z1_order // len(coboundaries),
    }


def corr(d1: float, z: np.ndarray, d2: float) -> Corr:
    return (float(d1), z, float(d2))


def delta(F: np.ndarray) -> Corr:
    return corr(1.0, np.eye(F.shape[0]), 1.0)


def graph(F: np.ndarray, q: float, n: int) -> Corr:
    return corr(q**n, np.linalg.matrix_power(F, n), 1.0)


def compose(A: Corr, B: Corr) -> Corr:
    d1, z, d2 = A
    e1, w, e2 = B
    return corr(d1 * e1, z @ w, d2 * e2)


def dagger(A: Corr, E: np.ndarray) -> Corr:
    d1, z, d2 = A
    return corr(d2, rosati(z, E), d1)


def projection_sides(A: Corr, B: Corr, C: Corr, E: np.ndarray) -> tuple[float, float]:
    lhs = ns_intersection(compose(A, B), C)
    rhs = ns_intersection(B, compose(dagger(A, E), C))
    return float(lhs), float(rhs)


def projection_defect(A: Corr, B: Corr, C: Corr, E: np.ndarray) -> float:
    lhs, rhs = projection_sides(A, B, C, E)
    return abs(lhs - rhs)


def trace_power(F: np.ndarray, n: int) -> float:
    return float(np.trace(np.linalg.matrix_power(F, n)).real)


def point_count(F: np.ndarray, q: float, n: int) -> float:
    return float(q**n + 1.0 - trace_power(F, n))


def retune_first_degree_for_projection(A: Corr, B: Corr, C: Corr, E: np.ndarray) -> Corr:
    product = compose(A, B)
    lhs, rhs = projection_sides(A, B, C, E)
    return corr(product[0] + (rhs - lhs) / C[2], product[1], product[2])


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
        "p1_pushforward_actual": False,
        "p2_pushforward_actual": False,
        "commutes_with_p1_pushforward": False,
        "commutes_with_p2_pushforward": False,
        "endpoint_degree_maps_primary": False,
        "p1_degree_preserved": False,
        "p2_degree_preserved": False,
        "finite_field_count_anchor_preserved": False,
        "graph_degree_anchor_preserved": False,
        "same_carrier_as_endpoint_maps": False,
        "symbolic_composition_substitute": False,
        "formal_adjoint_substitute": False,
        "projection_quotient_or_retuning": False,
        "declared_pushforward_square": False,
        "detached_boundary_exactness": False,
        "control_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
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
    ("p1_pushforward_actual", "p1_pushforward_not_actual"),
    ("p2_pushforward_actual", "p2_pushforward_not_actual"),
    ("commutes_with_p1_pushforward", "p1_pushforward_square_not_commuting"),
    ("commutes_with_p2_pushforward", "p2_pushforward_square_not_commuting"),
    ("endpoint_degree_maps_primary", "endpoint_degree_maps_not_primary"),
    ("p1_degree_preserved", "p1_degree_not_preserved"),
    ("p2_degree_preserved", "p2_degree_not_preserved"),
    ("finite_field_count_anchor_preserved", "finite_field_count_anchor_not_preserved"),
    ("graph_degree_anchor_preserved", "graph_degree_anchor_not_preserved"),
    ("same_carrier_as_endpoint_maps", "not_same_carrier_as_endpoint_maps"),
)


BANNED = (
    ("symbolic_composition_substitute", "symbolic_composition_substitute"),
    ("formal_adjoint_substitute", "formal_adjoint_substitute"),
    ("projection_quotient_or_retuning", "projection_quotient_or_retuning"),
    ("declared_pushforward_square", "declared_pushforward_square"),
    ("detached_boundary_exactness", "detached_boundary_exactness"),
    ("control_formable", "control_formable"),
)


def accepts_pushforward_compat(data) -> bool:
    return all(data[key] for key, _ in REQUIRED) and not any(
        data[key] for key, _ in BANNED
    )


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    out.extend(label for key, label in BANNED if data[key])
    return out


def live_source(**kwargs):
    data = source(
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
        p1_pushforward_actual=True,
        p2_pushforward_actual=True,
        commutes_with_p1_pushforward=True,
        commutes_with_p2_pushforward=True,
        endpoint_degree_maps_primary=True,
        p1_degree_preserved=True,
        p2_degree_preserved=True,
        finite_field_count_anchor_preserved=True,
        graph_degree_anchor_preserved=True,
        same_carrier_as_endpoint_maps=True,
        control_formable=False,
    )
    data.update(kwargs)
    return data


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]

gate(
    "BPC1 original DD.4 class remains the class pushed through the square",
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
bfl = oe | BOUNDARY | {
    "p1_boundary_fiber_actual",
    "p2_boundary_fiber_actual",
    "restricted_localization_actual",
}
compatible = bfl | BE_COMPAT

gate(
    "BPC2 doc-319 localization does not yet give endpoint pushforward compat",
    represented_slots(bfl) == {"carrier_object", "endpoint_maps", "dd4_boundary_killing"}
    and represented_slots(compatible)
    == {
        "carrier_object",
        "endpoint_maps",
        "dd4_boundary_killing",
        "boundary_endpoint_pushforward_compat",
    },
    "before=%s after=%s"
    % (
        ",".join(sorted(represented_slots(bfl))),
        ",".join(sorted(represented_slots(compatible))),
    ),
)


detached_boundary = live_source(
    p1_pushforward_actual=False,
    p2_pushforward_actual=False,
    commutes_with_p1_pushforward=False,
    commutes_with_p2_pushforward=False,
    endpoint_degree_maps_primary=False,
    p1_degree_preserved=False,
    p2_degree_preserved=False,
    finite_field_count_anchor_preserved=False,
    graph_degree_anchor_preserved=False,
    same_carrier_as_endpoint_maps=False,
    detached_boundary_exactness=True,
)

gate(
    "BPC3 detached boundary exactness is not square endpoint compatibility",
    not accepts_pushforward_compat(detached_boundary)
    and {
        "p1_pushforward_not_actual",
        "p2_pushforward_not_actual",
        "p1_pushforward_square_not_commuting",
        "p2_pushforward_square_not_commuting",
        "detached_boundary_exactness",
    }
    <= set(reasons(detached_boundary)),
    ",".join(reasons(detached_boundary)),
)


symbolic_composition = live_source(
    commutes_with_p1_pushforward=False,
    commutes_with_p2_pushforward=False,
    same_carrier_as_endpoint_maps=False,
    symbolic_composition_substitute=True,
)

gate(
    "BPC4 symbolic composition cannot replace pushforward commutation",
    not accepts_pushforward_compat(symbolic_composition)
    and {
        "p1_pushforward_square_not_commuting",
        "p2_pushforward_square_not_commuting",
        "not_same_carrier_as_endpoint_maps",
        "symbolic_composition_substitute",
    }
    <= set(reasons(symbolic_composition)),
    ",".join(reasons(symbolic_composition)),
)


formal_adjoint = live_source(
    commutes_with_p1_pushforward=False,
    commutes_with_p2_pushforward=False,
    endpoint_degree_maps_primary=False,
    graph_degree_anchor_preserved=False,
    formal_adjoint_substitute=True,
)

gate(
    "BPC5 formal adjoint/Rosati data cannot replace endpoint pushforwards",
    not accepts_pushforward_compat(formal_adjoint)
    and {
        "p1_pushforward_square_not_commuting",
        "p2_pushforward_square_not_commuting",
        "endpoint_degree_maps_not_primary",
        "graph_degree_anchor_not_preserved",
        "formal_adjoint_substitute",
    }
    <= set(reasons(formal_adjoint)),
    ",".join(reasons(formal_adjoint)),
)


q_true = 7
F_true = frobenius(q_true, 1)
E_true = weil_pairing(F_true, q_true)
D_true = delta(F_true)
G_true = graph(F_true, q_true, 1)
projection_11 = projection_defect(G_true, D_true, G_true, E_true)
actual_count2 = point_count(F_true, q_true, 2)
forced_count2 = q_true**2 + 1.0 - 2.0 * q_true
retuned_G = retune_first_degree_for_projection(G_true, D_true, G_true, E_true)
projection_quotient = live_source(
    finite_field_count_anchor_preserved=False,
    graph_degree_anchor_preserved=False,
    projection_quotient_or_retuning=True,
)

gate(
    "BPC6 projection quotient/retuning destroys count or graph-degree anchors",
    not accepts_pushforward_compat(projection_quotient)
    and projection_11 == 27.0
    and actual_count2 == 63.0
    and forced_count2 == 36.0
    and retuned_G[0] == -20.0
    and {
        "finite_field_count_anchor_not_preserved",
        "graph_degree_anchor_not_preserved",
        "projection_quotient_or_retuning",
    }
    <= set(reasons(projection_quotient)),
    "projection_defect=%.1f count2 %.1f->%.1f retuned_d1=%.1f"
    % (projection_11, actual_count2, forced_count2, retuned_G[0]),
)


declared_square = live_source(
    commutes_with_p1_pushforward=False,
    commutes_with_p2_pushforward=False,
    declared_pushforward_square=True,
)

gate(
    "BPC7 declared Beck-Chevalley square is not constructed commutation",
    not accepts_pushforward_compat(declared_square)
    and {
        "p1_pushforward_square_not_commuting",
        "p2_pushforward_square_not_commuting",
        "declared_pushforward_square",
    }
    <= set(reasons(declared_square)),
    ",".join(reasons(declared_square)),
)


control_lookalike = live_source(carrier_native=False, control_formable=True)

gate(
    "BPC8 pushforward-compatible control lookalike still fails carrier nativity",
    not accepts_pushforward_compat(control_lookalike)
    and {"not_carrier_native", "control_formable"} <= set(reasons(control_lookalike)),
    ",".join(reasons(control_lookalike)),
)


rank_degree_failures = [
    live_source(endpoint_rank_preserved=False),
    live_source(p1_degree_preserved=False),
    live_source(p2_degree_preserved=False),
    live_source(finite_field_count_anchor_preserved=False),
    live_source(graph_degree_anchor_preserved=False),
]

gate(
    "BPC9 endpoint rank, degree, count, and graph anchors are mandatory",
    not any(accepts_pushforward_compat(data) for data in rank_degree_failures)
    and {
        "endpoint_rank_not_preserved",
        "p1_degree_not_preserved",
        "p2_degree_not_preserved",
        "finite_field_count_anchor_not_preserved",
        "graph_degree_anchor_not_preserved",
    }
    <= set().union(*(set(reasons(data)) for data in rank_degree_failures)),
    "failures=%s"
    % sorted(set().union(*(set(reasons(data)) for data in rank_degree_failures))),
)


live_compatibility = live_source()
dead_sources = {
    "detached_boundary": detached_boundary,
    "symbolic_composition": symbolic_composition,
    "formal_adjoint": formal_adjoint,
    "projection_quotient": projection_quotient,
    "declared_square": declared_square,
    "control_lookalike": control_lookalike,
}

gate(
    "BPC10 only carrier boundary-localization pushforward compatibility passes",
    accepts_pushforward_compat(live_compatibility)
    and not any(accepts_pushforward_compat(data) for data in dead_sources.values())
    and represented_slots(compatible)
    == {
        "carrier_object",
        "endpoint_maps",
        "dd4_boundary_killing",
        "boundary_endpoint_pushforward_compat",
    }
    and represented_slots(compatible | CONTROL)
    == {
        "carrier_object",
        "endpoint_maps",
        "dd4_boundary_killing",
        "boundary_endpoint_pushforward_compat",
        "control_death",
    },
    "dead accepted=%d before C=%s after C=%s"
    % (
        sum(accepts_pushforward_compat(data) for data in dead_sources.values()),
        ",".join(sorted(represented_slots(compatible))),
        ",".join(sorted(represented_slots(compatible | CONTROL))),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nBPC1-BPC10 ALL PASS: boundary-pushforward compatibility contract pinned")
print(
    "VERDICT: the restricted dQ localization must commute with the actual "
    "p1_*,p2_* endpoint pushforwards in the same carrier, preserving endpoint "
    "rank, degree maps, finite-field counts, and graph degrees. Detached "
    "boundary exactness, symbolic composition, formal adjoints, declared "
    "squares, projection quotients/retunings, and control-formable lookalikes "
    "do not meet this contract."
)
