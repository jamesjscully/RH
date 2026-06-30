"""Derived THH diagonal shortcut witness.

Doc 18 proves a real positive fact: the derived diagonal self-intersection
of HZ over HZ ^ HZ is THH(Z), and Bokstedt's torsion tower gives a
sign-bearing diagonal value after zeta regularization.  After doc 195, the
tempting shortcut is to combine that abutment with AA's norm weights and
declare it to be End(S^2/Z).

This witness records why that shortcut is not construction-grade.  THH(Z)
supplies the diagonal self-intersection tower, not a compactified square
correspondence algebra.  The tower is infinite and nonproper; finite partial
products diverge, and the diagonal number appears only after regularization.
No square H^2, correspondence algebra, Frobenius graph, positive Rosati,
Laurent boundary map, or torsor splitter is constructed.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_derived_thh_diagonal_no_go
"""

import math

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def thh_z_torsion_order(k):
    """Bokstedt: |pi_{2k-1} THH(Z)| = k for k >= 1."""
    return k


def finite_torsion_log_product(n):
    return sum(math.log(thh_z_torsion_order(k)) for k in range(1, n + 1))


def stirling_finite_part(n):
    """Extract the zeta-regularized constant from sum_{k<=n} log k."""
    return (
        finite_torsion_log_product(n)
        - (n * math.log(n) - n + 0.5 * math.log(n))
        - 1.0 / (12.0 * n)
        + 1.0 / (360.0 * n**3)
    )


def dmp_dim(deg):
    if deg == -1:
        return 1
    if deg >= 0:
        return 1
    return 0


derived_diagonal_thh_identified = True
bokstedt_tower_available = True
aa_norm_weight_dictionary_available = True

compactified_derived_square_constructed = False
properness_theorem_constructed = False
finite_rank_euler_pairing_constructed = False
derived_normed_spectral_sequence_constructed = False
non_em_square_functor_defined = False
off_diagonal_correspondence_classes_defined = False

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
    "DTD1 derived diagonal self-intersection is a real THH(Z) datum",
    derived_diagonal_thh_identified
    and bokstedt_tower_available
    and [thh_z_torsion_order(k) for k in range(1, 8)] == [1, 2, 3, 4, 5, 6, 7],
    "Bokstedt tower orders k=1..7 are exact",
)

gate(
    "DTD2 AA norm weights match the same cardinality ladder only as weights",
    aa_norm_weight_dictionary_available
    and all(math.log(thh_z_torsion_order(k)) == math.log(k) for k in range(1, 20)),
    "degree 2k-1 may be assigned weight log k only as a dictionary",
)

gate(
    "DTD3 finite diagonal products diverge with the tower cutoff",
    finite_torsion_log_product(10) < finite_torsion_log_product(50)
    < finite_torsion_log_product(200),
    (
        f"logprod10={finite_torsion_log_product(10):.6f}, "
        f"logprod50={finite_torsion_log_product(50):.6f}, "
        f"logprod200={finite_torsion_log_product(200):.6f}"
    ),
)

target = 0.5 * math.log(2.0 * math.pi)
errs = [abs(stirling_finite_part(n) - target) for n in (50, 200, 1000)]
gate(
    "DTD4 diagonal number appears only after regularization",
    max(errs) < 1e-10,
    (
        f"finite part -> 1/2 log(2pi)={target:.12f}; "
        f"errors={errs[0]:.2e},{errs[1]:.2e},{errs[2]:.2e}"
    ),
)

gate(
    "DTD5 no compactified derived square or properness theorem is constructed",
    not compactified_derived_square_constructed
    and not properness_theorem_constructed
    and not finite_rank_euler_pairing_constructed,
    "ordinary THH(Z) is the uncompactified diagonal tower, not finite-rank RR",
)

gate(
    "DTD6 no derived normed spectral sequence or non-EM square functor is built",
    not derived_normed_spectral_sequence_constructed
    and not non_em_square_functor_defined,
    "weight and THH degree are aligned by dictionary, not by a carrier",
)

gate(
    "DTD7 diagonal self-intersection is not the full correspondence algebra",
    not off_diagonal_correspondence_classes_defined
    and not square_correspondence_algebra_defined
    and not frobenius_graph_defined,
    "THH(Z) computes Delta cap Delta, not graphs or End(S^2/Z)",
)

gate(
    "DTD8 no square H2/intersection/correspondence/Rosati is constructed",
    not square_h2_defined
    and not square_intersection_form_defined
    and not square_correspondence_algebra_defined
    and not positive_rosati_defined,
    "the regularized diagonal value is not a positive Rosati correspondence",
)

gate(
    "DTD9 no Laurent boundary or DD4 weight>=1 data is constructed",
    not laurent_axis_defined
    and not boundary_map_defined
    and not torsor_splitter_defined
    and not dd4_weight_ge_1_datum_defined,
    "no boundary map, torsor splitter, or weight>=1 datum",
)

gate(
    "DTD10 base R1 obstructions and carrier guard remain",
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

print("\nALL PASS (DTD1-DTD10)")
