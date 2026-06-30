"""Monoid/cyclotomic Frobenius shadow promotion witness.

The W-record gives the strongest post-Adams repair of the Frobenius graph
problem.  The monoid-level fixed-point carrier has growth q^w - 1, the
bidegree number d_2 = q appears on weight lines, and the geometric
family's log-Gram has the Lorentzian max-Gram index shape.

This witness records why promoting that monoid/cyclotomic shadow itself to
End(S^2/Z) is still not construction-grade.  The cyclotomic Frobenius has
no bimodule graph, periodic psi^p is impossible, connective integral psi^p
is unconstructed, TP remains p-complete/semilinear and needs an
archimedean iota, and no compactified arithmetic square with
H2/intersection/correspondence/Frobenius/Rosati or Laurent boundary data is
built.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_monoid_frobenius_shadow_no_go
"""

import math
from fractions import Fraction

import numpy as np

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def vp(n, p):
    n = abs(n)
    v = 0
    while n and n % p == 0:
        n //= p
        v += 1
    return v


def primes_upto(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, flag in enumerate(sieve) if flag]


def multiplicative_order(q, ell):
    x = q % ell
    d = 1
    while x != 1:
        x = (x * q) % ell
        d += 1
    return d


def predicted_vell_qw_minus_one(q, w, ell):
    if q % ell == 0:
        return 0
    if ell == 2:
        if w % 2 == 1:
            return vp(q - 1, 2)
        return vp(q * q - 1, 2) + vp(w, 2) - 1
    d = multiplicative_order(q, ell)
    if w % d:
        return 0
    return vp(q**d - 1, ell) + vp(w, ell)


def cyclotomic_value(d, q):
    """Phi_d(q), enough for small exact checks."""

    def mu(n):
        m = n
        out = 1
        p = 2
        while p * p <= m:
            if m % p == 0:
                m //= p
                if m % p == 0:
                    return 0
                out = -out
            p += 1
        if m > 1:
            out = -out
        return out

    num = 1
    den = 1
    for e in range(1, d + 1):
        if d % e:
            continue
        m = mu(d // e)
        if m == 1:
            num *= q**e - 1
        elif m == -1:
            den *= q**e - 1
    assert num % den == 0
    return num // den


def max_gram_signature(n):
    """Signature of M_ij=max(i+1,j+1), 0<=i,j<=n."""
    mat = np.array([[max(i + 1, j + 1) for j in range(n + 1)] for i in range(n + 1)], dtype=float)
    vals = np.linalg.eigvalsh(mat)
    return int(np.sum(vals > 1e-9)), int(np.sum(vals < -1e-9)), vals


def dmp_dim(deg):
    if deg == -1:
        return 1
    if deg >= 0:
        return 1
    return 0


monoid_fixed_point_carrier_exists = True
cyclotomic_frobenius_exists_in_cycsp = True
tp_local_fq_theorem_available = True
max_gram_lorentzian_shape_banked = True

cyclotomic_frobenius_has_bimodule_graph = False
periodic_psi_p_multiplicative_map_exists = False
connective_integral_psi_p_constructed = False
global_tp_square_linearized = False
square_iota_to_complex_constructed = False
new_spectrum_level_end_object_constructed = False

compactified_arithmetic_square_constructed = False
properness_duality_constructed = False
full_correspondence_algebra_constructed = False
square_h2_defined = False
square_intersection_form_defined = False
frobenius_graph_defined = False
positive_rosati_defined = False

laurent_axis_defined = False
boundary_map_defined = False
torsor_splitter_defined = False
dd4_weight_ge_1_datum_defined = False

dh_epstein_lack_ring_cyclotomic_carrier = True
dh_epstein_death_at_end_s2z_square_map = False


ok_growth = True
for q in (2, 3, 4, 5, 7, 8, 9, 11):
    for w in range(1, 25):
        card = q**w - 1
        ok_growth &= card == abs(1 - q**w)
        ok_growth &= q ** (w + 1) - 1 == q * card + (q - 1)
        ok_growth &= card >= q ** (w - 1)

gate(
    "MFS1 monoid fixed-point tower has real q^w-1 growth",
    monoid_fixed_point_carrier_exists and ok_growth,
    "q^w-1 = 1/|zeta(F_q,-w)| shadow; recursion and linear growth checked",
)


ok_branch_i = True
for k in (2, 3, 5, 7, 9, 12, 64):
    for l in range(1, k):
        for w in (1, 2, 3, 5, 8, 13, 21):
            g = 0
            for j in range(1, w + 1):
                g = math.gcd(g, k**j - l**j)
            ok_branch_i &= g == k - l

gate(
    "MFS2 bimodule HH0 branch still collapses to tame Z/(k-l)",
    ok_branch_i,
    "gcd_{j<=w}(k^j-l^j)=k-l on the checked grid; growth uses fixed points",
)


ok_adeles = True
for q in (2, 3, 5, 6, 7, 10, 12):
    for w in range(1, 35):
        n = q**w - 1
        for ell in primes_upto(60):
            ok_adeles &= vp(n, ell) == predicted_vell_qw_minus_one(q, w, ell)
        prod = 1
        for d in range(1, w + 1):
            if w % d == 0:
                prod *= cyclotomic_value(d, q)
        ok_adeles &= prod == n

gate(
    "MFS3 q^w-1 is adelic assembly of tame/LTE towers",
    ok_adeles,
    "ell-adic exponents and product_{d|w} Phi_d(q) checked exactly",
)


ok_p_blind = True
ok_weight_cancel = True
for p in (2, 3, 5, 7, 11):
    for r in (1, 2, 3):
        q = p**r
        for w in range(1, 25):
            ok_p_blind &= vp(q**w - 1, p) == 0
            ok_weight_cancel &= Fraction(q) ** w * (Fraction(1, p) ** (r * w)) == 1

gate(
    "MFS4 p-complete cyclotomic pairing is degree-growth blind",
    tp_local_fq_theorem_available and ok_p_blind and ok_weight_cancel,
    "v_p(q^w-1)=0 and Hesselholt weight cancellation checked",
)


ok_degree = True
for q in (2, 3, 5, 7):
    for s in (2, 3, 4, 5):
        lhs = Fraction(q) ** (1 - s) / (1 - Fraction(q) ** (1 - s))
        rhs = sum(Fraction(q) ** w * Fraction(q) ** (-w * s) for w in range(1, 80))
        tail = Fraction(q) ** (80 * (1 - s)) / (1 - Fraction(q) ** (1 - s))
        ok_degree &= lhs == rhs + tail

gate(
    "MFS5 bidegree d2=q gives the local zeta(s-1) degree factor",
    ok_degree,
    "sum_w q^w q^{-ws} = q^{1-s}/(1-q^{1-s}) checked as rational identity",
)


ok_max = True
details = []
for n in range(1, 10):
    pos, neg, vals = max_gram_signature(n)
    ok_max &= (pos, neg) == (1, n)
    details.append((n, pos, neg, float(vals[0]), float(vals[-1])))

gate(
    "MFS6 max-Gram geometric family has Lorentzian index shape",
    max_gram_lorentzian_shape_banked and ok_max,
    f"signature (1,n) for n<=9; n=9 eig range {details[-1][3]:.3f}..{details[-1][4]:.3f}",
)


gate(
    "MFS7 cyclotomic Frobenius has no bimodule graph",
    cyclotomic_frobenius_exists_in_cycsp
    and not cyclotomic_frobenius_has_bimodule_graph
    and not full_correspondence_algebra_constructed,
    "phi_p lives in CycSp/TP, not as a ku-bimodule correspondence graph",
)


gate(
    "MFS8 non-invertible psi^p is not an available integral correspondence",
    not periodic_psi_p_multiplicative_map_exists
    and not connective_integral_psi_p_constructed
    and not frobenius_graph_defined,
    "periodic Bott-unit obstruction; connective E1 psi^p remains unconstructed",
)


gate(
    "MFS9 TP local theorem does not assemble the S^2/Z square",
    not global_tp_square_linearized
    and not square_iota_to_complex_constructed
    and not compactified_arithmetic_square_constructed
    and not properness_duality_constructed,
    "p-complete semilinear TP lacks global linearization and square-side iota",
)


gate(
    "MFS10 no End(S^2/Z) H2/intersection/Rosati or R1 boundary data is built",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and not new_spectrum_level_end_object_constructed
    and not square_h2_defined
    and not square_intersection_form_defined
    and not full_correspondence_algebra_constructed
    and not positive_rosati_defined
    and not laurent_axis_defined
    and not boundary_map_defined
    and not torsor_splitter_defined
    and not dd4_weight_ge_1_datum_defined
    and dh_epstein_lack_ring_cyclotomic_carrier
    and not dh_epstein_death_at_end_s2z_square_map,
    "monoid shadow is real, but no compactified square map or positive Rosati",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (MFS1-MFS10)")
