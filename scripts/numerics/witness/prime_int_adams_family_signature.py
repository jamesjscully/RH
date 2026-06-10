"""C6''' (doc 21 sec 5): the doc-17 C4 signature protocol on the Adams
family matrices of the ku square.

Worker I (research/work/I-c6-ku-square.md, verified): the graph-pairing
pi_0-shadow of the Adams family on ku ^ ku has weight-w piece Z/|k-l|
for ALL w - so the per-weight log-cardinality matrix on the family
{Gamma_psi^1 = DIAGONAL, Gamma_psi^2, ..., Gamma_psi^n} is

    K[k,l] = log|k - l|   (k != l;  cardinalities - zero free choices),
    K[k,k] = t            (the graph self-pairing: RANK part, weight-w
                           piece Z - infinite; t is the same excess/
                           scheme slot as doc 18's diagonal constant).

This is structurally the FF Castelnuovo configuration {Delta, Gamma_F,
Gamma_F^2, ...}: the Hodge-index step needs the family Gram to be
LORENTZIAN, signature (1, n-1). The doc-17 C4 protocol asks: what
signature law does the integer family carry?

PRE-REGISTERED READINGS (fixed before the run; the n=3 hand-check
[[0,0,log2],[0,0,0],[log2,0,0]] with eigenvalues {log2, -log2, 0}
already shows kernel vectors from the log 1 = 0 band, so CND-exactness
is NOT expected):
  S1 (bare matrix, t = 0): signature of K_n for n = 3..60.
      R-a: (1, n-1) all n            -> natively Lorentzian: the
           Hodge-index SHAPE is carried by the cardinalities themselves;
           escalate (first index-shaped integer object in the program).
      R-b: (1, n-1-z) with z kernel vectors that DISAPPEAR for n >= 4
           (the log1 band stops generating kernel once rows differ)
           -> Lorentzian up to small-n artifacts; treat as R-a.
      R-c: >= 2 positive eigenvalues at any n -> NO index shape; the
           family matrix is not Castelnuovo material; record and close.
  S2 (diagonal dial): signature of K_n + t I as a function of t: the
      Lorentzian window is t in [-lambda_2, -lambda_1) where
      lambda_1 <= lambda_2 <= ... are the eigenvalues of K_n(t=0)
      (shifting cannot mix order); report the window [t_lo(n), t_hi(n))
      = [-lambda_2(n), -lambda_1(n)) and its n-scaling. Reading: if the
      window is nonempty and STABLE (t_lo bounded, t_hi growing), the
      index shape survives the open diagonal slot for a robust range -
      the homotopy theory then only needs to pin t INSIDE a fat window,
      not hit a point.
  S3 (landmarks, exploratory - NO claim): where 0, zeta'(0), and
      (1/2)log 2pi sit relative to the window. Recorded for the later
      scheme question; G-INT6: t is the single free slot, everything
      else is cardinalities.

OUTCOME (recorded 2026-06-10, first run): READING R-C. The bare matrix
has signature ~ (0.43n, 0.57n) - NOT Lorentzian - and the constant-t
Lorentzian window ESCAPES linearly (t_lo ~ 0.45 n), so no constant
graph self-pairing can produce the Castelnuovo shape asymptotically.
The gates below now assert the MEASURED law (refutation-grade witness:
exit 0 = the negative reproduces). Two notes for the record: (i) the
regularized TOTAL pairing (sum over weights, zeta(0) factor) is
-(1/2) log|k-l| - the mirrored matrix; signature flips (n-, n+), still
not Lorentzian: the verdict is normalization-independent; (ii) the FF
Castelnuovo form is NOT the bare Gram - it subtracts the fiber/bidegree
term (D^2 <= 2 d1 d2 after correction); graphs of psi^k should carry
bidegree ~ (1, k), so the corrected form K[k,l] - u(k+l) with the
k-DEPENDENT diagonal is the refined posing (doc 23) - left to C6''
where the true diagonal (twisted THH) becomes available.

Run:
    python3 -m scripts.numerics.witness.prime_int_adams_family_signature
"""
import math
import sys

import numpy as np

FAIL = []


def check(name, ok, detail):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    if not ok:
        FAIL.append(name)


def family_matrix(n):
    K = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                K[i, j] = math.log(abs(i - j))
    return K


# ---------------------------------------------------------------- S1
print("S1: signature of the bare family matrix K_n (t = 0)")
sigs = {}
bad_n = []
for n in range(3, 61):
    ev = np.linalg.eigvalsh(family_matrix(n))
    npos = int(np.sum(ev > 1e-9))
    nneg = int(np.sum(ev < -1e-9))
    z = n - npos - nneg
    sigs[n] = (npos, nneg, z)
    if npos != 1:
        bad_n.append(n)
for n in (3, 4, 5, 10, 20, 40, 60):
    print(f"    n = {n:>2}: signature (+,-,0) = {sigs[n]}")
not_lorentz = all(s[0] >= 2 for n, s in sigs.items() if n >= 4)
kernel_gone = all(s[2] == 0 for n, s in sigs.items() if n >= 4)
ratio60 = sigs[60][0] / 60.0
check("reading R-c reproduces (NOT Lorentzian)", not_lorentz and kernel_gone
      and 0.35 < ratio60 < 0.5,
      f">= 2 positive eigenvalues for all 4 <= n <= 60; kernel empty for "
      f"n >= 4; npos/n at 60 = {ratio60:.3f} (measured law ~0.43)")

# ---------------------------------------------------------------- S2
print("\nS2: the Lorentzian window of the diagonal dial t")
print("    window = [-lambda_2(n), -lambda_1(n)): K + tI Lorentzian iff "
      "exactly one eigenvalue of K exceeds -t")
rows = []
for n in (5, 10, 20, 40, 60, 100):
    ev = np.sort(np.linalg.eigvalsh(family_matrix(n)))
    t_lo, t_hi = -ev[1], -ev[0]
    rows.append((n, t_lo, t_hi))
    print(f"    n = {n:>3}: window t in [{t_lo:+.4f}, {t_hi:+.4f})   "
          f"width {t_hi - t_lo:.4f}")
window_ok = all(hi > lo for (_, lo, hi) in rows)
lo_escapes = rows[-1][1] > 10.0 and rows[-1][1] > 2.2 * rows[-3][1] / (100.0 / 40.0) * 0.8
lin = rows[-1][1] / rows[-3][1]
check("window escape reproduces (constant t excluded)", window_ok and lo_escapes,
      f"t_lo(100)/t_lo(40) = {lin:.2f} (~2.5 = linear growth): the "
      f"Lorentzian window escapes; NO constant diagonal works asymptotically")

# ---------------------------------------------------------------- S3
print("\nS3 (exploratory, no claim): landmark diagonal values vs the window")
zp0 = -0.5 * math.log(2 * math.pi)
for n, lo, hi in rows:
    marks = []
    for name, v in (("0", 0.0), ("zeta'(0)", zp0), ("+(1/2)log2pi", -zp0)):
        inside = "IN" if lo <= v < hi else "out"
        marks.append(f"{name}:{inside}")
    print(f"    n = {n:>3}: " + "  ".join(marks))
print("    (recorded for the scheme question; t is the single free slot)")

print(f"\n{'ALL PASS' if not FAIL else 'FAILURES: ' + ', '.join(FAIL)}")
sys.exit(0 if not FAIL else 1)
