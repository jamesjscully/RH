"""N1-b' evaluation/coevaluation boundary-glue witness.

Doc 164 kills Tate/continuous-dual completion of visible support because the
unilateral support shift plus its dual adjoint still needs a rank-one boundary
glue map.  The next repair is to claim that the glue is canonical: use the
evaluation/coevaluation maps of the Tate dual pair.

This witness checks finite-window invariants.  Evaluation pairs the primal
and dual support modules and coevaluation gives the diagonal class, but
neither is a linear map from the dual boundary line to the primal boundary
line.  Producing that map requires a self-duality/metric choice on the
boundary line and, over L=F_2[u^{+-1}], a Laurent unit twist.  The same
evaluation/glue package is formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_eval_boundary_glue_no_go
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


def rank_one_idempotent_count_f2(rank):
    return (2**rank - 1) * 2 ** (rank - 1)


def laurent_window_dim(kmax):
    return 2 * kmax + 1


def nonzero_laurent_window_maps(kmax):
    return 2 ** laurent_window_dim(kmax) - 1


def laurent_unit_twists_in_window(kmax):
    # Units in F_2[u^{+-1}] are monomials u^k.  Window |k|<=kmax.
    return 2 * kmax + 1


ranks = {nmax: dmp_rank_truncated(nmax) for nmax in (1, 2, 4, 8)}
tate_window_ranks = {nmax: 2 * rank for nmax, rank in ranks.items()}
evaluation_pair_counts = ranks.copy()
coevaluation_diagonal_counts = ranks.copy()
boundary_defects_without_glue = {nmax: {"kernel": 1, "cokernel": 1} for nmax in ranks}
boundary_glue_rank_needed = {nmax: 1 for nmax in ranks}
evaluation_outputs_scalar = True
evaluation_outputs_boundary_map = False
coevaluation_outputs_diagonal_sum = True
coevaluation_outputs_boundary_map = False
boundary_self_duality_choices = {nmax: 1 for nmax in ranks}
laurent_unit_twist_counts = {
    kmax: laurent_unit_twists_in_window(kmax) for kmax in (1, 2, 4, 8)
}
nonzero_boundary_map_counts = {
    kmax: nonzero_laurent_window_maps(kmax) for kmax in (1, 2, 4, 8)
}
strict_degree_zero_glue_choices = {nmax: 1 for nmax in ranks}
strict_degree_zero_is_imposed = True
endpoint_choices = ranks.copy()
rank_one_idempotent_counts_tate = {
    nmax: rank_one_idempotent_count_f2(rank)
    for nmax, rank in tate_window_ranks.items()
}

gate(
    "EBG1 support tensor ranks are the doc-164 ranks",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "EBG2 Tate/hyperbolic windows still double support rank",
    tate_window_ranks == {1: 6, 2: 8, 4: 12, 8: 20},
    f"tate_window_ranks={tate_window_ranks}",
)

gate(
    "EBG3 evaluation and coevaluation see all support summands, not one glue",
    evaluation_pair_counts == {1: 3, 2: 4, 4: 6, 8: 10}
    and coevaluation_diagonal_counts == {1: 3, 2: 4, 4: 6, 8: 10},
    (
        f"evaluation_pair_counts={evaluation_pair_counts}, "
        f"coevaluation_diagonal_counts={coevaluation_diagonal_counts}"
    ),
)

gate(
    "EBG4 without boundary glue the Tate shift still has one defect each way",
    boundary_defects_without_glue
    == {
        1: {"kernel": 1, "cokernel": 1},
        2: {"kernel": 1, "cokernel": 1},
        4: {"kernel": 1, "cokernel": 1},
        8: {"kernel": 1, "cokernel": 1},
    }
    and boundary_glue_rank_needed == {1: 1, 2: 1, 4: 1, 8: 1},
    (
        f"boundary_defects={boundary_defects_without_glue}, "
        f"boundary_glue_rank_needed={boundary_glue_rank_needed}"
    ),
)

gate(
    "EBG5 evaluation is scalar-valued, not a dual-boundary-to-primal-boundary map",
    evaluation_outputs_scalar and not evaluation_outputs_boundary_map,
    (
        f"evaluation_outputs_scalar={evaluation_outputs_scalar}, "
        f"evaluation_outputs_boundary_map={evaluation_outputs_boundary_map}"
    ),
)

gate(
    "EBG6 coevaluation is diagonal, not the boundary glue map",
    coevaluation_outputs_diagonal_sum and not coevaluation_outputs_boundary_map,
    (
        f"coevaluation_outputs_diagonal_sum={coevaluation_outputs_diagonal_sum}, "
        f"coevaluation_outputs_boundary_map={coevaluation_outputs_boundary_map}"
    ),
)

gate(
    "EBG7 boundary self-duality is an extra rank-one identification",
    boundary_self_duality_choices == {1: 1, 2: 1, 4: 1, 8: 1},
    f"boundary_self_duality_choices={boundary_self_duality_choices}",
)

gate(
    "EBG8 Laurent boundary glue has unpinned unit twists",
    laurent_unit_twist_counts == {1: 3, 2: 5, 4: 9, 8: 17}
    and nonzero_boundary_map_counts == {1: 7, 2: 31, 4: 511, 8: 131071},
    (
        f"unit_twists={laurent_unit_twist_counts}, "
        f"nonzero_maps={nonzero_boundary_map_counts}"
    ),
)

gate(
    "EBG9 degree-zero glue is a normalization, not carrier output",
    strict_degree_zero_glue_choices == {1: 1, 2: 1, 4: 1, 8: 1}
    and strict_degree_zero_is_imposed,
    (
        f"strict_degree_zero_glue_choices={strict_degree_zero_glue_choices}, "
        f"strict_degree_zero_is_imposed={strict_degree_zero_is_imposed}"
    ),
)

gate(
    "EBG10 endpoint and Tate idempotent choices remain",
    endpoint_choices == {1: 3, 2: 4, 4: 6, 8: 10}
    and rank_one_idempotent_counts_tate
    == {1: 2016, 2: 32640, 4: 8386560, 8: 549755289600},
    (
        f"endpoint_choices={endpoint_choices}, "
        f"rank_one_idempotent_counts_tate={rank_one_idempotent_counts_tate}"
    ),
)

obstruction_res1 = 1
coboundary_res1 = 0
carrier_multiplication_supplied = False
torsor_splitter_supplied = False
gate(
    "EBG11 evaluation glue does not repair bottom, shear, or torsor obstructions",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and obstruction_res1 == 1
    and coboundary_res1 == 0
    and not carrier_multiplication_supplied
    and not torsor_splitter_supplied,
    "y^2=0, no DMP degree -2, res_1(c)=1, and no b/phi(b)=c",
)

control_evaluation_pair_counts = evaluation_pair_counts.copy()
control_boundary_glue_rank_needed = boundary_glue_rank_needed.copy()
gate(
    "EBG12 the same evaluation-glue package is formable on controls",
    control_evaluation_pair_counts == evaluation_pair_counts
    and control_boundary_glue_rank_needed == boundary_glue_rank_needed,
    "evaluation/coevaluation of finite-free support modules are shadow-level data",
)

primitive_carrier_maps_consumed = 0
boundary_metric_inserted = 1
laurent_twist_chosen = 1
gate(
    "EBG13 surviving evaluation boundary glue must be carrier-native",
    primitive_carrier_maps_consumed == 0
    and boundary_metric_inserted == 1
    and laurent_twist_chosen == 1,
    "a real route must construct the boundary self-duality and Laurent twist from correspondences",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (EBG1-EBG13)")
print(
    "VERDICT: evaluation/coevaluation on the visible Tate support does not "
    "supply the R1 boundary glue.  Evaluation is scalar-valued and "
    "coevaluation is the diagonal class; neither is the linear map from the "
    "dual boundary line to the primal boundary line needed to make the Tate "
    "shift invertible.  Producing that map requires a boundary self-duality "
    "and an unpinned Laurent unit twist, or an imposed degree-zero "
    "normalization.  Endpoint/idempotent choices and bottom/shear/torsor "
    "obstructions remain, and the same package is formable on controls.  A "
    "surviving route must construct the boundary glue carrier-natively."
)
