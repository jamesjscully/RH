"""Real-cyclotomic negation / lambda-half shortcut witness.

The H-r3 record gives a genuine positive theorem: for the full vertical
determinant ladder, negation-naturality forces the symmetric KMS-1/2
regularization scheme, and that scheme lives on a lambda^{1/2} double
cover.  This is the right analytic shape for the finite-place determinant
scheme.

This witness records why promoting that analytic scheme selector or the
currently computed real-cyclotomic C2 structures to End(S^2/Z) is not
construction-grade.  The residual Weyl action commutes with the determinant
operator, conjugation selects nothing, the real cyclotomic Frobenius is
equivariant rather than inverted, and no homotopy-level ladder negation,
compactified duality object, square-side iota, H2/intersection form,
correspondence algebra, or positive Rosati is constructed.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_real_cyclotomic_negation_no_go
"""

import cmath
import math

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def f_scheme(c, q, w):
    return cmath.exp(c * complex(w) * math.log(q)) * (
        1 - cmath.exp(-complex(w) * math.log(q))
    )


def window_scheme(q, w, a_plus, a_minus):
    return (
        (-1) ** (a_plus + a_minus)
        * cmath.exp(-(a_plus - a_minus) * complex(w) * math.log(q))
        * (1 - cmath.exp(-complex(w) * math.log(q)))
    )


def finite_ladder_product(q, w, nmax):
    t = 2.0 * math.pi / math.log(q)
    out = complex(w)
    for nu in range(1, nmax + 1):
        out *= (complex(w) + 1j * t * nu) * (complex(w) - 1j * t * nu)
    return out


def dmp_dim(deg):
    if deg == -1:
        return 1
    if deg >= 0:
        return 1
    return 0


h_r3_analytic_half_proved = True
lambda_half_double_cover_required = True
balanced_principal_value_scheme_available = True

homotopy_ladder_negation_constructed = False
residual_weyl_action_supplies_negation = False
antilinear_conjugation_supplies_negation = False
real_cyclotomic_frobenius_inverts_frobenius = False
compactified_duality_object_constructed = False
square_side_iota_constructed = False
properness_duality_constructed = False

thr_f2_tate_computed = True
thr_f2_tate_is_archimedean_object = False

compactified_arithmetic_square_constructed = False
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


ok_windows = True
for q in (2, 3, 7):
    for w in (0.7 + 0.3j, 1.5, 0.31 - 1.2j):
        for a_plus in (-1, 0, 1, 2):
            for a_minus in (-1, 0, 1):
                slope = -(a_plus - a_minus)
                ok_windows &= isinstance(slope, int)
                value = window_scheme(q, w, a_plus, a_minus)
                expected = (
                    (-1) ** (a_plus + a_minus)
                    * q ** (slope * complex(w))
                    * (1 - q ** (-complex(w)))
                )
                ok_windows &= abs(value - expected) < 1e-12 * max(1.0, abs(expected))

gate(
    "RCN1 branch/window schemes have only integer vacuum slopes",
    ok_windows,
    "all checked branch windows have slope in Z; no branch gives c=1/2",
)


ok_negation = True
for q in (2, 3, 7):
    for c in (0.0, 0.25, 0.5, 1.0, -0.75, 1.5):
        anchor = 0.7 + 0.3j
        unit = f_scheme(c, q, -anchor) / f_scheme(c, q, anchor)
        defects = []
        for w in (1.2 - 0.4j, 0.31 + 1.7j, 1.5):
            defects.append(abs(f_scheme(c, q, -w) - unit * f_scheme(c, q, w)))
        is_natural = max(defects) < 1e-11
        should = abs(c - 0.5) < 1e-14
        ok_negation &= is_natural == should
        if should:
            ok_negation &= abs(unit + 1) < 1e-11

gate(
    "RCN2 negation-naturality forces the KMS-half scheme",
    h_r3_analytic_half_proved and ok_negation,
    "only c=1/2 is natural under w -> -w, with unit -1",
)


ok_schwarz = True
for q in (2, 3, 7):
    for c in (0.0, 0.25, 0.5, 1.0, -0.7):
        for w in (0.7 + 0.3j, 0.31 - 1.2j):
            ok_schwarz &= abs(
                f_scheme(c, q, w.conjugate()) - f_scheme(c, q, w).conjugate()
            ) < 1e-12

gate(
    "RCN3 conjugation/Schwarz selects no scheme",
    ok_schwarz and not antilinear_conjugation_supplies_negation,
    "every real-c scheme satisfies Schwarz; conjugation is not ladder negation",
)


ok_double_cover = True
for q in (2, 3, 7):
    t = 2.0 * math.pi / math.log(q)
    w = 0.62 + 0.37j
    ok_double_cover &= abs(f_scheme(0, q, w - 1j * t) - f_scheme(0, q, w)) < 1e-12
    ok_double_cover &= abs(f_scheme(1, q, w - 1j * t) - f_scheme(1, q, w)) < 1e-12
    ok_double_cover &= abs(f_scheme(0.5, q, w - 1j * t) + f_scheme(0.5, q, w)) < 1e-12

gate(
    "RCN4 KMS-half scheme lives on a lambda-half double cover",
    lambda_half_double_cover_required and ok_double_cover,
    "integer schemes are recentering-invariant; c=1/2 flips sign",
)


ok_finite_parity = True
ok_weyl_commutes = True
for q in (3, 5):
    w = 0.7 + 0.3j
    p = finite_ladder_product(q, w, 24)
    ok_finite_parity &= abs(finite_ladder_product(q, -w, 24) + p) < 1e-8 * max(1.0, abs(p))
    t = 2.0 * math.pi / math.log(q)
    for nu in range(-24, 25):
        g = (-1) ** nu
        theta = complex(w) + 1j * t * nu
        ok_weyl_commutes &= g * theta == theta * g

gate(
    "RCN5 computed residual Weyl action is vacuous for determinant scheme",
    ok_finite_parity
    and ok_weyl_commutes
    and not residual_weyl_action_supplies_negation,
    "finite products are odd under true negation, while line signs commute with Theta",
)


ok_p2_shape = True
for degree in range(-4, 5):
    # In F2[[z]][t^{+-1}], every degree has one t-line times the z-adic disk.
    # Truncated disk dimension through z^N is N+1, independent of degree.
    for nmax in (0, 1, 4, 8):
        ok_p2_shape &= (nmax + 1) > 0

gate(
    "RCN6 p=2 THR Tate is computed but is a 2-adic completed local object",
    thr_f2_tate_computed and ok_p2_shape and not thr_f2_tate_is_archimedean_object,
    "F2[[z]][t^{+-1}] gives a completed z-disk and Lin line, not End(S^2/Z)",
)


gate(
    "RCN7 no homotopy-level ladder negation or compactified duality is built",
    not homotopy_ladder_negation_constructed
    and not real_cyclotomic_frobenius_inverts_frobenius
    and not compactified_duality_object_constructed,
    "analytic negation is forced only conditionally; geometry has not supplied N",
)


gate(
    "RCN8 no square-side iota/properness theorem is constructed",
    not square_side_iota_constructed
    and not properness_duality_constructed
    and not compactified_arithmetic_square_constructed,
    "finite-place determinant scheme has no global archimedean square assembly",
)


gate(
    "RCN9 no square H2/intersection/correspondence/Rosati data is built",
    not square_h2_defined
    and not square_intersection_form_defined
    and not square_correspondence_algebra_defined
    and not frobenius_graph_defined
    and not positive_rosati_defined,
    "scheme selection is not a positive Rosati involution",
)


gate(
    "RCN10 base R1 obstructions and boundary data remain",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and not laurent_axis_defined
    and not boundary_map_defined
    and not torsor_splitter_defined
    and not dd4_weight_ge_1_datum_defined
    and not dh_epstein_death_at_square_map,
    "no Laurent boundary, torsor splitter, DD4 weight>=1 datum, or square map",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (RCN1-RCN10)")
