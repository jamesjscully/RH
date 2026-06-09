# 13 - The tracking equivalence (R-TRACK terminal result)

Status: R-TRACK rung RESOLVED, fail-closed, 2026-06-09. Sub-target (1) confirmed
tracking; sub-target (2) decided the fork: the tracking residual is EXACTLY a
zero cross-correlation. The rung terminates as an exact equivalence, not an
independent attack surface. The decision rule was fixed in advance (TODO R-TRACK,
and the fork framing agreed with the user 2026-06-09).

## 1. Sub-target (1): the tracking is real

`scripts/numerics/witness/prime_edge_tracking.py`. Per edge, with
BULK = S_0 + sum E_D + b b^*/alpha and r = v + b/alpha, terminal positivity is
EXACTLY the scalar criterion

```text
S_N = BULK - alpha r r^*   =>   S_N > 0  <=>  BULK > 0 and
tau := alpha r^* BULK^{-1} r < 1.
```

Measured (zeta, 14 edges 1.60 -> 4.96): tau < 1 on every edge; the tracking
signature emerges exactly as alpha grows:

```text
edge          alpha    cos(v, -b/alpha)   |r|/|b/alpha|
4.00->4.26    93.3        -0.03              1.09
4.26->4.50   168.1        +0.9962            0.181
4.50->4.76   318.6        +0.9994            0.037
4.76->4.96   401.4        +0.9995            0.033
```

The accumulated arithmetic transgression v converges to the geometric center
-b/alpha in direction AND magnitude, at the rate alpha grows.

DH control - DISCRIMINATING, PASSED: on the only edge where DH's old block is
alive (1.60->1.88), tau = 1.554 > 1 and eigmin(S_N) = -0.282: DH fails exactly
AS a tracking failure. Every later edge its old block is already indefinite
(eigmin(A) ~ -1.6): DH never re-enters the tracking regime. The tau-criterion
correctly separates zeta from DH; the frame is not dispersing.

## 2. Sub-target (2): the fork is decided - the residual is a zero-sum

Exact one-mode algebra: C_N = C_0 + sum E_C with E_C ~ u t^* gives

```text
C_N^* A^{-1} u = b + alpha v = alpha (v + b/alpha) = alpha r,
```

i.e. the tracking residual is the terminal old-shell coupling whitened through
A in the compliance direction. Combined with closure (09, 6'''): the margin form
on pole-killed type-R tests IS the spectral side. Predicted identity:

```text
r_s = (2/alpha) sum_{gamma>0} hhat_{A^{-1}u}(gamma) hhat_{shell_s}(gamma).
```

`scripts/numerics/witness/prime_edge_residual_zerosum.py` (5000 actual zeros,
gamma_max = 5447.9), edges 4.00 -> 4.96:

```text
edge        rel(chain,coup)  rel(coup,zeros)  rel(chain,zeros)  cos(chain,zeros)
4.00->4.26     4.7e-06          7.7e-04          7.7e-04           +1.00000
4.26->4.50     1.5e-04          3.7e-03          3.7e-03           +1.00000
4.50->4.76     1.5e-04          2.7e-03          2.8e-03           +1.00000
4.76->4.96     8.8e-05          1.1e-03          1.2e-03           +1.00000
closure sanity (full window R=4.96): rel Frobenius form-vs-zerosum = 8.8e-06
```

All differences sit at the doc-11 sigma_2 / zero-truncation scale. FORK (ii)
CONFIRMED: -b/alpha is the explicit-formula prediction of v; the residual has
NO content independent of the zeros.

## 3. The terminal statement (what the program has actually produced)

```text
Tracking equivalence (exact, per edge). For each edge L -> R of the nested
pole-killed filtration, with u the compliance direction, x = A^{-1}u the
whitened old-history profile, and BULK = S_0 + sum E_D + b b^*/alpha:

    edge positivity  <=>  alpha r^* BULK^{-1} r < 1,
    r = (2/alpha) [zero cross-correlation of x against the shell basis],

and (doc 00) uniform edge positivity along the filtration  <=>  RH.

"v tracks -b/alpha" IS "no zero resonates with the edge direction": the
arithmetic transgression equals the zero oscillation (explicit formula in
edge coordinates), so the tracking theorem is zero-repulsion restated -
faithful, exact, finite-dimensional per edge, and TERMINAL.
```

Consequences, fail-closed:

```text
1. There is no fork-(i) proof path: the inequality cannot close by geometric
   algebra, because its left side is spectrally exact - any proof of tau < 1
   must control zero cross-correlations, i.e. supply RH-strength arithmetic.
   Combined with 09 Finding 1 (slack-bearing estimates can never close: margins
   are e^{-1.5R} below natural scale) and 09 Finding 3 (unconditional ceiling =
   Huxley 7/12, far from sqrt-cancellation), no estimate-based route survives.
2. The program's honest terminal deliverables are therefore:
   (a) the certified reduction (doc 00 + 00a: nested target <=> RH, both
       directions, with O3 Case B anchored to the classical equivalence);
   (b) the exact structure theory: edge-window factorization (11), edge-
       compliance reduction (12), and this tracking equivalence (13) - RH as
       a uniform scalar inequality tau < 1 along a one-mode recursion;
   (c) the no-go map: every shortcut killed by its own witness (one-place
       passivity, subset inductions, per-cell lemmas/Maynard, slack estimates,
       frozen-response KYP, channel decompositions, smooth surrogates,
       mass-balance rank mechanism, Landau/annular detection).
3. What a future proof would need: a NEW source of positivity for zero
   cross-correlations that is not an estimate (the program's own guards say
   estimates die) and not zero-side input (noncircularity). Nothing in the
   current structure supplies it; recording this honestly is the result.
```

## 4. Relation to the goal "close the proof"

The proof of RH is not closed and cannot be closed from the present structure:
section 3 is a fail-closed termination of the last open attack surface this
program generated. What CAN be closed - and is now the active work - is the
program itself as a theorem-grade equivalence: certify the reduction end to end
(O3 Case B via Weil 1952/Bombieri anchoring), state the tracking equivalence
with its exact hypotheses (one-mode form with the doc-11 rank-2 correction),
and ship the certification harness so every claim stays reproducible.
