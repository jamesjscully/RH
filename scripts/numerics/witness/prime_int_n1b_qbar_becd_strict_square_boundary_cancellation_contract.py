r"""Boundary-cancellation contract for the strict-square signed character.

Doc 328 requires a carrier-native effectivity orientation that retains the
signed zero fiber as boundary/cancellation data.  This witness sharpens that
requirement: the signed cancellation must map to the DD.4 boundary
localization inside Qbar_BECD.  Weighted zero, positive/negative splitting,
Grothendieck group bookkeeping, formal attached cells, endpoint kernels, and
declared boundary maps do not construct the boundary-cancellation functor.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_strict_square_boundary_cancellation_contract
"""

from __future__ import annotations


failures: list[str] = []

REQUIRED_EDGES = {
    ("signed_character_algebra", "signed_zero_fiber"),
    ("signed_zero_fiber", "boundary_cancellation_functor"),
    ("boundary_cancellation_functor", "dd4_boundary_map"),
    ("dd4_boundary_map", "boundary_localization"),
    ("positive_cone", "internal_effectivity_domain"),
    ("boundary_localization", "internal_effectivity_domain"),
    ("character_convolution", "cancellation_module"),
    ("cancellation_module", "boundary_cancellation_functor"),
    ("internal_effectivity_domain", "endpoint"),
    ("boundary_localization", "pushforward"),
    ("endpoint", "pushforward"),
    ("pushforward", "graph"),
    ("graph", "rosati"),
    ("graph", "count_degree"),
    ("internal_effectivity_domain", "control_death"),
}


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def normalize(chi: dict[int, int]) -> dict[int, int]:
    return {key: val for key, val in sorted(chi.items()) if val != 0}


def chi_col(a, b, edges) -> dict[int, int]:
    out: dict[int, int] = {}
    for j, bj in enumerate(b):
        aj = sum(a[i] for i, jj in edges if jj == j)
        if bj != 0 and aj != 0:
            out[aj] = out.get(aj, 0) + bj
    return normalize(out)


def convolve_chi(left: dict[int, int], right: dict[int, int]) -> dict[int, int]:
    out: dict[int, int] = {}
    for a, ca in left.items():
        for b, cb in right.items():
            out[a * b] = out.get(a * b, 0) + ca * cb
    return normalize(out)


def positive_negative_split(chi: dict[int, int]) -> tuple[dict[int, int], dict[int, int]]:
    pos = {key: val for key, val in chi.items() if val > 0}
    neg = {key: -val for key, val in chi.items() if val < 0}
    return normalize(pos), normalize(neg)


def weighted_mass(chi: dict[int, int]) -> int:
    return sum(key * val for key, val in chi.items())


def positive_mass(chi: dict[int, int]) -> int:
    pos, _ = positive_negative_split(chi)
    return sum(key * val for key, val in pos.items())


def negative_mass(chi: dict[int, int]) -> int:
    _, neg = positive_negative_split(chi)
    return sum(key * val for key, val in neg.items())


def group_completion_pair(chi: dict[int, int]) -> tuple[tuple[tuple[int, int], ...], tuple[tuple[int, int], ...]]:
    pos, neg = positive_negative_split(chi)
    return tuple(pos.items()), tuple(neg.items())


def endpoint_degree_kernel(chi: dict[int, int]) -> bool:
    return weighted_mass(chi) == 0


def source(**kwargs):
    data = {
        "carrier_native": False,
        "strict_square_signed_character_actual": False,
        "signed_zero_fiber_actual": False,
        "boundary_cancellation_functor_actual": False,
        "dd4_boundary_map_actual": False,
        "represented_square_boundary_edges": False,
        "cancellation_not_just_weight_zero": False,
        "positive_negative_split_retained": False,
        "cancellation_convolution_module_compatible": False,
        "maps_cancellation_to_boundary_localization": False,
        "maps_boundary_to_internal_effectivity_domain": False,
        "generates_endpoint_integrality": False,
        "generates_pushforward_compatibility": False,
        "generates_graph_rosati_count": False,
        "generates_control_death": False,
        "controls_undefined_at_boundary": False,
        "dh_undefined_at_boundary": False,
        "epstein_undefined_at_boundary": False,
        "required_edges": set(),
        "weighted_sum_zero_selector": False,
        "positive_negative_split_only": False,
        "grothendieck_group_completion": False,
        "formal_boundary_cell": False,
        "external_chain_complex": False,
        "diagonal_total_zero_selector": False,
        "endpoint_kernel_definition": False,
        "declared_boundary_cancellation": False,
        "boundary_afterthought_filter": False,
        "control_formable": True,
        "dh_formable": True,
        "epstein_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("strict_square_signed_character_actual", "strict_square_signed_character_missing"),
    ("signed_zero_fiber_actual", "signed_zero_fiber_missing"),
    (
        "boundary_cancellation_functor_actual",
        "boundary_cancellation_functor_not_actual",
    ),
    ("dd4_boundary_map_actual", "dd4_boundary_map_not_actual"),
    ("represented_square_boundary_edges", "represented_square_boundary_edges_missing"),
    (
        "cancellation_not_just_weight_zero",
        "cancellation_reduced_to_weight_zero",
    ),
    ("positive_negative_split_retained", "positive_negative_split_not_retained"),
    (
        "cancellation_convolution_module_compatible",
        "cancellation_not_convolution_module_compatible",
    ),
    (
        "maps_cancellation_to_boundary_localization",
        "cancellation_not_mapped_to_boundary_localization",
    ),
    (
        "maps_boundary_to_internal_effectivity_domain",
        "boundary_not_mapped_to_internal_effectivity_domain",
    ),
    ("generates_endpoint_integrality", "endpoint_integrality_not_generated"),
    (
        "generates_pushforward_compatibility",
        "pushforward_compatibility_not_generated",
    ),
    ("generates_graph_rosati_count", "graph_rosati_count_not_generated"),
    ("generates_control_death", "control_death_not_generated"),
    ("controls_undefined_at_boundary", "controls_not_undefined_at_boundary"),
    ("dh_undefined_at_boundary", "dh_not_undefined_at_boundary"),
    ("epstein_undefined_at_boundary", "epstein_not_undefined_at_boundary"),
)

BANNED = (
    ("weighted_sum_zero_selector", "weighted_sum_zero_selector"),
    ("positive_negative_split_only", "positive_negative_split_only"),
    ("grothendieck_group_completion", "grothendieck_group_completion"),
    ("formal_boundary_cell", "formal_boundary_cell"),
    ("external_chain_complex", "external_chain_complex"),
    ("diagonal_total_zero_selector", "diagonal_total_zero_selector"),
    ("endpoint_kernel_definition", "endpoint_kernel_definition"),
    ("declared_boundary_cancellation", "declared_boundary_cancellation"),
    ("boundary_afterthought_filter", "boundary_afterthought_filter"),
    ("control_formable", "control_formable"),
    ("dh_formable", "dh_formable"),
    ("epstein_formable", "epstein_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_EDGES <= set(data["required_edges"]):
        out.append("required_boundary_cancellation_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_boundary_cancellation(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        strict_square_signed_character_actual=True,
        signed_zero_fiber_actual=True,
        boundary_cancellation_functor_actual=True,
        dd4_boundary_map_actual=True,
        represented_square_boundary_edges=True,
        cancellation_not_just_weight_zero=True,
        positive_negative_split_retained=True,
        cancellation_convolution_module_compatible=True,
        maps_cancellation_to_boundary_localization=True,
        maps_boundary_to_internal_effectivity_domain=True,
        generates_endpoint_integrality=True,
        generates_pushforward_compatibility=True,
        generates_graph_rosati_count=True,
        generates_control_death=True,
        controls_undefined_at_boundary=True,
        dh_undefined_at_boundary=True,
        epstein_undefined_at_boundary=True,
        required_edges=set(REQUIRED_EDGES),
        control_formable=False,
        dh_formable=False,
        epstein_formable=False,
    )
    data.update(kwargs)
    return data


L = ((1, 1), (1, 1), ((0, 0), (0, 1), (1, 0)))
C3 = ((3,), (1,), ((0, 0),))
F22 = ((2,), (2,), ((0, 0),))
ZERO_SPLIT = ((1, 2), (2, -1), ((0, 0), (1, 1)))

chi_L = chi_col(*L)
chi_C3 = chi_col(*C3)
chi_F22 = chi_col(*F22)
chi_zero = chi_col(*ZERO_SPLIT)
chi_zero_times_F22 = convolve_chi(chi_zero, chi_F22)

gate(
    "BCC1 signed zero fiber is balanced but has convolutional boundary content",
    chi_zero == {1: 2, 2: -1}
    and positive_negative_split(chi_zero) == ({1: 2}, {2: 1})
    and weighted_mass(chi_zero) == 0
    and positive_mass(chi_zero) == negative_mass(chi_zero) == 2
    and chi_zero_times_F22 == {2: 4, 4: -2}
    and weighted_mass(chi_zero_times_F22) == 0
    and positive_mass(chi_zero_times_F22) == negative_mass(chi_zero_times_F22) == 8,
    "zero=%s split=%s zero*F22=%s"
    % (chi_zero, positive_negative_split(chi_zero), chi_zero_times_F22),
)


weight_zero = live_source(
    boundary_cancellation_functor_actual=False,
    dd4_boundary_map_actual=False,
    represented_square_boundary_edges=False,
    cancellation_not_just_weight_zero=False,
    maps_cancellation_to_boundary_localization=False,
    weighted_sum_zero_selector=True,
    diagonal_total_zero_selector=True,
    control_formable=True,
    dh_formable=True,
    epstein_formable=True,
)

gate(
    "BCC2 weighted-zero selectors do not construct DD.4 boundary data",
    weighted_mass(chi_zero) == 0
    and weighted_mass(chi_zero_times_F22) == 0
    and endpoint_degree_kernel(chi_zero)
    and not accepts_boundary_cancellation(weight_zero)
    and {
        "boundary_cancellation_functor_not_actual",
        "dd4_boundary_map_not_actual",
        "represented_square_boundary_edges_missing",
        "cancellation_reduced_to_weight_zero",
        "cancellation_not_mapped_to_boundary_localization",
        "weighted_sum_zero_selector",
        "diagonal_total_zero_selector",
        "control_formable",
        "dh_formable",
        "epstein_formable",
    }
    <= set(reasons(weight_zero)),
    ",".join(reasons(weight_zero)),
)


split_only = live_source(
    boundary_cancellation_functor_actual=False,
    dd4_boundary_map_actual=False,
    represented_square_boundary_edges=False,
    maps_cancellation_to_boundary_localization=False,
    maps_boundary_to_internal_effectivity_domain=False,
    positive_negative_split_only=True,
    control_formable=True,
)

gate(
    "BCC3 positive/negative splitting is only bookkeeping",
    group_completion_pair(chi_zero) == (((1, 2),), ((2, 1),))
    and positive_mass(chi_zero) == negative_mass(chi_zero)
    and not accepts_boundary_cancellation(split_only)
    and {
        "boundary_cancellation_functor_not_actual",
        "dd4_boundary_map_not_actual",
        "represented_square_boundary_edges_missing",
        "cancellation_not_mapped_to_boundary_localization",
        "boundary_not_mapped_to_internal_effectivity_domain",
        "positive_negative_split_only",
        "control_formable",
    }
    <= set(reasons(split_only)),
    "pair=%s reasons=%s" % (group_completion_pair(chi_zero), ",".join(reasons(split_only))),
)


group_completion = live_source(
    boundary_cancellation_functor_actual=False,
    dd4_boundary_map_actual=False,
    represented_square_boundary_edges=False,
    cancellation_convolution_module_compatible=False,
    maps_cancellation_to_boundary_localization=False,
    grothendieck_group_completion=True,
    control_formable=True,
)

gate(
    "BCC4 Grothendieck completion does not supply the boundary map",
    group_completion_pair(chi_zero_times_F22) == (((2, 4),), ((4, 2),))
    and not accepts_boundary_cancellation(group_completion)
    and {
        "boundary_cancellation_functor_not_actual",
        "dd4_boundary_map_not_actual",
        "represented_square_boundary_edges_missing",
        "cancellation_not_convolution_module_compatible",
        "cancellation_not_mapped_to_boundary_localization",
        "grothendieck_group_completion",
        "control_formable",
    }
    <= set(reasons(group_completion)),
    "pair=%s reasons=%s"
    % (group_completion_pair(chi_zero_times_F22), ",".join(reasons(group_completion))),
)


formal_cell = live_source(
    carrier_native=False,
    boundary_cancellation_functor_actual=False,
    dd4_boundary_map_actual=False,
    represented_square_boundary_edges=False,
    maps_boundary_to_internal_effectivity_domain=False,
    formal_boundary_cell=True,
    external_chain_complex=True,
    control_formable=True,
)

gate(
    "BCC5 attached formal cells kill the relation externally",
    chi_zero == {1: 2, 2: -1}
    and chi_zero_times_F22 == convolve_chi(chi_zero, chi_F22)
    and not accepts_boundary_cancellation(formal_cell)
    and {
        "not_carrier_native",
        "boundary_cancellation_functor_not_actual",
        "dd4_boundary_map_not_actual",
        "represented_square_boundary_edges_missing",
        "boundary_not_mapped_to_internal_effectivity_domain",
        "formal_boundary_cell",
        "external_chain_complex",
        "control_formable",
    }
    <= set(reasons(formal_cell)),
    ",".join(reasons(formal_cell)),
)


endpoint_kernel = live_source(
    boundary_cancellation_functor_actual=False,
    dd4_boundary_map_actual=False,
    generates_endpoint_integrality=False,
    generates_pushforward_compatibility=False,
    endpoint_kernel_definition=True,
    boundary_afterthought_filter=True,
    control_formable=True,
)

gate(
    "BCC6 endpoint kernels are downstream boundary afterthoughts",
    endpoint_degree_kernel(chi_zero)
    and chi_L != chi_C3
    and not accepts_boundary_cancellation(endpoint_kernel)
    and {
        "boundary_cancellation_functor_not_actual",
        "dd4_boundary_map_not_actual",
        "endpoint_integrality_not_generated",
        "pushforward_compatibility_not_generated",
        "endpoint_kernel_definition",
        "boundary_afterthought_filter",
        "control_formable",
    }
    <= set(reasons(endpoint_kernel)),
    ",".join(reasons(endpoint_kernel)),
)


missing_module = live_source(
    cancellation_convolution_module_compatible=False,
    required_edges=REQUIRED_EDGES - {("character_convolution", "cancellation_module")},
)

gate(
    "BCC7 cancellation must be compatible with character convolution",
    not accepts_boundary_cancellation(missing_module)
    and {
        "cancellation_not_convolution_module_compatible",
        "required_boundary_cancellation_edges_missing",
    }
    <= set(reasons(missing_module)),
    ",".join(reasons(missing_module)),
)


control_balance = live_source(
    strict_square_signed_character_actual=False,
    boundary_cancellation_functor_actual=False,
    controls_undefined_at_boundary=False,
    dh_undefined_at_boundary=False,
    epstein_undefined_at_boundary=False,
    weighted_sum_zero_selector=True,
    endpoint_kernel_definition=True,
    control_formable=True,
    dh_formable=True,
    epstein_formable=True,
)

gate(
    "BCC8 controls/DH/Epstein can mimic balanced signed profiles",
    {1: 2, 2: -1} == chi_zero
    and weighted_mass({1: 2, 2: -1}) == 0
    and not accepts_boundary_cancellation(control_balance)
    and {
        "strict_square_signed_character_missing",
        "boundary_cancellation_functor_not_actual",
        "controls_not_undefined_at_boundary",
        "dh_not_undefined_at_boundary",
        "epstein_not_undefined_at_boundary",
        "weighted_sum_zero_selector",
        "endpoint_kernel_definition",
        "control_formable",
        "dh_formable",
        "epstein_formable",
    }
    <= set(reasons(control_balance)),
    ",".join(reasons(control_balance)),
)


missing_downstream = live_source(
    generates_endpoint_integrality=False,
    generates_pushforward_compatibility=False,
    generates_control_death=False,
    required_edges=REQUIRED_EDGES
    - {
        ("internal_effectivity_domain", "endpoint"),
        ("endpoint", "pushforward"),
        ("internal_effectivity_domain", "control_death"),
    },
)

gate(
    "BCC9 boundary cancellation must feed endpoint, pushforward, and death",
    not accepts_boundary_cancellation(missing_downstream)
    and {
        "endpoint_integrality_not_generated",
        "pushforward_compatibility_not_generated",
        "control_death_not_generated",
        "required_boundary_cancellation_edges_missing",
    }
    <= set(reasons(missing_downstream)),
    ",".join(reasons(missing_downstream)),
)


declared = live_source(
    boundary_cancellation_functor_actual=False,
    dd4_boundary_map_actual=False,
    represented_square_boundary_edges=False,
    required_edges=set(),
    declared_boundary_cancellation=True,
)

live = live_source()

dead_sources = {
    "weight_zero": weight_zero,
    "split_only": split_only,
    "group_completion": group_completion,
    "formal_cell": formal_cell,
    "endpoint_kernel": endpoint_kernel,
    "missing_module": missing_module,
    "control_balance": control_balance,
    "missing_downstream": missing_downstream,
    "declared": declared,
}

gate(
    "BCC10 only represented DD.4 boundary-cancellation functor passes",
    accepts_boundary_cancellation(live)
    and REQUIRED_EDGES <= live["required_edges"]
    and not any(accepts_boundary_cancellation(data) for data in dead_sources.values())
    and {
        "boundary_cancellation_functor_not_actual",
        "dd4_boundary_map_not_actual",
        "represented_square_boundary_edges_missing",
        "required_boundary_cancellation_edges_missing",
        "declared_boundary_cancellation",
    }
    <= set(reasons(declared)),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_boundary_cancellation(data) for data in dead_sources.values()),
        accepts_boundary_cancellation(live),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nBCC1-BCC10 ALL PASS: strict-square boundary-cancellation contract pinned")
print(
    "VERDICT: the signed zero-fiber datum must map through a represented "
    "boundary-cancellation functor to the DD.4 boundary localization. "
    "Weighted-zero tests, positive/negative splits, Grothendieck completion, "
    "formal cells, endpoint kernels, declared maps, and control/DH/Epstein "
    "balanced profiles do not construct that boundary interface."
)
