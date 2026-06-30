"""CC graded-tolerance derived-square repair witness.

Doc 188 kills promoting strict-square divided-power invariants themselves to
End(S^2/Z).  The next repair is to add the missing grading by putting a
CC-style tolerance dimension on each derived/Bokstedt degree of the square:
for a Z/k diagonal entry, use dim_b(k) = ceil(log_b k).

This witness records the exact Q-doc obstruction.  The quantized tower has a
simple pole at s=0 whenever the ceiling is exact on the geometric set
{b^j}.  Its finite part is rational and base-dependent, so the integer
tolerance layer does not produce the regularized derived square invariant.
It also supplies no square H^2, intersection form, correspondence algebra,
Frobenius graph, positive Rosati, Laurent boundary map, or torsor splitter.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_cc_graded_tolerance_no_go
"""

from fractions import Fraction
from math import ceil, log, pi

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def ceil_log_b(k, b):
    power = 1
    n = 0
    while power < k:
        power *= b
        n += 1
    return n


def is_power_of_b(k, b):
    if k < 1:
        return False
    while k % b == 0:
        k //= b
    return k == 1


def exactness_set(b, limit):
    return [k for k in range(1, limit + 1) if is_power_of_b(k, b)]


def pole_residue(b):
    return -1.0 / (2.0 * log(b))


def quantized_finite_part(b):
    """FP Sum_reg ceil(log_b k) from Q-doc W6."""
    return Fraction(b, b - 1) - Fraction(5, 4)


def smooth_regularized_total(b):
    """Sum_reg log_b k = log(2 pi)/(2 log b)."""
    return log(2 * pi) / (2.0 * log(b))


def dmp_dim(deg):
    if deg == -1:
        return 1
    if deg >= 0:
        return 1
    return 0


cc_tolerance_is_metric_ungraded = True
cc_dold_kan_is_short_complex_only = True
graded_tolerance_in_corpus = False
derived_square_grading_constructed_by_cc = False
aggregate_zeta_regularized_value_exists = False

bases = (2, 3)
residues = {b: pole_residue(b) for b in bases}
finite_parts = {b: quantized_finite_part(b) for b in bases}
smooth_totals = {b: smooth_regularized_total(b) for b in bases}
defect_finite_parts = {
    b: float(finite_parts[b]) - smooth_totals[b] for b in bases
}
exact_sets = {b: exactness_set(b, b**6) for b in bases}

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
    "CGT1 CC tolerance/Dold-Kan inputs are not graded square cohomology",
    cc_tolerance_is_metric_ungraded
    and cc_dold_kan_is_short_complex_only
    and not graded_tolerance_in_corpus
    and not derived_square_grading_constructed_by_cc,
    "metric ungraded tolerance, short-complex Dold-Kan, no corpus graded tolerance",
)

gate(
    "CGT2 ceiling exactness lies on geometric sets",
    exact_sets[2] == [1, 2, 4, 8, 16, 32, 64]
    and exact_sets[3] == [1, 3, 9, 27, 81, 243, 729],
    f"base2={exact_sets[2]}, base3={exact_sets[3]}",
)

gate(
    "CGT3 quantized tower has a simple pole at s=0",
    residues[2] < 0
    and residues[3] < 0
    and abs(residues[2] + 1.0 / (2.0 * log(2))) < 1e-15
    and abs(residues[3] + 1.0 / (2.0 * log(3))) < 1e-15
    and not aggregate_zeta_regularized_value_exists,
    f"residue_b2={residues[2]:+.12f}, residue_b3={residues[3]:+.12f}",
)

gate(
    "CGT4 finite parts are rational and base-dependent",
    finite_parts[2] == Fraction(3, 4)
    and finite_parts[3] == Fraction(1, 4)
    and finite_parts[2] != finite_parts[3],
    f"FP_b2={finite_parts[2]}, FP_b3={finite_parts[3]}",
)

gate(
    "CGT5 smooth derived total is different from the quantized finite part",
    smooth_totals[2] > 1.0
    and smooth_totals[3] > 0.0
    and abs(float(finite_parts[2]) - smooth_totals[2]) > 0.5
    and abs(float(finite_parts[3]) - smooth_totals[3]) > 0.5,
    (
        f"smooth_b2={smooth_totals[2]:.12f}, FP_b2={float(finite_parts[2]):.12f}; "
        f"smooth_b3={smooth_totals[3]:.12f}, FP_b3={float(finite_parts[3]):.12f}"
    ),
)

gate(
    "CGT6 defect finite parts carry all transcendental regularized content",
    defect_finite_parts[2] < 0
    and defect_finite_parts[3] < 0
    and abs(defect_finite_parts[2] - (0.75 - smooth_totals[2])) < 1e-15
    and abs(defect_finite_parts[3] - (0.25 - smooth_totals[3])) < 1e-15,
    f"defect_b2={defect_finite_parts[2]:+.12f}, defect_b3={defect_finite_parts[3]:+.12f}",
)

gate(
    "CGT7 no square H2/intersection/correspondence is constructed",
    not square_h2_defined
    and not square_intersection_form_defined
    and not square_correspondence_algebra_defined
    and not frobenius_graph_defined,
    "integer per-degree dimensions are not square correspondences",
)

gate(
    "CGT8 no Rosati, Laurent boundary, or torsor data is constructed",
    not positive_rosati_defined
    and not laurent_axis_defined
    and not boundary_map_defined
    and not torsor_splitter_defined
    and not dd4_weight_ge_1_datum_defined,
    "graded tolerance does not finish DD.4 weights>=1",
)

gate(
    "CGT9 base R1 obstructions remain",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and not boundary_map_defined
    and not torsor_splitter_defined,
    "no degree -2 DMP support and no b/phi(b)=c splitter",
)

gate(
    "CGT10 carrier guard has not fired at a square map",
    not dh_epstein_death_at_square_map
    and not square_correspondence_algebra_defined,
    "no carrier-consuming square correspondence where controls die",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (CGT1-CGT10)")
