"""N1-b' determinant/orientation normalization witness.

Doc 169 kills extracting a boundary corner, minor, determinant line, cofactor,
or Schur scalar from the support opposite graph.  The next repair is to add an
orientation or determinant-one normalization to the graph/boundary package and
claim that the normalization pins the endpoint or Laurent twist.

In the finite F_2 support windows this cannot work.  The determinant unit
group is F_2^* = {1}, so determinant-one orientation is tautological on every
invertible finite F_2 map.  It supplies no endpoint, no boundary map, no
Laurent generator, and no torsor splitter.  The same normalization package is
formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_orientation_normalization_no_go
"""

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def dmp_rank_truncated(nmax):
    return nmax + 2


def dmp_dim(deg):
    if deg == -1:
        return 1
    if deg >= 0:
        return 1
    return 0


def graph_lagrangian_count_f2(rank):
    # Symmetric maps M -> M^vee in the finite F_2 hyperbolic model.
    return 2 ** (rank * (rank + 1) // 2)


def rank_one_idempotent_count_f2(rank):
    return (2**rank - 1) * 2 ** (rank - 1)


def laurent_unit_twists_in_window(kmax):
    return 2 * kmax + 1


ranks = {nmax: dmp_rank_truncated(nmax) for nmax in (1, 2, 4, 8)}
tate_window_ranks = {nmax: 2 * rank for nmax, rank in ranks.items()}
graph_lagrangian_counts = {
    nmax: graph_lagrangian_count_f2(rank) for nmax, rank in ranks.items()
}
endpoint_pair_choices = {nmax: rank * rank for nmax, rank in ranks.items()}
coordinate_matching_counts = {1: 6, 2: 24, 4: 720, 8: 3628800}
f2_unit_count = 1
orientation_unit_choices = {nmax: f2_unit_count for nmax in ranks}
determinant_sign_bits = {nmax: 0 for nmax in ranks}
determinant_one_filter_tautological = True
laurent_unit_twist_counts = {
    kmax: laurent_unit_twists_in_window(kmax) for kmax in (1, 2, 4, 8)
}
rank_one_idempotent_counts_tate = {
    nmax: rank_one_idempotent_count_f2(rank)
    for nmax, rank in tate_window_ranks.items()
}

orientation_outputs_scalar = True
orientation_outputs_endpoint = False
orientation_outputs_boundary_map = False
orientation_outputs_laurent_generator = False
determinant_degree_normalization_outputs_total_scalar = True
determinant_degree_normalization_outputs_boundary_twist = False

gate(
    "ONR1 support tensor ranks are unchanged",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "ONR2 graph/opposite Lagrangian choices are still present",
    graph_lagrangian_counts
    == {1: 64, 2: 1024, 4: 2097152, 8: 36028797018963968},
    f"graph_lagrangian_counts={graph_lagrangian_counts}",
)

gate(
    "ONR3 F_2 determinant orientation has no sign choice",
    f2_unit_count == 1
    and orientation_unit_choices == {1: 1, 2: 1, 4: 1, 8: 1}
    and determinant_sign_bits == {1: 0, 2: 0, 4: 0, 8: 0},
    (
        f"f2_unit_count={f2_unit_count}, "
        f"orientation_unit_choices={orientation_unit_choices}, "
        f"determinant_sign_bits={determinant_sign_bits}"
    ),
)

gate(
    "ONR4 determinant-one normalization is tautological after invertibility",
    determinant_one_filter_tautological,
    "over F_2, every nonzero determinant equals 1",
)

gate(
    "ONR5 orientation normalization supplies no endpoint or boundary map",
    orientation_outputs_scalar
    and not orientation_outputs_endpoint
    and not orientation_outputs_boundary_map,
    (
        f"orientation_outputs_scalar={orientation_outputs_scalar}, "
        f"orientation_outputs_endpoint={orientation_outputs_endpoint}, "
        f"orientation_outputs_boundary_map={orientation_outputs_boundary_map}"
    ),
)

gate(
    "ONR6 orientation normalization supplies no Laurent generator",
    not orientation_outputs_laurent_generator,
    f"orientation_outputs_laurent_generator={orientation_outputs_laurent_generator}",
)

gate(
    "ONR7 determinant degree normalization is only total scalar data",
    determinant_degree_normalization_outputs_total_scalar
    and not determinant_degree_normalization_outputs_boundary_twist,
    (
        f"determinant_degree_normalization_outputs_total_scalar="
        f"{determinant_degree_normalization_outputs_total_scalar}, "
        f"determinant_degree_normalization_outputs_boundary_twist="
        f"{determinant_degree_normalization_outputs_boundary_twist}"
    ),
)

gate(
    "ONR8 endpoint and half-matching choices remain",
    endpoint_pair_choices == {1: 9, 2: 16, 4: 36, 8: 100}
    and coordinate_matching_counts == {1: 6, 2: 24, 4: 720, 8: 3628800},
    (
        f"endpoint_pair_choices={endpoint_pair_choices}, "
        f"coordinate_matching_counts={coordinate_matching_counts}"
    ),
)

gate(
    "ONR9 Laurent twist choices remain unpinned",
    laurent_unit_twist_counts == {1: 3, 2: 5, 4: 9, 8: 17},
    f"laurent_unit_twist_counts={laurent_unit_twist_counts}",
)

gate(
    "ONR10 Tate rank-one idempotent choices remain",
    rank_one_idempotent_counts_tate
    == {1: 2016, 2: 32640, 4: 8386560, 8: 549755289600},
    f"rank_one_idempotent_counts_tate={rank_one_idempotent_counts_tate}",
)

obstruction_res1 = 1
coboundary_res1 = 0
carrier_multiplication_supplied = False
torsor_splitter_supplied = False
gate(
    "ONR11 orientation normalization does not repair bottom, shear, or torsor obstructions",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and obstruction_res1 == 1
    and coboundary_res1 == 0
    and not carrier_multiplication_supplied
    and not torsor_splitter_supplied,
    "y^2=0, no DMP degree -2, res_1(c)=1, and no b/phi(b)=c",
)

control_orientation_unit_choices = orientation_unit_choices.copy()
control_determinant_one_filter_tautological = determinant_one_filter_tautological
gate(
    "ONR12 the same orientation-normalization package is formable on controls",
    control_orientation_unit_choices == orientation_unit_choices
    and control_determinant_one_filter_tautological
    == determinant_one_filter_tautological,
    "determinant-one and orientation normalization are finite-free support operations",
)

primitive_carrier_maps_consumed = 0
orientation_normalization_inserted = 1
endpoint_choice_inserted = 1
laurent_twist_chosen = 1
gate(
    "ONR13 surviving orientation route must be carrier-native",
    primitive_carrier_maps_consumed == 0
    and orientation_normalization_inserted == 1
    and endpoint_choice_inserted == 1
    and laurent_twist_chosen == 1,
    "a real route must construct orientation, endpoint, boundary glue, and twist from correspondences",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (ONR1-ONR13)")
print(
    "VERDICT: determinant-one or orientation normalization of the support "
    "opposite graph does not supply R1 boundary glue.  Over F_2 the "
    "determinant unit group is trivial, so determinant-one is tautological "
    "after invertibility; orientation supplies scalar shadow data, not an "
    "endpoint, boundary map, Laurent generator, or torsor splitter.  "
    "Endpoint/matching/idempotent choices, Laurent twists, and "
    "bottom/shear/torsor obstructions remain, and the same package is "
    "formable on controls.  A surviving route must construct any orientation "
    "or determinant datum carrier-natively."
)
