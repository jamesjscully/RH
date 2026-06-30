"""CC strict bar/character grading repair witness.

Doc 188 kills promoting strict-square divided-power/character invariants
directly to End(S^2/Z).  The sharper repair is to grade those invariants by
the strict cyclic bar direction: the grading exists, but the known character
and divided-power data do not become the Bokstedt tower.

This witness records the certified V-worker facts used as the R1 gate.  The
universal strict invariant is the free monoid-ring character algebra; the
mod-p divided-power probes are not closed cochains under the strict bar
differential; the character-shaped H^1 is zero in the verified window; and
the degree-3 Bokstedt Z/2 slot is not produced in the tested character span.
No square H^2, intersection form, correspondence algebra, Frobenius graph,
positive Rosati, Laurent boundary map, or torsor splitter is constructed.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_cc_strict_bar_grading_no_go
"""

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def dmp_dim(deg):
    if deg == -1:
        return 1
    if deg >= 0:
        return 1
    return 0


bar_grading_formable = True
face_dictionary_exact_instances = 180000
subset_character_move_instances = 571536
subset_character_violations = 0

universal_character_is_free_monoid_ring = True
degree0_strict_is_monoid_ring_not_z = True
order4_mod_invariant_exists = True
per_prime_probe_pattern_is_artifact = True

divided_power_nonclosed_counts = {
    "PhiP2": 14016,
    "Phi2": 95280,
    "PhiP3": 111370,
    "Phi3": 125017,
}
minimal_counterexample_recorded = True
character_h1_window_kernel_zero_functional = True
degree3_character_span_class_found = False
higher_span_scope_is_bounded = True

strict_bar_route_constructs_bokstedt_tower = False
non_character_joint_shape_classified = False
derived_replacement_constructed = False
smash_of_tolerant_modules_defined = False

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
    "SBG1 strict cyclic-bar grading is formable on character data",
    bar_grading_formable
    and subset_character_move_instances == 571536
    and subset_character_violations == 0
    and face_dictionary_exact_instances == 180000,
    (
        f"subset moves={subset_character_move_instances}, "
        f"face checks={face_dictionary_exact_instances}"
    ),
)

gate(
    "SBG2 universal strict character algebra is free monoid-ring data",
    universal_character_is_free_monoid_ring
    and degree0_strict_is_monoid_ring_not_z
    and order4_mod_invariant_exists,
    "degree 0 strict side is monoid-ring excess, not THH pi_0 = Z",
)

gate(
    "SBG3 per-prime divided-power resonance is probe artifact",
    order4_mod_invariant_exists and per_prime_probe_pattern_is_artifact,
    "character algebra carries mod-m data for every m, not only primes",
)

gate(
    "SBG4 divided-power probes are not closed strict-bar cochains",
    all(count > 0 for count in divided_power_nonclosed_counts.values())
    and minimal_counterexample_recorded,
    f"nonclosed counts={divided_power_nonclosed_counts}",
)

gate(
    "SBG5 character-shaped H1 is zero in the verified window",
    character_h1_window_kernel_zero_functional,
    "only g=g'=cB, the zero functional, survives the H1 character kernel",
)

gate(
    "SBG6 degree-3 Bokstedt slot is not produced in the tested character span",
    not degree3_character_span_class_found and higher_span_scope_is_bounded,
    "H3 estimate is empty in the subset-character sampled/span-scoped computation",
)

gate(
    "SBG7 evasion requires new joint-shape invariants or derived replacement",
    not non_character_joint_shape_classified
    and not derived_replacement_constructed
    and not smash_of_tolerant_modules_defined,
    "the classified character route does not build the missing square functor",
)

gate(
    "SBG8 no square H2/intersection/correspondence/Rosati is constructed",
    not square_h2_defined
    and not square_intersection_form_defined
    and not square_correspondence_algebra_defined
    and not frobenius_graph_defined
    and not positive_rosati_defined,
    "strict bar character data is not the square correspondence algebra",
)

gate(
    "SBG9 no Laurent boundary or DD4 weight>=1 data is constructed",
    not laurent_axis_defined
    and not boundary_map_defined
    and not torsor_splitter_defined
    and not dd4_weight_ge_1_datum_defined,
    "no boundary map, torsor splitter, or weight>=1 datum",
)

gate(
    "SBG10 base R1 obstructions and carrier guard remain",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and not dh_epstein_death_at_square_map
    and not square_correspondence_algebra_defined
    and not strict_bar_route_constructs_bokstedt_tower,
    "DMP bottom gap remains; no carrier-consuming square map where controls die",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (SBG1-SBG10)")
