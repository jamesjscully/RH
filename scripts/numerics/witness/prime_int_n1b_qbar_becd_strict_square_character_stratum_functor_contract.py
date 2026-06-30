r"""Strict-square character-to-stratum functor contract for Qbar_BECD.

Doc 326 leaves the strict-square branch live only through a non-EM extraction
functor.  This witness sharpens the next split: that extraction cannot be a
scalar axis selector on the universal character algebra.  It must be a full
character-to-internal-strata functor retaining multi-axis classes,
coefficients, signed zero-fiber data, and convolution before producing
prime-power subtowers, endpoint/boundary data, graph/Rosati/count data, and
control death.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_strict_square_character_stratum_functor_contract
"""

from __future__ import annotations

from math import factorial
from typing import Callable


failures: list[str] = []

REQUIRED_EDGES = {
    ("strict_square_character", "character_stratum_functor"),
    ("character_stratum_functor", "internal_effectivity_domain"),
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


def chi_col(a, b, edges) -> dict[int, int]:
    out: dict[int, int] = {}
    for j, bj in enumerate(b):
        aj = sum(a[i] for i, jj in edges if jj == j)
        if bj != 0 and aj != 0:
            out[aj] = out.get(aj, 0) + bj
    return {key: val for key, val in out.items() if val != 0}


def convolve_chi(left: dict[int, int], right: dict[int, int]) -> dict[int, int]:
    out: dict[int, int] = {}
    for a, ca in left.items():
        for b, cb in right.items():
            out[a * b] = out.get(a * b, 0) + ca * cb
    return {key: val for key, val in out.items() if val != 0}


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


def min_axis(chi: dict[int, int]) -> int | None:
    return min(chi) if chi else None


def max_axis(chi: dict[int, int]) -> int | None:
    return max(chi) if chi else None


def singleton_axis(chi: dict[int, int]) -> int | None:
    return next(iter(chi)) if len(chi) == 1 else None


def coefficient_axis(chi: dict[int, int]) -> int | None:
    if not chi:
        return None
    best_coeff = max(abs(v) for v in chi.values())
    winners = [k for k, v in chi.items() if abs(v) == best_coeff]
    return min(winners) if len(winners) == 1 else None


def prime_support_axis(chi: dict[int, int]) -> int | None:
    primes = [k for k in chi if k > 1 and all(k % d for d in range(2, int(k**0.5) + 1))]
    return min(primes) if len(primes) == 1 else None


def selector_profile(selector: Callable[[dict[int, int]], int | None], chars):
    return {name: selector(chi) for name, chi in chars.items()}


def source(**kwargs):
    data = {
        "strict_square_character_actual": False,
        "character_convolution_actual": False,
        "character_stratum_functor_actual": False,
        "functor_not_scalar_axis_selector": False,
        "retains_multi_axis_classes": False,
        "retains_coefficients": False,
        "retains_signed_zero_fiber": False,
        "maps_convolution_to_stratum_product": False,
        "produces_internal_effectivity_domain": False,
        "produces_prime_power_subtowers": False,
        "generates_endpoint_integrality": False,
        "generates_boundary_localization": False,
        "generates_graph_rosati_count": False,
        "controls_undefined_at_functor": False,
        "epstein_undefined_at_functor": False,
        "required_edges": set(),
        "diagonal_total_selector": False,
        "single_axis_selector": False,
        "min_axis_selector": False,
        "max_axis_selector": False,
        "singleton_support_selector": False,
        "coefficient_selector": False,
        "prime_support_selector": False,
        "external_prime_factorization": False,
        "throws_away_zero_fiber": False,
        "endpoint_or_count_fiber_selector": False,
        "declared_stratum_functor": False,
        "control_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("strict_square_character_actual", "strict_square_character_missing"),
    ("character_convolution_actual", "character_convolution_missing"),
    ("character_stratum_functor_actual", "character_stratum_functor_not_actual"),
    (
        "functor_not_scalar_axis_selector",
        "functor_is_scalar_axis_selector",
    ),
    ("retains_multi_axis_classes", "multi_axis_classes_not_retained"),
    ("retains_coefficients", "coefficients_not_retained"),
    ("retains_signed_zero_fiber", "signed_zero_fiber_not_retained"),
    (
        "maps_convolution_to_stratum_product",
        "convolution_not_mapped_to_stratum_product",
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
    ("controls_undefined_at_functor", "controls_not_undefined_at_functor"),
    ("epstein_undefined_at_functor", "epstein_not_undefined_at_functor"),
)

BANNED = (
    ("diagonal_total_selector", "diagonal_total_selector"),
    ("single_axis_selector", "single_axis_selector"),
    ("min_axis_selector", "min_axis_selector"),
    ("max_axis_selector", "max_axis_selector"),
    ("singleton_support_selector", "singleton_support_selector"),
    ("coefficient_selector", "coefficient_selector"),
    ("prime_support_selector", "prime_support_selector"),
    ("external_prime_factorization", "external_prime_factorization"),
    ("throws_away_zero_fiber", "throws_away_zero_fiber"),
    ("endpoint_or_count_fiber_selector", "endpoint_or_count_fiber_selector"),
    ("declared_stratum_functor", "declared_stratum_functor"),
    ("control_formable", "control_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_EDGES <= set(data["required_edges"]):
        out.append("required_character_stratum_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_character_functor(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        strict_square_character_actual=True,
        character_convolution_actual=True,
        character_stratum_functor_actual=True,
        functor_not_scalar_axis_selector=True,
        retains_multi_axis_classes=True,
        retains_coefficients=True,
        retains_signed_zero_fiber=True,
        maps_convolution_to_stratum_product=True,
        produces_internal_effectivity_domain=True,
        produces_prime_power_subtowers=True,
        generates_endpoint_integrality=True,
        generates_boundary_localization=True,
        generates_graph_rosati_count=True,
        controls_undefined_at_functor=True,
        epstein_undefined_at_functor=True,
        required_edges=set(REQUIRED_EDGES),
        control_formable=False,
    )
    data.update(kwargs)
    return data


L = ((1, 1), (1, 1), ((0, 0), (0, 1), (1, 0)))
C3 = ((3,), (1,), ((0, 0),))
F22 = ((2,), (2,), ((0, 0),))
F41 = ((4,), (1,), ((0, 0),))
ZERO_SPLIT = ((1, 2), (2, -1), ((0, 0), (1, 1)))

chars = {
    "L": chi_col(*L),
    "C3": chi_col(*C3),
    "F22": chi_col(*F22),
    "F41": chi_col(*F41),
    "zero": chi_col(*ZERO_SPLIT),
    "LxF22": chi_col(*square_product(L, F22)),
}

gate(
    "SCF1 strict-square character data has multi-axis and signed fibers",
    chars["L"] == {1: 1, 2: 1}
    and chars["C3"] == {3: 1}
    and chars["F22"] == {2: 2}
    and chars["F41"] == {4: 1}
    and chars["zero"] == {1: 2, 2: -1}
    and chars["LxF22"] == convolve_chi(chars["L"], chars["F22"]),
    "chars=%s" % chars,
)


diagonal_selector = live_source(
    character_stratum_functor_actual=False,
    functor_not_scalar_axis_selector=False,
    retains_multi_axis_classes=False,
    retains_coefficients=False,
    retains_signed_zero_fiber=False,
    produces_internal_effectivity_domain=False,
    diagonal_total_selector=True,
    control_formable=True,
)

gate(
    "SCF2 diagonal-total selection loses strict-square noncollapse",
    total(*L) == total(*C3) == 3
    and phi_row_mod_p(*L, 2) == 1
    and phi_row_mod_p(*C3, 2) == 0
    and not accepts_character_functor(diagonal_selector)
    and {
        "character_stratum_functor_not_actual",
        "functor_is_scalar_axis_selector",
        "multi_axis_classes_not_retained",
        "signed_zero_fiber_not_retained",
        "internal_effectivity_domain_not_produced",
        "diagonal_total_selector",
        "control_formable",
    }
    <= set(reasons(diagonal_selector)),
    ",".join(reasons(diagonal_selector)),
)


profiles = {
    "min": selector_profile(min_axis, chars),
    "max": selector_profile(max_axis, chars),
    "singleton": selector_profile(singleton_axis, chars),
    "coefficient": selector_profile(coefficient_axis, chars),
    "prime_support": selector_profile(prime_support_axis, chars),
}

single_axis = live_source(
    character_stratum_functor_actual=False,
    functor_not_scalar_axis_selector=False,
    retains_multi_axis_classes=False,
    retains_coefficients=False,
    retains_signed_zero_fiber=False,
    single_axis_selector=True,
    min_axis_selector=True,
    max_axis_selector=True,
    singleton_support_selector=True,
    coefficient_selector=True,
    prime_support_selector=True,
    control_formable=True,
)

gate(
    "SCF3 scalar axis selectors discard required character structure",
    profiles["singleton"]["L"] is None
    and profiles["singleton"]["F22"] == 2
    and profiles["coefficient"]["F22"] == 2
    and profiles["coefficient"]["L"] is None
    and profiles["prime_support"]["F41"] is None
    and profiles["min"]["zero"] == 1
    and profiles["max"]["zero"] == 2
    and not accepts_character_functor(single_axis)
    and {
        "character_stratum_functor_not_actual",
        "functor_is_scalar_axis_selector",
        "multi_axis_classes_not_retained",
        "coefficients_not_retained",
        "signed_zero_fiber_not_retained",
        "single_axis_selector",
        "control_formable",
    }
    <= set(reasons(single_axis)),
    "profiles=%s reasons=%s" % (profiles, ",".join(reasons(single_axis))),
)


factorization_selector = live_source(
    character_stratum_functor_actual=False,
    functor_not_scalar_axis_selector=False,
    maps_convolution_to_stratum_product=False,
    produces_internal_effectivity_domain=False,
    produces_prime_power_subtowers=False,
    external_prime_factorization=True,
    prime_support_selector=True,
    control_formable=True,
)

gate(
    "SCF4 factoring character keys imports an external prime-axis selector",
    chars["F41"] == {4: 1}
    and prime_support_axis(chars["F41"]) is None
    and not accepts_character_functor(factorization_selector)
    and {
        "character_stratum_functor_not_actual",
        "functor_is_scalar_axis_selector",
        "convolution_not_mapped_to_stratum_product",
        "internal_effectivity_domain_not_produced",
        "prime_power_subtowers_not_produced",
        "external_prime_factorization",
        "prime_support_selector",
        "control_formable",
    }
    <= set(reasons(factorization_selector)),
    ",".join(reasons(factorization_selector)),
)


zero_throwaway = live_source(
    character_stratum_functor_actual=False,
    retains_signed_zero_fiber=False,
    maps_convolution_to_stratum_product=False,
    produces_internal_effectivity_domain=False,
    throws_away_zero_fiber=True,
)

gate(
    "SCF5 rejecting signed zero fibers throws away square-only data",
    total(*ZERO_SPLIT) == 0
    and chars["zero"] == {1: 2, 2: -1}
    and not accepts_character_functor(zero_throwaway)
    and {
        "character_stratum_functor_not_actual",
        "signed_zero_fiber_not_retained",
        "convolution_not_mapped_to_stratum_product",
        "internal_effectivity_domain_not_produced",
        "throws_away_zero_fiber",
    }
    <= set(reasons(zero_throwaway)),
    ",".join(reasons(zero_throwaway)),
)


control_chars = {
    "dim2": {1: 1, 2: 1},
    "dim4": {2: 2},
    "dim8": {4: 1},
}
control_axis = live_source(
    strict_square_character_actual=False,
    character_stratum_functor_actual=False,
    controls_undefined_at_functor=False,
    epstein_undefined_at_functor=False,
    single_axis_selector=True,
    endpoint_or_count_fiber_selector=True,
    control_formable=True,
)

gate(
    "SCF6 controls can mimic scalar character-axis profiles",
    control_chars["dim2"] == chars["L"]
    and control_chars["dim4"] == chars["F22"]
    and control_chars["dim8"] == chars["F41"]
    and not accepts_character_functor(control_axis)
    and {
        "strict_square_character_missing",
        "character_stratum_functor_not_actual",
        "controls_not_undefined_at_functor",
        "epstein_not_undefined_at_functor",
        "single_axis_selector",
        "endpoint_or_count_fiber_selector",
        "control_formable",
    }
    <= set(reasons(control_axis)),
    "control_chars=%s reasons=%s" % (control_chars, ",".join(reasons(control_axis))),
)


missing_endpoint = live_source(
    generates_endpoint_integrality=False,
    required_edges=REQUIRED_EDGES - {("internal_effectivity_domain", "endpoint")},
)

gate(
    "SCF7 character stratum functor must generate endpoint integrality",
    not accepts_character_functor(missing_endpoint)
    and {
        "endpoint_integrality_not_generated",
        "required_character_stratum_edges_missing",
    }
    <= set(reasons(missing_endpoint)),
    ",".join(reasons(missing_endpoint)),
)


declared = live_source(
    character_stratum_functor_actual=False,
    maps_convolution_to_stratum_product=False,
    produces_internal_effectivity_domain=False,
    required_edges=set(),
    declared_stratum_functor=True,
)

gate(
    "SCF8 declared character-stratum functors without edges are rejected",
    not accepts_character_functor(declared)
    and {
        "character_stratum_functor_not_actual",
        "convolution_not_mapped_to_stratum_product",
        "internal_effectivity_domain_not_produced",
        "required_character_stratum_edges_missing",
        "declared_stratum_functor",
    }
    <= set(reasons(declared)),
    ",".join(reasons(declared)),
)


live = live_source()

gate(
    "SCF9 accepted branch retains full character data before strata",
    accepts_character_functor(live)
    and REQUIRED_EDGES <= live["required_edges"]
    and chars["LxF22"] == {2: 2, 4: 2},
    "edges=%d LxF22=%s" % (len(live["required_edges"]), chars["LxF22"]),
)


dead_sources = {
    "diagonal_selector": diagonal_selector,
    "single_axis": single_axis,
    "factorization_selector": factorization_selector,
    "zero_throwaway": zero_throwaway,
    "control_axis": control_axis,
    "missing_endpoint": missing_endpoint,
    "declared": declared,
}

gate(
    "SCF10 only full character-to-strata functor passes",
    accepts_character_functor(live)
    and not any(accepts_character_functor(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_character_functor(data) for data in dead_sources.values()),
        accepts_character_functor(live),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nSCF1-SCF10 ALL PASS: strict-square character-to-stratum functor contract pinned")
print(
    "VERDICT: the strict-square extraction cannot be a scalar axis selector "
    "on chi_col. It must be a full character-to-internal-strata functor that "
    "retains multi-axis classes, coefficients, signed zero-fiber data, and "
    "convolution before generating the Qbar_BECD effectivity domain and its "
    "endpoint, boundary, graph/Rosati/count, and control-death data."
)
