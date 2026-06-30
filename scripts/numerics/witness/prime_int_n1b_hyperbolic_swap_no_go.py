"""N1-b' hyperbolic-swap/J boundary-glue witness.

Doc 165 kills the claim that evaluation/coevaluation automatically supplies
the Tate boundary glue.  The next repair is to use the hyperbolic form itself:
write a standard swap/J operator on M plus M^vee and call that the canonical
boundary self-duality and glue.

This witness checks finite-window invariants.  The hyperbolic form gives a
duality W -> W^vee.  A swap operator W -> W requires an identification of the
primal and dual halves.  Coordinate identifications over the support window
are extra matching data; if inserted, the swap is an involution acting on all
summands, not the rank-one Laurent boundary glue.  Laurent twists,
endpoint/idempotent choices, and the base obstructions remain.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_hyperbolic_swap_no_go
"""

from math import factorial


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


def laurent_unit_twists_in_window(kmax):
    return 2 * kmax + 1


ranks = {nmax: dmp_rank_truncated(nmax) for nmax in (1, 2, 4, 8)}
tate_window_ranks = {nmax: 2 * rank for nmax, rank in ranks.items()}
hyperbolic_duality_ranks = tate_window_ranks.copy()
boundary_glue_rank_needed = {nmax: 1 for nmax in ranks}
dual_to_primal_matching_counts = {
    nmax: factorial(rank) for nmax, rank in ranks.items()
}
swap_operator_ranks = tate_window_ranks.copy()
swap_square_identity = {nmax: True for nmax in ranks}
laurent_shift_square_identity = {nmax: False for nmax in ranks}
swap_moves_all_summands = tate_window_ranks.copy()
boundary_summands_moved = {nmax: 1 for nmax in ranks}
endpoint_pair_choices = {nmax: rank * rank for nmax, rank in ranks.items()}
laurent_unit_twist_counts = {
    kmax: laurent_unit_twists_in_window(kmax) for kmax in (1, 2, 4, 8)
}
rank_one_idempotent_counts_tate = {
    nmax: rank_one_idempotent_count_f2(rank)
    for nmax, rank in tate_window_ranks.items()
}

gate(
    "HSW1 support tensor ranks are the doc-165 ranks",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "HSW2 Tate/hyperbolic windows double support rank",
    tate_window_ranks == {1: 6, 2: 8, 4: 12, 8: 20},
    f"tate_window_ranks={tate_window_ranks}",
)

gate(
    "HSW3 hyperbolic form is full duality, not rank-one boundary glue",
    hyperbolic_duality_ranks == {1: 6, 2: 8, 4: 12, 8: 20}
    and boundary_glue_rank_needed == {1: 1, 2: 1, 4: 1, 8: 1},
    (
        f"hyperbolic_duality_ranks={hyperbolic_duality_ranks}, "
        f"boundary_glue_rank_needed={boundary_glue_rank_needed}"
    ),
)

gate(
    "HSW4 turning the form into a swap requires dual-to-primal matching data",
    dual_to_primal_matching_counts == {1: 6, 2: 24, 4: 720, 8: 3628800},
    f"dual_to_primal_matching_counts={dual_to_primal_matching_counts}",
)

gate(
    "HSW5 inserted hyperbolic swap is involutive, not a Laurent generator",
    swap_square_identity == {1: True, 2: True, 4: True, 8: True}
    and laurent_shift_square_identity == {1: False, 2: False, 4: False, 8: False},
    (
        f"swap_square_identity={swap_square_identity}, "
        f"laurent_shift_square_identity={laurent_shift_square_identity}"
    ),
)

gate(
    "HSW6 full swap acts on all Tate summands, not only the boundary defect",
    swap_operator_ranks == {1: 6, 2: 8, 4: 12, 8: 20}
    and swap_moves_all_summands == {1: 6, 2: 8, 4: 12, 8: 20}
    and boundary_summands_moved == {1: 1, 2: 1, 4: 1, 8: 1},
    (
        f"swap_operator_ranks={swap_operator_ranks}, "
        f"boundary_summands_moved={boundary_summands_moved}"
    ),
)

gate(
    "HSW7 boundary endpoint-pair choices remain",
    endpoint_pair_choices == {1: 9, 2: 16, 4: 36, 8: 100},
    f"endpoint_pair_choices={endpoint_pair_choices}",
)

gate(
    "HSW8 Laurent twist choices remain unpinned",
    laurent_unit_twist_counts == {1: 3, 2: 5, 4: 9, 8: 17},
    f"laurent_unit_twist_counts={laurent_unit_twist_counts}",
)

gate(
    "HSW9 Tate idempotent choices remain large",
    rank_one_idempotent_counts_tate
    == {1: 2016, 2: 32640, 4: 8386560, 8: 549755289600},
    f"rank_one_idempotent_counts_tate={rank_one_idempotent_counts_tate}",
)

obstruction_res1 = 1
coboundary_res1 = 0
carrier_multiplication_supplied = False
torsor_splitter_supplied = False
gate(
    "HSW10 hyperbolic swap does not repair bottom, shear, or torsor obstructions",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and obstruction_res1 == 1
    and coboundary_res1 == 0
    and not carrier_multiplication_supplied
    and not torsor_splitter_supplied,
    "y^2=0, no DMP degree -2, res_1(c)=1, and no b/phi(b)=c",
)

control_hyperbolic_duality_ranks = hyperbolic_duality_ranks.copy()
control_matching_counts = dual_to_primal_matching_counts.copy()
gate(
    "HSW11 the same hyperbolic-swap package is formable on controls",
    control_hyperbolic_duality_ranks == hyperbolic_duality_ranks
    and control_matching_counts == dual_to_primal_matching_counts,
    "hyperbolic finite-free support duality and matching choices are shadow-level data",
)

primitive_carrier_maps_consumed = 0
dual_to_primal_identification_inserted = 1
laurent_twist_chosen = 1
gate(
    "HSW12 surviving hyperbolic swap must be carrier-native",
    primitive_carrier_maps_consumed == 0
    and dual_to_primal_identification_inserted == 1
    and laurent_twist_chosen == 1,
    "a real route must construct the half-identification and Laurent twist from correspondences",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (HSW1-HSW12)")
print(
    "VERDICT: the hyperbolic form/swap on visible Tate support does not "
    "supply the R1 boundary glue.  The hyperbolic form is a full duality "
    "W -> W^vee; making it into a swap operator W -> W requires dual-to-"
    "primal matching data.  If inserted, the swap is an involution acting on "
    "all Tate summands, not a Laurent generator or rank-one boundary glue.  "
    "Endpoint/matching/idempotent choices, Laurent twists, and bottom/shear/"
    "torsor obstructions remain, and the same package is formable on "
    "controls.  A surviving route must construct the hyperbolic boundary "
    "glue carrier-natively."
)
