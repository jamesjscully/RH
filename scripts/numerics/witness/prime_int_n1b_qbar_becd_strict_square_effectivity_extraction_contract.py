r"""Strict-square to effectivity-domain extraction contract for Qbar_BECD.

Docs 323-325 say the missing first generator is a non-circular represented
internal effectivity stratum.  Docs 187-188 left one strong local positive
signal: the strict Gamma-set square has object-level divided-power/character
data that does not collapse to the diagonal.  This witness isolates the only
way that signal can still matter: an actual non-EM extraction functor must
turn strict-square character data into the Qbar_BECD internal effectivity
stratum and generate endpoint, boundary, graph/Rosati/count, and control
death from it.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_strict_square_effectivity_extraction_contract
"""

from __future__ import annotations

from math import factorial


failures: list[str] = []

REQUIRED_EDGES = {
    ("strict_square_data", "extraction_functor"),
    ("extraction_functor", "internal_effectivity_domain"),
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


def column_sums(a, b, edges) -> list[int]:
    cols = [0] * len(b)
    for i, j in edges:
        cols[j] += a[i]
    return cols


def row_sums(a, b, edges) -> list[int]:
    rows = [0] * len(a)
    for i, j in edges:
        rows[i] += b[j]
    return rows


def phi_col_mod_p(a, b, edges, p: int) -> int:
    cols = column_sums(a, b, edges)
    return sum((b[j] ** p) * binom_int(cols[j], p) for j in range(len(b))) % p


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


def valuation_depth(n: int, p: int) -> int | None:
    depth = 0
    while n > 1 and n % p == 0:
        n //= p
        depth += 1
    if n != 1:
        return None
    return depth


def source(**kwargs):
    data = {
        "strict_square_object_data_actual": False,
        "diagonal_fiber_noncollapse_visible": False,
        "bilinear_factorization_memory_visible": False,
        "universal_character_data_visible": False,
        "extraction_functor_actual": False,
        "extraction_non_em": False,
        "extraction_not_diagonal_factorizing": False,
        "maps_characters_to_internal_strata": False,
        "produces_internal_effectivity_domain": False,
        "produces_prime_power_towers": False,
        "produces_valuation_depth": False,
        "generates_endpoint_integrality": False,
        "generates_boundary_localization": False,
        "generates_graph_rosati_count": False,
        "controls_undefined_at_extraction": False,
        "epstein_undefined_at_extraction": False,
        "required_edges": set(),
        "raw_divided_power_promoted": False,
        "raw_character_monoid_promoted": False,
        "published_diagonal_probe": False,
        "ad_hoc_grading_dictionary": False,
        "external_prime_axis_selector": False,
        "endpoint_or_count_fiber_extraction": False,
        "declared_extraction_functor": False,
        "control_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("strict_square_object_data_actual", "strict_square_object_data_missing"),
    ("diagonal_fiber_noncollapse_visible", "diagonal_fiber_noncollapse_not_visible"),
    (
        "bilinear_factorization_memory_visible",
        "bilinear_factorization_memory_not_visible",
    ),
    ("universal_character_data_visible", "universal_character_data_not_visible"),
    ("extraction_functor_actual", "extraction_functor_not_actual"),
    ("extraction_non_em", "extraction_not_non_em"),
    (
        "extraction_not_diagonal_factorizing",
        "extraction_factorizes_through_diagonal",
    ),
    (
        "maps_characters_to_internal_strata",
        "characters_not_mapped_to_internal_strata",
    ),
    (
        "produces_internal_effectivity_domain",
        "internal_effectivity_domain_not_produced",
    ),
    ("produces_prime_power_towers", "prime_power_towers_not_produced"),
    ("produces_valuation_depth", "valuation_depth_not_produced"),
    ("generates_endpoint_integrality", "endpoint_integrality_not_generated"),
    (
        "generates_boundary_localization",
        "boundary_localization_not_generated",
    ),
    ("generates_graph_rosati_count", "graph_rosati_count_not_generated"),
    ("controls_undefined_at_extraction", "controls_not_undefined_at_extraction"),
    ("epstein_undefined_at_extraction", "epstein_not_undefined_at_extraction"),
)

BANNED = (
    ("raw_divided_power_promoted", "raw_divided_power_promoted"),
    ("raw_character_monoid_promoted", "raw_character_monoid_promoted"),
    ("published_diagonal_probe", "published_diagonal_probe"),
    ("ad_hoc_grading_dictionary", "ad_hoc_grading_dictionary"),
    ("external_prime_axis_selector", "external_prime_axis_selector"),
    ("endpoint_or_count_fiber_extraction", "endpoint_or_count_fiber_extraction"),
    ("declared_extraction_functor", "declared_extraction_functor"),
    ("control_formable", "control_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_EDGES <= set(data["required_edges"]):
        out.append("required_extraction_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_extraction(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        strict_square_object_data_actual=True,
        diagonal_fiber_noncollapse_visible=True,
        bilinear_factorization_memory_visible=True,
        universal_character_data_visible=True,
        extraction_functor_actual=True,
        extraction_non_em=True,
        extraction_not_diagonal_factorizing=True,
        maps_characters_to_internal_strata=True,
        produces_internal_effectivity_domain=True,
        produces_prime_power_towers=True,
        produces_valuation_depth=True,
        generates_endpoint_integrality=True,
        generates_boundary_localization=True,
        generates_graph_rosati_count=True,
        controls_undefined_at_extraction=True,
        epstein_undefined_at_extraction=True,
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

L_total = total(*L)
C3_total = total(*C3)
L_phi2 = phi_row_mod_p(*L, 2)
C3_phi2 = phi_row_mod_p(*C3, 2)
F22_total = total(*F22)
F41_total = total(*F41)
F22_phi3 = phi_col_mod_p(*F22, 3)
F41_phi3 = phi_col_mod_p(*F41, 3)
zero_chi = chi_col(*ZERO_SPLIT)
chi_L = chi_col(*L)
chi_C3 = chi_col(*C3)
chi_F22 = chi_col(*F22)
chi_F41 = chi_col(*F41)
prod_chi = chi_col(*square_product(L, F22))

gate(
    "SSE1 strict square has real object-level noncollapse",
    L_total == C3_total == 3
    and L_phi2 == 1
    and C3_phi2 == 0
    and F22_total == F41_total == 4
    and F22_phi3 == 0
    and F41_phi3 == 1
    and zero_chi == {1: 2, 2: -1},
    "mu(L)=mu(C3)=%d Phi2=%d/%d Phi3=%d/%d zero_chi=%s"
    % (L_total, L_phi2, C3_phi2, F22_phi3, F41_phi3, zero_chi),
)


gate(
    "SSE2 universal character convolution is real but overproduces axes",
    chi_L == {1: 1, 2: 1}
    and chi_C3 == {3: 1}
    and chi_F22 == {2: 2}
    and chi_F41 == {4: 1}
    and prod_chi == convolve_chi(chi_L, chi_F22),
    "chiL=%s chiC3=%s chiF22=%s chiF41=%s prod=%s"
    % (chi_L, chi_C3, chi_F22, chi_F41, prod_chi),
)


raw_divided = live_source(
    extraction_functor_actual=False,
    extraction_non_em=False,
    maps_characters_to_internal_strata=False,
    produces_internal_effectivity_domain=False,
    generates_endpoint_integrality=False,
    generates_boundary_localization=False,
    generates_graph_rosati_count=False,
    controls_undefined_at_extraction=False,
    epstein_undefined_at_extraction=False,
    required_edges={("strict_square_data", "internal_effectivity_domain")},
    raw_divided_power_promoted=True,
    control_formable=True,
)

gate(
    "SSE3 raw divided-power invariants are not the extraction functor",
    not accepts_extraction(raw_divided)
    and {
        "extraction_functor_not_actual",
        "characters_not_mapped_to_internal_strata",
        "internal_effectivity_domain_not_produced",
        "endpoint_integrality_not_generated",
        "boundary_localization_not_generated",
        "graph_rosati_count_not_generated",
        "controls_not_undefined_at_extraction",
        "epstein_not_undefined_at_extraction",
        "required_extraction_edges_missing",
        "raw_divided_power_promoted",
        "control_formable",
    }
    <= set(reasons(raw_divided)),
    ",".join(reasons(raw_divided)),
)


raw_character = live_source(
    extraction_functor_actual=False,
    maps_characters_to_internal_strata=False,
    produces_internal_effectivity_domain=False,
    produces_prime_power_towers=False,
    produces_valuation_depth=False,
    required_edges=set(),
    raw_character_monoid_promoted=True,
    external_prime_axis_selector=True,
    control_formable=True,
)

gate(
    "SSE4 raw character monoid is not a canonical effectivity stratum",
    not accepts_extraction(raw_character)
    and {
        "extraction_functor_not_actual",
        "characters_not_mapped_to_internal_strata",
        "internal_effectivity_domain_not_produced",
        "prime_power_towers_not_produced",
        "valuation_depth_not_produced",
        "required_extraction_edges_missing",
        "raw_character_monoid_promoted",
        "external_prime_axis_selector",
        "control_formable",
    }
    <= set(reasons(raw_character)),
    ",".join(reasons(raw_character)),
)


diagonal_probe = live_source(
    diagonal_fiber_noncollapse_visible=False,
    bilinear_factorization_memory_visible=False,
    extraction_not_diagonal_factorizing=False,
    maps_characters_to_internal_strata=False,
    required_edges=set(),
    published_diagonal_probe=True,
)

gate(
    "SSE5 published diagonal probes lose the square-only split",
    L_total == C3_total
    and not accepts_extraction(diagonal_probe)
    and {
        "diagonal_fiber_noncollapse_not_visible",
        "bilinear_factorization_memory_not_visible",
        "extraction_factorizes_through_diagonal",
        "characters_not_mapped_to_internal_strata",
        "required_extraction_edges_missing",
        "published_diagonal_probe",
    }
    <= set(reasons(diagonal_probe)),
    ",".join(reasons(diagonal_probe)),
)


ad_hoc_degree = live_source(
    extraction_functor_actual=False,
    extraction_non_em=False,
    produces_internal_effectivity_domain=False,
    domain_note="Phi2_as_degree_3",
    ad_hoc_grading_dictionary=True,
    control_formable=True,
)

gate(
    "SSE6 ad-hoc grading dictionaries do not extract the domain",
    not accepts_extraction(ad_hoc_degree)
    and {
        "extraction_functor_not_actual",
        "extraction_not_non_em",
        "internal_effectivity_domain_not_produced",
        "ad_hoc_grading_dictionary",
        "control_formable",
    }
    <= set(reasons(ad_hoc_degree)),
    ",".join(reasons(ad_hoc_degree)),
)


fiber_extraction = live_source(
    extraction_functor_actual=False,
    produces_internal_effectivity_domain=False,
    generates_endpoint_integrality=False,
    generates_graph_rosati_count=False,
    endpoint_or_count_fiber_extraction=True,
    control_formable=True,
)

gate(
    "SSE7 endpoint/count-fiber extraction reverses first-generation direction",
    not accepts_extraction(fiber_extraction)
    and {
        "extraction_functor_not_actual",
        "internal_effectivity_domain_not_produced",
        "endpoint_integrality_not_generated",
        "graph_rosati_count_not_generated",
        "endpoint_or_count_fiber_extraction",
        "control_formable",
    }
    <= set(reasons(fiber_extraction)),
    ",".join(reasons(fiber_extraction)),
)


declared = live_source(
    extraction_functor_actual=False,
    extraction_non_em=False,
    extraction_not_diagonal_factorizing=False,
    maps_characters_to_internal_strata=False,
    produces_internal_effectivity_domain=False,
    required_edges=set(),
    declared_extraction_functor=True,
)

gate(
    "SSE8 declared extraction functor without represented edges is rejected",
    not accepts_extraction(declared)
    and {
        "extraction_functor_not_actual",
        "extraction_not_non_em",
        "extraction_factorizes_through_diagonal",
        "characters_not_mapped_to_internal_strata",
        "internal_effectivity_domain_not_produced",
        "required_extraction_edges_missing",
        "declared_extraction_functor",
    }
    <= set(reasons(declared)),
    ",".join(reasons(declared)),
)


tower = [2**k for k in range(6)]
depths = [valuation_depth(n, 2) for n in tower]
live = live_source()

gate(
    "SSE9 accepted branch is extraction functor to internal effectivity strata",
    accepts_extraction(live)
    and tower == [1, 2, 4, 8, 16, 32]
    and depths == [0, 1, 2, 3, 4, 5]
    and REQUIRED_EDGES <= live["required_edges"],
    "tower=%s depths=%s edges=%d" % (tower, depths, len(live["required_edges"])),
)


dead_sources = {
    "raw_divided": raw_divided,
    "raw_character": raw_character,
    "diagonal_probe": diagonal_probe,
    "ad_hoc_degree": ad_hoc_degree,
    "fiber_extraction": fiber_extraction,
    "declared": declared,
}

gate(
    "SSE10 only represented strict-square extraction passes",
    accepts_extraction(live)
    and not any(accepts_extraction(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_extraction(data) for data in dead_sources.values()),
        accepts_extraction(live),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nSSE1-SSE10 ALL PASS: strict-square effectivity extraction contract pinned")
print(
    "VERDICT: strict Gamma-set square divided-power/character data remains a "
    "credible positive signal only through an actual non-EM extraction functor "
    "to Qbar_BECD internal effectivity strata. Raw invariants, character "
    "monoids, diagonal probes, ad-hoc gradings, endpoint/count fibers, and "
    "declared functors do not meet this contract."
)
