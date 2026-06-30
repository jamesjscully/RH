r"""Signed-character effectivity contract for the strict-square branch.

Doc 327 requires a full character-to-internal-strata functor.  This witness
sharpens the next bottleneck: the functor must include a carrier-native
effectivity orientation on the signed strict-square character algebra.  It
cannot get positivity by truncating signs, taking absolute values, quotienting
to support, deleting the signed zero fiber, using diagonal totals, or
recovering effectivity as an endpoint/count/control filter.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_strict_square_signed_character_effectivity_contract
"""

from __future__ import annotations

from math import factorial


failures: list[str] = []

REQUIRED_EDGES = {
    ("strict_square_character", "signed_character_algebra"),
    ("signed_character_algebra", "character_convolution"),
    ("signed_character_algebra", "effectivity_orientation"),
    ("effectivity_orientation", "positive_cone"),
    ("positive_cone", "internal_effectivity_domain"),
    ("signed_zero_fiber", "boundary_cancellation"),
    ("boundary_cancellation", "boundary"),
    ("character_convolution", "stratum_product"),
    ("stratum_product", "internal_effectivity_domain"),
    ("internal_effectivity_domain", "prime_power_subtowers"),
    ("internal_effectivity_domain", "endpoint"),
    ("internal_effectivity_domain", "boundary"),
    ("internal_effectivity_domain", "control_death"),
    ("endpoint", "pushforward"),
    ("boundary", "pushforward"),
    ("pushforward", "graph"),
    ("graph", "rosati"),
    ("graph", "count_degree"),
}


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def binom_int(n: int, p: int) -> int:
    num = 1
    for i in range(p):
        num *= n - i
    return num // factorial(p)


def total(a, b, edges) -> int:
    return sum(a[i] * b[j] for i, j in edges)


def row_sums(a, b, edges) -> list[int]:
    rows = [0] * len(a)
    for i, j in edges:
        rows[i] += b[j]
    return rows


def phi_row_mod_p(a, b, edges, p: int) -> int:
    rows = row_sums(a, b, edges)
    return sum((a[i] ** p) * binom_int(rows[i], p) for i in range(len(a))) % p


def normalize(chi: dict[int, int]) -> dict[int, int]:
    return {key: val for key, val in sorted(chi.items()) if val != 0}


def chi_col(a, b, edges) -> dict[int, int]:
    out: dict[int, int] = {}
    for j, bj in enumerate(b):
        aj = sum(a[i] for i, jj in edges if jj == j)
        if bj != 0 and aj != 0:
            out[aj] = out.get(aj, 0) + bj
    return normalize(out)


def add_chi(*chars: dict[int, int]) -> dict[int, int]:
    out: dict[int, int] = {}
    for chi in chars:
        for key, val in chi.items():
            out[key] = out.get(key, 0) + val
    return normalize(out)


def convolve_chi(left: dict[int, int], right: dict[int, int]) -> dict[int, int]:
    out: dict[int, int] = {}
    for a, ca in left.items():
        for b, cb in right.items():
            out[a * b] = out.get(a * b, 0) + ca * cb
    return normalize(out)


def square_product(x, y):
    a, b, edges = x
    c, d, fedges = y
    new_a = tuple(ai * ck for ai in a for ck in c)
    new_b = tuple(bj * dl for bj in b for dl in d)
    new_edges = []
    for i, j in edges:
        for k, l in fedges:
            new_edges.append((i * len(c) + k, j * len(d) + l))
    return new_a, new_b, tuple(new_edges)


def positive_part(chi: dict[int, int]) -> dict[int, int]:
    return normalize({key: val for key, val in chi.items() if val > 0})


def abs_map(chi: dict[int, int]) -> dict[int, int]:
    return normalize({key: abs(val) for key, val in chi.items()})


def support_map(chi: dict[int, int]) -> dict[int, int]:
    return normalize({key: 1 for key in chi})


def sign_map(chi: dict[int, int]) -> dict[int, int]:
    return normalize({key: 1 if val > 0 else -1 for key, val in chi.items()})


def diagonal_total_positive(square) -> bool:
    return total(*square) >= 0


def prime_power_axes(chi: dict[int, int]) -> dict[tuple[int, int], int]:
    axes: dict[tuple[int, int], int] = {}
    for key, val in chi.items():
        n = key
        d = 2
        while d * d <= n:
            exponent = 0
            while n % d == 0:
                n //= d
                exponent += 1
            if exponent:
                axes[(d, exponent)] = axes.get((d, exponent), 0) + val
            d += 1
        if n > 1:
            axes[(n, 1)] = axes.get((n, 1), 0) + val
    return {key: val for key, val in sorted(axes.items()) if val != 0}


def source(**kwargs):
    data = {
        "strict_square_character_actual": False,
        "signed_character_algebra_actual": False,
        "character_convolution_actual": False,
        "carrier_native_effectivity_orientation_actual": False,
        "positive_cone_actual": False,
        "orientation_retains_multi_axis_classes": False,
        "orientation_retains_coefficients": False,
        "orientation_retains_negative_coefficients_as_boundary_data": False,
        "orientation_retains_signed_zero_fiber": False,
        "orientation_additive": False,
        "orientation_convolution_compatible": False,
        "maps_positive_cone_to_internal_effectivity_strata": False,
        "maps_cancellation_to_boundary_localization": False,
        "produces_internal_effectivity_domain": False,
        "produces_prime_power_subtowers": False,
        "generates_endpoint_integrality": False,
        "generates_boundary_localization": False,
        "generates_graph_rosati_count": False,
        "generates_control_death": False,
        "controls_undefined_at_orientation": False,
        "dh_undefined_at_orientation": False,
        "epstein_undefined_at_orientation": False,
        "required_edges": set(),
        "positive_part_truncation": False,
        "absolute_value_map": False,
        "sign_quotient": False,
        "support_only_map": False,
        "drops_negative_coefficients": False,
        "drops_signed_zero_fiber": False,
        "diagonal_total_positive_selector": False,
        "external_ordering": False,
        "external_prime_factorization": False,
        "endpoint_or_count_filter": False,
        "declared_positive_cone": False,
        "control_formable": True,
        "dh_formable": True,
        "epstein_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("strict_square_character_actual", "strict_square_character_missing"),
    ("signed_character_algebra_actual", "signed_character_algebra_missing"),
    ("character_convolution_actual", "character_convolution_missing"),
    (
        "carrier_native_effectivity_orientation_actual",
        "carrier_native_effectivity_orientation_not_actual",
    ),
    ("positive_cone_actual", "positive_cone_not_actual"),
    ("orientation_retains_multi_axis_classes", "multi_axis_classes_not_retained"),
    ("orientation_retains_coefficients", "coefficients_not_retained"),
    (
        "orientation_retains_negative_coefficients_as_boundary_data",
        "negative_coefficients_not_retained_as_boundary_data",
    ),
    ("orientation_retains_signed_zero_fiber", "signed_zero_fiber_not_retained"),
    ("orientation_additive", "orientation_not_additive"),
    (
        "orientation_convolution_compatible",
        "orientation_not_convolution_compatible",
    ),
    (
        "maps_positive_cone_to_internal_effectivity_strata",
        "positive_cone_not_mapped_to_internal_strata",
    ),
    (
        "maps_cancellation_to_boundary_localization",
        "cancellation_not_mapped_to_boundary",
    ),
    (
        "produces_internal_effectivity_domain",
        "internal_effectivity_domain_not_produced",
    ),
    ("produces_prime_power_subtowers", "prime_power_subtowers_not_produced"),
    ("generates_endpoint_integrality", "endpoint_integrality_not_generated"),
    (
        "generates_boundary_localization",
        "boundary_localization_not_generated",
    ),
    ("generates_graph_rosati_count", "graph_rosati_count_not_generated"),
    ("generates_control_death", "control_death_not_generated"),
    ("controls_undefined_at_orientation", "controls_not_undefined_at_orientation"),
    ("dh_undefined_at_orientation", "dh_not_undefined_at_orientation"),
    ("epstein_undefined_at_orientation", "epstein_not_undefined_at_orientation"),
)

BANNED = (
    ("positive_part_truncation", "positive_part_truncation"),
    ("absolute_value_map", "absolute_value_map"),
    ("sign_quotient", "sign_quotient"),
    ("support_only_map", "support_only_map"),
    ("drops_negative_coefficients", "drops_negative_coefficients"),
    ("drops_signed_zero_fiber", "drops_signed_zero_fiber"),
    ("diagonal_total_positive_selector", "diagonal_total_positive_selector"),
    ("external_ordering", "external_ordering"),
    ("external_prime_factorization", "external_prime_factorization"),
    ("endpoint_or_count_filter", "endpoint_or_count_filter"),
    ("declared_positive_cone", "declared_positive_cone"),
    ("control_formable", "control_formable"),
    ("dh_formable", "dh_formable"),
    ("epstein_formable", "epstein_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_EDGES <= set(data["required_edges"]):
        out.append("required_signed_effectivity_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_signed_effectivity(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        strict_square_character_actual=True,
        signed_character_algebra_actual=True,
        character_convolution_actual=True,
        carrier_native_effectivity_orientation_actual=True,
        positive_cone_actual=True,
        orientation_retains_multi_axis_classes=True,
        orientation_retains_coefficients=True,
        orientation_retains_negative_coefficients_as_boundary_data=True,
        orientation_retains_signed_zero_fiber=True,
        orientation_additive=True,
        orientation_convolution_compatible=True,
        maps_positive_cone_to_internal_effectivity_strata=True,
        maps_cancellation_to_boundary_localization=True,
        produces_internal_effectivity_domain=True,
        produces_prime_power_subtowers=True,
        generates_endpoint_integrality=True,
        generates_boundary_localization=True,
        generates_graph_rosati_count=True,
        generates_control_death=True,
        controls_undefined_at_orientation=True,
        dh_undefined_at_orientation=True,
        epstein_undefined_at_orientation=True,
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
F41 = ((4,), (1,), ((0, 0),))
ZERO_SPLIT = ((1, 2), (2, -1), ((0, 0), (1, 1)))
UNIT_2 = {2: 1}

chars = {
    "L": chi_col(*L),
    "C3": chi_col(*C3),
    "F22": chi_col(*F22),
    "F41": chi_col(*F41),
    "zero": chi_col(*ZERO_SPLIT),
    "LxF22": chi_col(*square_product(L, F22)),
}

gate(
    "SCE1 signed character algebra retains cancellation and convolution",
    chars["L"] == {1: 1, 2: 1}
    and chars["C3"] == {3: 1}
    and chars["F22"] == {2: 2}
    and chars["F41"] == {4: 1}
    and chars["zero"] == {1: 2, 2: -1}
    and add_chi(chars["zero"], UNIT_2) == {1: 2}
    and convolve_chi(chars["zero"], chars["F22"]) == {2: 4, 4: -2}
    and chars["LxF22"] == convolve_chi(chars["L"], chars["F22"]),
    "chars=%s zero*F22=%s"
    % (chars, convolve_chi(chars["zero"], chars["F22"])),
)


positive_truncation = live_source(
    carrier_native_effectivity_orientation_actual=False,
    positive_cone_actual=False,
    orientation_retains_negative_coefficients_as_boundary_data=False,
    orientation_retains_signed_zero_fiber=False,
    orientation_additive=False,
    maps_cancellation_to_boundary_localization=False,
    positive_part_truncation=True,
    drops_negative_coefficients=True,
    control_formable=True,
    dh_formable=True,
    epstein_formable=True,
)

gate(
    "SCE2 positive-part truncation erases the signed cancellation datum",
    positive_part(add_chi(chars["zero"], UNIT_2))
    != add_chi(positive_part(chars["zero"]), positive_part(UNIT_2))
    and positive_part(chars["zero"]) == {1: 2}
    and not accepts_signed_effectivity(positive_truncation)
    and {
        "carrier_native_effectivity_orientation_not_actual",
        "positive_cone_not_actual",
        "negative_coefficients_not_retained_as_boundary_data",
        "signed_zero_fiber_not_retained",
        "orientation_not_additive",
        "cancellation_not_mapped_to_boundary",
        "positive_part_truncation",
        "drops_negative_coefficients",
        "control_formable",
        "dh_formable",
        "epstein_formable",
    }
    <= set(reasons(positive_truncation)),
    ",".join(reasons(positive_truncation)),
)


absolute_value = live_source(
    carrier_native_effectivity_orientation_actual=False,
    positive_cone_actual=False,
    orientation_retains_negative_coefficients_as_boundary_data=False,
    orientation_additive=False,
    maps_cancellation_to_boundary_localization=False,
    absolute_value_map=True,
    control_formable=True,
    dh_formable=True,
    epstein_formable=True,
)

control_profiles = {
    "positive_zero": {1: 2},
    "absolute_zero": {1: 2, 2: 1},
    "support_L": {1: 1, 2: 1},
    "tower_dim4": {2: 2},
}

gate(
    "SCE3 absolute values turn cancellation into a positive control profile",
    abs_map(chars["zero"]) == control_profiles["absolute_zero"]
    and abs_map(add_chi(chars["zero"], UNIT_2))
    != add_chi(abs_map(chars["zero"]), abs_map(UNIT_2))
    and not accepts_signed_effectivity(absolute_value)
    and {
        "carrier_native_effectivity_orientation_not_actual",
        "positive_cone_not_actual",
        "negative_coefficients_not_retained_as_boundary_data",
        "orientation_not_additive",
        "cancellation_not_mapped_to_boundary",
        "absolute_value_map",
        "control_formable",
    }
    <= set(reasons(absolute_value)),
    "abs(zero)=%s reasons=%s" % (abs_map(chars["zero"]), ",".join(reasons(absolute_value))),
)


support_quotient = live_source(
    carrier_native_effectivity_orientation_actual=False,
    positive_cone_actual=False,
    orientation_retains_coefficients=False,
    orientation_retains_negative_coefficients_as_boundary_data=False,
    orientation_retains_signed_zero_fiber=False,
    sign_quotient=True,
    support_only_map=True,
    drops_negative_coefficients=True,
    control_formable=True,
)

gate(
    "SCE4 sign/support quotients lose coefficients and zero-fiber shape",
    support_map(chars["F22"]) == support_map(UNIT_2) == {2: 1}
    and support_map(chars["zero"]) == support_map(chars["L"]) == {1: 1, 2: 1}
    and sign_map(chars["F22"]) == sign_map(UNIT_2) == {2: 1}
    and not accepts_signed_effectivity(support_quotient)
    and {
        "carrier_native_effectivity_orientation_not_actual",
        "positive_cone_not_actual",
        "coefficients_not_retained",
        "negative_coefficients_not_retained_as_boundary_data",
        "signed_zero_fiber_not_retained",
        "sign_quotient",
        "support_only_map",
        "drops_negative_coefficients",
        "control_formable",
    }
    <= set(reasons(support_quotient)),
    "support(zero)=%s support(L)=%s reasons=%s"
    % (support_map(chars["zero"]), support_map(chars["L"]), ",".join(reasons(support_quotient))),
)


zero_deletion = live_source(
    orientation_retains_signed_zero_fiber=False,
    maps_cancellation_to_boundary_localization=False,
    drops_signed_zero_fiber=True,
)

gate(
    "SCE5 deleting the signed zero fiber deletes square-only data",
    total(*ZERO_SPLIT) == 0
    and chars["zero"] == {1: 2, 2: -1}
    and not accepts_signed_effectivity(zero_deletion)
    and {
        "signed_zero_fiber_not_retained",
        "cancellation_not_mapped_to_boundary",
        "drops_signed_zero_fiber",
    }
    <= set(reasons(zero_deletion)),
    ",".join(reasons(zero_deletion)),
)


diagonal_total = live_source(
    strict_square_character_actual=False,
    carrier_native_effectivity_orientation_actual=False,
    positive_cone_actual=False,
    orientation_retains_multi_axis_classes=False,
    orientation_retains_signed_zero_fiber=False,
    maps_positive_cone_to_internal_effectivity_strata=False,
    diagonal_total_positive_selector=True,
    control_formable=True,
)

gate(
    "SCE6 diagonal-total positivity collapses the strict-square split",
    total(*L) == total(*C3) == 3
    and phi_row_mod_p(*L, 2) == 1
    and phi_row_mod_p(*C3, 2) == 0
    and diagonal_total_positive(ZERO_SPLIT)
    and not accepts_signed_effectivity(diagonal_total)
    and {
        "strict_square_character_missing",
        "carrier_native_effectivity_orientation_not_actual",
        "positive_cone_not_actual",
        "multi_axis_classes_not_retained",
        "signed_zero_fiber_not_retained",
        "positive_cone_not_mapped_to_internal_strata",
        "diagonal_total_positive_selector",
        "control_formable",
    }
    <= set(reasons(diagonal_total)),
    ",".join(reasons(diagonal_total)),
)


external_factor = live_source(
    produces_prime_power_subtowers=False,
    orientation_convolution_compatible=False,
    external_ordering=True,
    external_prime_factorization=True,
)

gate(
    "SCE7 external ordering/factorization cannot supply the positive cone",
    prime_power_axes(chars["F41"]) == {(2, 2): 1}
    and chars["F41"] == {4: 1}
    and not accepts_signed_effectivity(external_factor)
    and {
        "orientation_not_convolution_compatible",
        "prime_power_subtowers_not_produced",
        "external_ordering",
        "external_prime_factorization",
    }
    <= set(reasons(external_factor)),
    "axes=%s reasons=%s" % (prime_power_axes(chars["F41"]), ",".join(reasons(external_factor))),
)


endpoint_count_filter = live_source(
    strict_square_character_actual=False,
    carrier_native_effectivity_orientation_actual=False,
    controls_undefined_at_orientation=False,
    dh_undefined_at_orientation=False,
    epstein_undefined_at_orientation=False,
    endpoint_or_count_filter=True,
    control_formable=True,
    dh_formable=True,
    epstein_formable=True,
)

gate(
    "SCE8 endpoint/count/control filters mimic positive character profiles",
    control_profiles["positive_zero"] == positive_part(chars["zero"])
    and control_profiles["absolute_zero"] == abs_map(chars["zero"])
    and control_profiles["support_L"] == support_map(chars["L"])
    and control_profiles["tower_dim4"] == chars["F22"]
    and not accepts_signed_effectivity(endpoint_count_filter)
    and {
        "strict_square_character_missing",
        "carrier_native_effectivity_orientation_not_actual",
        "controls_not_undefined_at_orientation",
        "dh_not_undefined_at_orientation",
        "epstein_not_undefined_at_orientation",
        "endpoint_or_count_filter",
        "control_formable",
        "dh_formable",
        "epstein_formable",
    }
    <= set(reasons(endpoint_count_filter)),
    "control_profiles=%s reasons=%s"
    % (control_profiles, ",".join(reasons(endpoint_count_filter))),
)


missing_boundary_control = live_source(
    maps_cancellation_to_boundary_localization=False,
    generates_control_death=False,
    required_edges=REQUIRED_EDGES
    - {
        ("signed_zero_fiber", "boundary_cancellation"),
        ("boundary_cancellation", "boundary"),
        ("internal_effectivity_domain", "control_death"),
    },
)

gate(
    "SCE9 signed effectivity must feed boundary and control death",
    not accepts_signed_effectivity(missing_boundary_control)
    and {
        "cancellation_not_mapped_to_boundary",
        "control_death_not_generated",
        "required_signed_effectivity_edges_missing",
    }
    <= set(reasons(missing_boundary_control)),
    ",".join(reasons(missing_boundary_control)),
)


declared_cone = live_source(
    carrier_native_effectivity_orientation_actual=False,
    positive_cone_actual=False,
    required_edges=set(),
    declared_positive_cone=True,
)

live = live_source()

dead_sources = {
    "positive_truncation": positive_truncation,
    "absolute_value": absolute_value,
    "support_quotient": support_quotient,
    "zero_deletion": zero_deletion,
    "diagonal_total": diagonal_total,
    "external_factor": external_factor,
    "endpoint_count_filter": endpoint_count_filter,
    "missing_boundary_control": missing_boundary_control,
    "declared_cone": declared_cone,
}

gate(
    "SCE10 only carrier-native signed-character effectivity passes",
    accepts_signed_effectivity(live)
    and REQUIRED_EDGES <= live["required_edges"]
    and not any(accepts_signed_effectivity(data) for data in dead_sources.values())
    and {
        "carrier_native_effectivity_orientation_not_actual",
        "positive_cone_not_actual",
        "required_signed_effectivity_edges_missing",
        "declared_positive_cone",
    }
    <= set(reasons(declared_cone)),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_signed_effectivity(data) for data in dead_sources.values()),
        accepts_signed_effectivity(live),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nSCE1-SCE10 ALL PASS: strict-square signed-character effectivity contract pinned")
print(
    "VERDICT: the strict-square character-to-strata functor now needs a "
    "carrier-native effectivity orientation on the signed character algebra. "
    "Positive-part truncation, absolute value, sign/support quotients, "
    "zero-fiber deletion, diagonal-total positivity, external factorization, "
    "endpoint/count filters, and control/DH/Epstein-formable packages do not "
    "construct the Qbar_BECD internal effectivity stratum."
)
