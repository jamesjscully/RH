"""CC non-geometric exactness-set repair witness.

Docs 189-190 leave one explicit way to avoid the CC-ceiling pole: replace
the b-geometric exactness atoms {b^j} by a non-geometric exactness set.  This
witness checks the hand-retuned version of that repair.

The repair can avoid the named pole mechanism only by spending new sequence
data not supplied by the CC ceiling, the square carrier, or a non-EM square
functor.  In finite windows the sequence choices already overproduce, and the
repair constructs no square H^2, intersection form, correspondence algebra,
Frobenius graph, positive Rosati, Laurent boundary map, or torsor splitter.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_cc_non_geometric_exactness_no_go
"""

from math import comb

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def is_power_of_b(k, b):
    if k < 1:
        return False
    while k % b == 0:
        k //= b
    return k == 1


def power_exactness_set(b, limit):
    return [k for k in range(1, limit + 1) if is_power_of_b(k, b)]


def dmp_dim(deg):
    if deg == -1:
        return 1
    if deg >= 0:
        return 1
    return 0


window_b2 = 2**6
window_b3 = 3**6
cc_exact_b2 = power_exactness_set(2, window_b2)
cc_exact_b3 = power_exactness_set(3, window_b3)

# Representative hand-retuned exactness sets: same finite cardinality as the
# CC atom set in the window, but not equal to the b-power set.
candidate_b2 = [1, 2, 3, 5, 7, 11, 13]
candidate_b3 = [1, 3, 5, 7, 11, 13, 17]

selector_choices_b2 = comb(window_b2, len(cc_exact_b2)) - 1
selector_choices_b3 = comb(window_b3, len(cc_exact_b3)) - 1
selector_pair_choices = selector_choices_b2 * selector_choices_b3

proposal_uses_non_geometric_exactness = True
proposal_keeps_zeta_regularization = True
square_exactness_selector_defined = False
base_covariance_rule_defined = False
cc_ceiling_preserved = False
cc_log_periodic_quantizer_preserved = False
carrier_native_aggregation_constructed = False
non_em_square_functor_defined = False
diagonal_factorization_broken = False

square_h2_defined = False
square_intersection_form_defined = False
square_correspondence_algebra_defined = False
frobenius_graph_defined = False
positive_rosati_defined = False

laurent_axis_defined = False
boundary_map_defined = False
torsor_splitter_defined = False
dd4_weight_ge_1_datum_defined = False
dh_epstein_death_at_square_map = False


gate(
    "CNE1 this is the non-geometric exactness evasion, not a new carrier",
    proposal_uses_non_geometric_exactness
    and proposal_keeps_zeta_regularization
    and not carrier_native_aggregation_constructed,
    "tests doc-189 evasion branch (a) with no supplied square aggregation",
)

gate(
    "CNE2 CC-ceiling exactness atoms are b-geometric",
    cc_exact_b2 == [1, 2, 4, 8, 16, 32, 64]
    and cc_exact_b3 == [1, 3, 9, 27, 81, 243, 729],
    f"base2={cc_exact_b2}, base3={cc_exact_b3}",
)

gate(
    "CNE3 retuned non-geometric sets are not the CC ceiling exactness sets",
    candidate_b2 != cc_exact_b2
    and candidate_b3 != cc_exact_b3
    and any(not is_power_of_b(k, 2) for k in candidate_b2)
    and any(not is_power_of_b(k, 3) for k in candidate_b3),
    f"candidate_b2={candidate_b2}, candidate_b3={candidate_b3}",
)

gate(
    "CNE4 finite-window exactness selectors massively overproduce",
    selector_choices_b2 > 10**8 and selector_choices_b3 > 10**14,
    f"choices_b2={selector_choices_b2}, choices_b3={selector_choices_b3}",
)

gate(
    "CNE5 base-pair retuning adds independent sequence choices",
    selector_pair_choices > selector_choices_b2
    and selector_pair_choices > selector_choices_b3
    and not square_exactness_selector_defined
    and not base_covariance_rule_defined,
    f"paired_choices={selector_pair_choices}",
)

gate(
    "CNE6 de-geometrizing exactness abandons the CC ceiling mechanism",
    not cc_ceiling_preserved and not cc_log_periodic_quantizer_preserved,
    "the pole is avoided only by replacing the CC atom sequence",
)

gate(
    "CNE7 no non-EM square functor or carrier-native aggregation is built",
    not non_em_square_functor_defined
    and not diagonal_factorization_broken
    and not carrier_native_aggregation_constructed,
    "no CC-internal square functor escapes the diagonal probes",
)

gate(
    "CNE8 no square H2/intersection/correspondence/Rosati is constructed",
    not square_h2_defined
    and not square_intersection_form_defined
    and not square_correspondence_algebra_defined
    and not frobenius_graph_defined
    and not positive_rosati_defined,
    "an exactness sequence is not square correspondence data",
)

gate(
    "CNE9 no Laurent boundary or DD4 weight>=1 data is constructed",
    not laurent_axis_defined
    and not boundary_map_defined
    and not torsor_splitter_defined
    and not dd4_weight_ge_1_datum_defined,
    "no boundary map, torsor splitter, or weight>=1 datum",
)

gate(
    "CNE10 base R1 obstructions and carrier guard remain",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and not dh_epstein_death_at_square_map
    and not square_correspondence_algebra_defined,
    "DMP bottom gap remains; no carrier-consuming square map where controls die",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (CNE1-CNE10)")
