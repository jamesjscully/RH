# HH - Probe 1 (doc 32): the Weil form against the certified Lorentzian index face

Status: executed 2026-06-10 (fresh context, worker HH). Task: doc 32
PROBE 1. Required reading completed in order: docs 32, 31, 13; W-doc
sec 5 (max-Gram lemma); AA (strict norm-Gram); doc 19 (supply
dictionary). Witnesses rerun this session, ALL PASS, lead conventions
unchanged: prime_int_bb_global_assembly, prime_cc_thh_norm_filtration.
New witness (pre-registered gates H1-H7, fail-closed, exit-gated):

    python3 -m scripts.numerics.witness.prime_hh_weil_index_factorization

Discipline: F1 (zeros via fork_lib COMPARISON ONLY, gate H7); G-INT6
choice ledger in sec 5; carrier guard rerun on DH (gate H6); no
zero-side input anywhere in the construction.

## 0. The fork, posed and the verdict

QUESTION (doc 32 probe 1): does the Weil/tracking form factor through
the certified Lorentzian index face ((w log p) MAX + E of W sec 5 /
AA's strict CC norm-Gram), restricted to an identifiable cone?

VERDICT: **(b) -- factors with a structured defect, and the prime side
factors EXACTLY (defect 0).** Precisely:

```text
THEOREM HH.1 (exact; gate H1, Fraction arithmetic, zero tolerance).
In the coefficient space of the geometric family {[p^i]}_{i=0..n}, the
difference classes d_k = [p^k] - [p^{k-1}] (AA's classes, k = 1..n)
DIAGONALIZE the certified index face:
    <d_k, d_l>_{(w log p) MAX}  = -(w log p) delta_kl
    <d_k, d_l>_{CC strict}      = -(w log p) delta_kl
                                  - log2 (2 delta_kl - delta_{|k-l|=1}).
The unit class [1] = e_0 is NULL in both faces (lightlike), with
<e_0, d_k> = w log p (+ log 2 at k = 1 = AA's N([p^w]-[1]) = 2p^w);
span{d_k} = the sum-zero (degree-zero) hyperplane, on which -M is PD
(maximal spacelike); its M-orthocomplement MAX^{-1} 1 is TIMELIKE
(1^T MAX^{-1} 1 > 0 exactly).  In particular, at w = 1:

    Lambda(p^k) = log p = -<d_k, d_k>_M   for EVERY k:

THE VON MANGOLDT ATOM WEIGHT IS MINUS THE SELF-INTERSECTION OF THE
LADDER STEP.  (Doc 19's supply dictionary, upgraded from the diagonal
of the Gram -- AA gate N8 -- to the full Gram.)

CONSEQUENCE (gates H2, H3; exact rearrangement, rel <= 1e-12 witnessed).
With the doc-19 sample map (sec 2 below: T_p(g) = sum_k g-check(k log p) d_k,
Theta_p = 2 sum_k p^{-k/2} d_k the KMS-1/2 geometric series), the EF
prime side on the doc-13 ladder factors EXACTLY:
    P_R(g) = - sum_p <T_p(g), Theta_p>_{(log p) MAX}        (defect 0)
and the full Weil form (doc-13 margin form, pole-killed class) is
    Q(g) = M_R(g) = W_inf(g) + sum_p <T_p(g), Theta_p>_M.
THE DEFECT IS R(g) = W_inf(g): the archimedean supply, identically --
not a residue, not noise, ONE banked object (doc 19 sec 2's digamma
carrier; doc 31 exit B; BB's missing archimedean Poisson unit).
```

The task card's pre-registered prediction "R should be the zero-side
term" is REFUTED in the precise sense: by doc-09 closure the zero side
equals the WHOLE pole-killed form Q(g), so the defect of the
index-face factorization is the archimedean term, not the zero term.
Equivalently the identity above IS the explicit formula read in
lattice coordinates -- gate H7 (F1, zeros comparison only) returns
EF-DERIVED exactly as pre-registered. Per doc 16's trichotomy this
sits at LEVEL-1 BOCHNER: no new sign content is claimed. The probe's
product is the GEOMETRY the coordinates expose (secs 3-4).

## 1. Both sides, as computed

WEIL SIDE (doc-13 conventions, prime_ladder_scaling): test class =
even raised-cosine packets f = sum_a x_a bump_a (support <= cmax + hw
= 2.48), quadratic tests g = f * f~ (support <= 4.96 = R); atom value
x^T blk_n x = (2 Lambda(n)/sqrt(n)) (f*f)(log n); margin form
M_R = W_inf - P_R; pole-killed nested bases per rung; on this class
M_R = zero side exactly (doc 09 6''', doc 13).

INDEX SIDE: the certified Lorentzian (1, n) faces -- W sec 5's
(w log p) MAX + E with the exact max-Gram lemma, and AA's strict CC
norm-Gram (log p) MAX + log2 (J - I), certified with no low-weight
anomaly. Positive cone: the Perron/degree direction; negative
complement: everything degree-orthogonal.

## 2. The map T, precise (G-INT6: every choice logged in sec 5)

```text
samples      c_{p,k}(g) = (f*f)(k log p) = g-check at the ladder
             frequency k log p   [doc 19's dictionary; linear in g]
map          T_p(g) = sum_{k=1}^{n_p} c_{p,k}(g) d_k
             (n_p = floor(R / log p): the tower inside the window)
dual vector  Theta_p = 2 sum_{k=1}^{n_p} p^{-k/2} d_k
             (the KMS-1/2 geometric series; the p^{-k/2} is doc 19's
             self-dual normalization, the only place beta = 1/2 enters)
identity     P_R(g) = - sum_p <T_p(g), Theta_p>_{(log p) MAX}   exact
             (gate H3a, rel <= 1e-12 over all places x 5 tests;
             algebraic content = Theorem HH.1 diagonalization)
CC strict    defect of the strict face vs the exact MAX face:
             <T,Theta>_CC - <T,Theta>_MAX = -log2 (t . theta)
             (gate H3b) -- the "2" of AA's N = 2 p^max, a bounded
             nearest-neighbor Dirichlet-type correction, structured.
```

Two structural facts the identity exposes, both exact:

1. ZETA IS THE UNTUNED CASE (gate H6a): coeff(p^k)/log p = 1 to
   1e-12 for every tower entry -- Theta_p needs NO per-atom retuning;
   the entire arithmetic weight system Lambda is absorbed by the GRAM
   (Lambda = -<d,d>), leaving only the KMS-1/2 geometric series.
2. THE POLE IS OUTSIDE THE LATTICE (gate H3c):
   <Theta_p, Theta_p>_M = -4 log p sum_{k<=n_p} p^{-k} -> -4 log p/(p-1);
   sum_p ||Theta_p||^2_{-M} diverges like -4 zeta'/zeta near s = 1:
   the assembled KMS vector has divergent spacelike norm -- the s = 1
   pole is the statement that Theta is not in the lattice completion.

## 3. The geometry (the probe's real product)

```text
(i)   T's image avoids the positive cone ENTIRELY: T_p(g) lies in
      span{d_k} = the degree-zero hyperplane, which is MAXIMAL
      SPACELIKE (Thm HH.1).  The certified face's Perron direction --
      the thing the Castelnuovo mechanism is built around -- is IDLE
      in the Weil form: the index face homes the PRIME side only, and
      homes it on its spacelike boundary.
(ii)  The unit class [1] is on the LIGHT CONE (null), pairing
      <[1], d_k> = log p: the monoid unit is the lightlike completion
      of the frame (this nullity is AA's "exactly-zero leading pivot"
      disclosure, now structural).
(iii) The image cone is the MOMENT CONE (gate H5a): by Herglotz/
      Bochner the sample sequences (c_0, c_1, ..., c_{n_p}) of the
      admissible class are PSD-Toeplitz -- witnessed over 200
      pole-killed tests, 4 places.  So in lattice coordinates Weil
      positivity reads: the functional (W_inf, Theta) is in the DUAL
      of the moment cone -- which is the CC20 Toeplitz mechanism
      (doc 16 level-1), now carrying an M-geometry.
(iv)  PROPERNESS (gate H5b): the image is proper in the spacelike
      part with R-dependent aperture: ||T(g)||_{-M} <= c_0(g)
      sqrt(psi(e^R)) (theorem-implied via |c_k| <= c_0); measured
      aperture far inside the bound (reported by the witness).  The
      aperture grows with R -- properness is rung-wise, not uniform:
      the same regularization wall as doc 19 sec 5, in cone language.
(v)   CONE-MEMBERSHIP STATEMENT (reachable, and reached -- in the
      DUAL form): on each rung, RH-at-the-rung = margin form >= 0 =
          W_inf(g) + sum_p <T_p(g), Theta_p>_M  >=  0   for all g,
      i.e. the functional (1, Theta) lies in the DUAL CONE of the
      image cone K_R = {(W_inf(g), T(g)) : g admissible} (a convex
      cone: the class is scaling-closed, the map linear).  The slack
      of this dual-cone membership IS doc 13's tau < 1, already
      certificate-grade on the computed ladder (X-doc).
(vi)  THE STRONGER "POSITIVE BUDGET" READING FAILS (gate H4, measured,
      pre-registered both ways): eigmin of the W_inf block on the
      pole-killed bases goes NEGATIVE from rung R = 2.30 and falls
      ~linearly to -0.907 at R = 4.96 while the margin stays positive
      (n_-(P_R block) ~ dim/3 alongside).  So Weil positivity is NOT
      "a positive archimedean budget dominates the spacelike norm":
      BOTH coordinates are signed on the class, and the inequality is
      a genuine joint cancellation -- the dual-cone form (v) is the
      strongest true geometric statement at this layer.
(vii) the timelike room starves: 1^T MAX^{-1} 1 = 1/n EXACTLY (H1d),
      i.e. the M-norm of the face's timelike complement direction
      decays like 1/(n log p) as the tower deepens -- the certified
      face's positive direction is not only idle, its budget per
      place shrinks as the window grows.
```

Reading against doc 32's failure-mode forecast: "if effectivity on the
square requires an input equivalent to zero-repulsion, the
conservation law wins; probe 1's defect measurement is the early
detector." The defect is now measured AS ONE OBJECT: R(g) = W_inf(g),
and the geometry says WHY it is conserved -- every lattice direction
the program has certified is spacelike-or-null for the Weil form; the
missing positivity is exactly the missing timelike unit at infinity
(doc 31 exit B, triply specified there; BB's archimedean Poisson
exchange; FF's rational layer). Three independent threads and this
probe now name the SAME slot.

## 4. Carrier guard (gate H6, decisive gate rerun on DH)

```text
zeta     dictionary formable, untuned (H6a): Lambda(p^k) = -<d_k,d_k>,
         Theta = pure KMS series.
DH       dictionary UNFORMABLE, twice over (H6b): atoms with NEGATIVE
         weight (Lambda = -<d,d> >= 0 violated: self-intersections
         cannot be retuned) and atoms at NON-PRIME-POWERS (no tower,
         no d-address).  The decisive gate fails at the object level.
Epstein  the MAX face alone is carrier-blind (AA N9, banked): an
         Epstein-shaped degree-separated family has the same
         Lorentzian Gram.  ALL discrimination lives in T -- in the
         monoid/unique-factorization structure that gives every EF
         atom a tower address with the right self-intersection.
```

## 5. G-INT6 choice ledger

```text
choice                          status
family {[p^i]} per place        forced (W: FF configuration; banked)
difference frame d_k            forced up to the receptacle: the only
                                vector choice is using [1] = [p^0] as
                                the sum-zero receptacle; alternatives
                                (drop [1]) leave a rank-2 indefinite
                                contamination u1^T+1u^T in every
                                pairing -- [1] is the unique choice
                                killing it; logged, not tuned
samples c_k = g-check(k logp)   doc 19's dictionary verbatim
Theta weights 2 p^{-k/2}        forced by matching the EF atom weight
                                2 Lambda(n)/sqrt(n); the log p factor
                                comes OUT OF THE GRAM (Thm HH.1) --
                                zero residual freedom (H6a: ratio = 1
                                exactly); beta = 1/2 enters here and
                                only here
quadratic-vs-linear reading     LOGGED DECISION: the task card's
                                Q(g) = -<T(g),T(g)>_M reading is
                                degree-inconsistent (Q linear in g,
                                the form quadratic); the factorization
                                is taken in the linear/pairing form
                                with the quadratic structure carried
                                by the moment-cone constraint on T(g)
                                (sec 3(iii)); no gate depends on a
                                tuned scale
grids/tolerances                calibration only (T=250 budget per
                                doc 11; exact gates use Fraction)
```

## 6. Witness results (ALL PASS, exit 0; one run, no gate changed)

```text
H1abc EXACT (Fraction, zero tolerance): d-frame diagonalization,
      [1] null, cross terms as stated.  H1d: 1^T MAX^{-1} 1 = 1/n
      exactly (n = 3, 5, 8, 12).
H2    wiring t-grid vs independent u-quadrature: assembled prime side
      rel <= 4.1e-04 (worst per-atom 2.1e-03; T=250 budget).
H3a   P_R = -sum_p <T,Theta>_MAX: rel <= 7.3e-15 (5 tests x 34 places).
H3b   CC-strict defect = -log2 (t.theta): err <= 2.1e-17; J-part 0.
H3c   ||Theta_p||^2 closed form: rel <= 3.7e-16; window total 17.56,
      divergent in R (the s = 1 pole).
H4    rung rearrangement exact; eigmin(Winf-block): +0.284 at R=1.60
      falling through 0 at R ~ 2.2 to -0.907 at R=4.96; n_-(P block)
      5 -> 12; margin eigmin positive on every rung (doc-13 values).
      READING: SIGNED DEFECT (sec 3(vi)).
H5a   Toeplitz/Herglotz: worst -eigmin/c0 = 0.0 over 200 tests,
      places {2,3,5,7}: the image is in the moment cone.
H5b   properness aperture: max ||T(g)||_{-M}/c0 = 1.277, median 0.684,
      vs theorem bound sqrt(psi(e^R)) = 11.9: the image sits far
      inside the Bochner box (measured law, not fitted).
H6a   zeta: coeff(p^k)/log p = 1 to 0.0e+00 -- untuned dictionary.
H6b   DH: 42 negative-weight atoms + 45 non-prime-power atoms in the
      window: dictionary unformable twice over.
H7    F1 (zeros COMPARISON ONLY, K=3000): rel = 1.1e-05, cos = 1.000:
      EF-DERIVED, as pre-registered.
```

## 7. Honest limits

1. No new positivity: gate H7's EF-DERIVED verdict is the pre-registered
   honesty -- the factorization is the explicit formula in lattice
   coordinates; doc 16's trichotomy places it at level-1 Bochner. The
   product is structural location, not sign content.
2. Theorem HH.1 is exact but small (finite linear algebra); its value
   is that it is the FIRST exact identity tying the EF atom weights to
   self-intersections in the certified index object, with zero tuning.
3. The moment-cone/properness statements are rung-wise (R-dependent
   aperture); nothing uniform in R is claimed -- the uniform statement
   is exactly the wall (doc 13: no estimate route).
4. The archimedean defect W_inf is characterized (the one continuum
   slot), not constructed: this probe DETECTS doc 32's failure mode,
   it does not cross it. Whether the JJ road's integer-RR unit can
   supply the missing timelike coordinate is exactly exit B's open
   construction.
5. The signed-defect finding (sec 3(vi)) cuts BOTH ways: it kills the
   cheap "positivity = archimedean budget" reading, but it also means
   any future archimedean unit cannot simply be added as a PD block --
   it must couple (the joint cancellation is load-bearing), consistent
   with GG/BB's coupling demand rather than a per-place patch.
6. Numerical-method note (disclosed): H5a's tolerance was set relative
   to c0 before the run; measured violation was exactly 0.0, so the
   quadrature-floor concern noted during design never bit and no gate
   was changed.
