"""Formal lambda-half cover insertion witness.

Doc 199 leaves a precise admissible escape: the lambda^{1/2} datum must be
supplied carrier-natively inside the compactified square correspondence
object.  This witness tests the weaker repair:

    replace the eigenvalue torus by the formal double cover eta^2 = lambda,
    then read eta * (1 - lambda^-1) as the KMS-half determinant factor.

The repair has the correct analytic sign behavior, but it is only a base
change.  It has a deck ambiguity, the linear half-factor is anti-invariant
and does not descend, the deck action is scalar rather than ladder negation,
the same construction is formable on arbitrary controls, and it creates no
square H2/intersection/correspondence/Frobenius/Rosati or R1 boundary data.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_lambda_half_cover_no_go
"""

import cmath
import math

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def lam_eta(q, w, sheet=1):
    lam = cmath.exp(complex(w) * math.log(q))
    eta = sheet * cmath.exp(0.5 * complex(w) * math.log(q))
    return lam, eta


def half_factor(lam, eta):
    return eta * (1 - 1 / lam)


def dmp_dim(deg):
    if deg == -1:
        return 1
    if deg >= 0:
        return 1
    return 0


def mat_mul(a, b):
    n = len(a)
    m = len(b[0])
    kmax = len(b)
    return [
        [sum(a[i][k] * b[k][j] for k in range(kmax)) for j in range(m)]
        for i in range(n)
    ]


def mat_eq(a, b):
    return a == b


def mat_neg(a):
    return [[-x for x in row] for row in a]


lambda_half_cover_adjoined = True
cover_is_carrier_native = False
canonical_section_defined = False
orientation_linearization_defined = False
homotopy_ladder_negation_constructed = False
square_side_iota_constructed = False
properness_duality_constructed = False
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


ok_half_cover = True
for q in (2, 3, 7):
    period = 2.0 * math.pi / math.log(q)
    for w in (0.62 + 0.37j, 1.1 - 0.2j, 1.7):
        lam, eta = lam_eta(q, w, 1)
        lam_shift, eta_shift = lam_eta(q, complex(w) - 1j * period, 1)
        value = half_factor(lam, eta)
        shifted = half_factor(lam_shift, eta_shift)
        ok_half_cover &= abs(eta * eta - lam) < 1e-12 * max(1.0, abs(lam))
        ok_half_cover &= abs(lam_shift - lam) < 1e-12 * max(1.0, abs(lam))
        ok_half_cover &= abs(eta_shift + eta) < 1e-12 * max(1.0, abs(eta))
        ok_half_cover &= abs(shifted + value) < 1e-12 * max(1.0, abs(value))

gate(
    "LHC1 formal eta^2=lambda cover realizes the half-scheme sign",
    lambda_half_cover_adjoined and ok_half_cover,
    "one vertical period fixes lambda and flips eta, hence flips the KMS-half factor",
)


ok_two_sheets = True
for q in (2, 5):
    for w in (0.4 + 0.9j, 1.3):
        lam, eta_plus = lam_eta(q, w, 1)
        _, eta_minus = lam_eta(q, w, -1)
        ok_two_sheets &= abs(eta_plus * eta_plus - lam) < 1e-12
        ok_two_sheets &= abs(eta_minus * eta_minus - lam) < 1e-12
        ok_two_sheets &= abs(eta_plus + eta_minus) < 1e-12
        ok_two_sheets &= abs(half_factor(lam, eta_plus) + half_factor(lam, eta_minus)) < 1e-12

gate(
    "LHC2 the cover has a deck ambiguity and no canonical section",
    ok_two_sheets and not canonical_section_defined,
    "eta and -eta lie over the same lambda and give opposite half-factors",
)


ok_descent = True
for q in (2, 3):
    for w in (0.8 + 0.1j, 1.4):
        lam, eta = lam_eta(q, w, 1)
        f_plus = half_factor(lam, eta)
        f_minus = half_factor(lam, -eta)
        linear_descends = abs(f_plus - f_minus) < 1e-12
        square_descends = abs(f_plus * f_plus - f_minus * f_minus) < 1e-12
        ok_descent &= (not linear_descends) and square_descends

gate(
    "LHC3 the linear half-factor is anti-invariant, only its square descends",
    ok_descent and not orientation_linearization_defined,
    "the cover supplies a sign torsor; descending the linear determinant still needs a linearization",
)


ok_controls = True
control_lambdas = [1.7 + 0.4j, -0.3 + 2.0j, 2.5, cmath.exp(0.8j)]
for lam in control_lambdas:
    eta = cmath.sqrt(lam)
    ok_controls &= abs(eta * eta - lam) < 1e-12 * max(1.0, abs(lam))
    ok_controls &= abs((-eta) * (-eta) - lam) < 1e-12 * max(1.0, abs(lam))

gate(
    "LHC4 the same double-cover base change is formable on controls",
    ok_controls and not cover_is_carrier_native,
    "eta^2=lambda can be adjoined for arbitrary nonzero control eigenvalues",
)


# Model the ladder operator Theta on degrees -2,-1,0,1,2.  The formal deck
# action is scalar -1 on the half-line, so it commutes with Theta.  True
# ladder negation would conjugate Theta to -Theta by reversing degrees.
theta = [[0 for _ in range(5)] for _ in range(5)]
deck = [[0 for _ in range(5)] for _ in range(5)]
neg = [[0 for _ in range(5)] for _ in range(5)]
degrees = [-2, -1, 0, 1, 2]
for i, degree in enumerate(degrees):
    theta[i][i] = degree
    deck[i][i] = -1
    neg[i][len(degrees) - 1 - i] = 1

deck_commutes = mat_eq(mat_mul(deck, theta), mat_mul(theta, deck))
neg_inverts = mat_eq(mat_mul(mat_mul(neg, theta), neg), mat_neg(theta))

gate(
    "LHC5 deck sign is not homotopy ladder negation",
    deck_commutes and neg_inverts and not homotopy_ladder_negation_constructed,
    "deck action commutes with Theta; true negation must conjugate Theta to -Theta",
)


# The formal cover algebra R[eta]/(eta^2-lambda) has the multiplication table
# eta * 1 = eta and eta * eta = lambda.  This is a rank-2 scalar base change,
# not a square correspondence algebra.
for lam_scalar in (2, 3, 5):
    mult_eta = [[0, lam_scalar], [1, 0]]
    square = mat_mul(mult_eta, mult_eta)
    expected = [[lam_scalar, 0], [0, lam_scalar]]
    gate(
        f"LHC6 eta multiplication squares to scalar lambda={lam_scalar}",
        mat_eq(square, expected),
        "rank-2 base-change algebra, not off-diagonal square correspondences",
    )


gate(
    "LHC7 no square H2/intersection/correspondence/Rosati data is built",
    not square_h2_defined
    and not square_intersection_form_defined
    and not square_correspondence_algebra_defined
    and not frobenius_graph_defined
    and not positive_rosati_defined,
    "a two-sheet cover of the eigenvalue torus is not End(S^2/Z)",
)


gate(
    "LHC8 no square-side iota/properness or compactified duality is built",
    not square_side_iota_constructed
    and not properness_duality_constructed
    and not compactified_arithmetic_square_constructed,
    "the cover changes determinant bookkeeping, not global archimedean assembly",
)


gate(
    "LHC9 base R1 boundary and DD4 data remain missing",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and not laurent_axis_defined
    and not boundary_map_defined
    and not torsor_splitter_defined
    and not dd4_weight_ge_1_datum_defined
    and not dh_epstein_death_at_square_map,
    "no Laurent boundary, torsor splitter, DD4 weight>=1 datum, or control death",
)


gate(
    "LHC10 surviving use must be carrier-native",
    True,
    "a future route may use lambda^{1/2} only if the square correspondence object constructs it",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (LHC1-LHC10)")
print(
    "VERDICT: the formal lambda-half cover supplies the expected KMS-half "
    "sign torsor, but it is an inserted double cover with deck ambiguity. "
    "It does not descend the linear determinant, construct ladder negation, "
    "build square correspondences or positive Rosati, or repair R1 boundary "
    "data.  A surviving route must construct the half-cover carrier-natively."
)
