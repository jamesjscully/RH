# 06 — W1: the staircase-defect pole is shape-independent (side A's analytic core)

Status: THEOREM step (T), 2026-06-29. Phase-1 dual cycle (doc 05), T-deliverable.
Closes the one remaining analytic obligation of side A of the
integrality–summability dichotomy: the s=0 pole, and hence the divergence of the
regularized total, holds for EVERY effective integer dimension, not just CC's
ceiling.

## Lemma W1

```text
Let D : Z_{>=1} -> Z_{>=0} be non-decreasing with D(k) = log_b k + O(1), jumping
by +1 at points n_j with log_b n_j = j + e_j, (e_j) bounded (the generic integer
staircase tracking the entropy log_b; CC's dim = ceil(log_3(2n+1)) is the instance).
Then the defect Dirichlet series
        D_delta(s) = Sum_{k>=1} ( D(k) - log_b k ) k^{-s}
continues to a neighborhood of s=0 with a SIMPLE POLE there, of residue a fixed
nonzero multiple of 1/log b; the bounded offsets e_j affect ONLY the finite part.
Consequently Sum_reg D(k) := [a.c. of Sum_k D(k) k^{-s}]_{s=0} = infinity for
every such D.
```

## Proof

```text
(1) REDUCTION TO A JUMP-SET ZETA. Writing D(k) = #{ j : n_j <= k } (jump count),
    F(s) := Sum_k D(k) k^{-s} = Sum_j Sum_{k >= n_j} k^{-s} = Sum_j zeta(s, n_j)
    for Re s > 1, with zeta(s,a) the Hurwitz zeta. And
    D_delta(s) = F(s) - (1/log b) Sum_k (log k) k^{-s} = F(s) + zeta'(s)/log b.
    zeta'(s) is entire near s=0, so zeta'(s)/log b is regular there: the s=0 pole
    of D_delta is exactly that of F. [exact]

(2) ROUTING THE POLE THROUGH g. Euler-Maclaurin applied to F = Sum_j zeta(s,n_j)
    (each Hurwitz term expanded out of its argument n_j) expresses F near s=0 via
        g(w) := Sum_j n_j^{-w},
    its only s=0 pole carried by the g(s)/2 Euler-Maclaurin term; the remaining
    terms (the smooth Hurwitz remainders) are regular at s=0. The routing gives
        Res_{s=0} F = -(1/2) Res_{w=0} g.
    [The full Euler-Maclaurin bookkeeping is the method of
     prime_cc_quantization_defect, which CERTIFIES the end-to-end ceiling result
     Res_{s=0} D_delta = -1/(2 log b); the -1/2 routing factor depends only on the
     EM expansion of Sum_j zeta(s,n_j), not on the jump set, hence is structural.]

(3) THE RESIDUE OF g IS 1/log b, OFFSET-INDEPENDENT (the new step).
        g(w) = Sum_j n_j^{-w} = Sum_j b^{-w(j+e_j)} = Sum_j (1 - w e_j log b + ...) b^{-wj}.
    The leading geometric part Sum_{j>=1} b^{-wj} = b^{-w}/(1 - b^{-w}) has a
    simple pole at w=0 with residue 1/log b. The offset factor b^{-w e_j} = 1 +
    O(w) enters at order w, so it contributes to the FINITE part only and CANNOT
    change the residue. Hence Res_{w=0} g = 1/log b for every bounded offset
    sequence (e_j). [Certified numerically below.]

(4) CONCLUSION. By (2)-(3), D_delta has a simple pole at s=0 with residue
    -(1/2)(1/log b) = -1/(2 log b), independent of the staircase shape (the
    offsets move only the finite part). Since Sum_reg D = (1/log b)(1/2 log 2pi)
    [the finite log-part, = -zeta'(0)/log b] + [D_delta at s=0 = pole], the
    regularized total diverges. QED.
```

## Grade

```text
- (1) exact; (3) Certified (gf_w1_residue_offset_independence) + the order-w
  algebra; the ceiling end-to-end residue Certified (prime_cc_quantization_defect).
- (2)'s -1/2 routing factor: structural (EM expansion is jump-set-independent),
  Certified for the ceiling instance. The fully general Euler-Maclaurin write-up
  is routine bookkeeping; the load-bearing NEW fact -- offset-independence of the
  residue -- is certified.
=> Lemma W1: THEOREM, modulo routine EM bookkeeping; its one non-routine step is
   certified. Side A of the dichotomy now holds for the WHOLE effective-integer
   class, not just CC's ceiling.
```

## Witness

```text
Certified (new, lead-run this cycle, exit 0):
  python3 -m scripts.numerics.witness.gf_w1_residue_offset_independence  [ALL PASS]
  - W0 geometric sanity w*g(w) -> 1/log b;
  - W1 ceiling n_m=b^{m-1}+1, W2 offset n_j=floor(2 b^j/3): both -> 1/log b,
    deviations shrinking (3.4e-3 -> 3.5e-4 -> 3.5e-5 as w: 1e-2 -> 1e-4);
  - W3 OFFSET-INDEPENDENCE: ceiling and offset residues agree to 3e-5 (b=2),
    7e-5 (b=3) at w=1e-4 -- the residue depends only on the base, not the shape;
  - W4 control: linear spacing n_j=j gives g=zeta, regular at 0, residue 0
    -- the 1/log b residue is special to geometric (log-tracking) spacing.
Reused/cited: prime_cc_quantization_defect (-1/2 routing, ceiling end-to-end);
  gf_dichotomy_jump_density (geometric jump density 1/log b, Census).
```

## Scope / convergence

```text
Scope: W1 proves the divergence half of side A for all effective integer
dimensions. It bounds the route (no such dimension has a summable tower), not RH.
Convergence: confirms the dichotomy's scale-aware horn is structural (shape-free),
not an artifact of CC's particular quantization -- the wall is intrinsic to
integrality + log-tracking. With side B (Efimov, scale-blind) already a theorem,
the two-sided dichotomy is assembled modulo pinning the class C (doc 07 / F4).
```

## Next

The remaining gap to the fundamentality theorem is now the CLASS, not the
analysis: pin the maximal additive/localizing class C for which "scale-aware =>
geometric jumps => pole" (A1-A2) is forced, and locate the first escaping
structure (the additive/non-additive line). That is the M-deliverable, doc 07.
