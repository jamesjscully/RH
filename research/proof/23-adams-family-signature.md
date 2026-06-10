# 23 - C6''' first pass: the bare Adams family matrix is NOT Castelnuovo material (fail-closed negative)

Status: 2026-06-10. Witness: prime_int_adams_family_signature.py
(refutation-grade: exit 0 = the negative reproduces; pre-registered
readings R-a/R-b/R-c in the docstring, outcome R-c).

## 1. The test

The Adams family on the ku square - {Gamma_psi^1 = Delta, Gamma_psi^2,
..., Gamma_psi^n}, the program's only Frobenius-graph analogue - has
verified per-weight pairing cardinalities |k - l| (worker I). The
doc-17 C4 protocol asks whether the family Gram K[k,l] = log|k-l|
(off-diagonal; cardinalities, zero free choices) with the open diagonal
slot t carries the Lorentzian (1, n-1) signature that the FF
Castelnuovo/Hodge-index step requires.

## 2. The verdict (reading R-c)

- Bare matrix: signature ~ (0.43 n, 0.57 n). Not Lorentzian at any
  n >= 4 (n = 3 has a log1-band kernel artifact).
- Constant diagonal excluded ASYMPTOTICALLY: the Lorentzian window
  [-lambda_2(n), -lambda_1(n)) escapes linearly (t_lo ~ 0.45 n), so no
  fixed graph self-pairing value can produce the index shape at scale.
- Normalization-independent: the regularized total pairing is
  -(1/2) log|k-l| (the zeta(0) factor - the scheme again), which only
  mirrors the signature; still not Lorentzian.

## 3. What the negative teaches (and the refined posing)

The FF Castelnuovo form is NOT the bare graph Gram. On a surface the
index inequality D^2 <= 2 d_1 d_2 holds AFTER the fiber/bidegree
correction (projecting out the two ruling classes); graphs of Frobenius
powers have growing bidegree, and their self-intersections grow
correspondingly. The analogue here: psi^k should carry bidegree
~ (1, k) (psi^k acts by k on the Bott class), so the candidate
corrected form is

    C[k,l] = <Gamma_k, Gamma_l> - u (d_1(k) d_2(l) + d_1(l) d_2(k))/2
           ~ log|k-l| - u (k + l)/2-type,   with a k-DEPENDENT diagonal.

Both missing ingredients - the true diagonal <Gamma_k, Gamma_k> and the
fiber classes' pairings - are exactly what the pi_0 shadow cannot see:
they live in the full Adams-twisted THH(ku), i.e. C6'' (the minimal
computable instance posed in the I-doc). C6''' therefore CLOSES as a
first pass with a transferable conclusion: no shortcut to the index
through the shadow cardinalities alone; the Castelnuovo question is
well-posed only after C6'' supplies the diagonal and the fiber data.
G-INT6 ledger: off-diagonal = cardinalities (0 choices); the failed
readings spent 0 free parameters - an honest negative, not a fit.

## 4. Status

C6''' closed (first pass, negative, recorded). The Castelnuovo question
moves into C6'' as its primary motivation: the twisted computation now
has a concrete downstream consumer (the corrected family form of sec 3).
