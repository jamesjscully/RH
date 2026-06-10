# 25 - The p = 2 anomaly computed: at 2 the real place degenerates to a complex place, and the scheme selector lives at the prime 2

Status: 2026-06-10. Synthesis of worker S (research/work/S-thr-p2.md,
witness prime_int_thr_p2_anomaly.py ALL PASS, lead-rerun; all five
pre-registered readings S-r1..S-r5 passed as registered) together with
the same-day worker O result (doc 24 as amended). Closes doc 24's
p = 2 gap; opens the sharpest convergence of the rung.

## 1. The new theorem

Theorem S.1 (worker S; no prior computation located in the literature):

    THR(F_2)^{tC_2} ~ prod_{n>=0} Sigma^{2n} (HF_2)^{tC_2},
    pi_* = F_2[[z]][t^{+-1}]   (z = t^2 x, weight 1, |z| = 0)

- theorem-grade additively (DMPR's genuine splitting of THR(F_2)
forces Borel formality, so the Tate spectral sequence collapses; ring
form up to a stated generator-choice caveat). The complete Tate square
with maps is in the S-doc, integer-exact and witnessed. The M-doc's
"missing computation" debt is discharged in closed form.

## 2. The anatomy of the anomaly (verdict s2 containing s1)

The p = 2 fixed points factorize EXACTLY:

```text
F_2[xbar, y] = (fold core F_2[xbar^2])   the odd-p Gamma_R ladder
             x ({1, xbar} doubling)      eigenvalue DEGENERATION
             x (F_2[y] Euler tower)      the permanent rank-2 part
```

(i) THE DOUBLING IS GAMMA_C: Serre's F_infinity eigenvalue selection
(-1)^n degenerates mod 2, the res-visible ladder unfolds to all
n >= 0, and the regularized characteristic function is the
Gamma_C-shape - with the exact identity prod_reg(s+n) =
prod_reg(s+2n) * prod_reg(s+2n+1) mirroring Legendre's duplication
Gamma_R(s) Gamma_R(s+1) = Gamma_C(s). At 2, the REAL place degenerates
to a COMPLEX place. This is a computed statement, not an analogy.

(ii) THE EULER TOWER RAISES RANK: the y-tower has no odd-p analogue
and is not a ladder correction - the full degree carrier is the Barnes
double Gamma Gamma_2(s | 1, 2) with QUADRATIC anomalous dimension
(rank-2 certificate: nonzero second difference, witnessed). The
permanent part of the anomaly is a genuinely two-dimensional
archimedean object at the prime 2.

## 3. The convergence: the scheme selector lives at 2

Three independent results now point at the same place:

```text
O (Prop A6):  the symmetric determinant requires a canonical
              lambda^{1/2} - it lives on a DOUBLE COVER of the
              eigenvalue space; any H-r3 carrier must be 2-primary.
S (S-r5):     at p = 2 - the unique prime with nonvanishing reflection
              Tate - duality completion DOES happen at the reflection,
              and what it completes is the 2-adic Euler ladder in
              SELF-DUAL KMS-1/2 FORM (per weight n the full line gives
              2 sinh((s+n) log 2 / 2) = 2^{(s+n)/2}(1 - 2^{-(s+n)})).
              The symmetric scheme APPEARS GEOMETRICALLY exactly at 2.
              Also: pi_0 = F_2[[z]] - the reflection sector acquires a
              geometric direction (a formal disk) only at 2.
CC:           the canonical divisor of compactified Spec Z is K =
              -2{2} - supported at the prime 2 (recorded as a rhyme,
              with the N-doc's bookkeeping caveat).
```

Reading (flagged as reading, not theorem): the KMS-1/2 scheme's
carrier - the open H-r3(hom)/L-hom of doc 24 - should be sought in the
2-primary/double-cover sector, where worker S has now EXHIBITED a
self-dual-form Euler factor inside a genuine equivariant computation.
Fork F1's three ranked probes (O-doc sec 4.7) should be run against
the S-doc's Tate square first; O's lambda^{1/2} kill-test applies.

## 4. Gap ledger

- Ring identification up to filtration-preserving generator choice;
  y -> tx is leading-term (S-doc honest limits).
- The Gamma_2 reading uses the DEGREE grading where docs 19/20 used
  weight - a convention boundary flagged for Q-SCHEME bookkeeping.
- THR(Z) at 2 and the compactified archimedean object remain untouched
  (C5''' burden unchanged).
- The sqrt(2)-modulus reading of the Lin line is a reading.

## 5. Status

Doc 24's gap ledger item "p = 2 anomalous, not resolved" is replaced
by: p = 2 COMPUTED - degeneration (Gamma_C) x rank-raising (Gamma_2),
with the self-dual local factor appearing geometrically. Gate
C5''-infty's open items: (infty-2) the 1/(2pi) scale; (infty-3'')
L-hom/F1, now with a concrete 2-primary search target; (infty-4) rank
factors - note the Barnes Gamma_2 of sec 2(ii) is the first RANK-2
archimedean object the program has produced from homotopy theory, and
the s(s-1) pole pair is itself rank-2: flagged as a candidate
identification for (infty-4), unexplored.
