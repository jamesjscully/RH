# Y - Ambiguity (L) DECIDED from the literature: NO divided class at 2p; the dodge executed; the truncation relocates to w = p^2-1

Status: 2026-06-10, worker Y (fresh context). Task: doc 27 ranked front 1
(resolve (L), execute T's pre-registered dodge pi_{2p}X(1+3p)). Witness:
prime_twisted_lattice_decider.py (NEW, ALL PASS, exit-gated, ~20 s);
prime_twisted_fork_filtration_zero.py re-run this session: ALL PASS.
Lineage: T-doc secs 5-6 ((L)/(S), Theorem T.3, the three-way table, the
dodge), P-doc secs 2a/5 (transport, branch signatures), doc 27 front 1.
New refs archived: refs/baker-richter2005-cooperation-connective-adams-
summand-0506455.pdf (+ extraction baker-richter2005.txt), refs/culver2018-
bp2-cooperations-odd-1809.06898.pdf (+ culver2018-odd.txt).

## 1. Verdict on (L): NO - the divided class is NOT connective at 2p

THE LITERATURE STATEMENT (citation-grade, re-verified against the PDF this
session). Baker-Richter, "On the cooperation algebra of the connective
Adams summand", arXiv:math/0506455v2, Section 8, "Summary" (p. 17),
quoting Kane, Operations in connective K-theory, Mem. AMS 254 (1981),
(19.6.1), obtained via Adams' criterion [Stable Homotopy and Generalised
Homology, III.17.6]:

    "Kane [5, (19:6:1)], using Adams' criterion [1, III,17.6], worked out
    what the image of the torsion-free part of l_* l is when we pass to
    l_* l (x) Q. The generators for the image of l_* l in l_* l (x) Q are

        t_{n,i} = u^i v(v-(p-1)u)...(v-(n-1)(p-1)u) / p^i,
                  0 <= i <= nu_p(n!)."

(l = connective Adams summand, l_* = Z_(p)[u], |u| = |v| = 2(p-1); the
relation u t_{n,i} = p t_{n,i+1} holds.) Baker-Richter prove independently
(their secs 5-8) that all torsion in l_* l is simple p-torsion = u-torsion
(Prop 7.3, from Kane Prop 9.1) and the Kunneth SS collapses (Cor 7.4) -
the torsion-free image above is the whole non-torsion story.

CONSEQUENCE (the (L) answer, exact). Each division by p costs a
multiplication by u: since nu_p(n!) = 0 for n < p, the FIRST p-divided
class is t_{p,1} = u q_p / p, in (u,v)-degree p+1, homotopy degree
2(p-1)(p+1) = 2p^2-2. Via the Adams splitting ku_(p) = wedge_{0<=i<=p-2}
Sigma^{2i} l (B-R sec 1) and pi_{2m}(Sigma^{2i} l) -> Z_(p) beta^m a
p-local iso on each rational line, the weight-w coordinate lattice L_w of
pi_{2w}(ku_p (x) ku) is spanned by t^j g(t^{p-1}), g in Kane's lattice
(torsion has zero rational coordinates and is invisible to the skeletal
d^1). Smallest total degree carrying any p-denominator: 2(p-1)(p+1) =
2(p^2-1). Hence:

    ku_{2w}(ku)_(p) / torsion = the SMALL (monomial) lattice
    Z_(p){beta_0^{w-b} beta_1^b}  for ALL w <= p^2-2;  in particular at
    w = p the binom(t,p)/divided class is ABSENT.  (L) = NO.

T's trichotomy row "+ binomial/numerical (KU_0 KU-style)" is therefore NOT
the connective lattice at low weights: the numerical staircase (death at
w >= p for c = 1) is a periodic-lattice artifact. The connectivity
constraint is exactly "every /p costs a beta_0^{p-1}".

## 2. What the lattice does at the first divided weight (NEW, witnessed)

The relocation, not the disappearance, of the truncation (witness Y2/Y3,
exact integer arithmetic, grid p in {3,5,7}, u in {1,2,3}, c in {1,2,3}):

  - UNIFORM RANGE: image ideal {f(1) - f(alpha) : f in L_w} has valuation
    EXACTLY c for every 1 <= w <= p^2-2 (Y2). At w = p: |E^2_{0,2p}| =
    p^c - no filtration-0 death, no LTE bump (Theorem T.3 re-confirmed
    with the true lattice).
  - FIRST DROP: at w = p^2-1 the class t_{p,1} enters with coordinate
    q_p(1, t^{p-1})/p and the valuation drops to EXACTLY c-1, staying
    c-1 through the probed window [p^2-1, p^2+p] (Y3; pre-registered,
    confirmed on the full grid; hand-checked at p = 3, alpha = 4:
    (q_3(1,1) - q_3(1,16))/3 = -895, a 3-adic unit). For c = 1 this is
    FILTRATION-0 DEATH at w >= p^2-1: the truncated third law is real
    but with w_0 = p^2-1, not p. Floor: never below c-1 on the grid
    (divided differences of i-divided numerical classes lose only one
    power of p; derivation sketch in the witness, grid-gated only).

Decided filtration-0 family signature (Y5, arb prec 350): for c = 1,
D(s) = log p * sum_{w<p^2-1} w^{-s} - ENTIRE, value (p^2-2) log p at
s = 0; for c >= 2 regular at 0 with value (-(c-1)/2 + p^2-2) log p. NO
s = 0 pole, NO zeta factor at filtration 0 for ANY wild alpha - the exact
quantitative form of Theorem T.3's exclusion.

## 3. The dodge executed: pi_{2p} X(1+3p) = Z/p, branch (i)

At alpha = 1+3p (p >= 5; for p = 3, 1+3p = 1+p^2 falls in T6e's c = 2
regime, equally rigid), T6d holds: 1+-u = {4,-2} are units mod p, so no
theta = +-1 can bump the k = 1 mu-locus tower - (S) does not bite (Y4
re-gates the arithmetic). The three-way table at degree 2p then collapses:

  - truncated 0: KILLED by (L) = NO (no divided class at w = p; death
    relocated to w >= p^2-1, far above 2p);
  - (ii) Z/p^2: KILLED at u = 3 by T6d rigidity (no bump mechanism);
  - (i) Z/p: the survivor.   pi_{2p} X(1+3p) = Z/p  (UNIFORM).

BRANCH VERDICT at the dodge point: (i). The local Euler supply is NOT a
factor of the twisted family there: no LTE bump, no s = 0 pole, no
per-weight Lorentzian scaling sourced from this corner (W-doc sec 9
consumer: the gate stays closed).

TRANSPORT to alpha = 1+p (P-doc 2a; the family is one function on Z_p^x).
(L) is alpha-independent, so at the canonical instance the 2p row
collapses to {(i) Z/p, (ii) Z/p^2}, decided SOLELY by the sign of the
relative unit theta (T6c) - i.e. by O3's unbuilt twisted cyclic structure
(KMN rebuild, which T.1 proved unavoidable). What is now known at 1+p:
truncated-0 is excluded at 2p; filtration 0 contributes exactly Z/p; and
branch (ii) AS A FAMILY LAW is dead - it fails at every u != +-1 member,
so even a Z/p^2 outcome at 1+p would be the u = +-1 sign accident, not
the LTE tower law. The pole-bearing branch's "local Euler supply as a
family factor" is refuted at filtration 0 (T.3 + sec 2) and at the
abutment for all rigid members; it survives only as a filtration >= 1
question at the measure-zero locus u = +-1 mod p, c = 1.

## 4. Honest limits

1. Kane (19.6.1) is consumed through Baker-Richter's published quotation
   (exact formula, theorem number, provenance Adams III.17.6); Kane's
   Memoir itself and Lellmann (J. LMS 29 (1984) 562-576) were not
   independently opened (paywalled). B-R's own secs 5-8 re-derive the
   surrounding structure (torsion simple, collapse, congruences), so the
   formula is corroborated, not bare.
2. The Adams-splitting translation (sec 1) is mine: standard bookkeeping
   (p-local splitting + rational lines), paper-level, not in print in
   this form for ku (x) ku.
3. The assembly pi_{2p}X(1+3p) = Z/p inherits T's framework caveats: the
   three-way table is exhaustive at 2p only below (L)+(S); unnamed
   filtration >= 1 contributions/extensions beyond the mu-locus tower
   would evade it (T-doc honest limits 1-4 apply verbatim).
4. The Y3 floor (never below c-1) and the c >= 2 tail law are grid facts
   with a derivation sketch; the w -> infinity staircase is not proved.
5. Flags f1-f2 (T-doc sec 5) are untouched; sec 2 says nothing about the
   abutment at w >= p^2-1, only about filtration 0.

## 5. G-INT6 ledger

Free choices: grids p in {3,5,7(,11)}, u in {1,2,3}, c in {1,2,3}, window
[p^2-1, p^2+p] (cost-bounded, spans the regimes, not tuned). Pre-registered
readings Y1-Y5 written into the docstring before the run; all PASS on the
first run, including the genuinely falsifiable Y3 drop (= c-1 exactly) and
its u-uniformity (my own intermediate hand-analysis had flagged a possible
u-dependence at u = 2; the run refutes the worry - recorded). Fitted
objects: NONE. The one literature unknown that remains ((S)'s theta at
u = +-1) is recorded as ignorance with a named owner (KMN rebuild), not
resolved by preference.

## 6. Files

- research/work/Y-lattice-decider.md (this doc)
- scripts/numerics/witness/prime_twisted_lattice_decider.py (NEW witness)
- research/proof/refs/baker-richter2005-cooperation-connective-adams-
  summand-0506455.pdf, baker-richter2005.txt (the (L) source)
- research/proof/refs/culver2018-bp2-cooperations-odd-1809.06898.pdf,
  culver2018-odd.txt (corroborating odd-primary cooperations context)
