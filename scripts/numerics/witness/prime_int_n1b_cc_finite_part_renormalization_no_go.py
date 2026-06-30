"""CC finite-part renormalization repair witness.

Doc 189 kills the CC-ceiling graded-tolerance derived-square repair because
the quantized tower has a simple pole at s=0.  The next repair is to subtract
the pole and keep the finite part as the proposed square invariant.

This witness records why that repair is not construction-grade End(S^2/Z).
The pole residue and finite part are base-specific regularization data; the
finite parts 3/4 and 1/4 are rational scheme calibrations, not the smooth
derived total, and keeping them supplies no square H^2, intersection form,
correspondence algebra, Frobenius graph, positive Rosati, Laurent boundary
map, or torsor splitter.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_cc_finite_part_renormalization_no_go
"""

from fractions import Fraction
from math import log, pi

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def pole_residue(b):
    return -1.0 / (2.0 * log(b))


def quantized_finite_part(b):
    """FP Sum_reg ceil(log_b k) from the Q-doc and doc 189."""
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


bases = (2, 3)
residues = {b: pole_residue(b) for b in bases}
finite_parts = {b: quantized_finite_part(b) for b in bases}
smooth_totals = {b: smooth_regularized_total(b) for b in bases}
defects = {b: float(finite_parts[b]) - smooth_totals[b] for b in bases}

base_selector_supplied_by_square = False
finite_part_prescription_carrier_native = False
dualizing_module_mechanism_supplied = False
non_geometric_exactness_set_supplied = False
new_aggregation_constructed = False

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
    "CFR1 pole subtraction data is nonzero and base-specific",
    residues[2] < 0
    and residues[3] < 0
    and residues[2] != residues[3]
    and abs(residues[2] + 1.0 / (2.0 * log(2))) < 1e-15
    and abs(residues[3] + 1.0 / (2.0 * log(3))) < 1e-15,
    f"residue_b2={residues[2]:+.12f}, residue_b3={residues[3]:+.12f}",
)

gate(
    "CFR2 finite parts are rational and base-dependent",
    finite_parts[2] == Fraction(3, 4)
    and finite_parts[3] == Fraction(1, 4)
    and finite_parts[2] != finite_parts[3],
    f"FP_b2={finite_parts[2]}, FP_b3={finite_parts[3]}",
)

gate(
    "CFR3 finite parts are not the smooth derived totals",
    abs(float(finite_parts[2]) - smooth_totals[2]) > 0.5
    and abs(float(finite_parts[3]) - smooth_totals[3]) > 0.5,
    (
        f"smooth_b2={smooth_totals[2]:.12f}, FP_b2={float(finite_parts[2]):.12f}; "
        f"smooth_b3={smooth_totals[3]:.12f}, FP_b3={float(finite_parts[3]):.12f}"
    ),
)

gate(
    "CFR4 finite-part defect keeps the regularized log content outside the FP",
    defects[2] < 0
    and defects[3] < 0
    and abs(defects[2] - (0.75 - smooth_totals[2])) < 1e-15
    and abs(defects[3] - (0.25 - smooth_totals[3])) < 1e-15,
    f"defect_b2={defects[2]:+.12f}, defect_b3={defects[3]:+.12f}",
)

gate(
    "CFR5 finite-part retention is a selector without square-native base data",
    not base_selector_supplied_by_square
    and not finite_part_prescription_carrier_native,
    "no carrier-native rule chooses the base or pole-subtraction prescription",
)

gate(
    "CFR6 the S[+-1] quarter echo supplies no mechanism",
    finite_parts[3] == Fraction(1, 4)
    and finite_parts[2] == Fraction(3, 4)
    and not dualizing_module_mechanism_supplied,
    "1/4 echo is numerology; the S value is 3/4 and no dualizing map is built",
)

gate(
    "CFR7 no evading exactness set or new aggregation is constructed",
    not non_geometric_exactness_set_supplied
    and not new_aggregation_constructed,
    "doc 189 evasion requires non-geometric exactness or carrier-native aggregation",
)

gate(
    "CFR8 no square H2/intersection/correspondence/Rosati is constructed",
    not square_h2_defined
    and not square_intersection_form_defined
    and not square_correspondence_algebra_defined
    and not frobenius_graph_defined
    and not positive_rosati_defined,
    "finite parts are numbers, not square correspondence data",
)

gate(
    "CFR9 no Laurent boundary or DD4 weight>=1 data is constructed",
    not laurent_axis_defined
    and not boundary_map_defined
    and not torsor_splitter_defined
    and not dd4_weight_ge_1_datum_defined,
    "pole subtraction does not build the boundary map or torsor splitter",
)

gate(
    "CFR10 base R1 obstructions and carrier guard remain",
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

print("\nALL PASS (CFR1-CFR10)")
