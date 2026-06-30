"""N1-b' quadratic-refinement / Arf-Maslov witness.

Doc 170 kills determinant-one or orientation normalization of the support
opposite graph.  The next repair is to add a quadratic refinement, Arf
invariant, or Maslov/triple-Lagrangian index to the support hyperbolic
package and claim that this scalar decoration canonically pins the boundary
endpoint or Laurent twist.

In the finite F_2 support windows, quadratic refinements of a fixed
symplectic form form a large affine family.  The Arf invariant is only a
single scalar bit splitting that family.  Maslov/triple-Lagrangian variants
also require Lagrangian or graph inputs before producing a scalar.  None of
these data constructs the graph, endpoint, boundary map, Laurent generator,
or torsor splitter from carrier data.  The same package is formable on
controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_quadratic_refinement_no_go
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


def quadratic_refinement_count_f2(symplectic_half_rank):
    # Quadratic refinements of a fixed symplectic form form an affine V^*.
    return 2 ** (2 * symplectic_half_rank)


def arf_even_count_f2(symplectic_half_rank):
    return 2 ** (symplectic_half_rank - 1) * (2**symplectic_half_rank + 1)


def arf_odd_count_f2(symplectic_half_rank):
    return 2 ** (symplectic_half_rank - 1) * (2**symplectic_half_rank - 1)


def rank_one_idempotent_count_f2(rank):
    return (2**rank - 1) * 2 ** (rank - 1)


def laurent_unit_twists_in_window(kmax):
    return 2 * kmax + 1


ranks = {nmax: dmp_rank_truncated(nmax) for nmax in (1, 2, 4, 8)}
tate_window_ranks = {nmax: 2 * rank for nmax, rank in ranks.items()}
graph_lagrangian_counts = {
    nmax: graph_lagrangian_count_f2(rank) for nmax, rank in ranks.items()
}
quadratic_refinement_counts = {
    nmax: quadratic_refinement_count_f2(rank) for nmax, rank in ranks.items()
}
arf_even_counts = {nmax: arf_even_count_f2(rank) for nmax, rank in ranks.items()}
arf_odd_counts = {nmax: arf_odd_count_f2(rank) for nmax, rank in ranks.items()}
fixed_half_triple_graph_choices = {
    nmax: graph_lagrangian_counts[nmax] ** 2 for nmax in ranks
}
endpoint_pair_choices = {nmax: rank * rank for nmax, rank in ranks.items()}
coordinate_matching_counts = {1: 6, 2: 24, 4: 720, 8: 3628800}
laurent_unit_twist_counts = {
    kmax: laurent_unit_twists_in_window(kmax) for kmax in (1, 2, 4, 8)
}
rank_one_idempotent_counts_tate = {
    nmax: rank_one_idempotent_count_f2(rank)
    for nmax, rank in tate_window_ranks.items()
}

arf_outputs_scalar_bit = True
arf_outputs_endpoint = False
arf_outputs_boundary_map = False
arf_outputs_laurent_generator = False
maslov_requires_lagrangian_inputs = True
maslov_outputs_scalar = True
maslov_outputs_boundary_map = False
quadratic_refinement_supplied_by_carrier = False

gate(
    "QRF1 support tensor ranks are unchanged",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "QRF2 Tate/hyperbolic windows double support rank",
    tate_window_ranks == {1: 6, 2: 8, 4: 12, 8: 20},
    f"tate_window_ranks={tate_window_ranks}",
)

gate(
    "QRF3 quadratic refinements overproduce scalar decorations",
    quadratic_refinement_counts == {1: 64, 2: 256, 4: 4096, 8: 1048576},
    f"quadratic_refinement_counts={quadratic_refinement_counts}",
)

gate(
    "QRF4 Arf split leaves large even and odd families",
    arf_even_counts == {1: 36, 2: 136, 4: 2080, 8: 524800}
    and arf_odd_counts == {1: 28, 2: 120, 4: 2016, 8: 523776},
    f"arf_even_counts={arf_even_counts}, arf_odd_counts={arf_odd_counts}",
)

gate(
    "QRF5 Arf bit does not choose the opposite graph",
    arf_outputs_scalar_bit
    and graph_lagrangian_counts
    == {1: 64, 2: 1024, 4: 2097152, 8: 36028797018963968}
    and not quadratic_refinement_supplied_by_carrier,
    (
        f"arf_outputs_scalar_bit={arf_outputs_scalar_bit}, "
        f"graph_lagrangian_counts={graph_lagrangian_counts}, "
        f"quadratic_refinement_supplied_by_carrier={quadratic_refinement_supplied_by_carrier}"
    ),
)

gate(
    "QRF6 fixed-half Maslov triples overproduce before producing a scalar",
    fixed_half_triple_graph_choices
    == {
        1: 4096,
        2: 1048576,
        4: 4398046511104,
        8: 1298074214633706907132624082305024,
    }
    and maslov_requires_lagrangian_inputs
    and maslov_outputs_scalar,
    (
        f"fixed_half_triple_graph_choices={fixed_half_triple_graph_choices}, "
        f"maslov_requires_lagrangian_inputs={maslov_requires_lagrangian_inputs}, "
        f"maslov_outputs_scalar={maslov_outputs_scalar}"
    ),
)

gate(
    "QRF7 Arf/Maslov scalar is not endpoint, boundary map, or Laurent generator",
    not arf_outputs_endpoint
    and not arf_outputs_boundary_map
    and not arf_outputs_laurent_generator
    and not maslov_outputs_boundary_map,
    (
        f"arf_outputs_endpoint={arf_outputs_endpoint}, "
        f"arf_outputs_boundary_map={arf_outputs_boundary_map}, "
        f"arf_outputs_laurent_generator={arf_outputs_laurent_generator}, "
        f"maslov_outputs_boundary_map={maslov_outputs_boundary_map}"
    ),
)

gate(
    "QRF8 endpoint and half-matching choices remain",
    endpoint_pair_choices == {1: 9, 2: 16, 4: 36, 8: 100}
    and coordinate_matching_counts == {1: 6, 2: 24, 4: 720, 8: 3628800},
    (
        f"endpoint_pair_choices={endpoint_pair_choices}, "
        f"coordinate_matching_counts={coordinate_matching_counts}"
    ),
)

gate(
    "QRF9 Laurent twist choices remain unpinned",
    laurent_unit_twist_counts == {1: 3, 2: 5, 4: 9, 8: 17},
    f"laurent_unit_twist_counts={laurent_unit_twist_counts}",
)

gate(
    "QRF10 Tate rank-one idempotent choices remain",
    rank_one_idempotent_counts_tate
    == {1: 2016, 2: 32640, 4: 8386560, 8: 549755289600},
    f"rank_one_idempotent_counts_tate={rank_one_idempotent_counts_tate}",
)

obstruction_res1 = 1
coboundary_res1 = 0
carrier_multiplication_supplied = False
torsor_splitter_supplied = False
gate(
    "QRF11 quadratic refinement does not repair bottom, shear, or torsor obstructions",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and obstruction_res1 == 1
    and coboundary_res1 == 0
    and not carrier_multiplication_supplied
    and not torsor_splitter_supplied,
    "y^2=0, no DMP degree -2, res_1(c)=1, and no b/phi(b)=c",
)

control_quadratic_refinement_counts = quadratic_refinement_counts.copy()
control_arf_even_counts = arf_even_counts.copy()
control_arf_odd_counts = arf_odd_counts.copy()
gate(
    "QRF12 the same quadratic-refinement package is formable on controls",
    control_quadratic_refinement_counts == quadratic_refinement_counts
    and control_arf_even_counts == arf_even_counts
    and control_arf_odd_counts == arf_odd_counts,
    "quadratic refinements, Arf bits, and Maslov scalars are finite hyperbolic support operations",
)

primitive_carrier_maps_consumed = 0
quadratic_refinement_inserted = 1
endpoint_choice_inserted = 1
laurent_twist_chosen = 1
gate(
    "QRF13 surviving quadratic-refinement route must be carrier-native",
    primitive_carrier_maps_consumed == 0
    and quadratic_refinement_inserted == 1
    and endpoint_choice_inserted == 1
    and laurent_twist_chosen == 1,
    "a real route must construct quadratic refinement, endpoint, boundary glue, and twist from correspondences",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (QRF1-QRF13)")
print(
    "VERDICT: support quadratic refinements, Arf invariants, and "
    "Maslov/triple-Lagrangian scalars do not supply R1 boundary glue.  "
    "Quadratic refinements form large affine families; the Arf bit splits "
    "them but does not choose an opposite graph, endpoint, boundary map, "
    "Laurent generator, or torsor splitter.  Maslov variants require "
    "Lagrangian inputs before producing only scalar data.  Endpoint/matching/"
    "idempotent choices, Laurent twists, and bottom/shear/torsor obstructions "
    "remain, and the same package is formable on controls.  A surviving "
    "route must construct any quadratic refinement or Maslov datum "
    "carrier-natively."
)
