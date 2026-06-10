# II - PROBE 2: does the integer signature flow of the growing count-pairing family see the zeros?

Status: fresh-context worker II, 2026-06-10. Charter: doc 32 PROBE 2.
Required reading executed in order: doc 32; doc 17 (G-INT gates, C4
protocol); doc 23 incl. secs 5-6; W-monoid-frobenius.md sec 5 (max-Gram
lemma, t-window); AA-cc-thh-probe.md (strict norm-Gram, Thm AA.1);
GG-global-cancellation.md (renormalized survivor = the EF sigma=0
shell). Inherited witnesses rerun by me BEFORE any new work:
prime_int_gc_k3_barnes_rank.py ALL PASS (KG1-KG5, exit 0),
prime_cc_thh_norm_filtration.py ALL PASS (N1-N9, exit 0).

New witness (pre-registered, fail-closed, exit-gated):

    python3 -m scripts.numerics.witness.prime_int_ii_signature_flow

Sections 0-2 below were written BEFORE the witness was first run; the
verdict sections follow after. The zero data (fork_lib.zeta_gammas) is
loaded ONLY after the loci/spectra are computed and hash-frozen; the
witness prints the freeze hash before the first import of zero data,
and the hash is logged in sec 4.

## 0. The object (zero new choices; every ingredient sourced)

THE GLOBAL FAMILY at weight w, place set P <= X: the unit class [1]
(once - it is the SAME class at every place; this is GG's "one
continuum unit", counted once, not once per place) together with the
classes [n^w] for n a prime power <= X. This is exactly the union over
places p <= X of W/AA's geometric families {[p^{wi}] : p^i <= X},
glued along the shared unit; the truncation p^i <= X matches GG's
shell q <= X. GG's NORMALIZATION is used verbatim: the renormalized
global survivor is supported on log(prime powers) with UNIT weights
(GG sec 4.3) - so each prime-power atom enters the family once, weight
one, and the only continuum/zero-mode object (the unit) enters once
globally. No other weighting is introduced.

THE GRAM (AA Thm AA.1, extended cross-place): the strict CC-norm Gram

    M(w, X)[a, b] = log N([A_a] - [A_b]) = log 2 + max(d_a, d_b)
                    (a != b),   M[a, a] = d_a = w log A_a^(1/w)
                    i.e. d_a = w log n_a  for atom n_a, d_unit = 0.

Cross-place the SAME shared-row representative as AA's N4 works: for
A > B >= 1 take a = (B, A - B), b = (1, -1), S = {(0,0),(1,0),(0,1)};
masses (A, 2), so N <= 2A; AA Thm AA.1(ii) gives N >= 2 max(A, B).
Hence N([A] - [B]) = 2 max(A, B) for ALL distinct A, B (witness gate
II1 checks the construction's masses and the bound integer-exactly).
So M(w, X) = w MAX(D) + log2 (J - I) with D = sorted degrees
{0} u {w log n : n prime power <= X} - distinct (p^a = q^b is
impossible; integer-exact gate). One matrix, zero free parameters.

THE INTEGER OBSERVABLE: the signature sig(w, X, t) = (n_+, n_-) of
M(w, X) + tI. Since eig(M + tI) = eig(M) + t, the JUMP LOCI in t are
exactly t_k = -lambda_k(M(w, X)): the loci ARE the (negated) spectrum.
n_+ <= 2 always (exact argument: M + tI = [w(u1^T + 1u^T) + log2 J] +
[-w MIN - (log2 - t) I]; first bracket has n_+ <= 2 (rank-2 signature
(1,1) plus rank-1 PSD), second is negative semidefinite for
t <= log 2; Weyl). Whether n_+ = 1 (Lorentzian) survives the GLOBAL
assembly (degree gaps shrink like 1/X) is itself recorded. The flow:
as X grows, M(w, X') for X' < X is a principal submatrix (atoms only
added), and the loci flow/jump.

## 1. PRE-REGISTERED FORK (written before any run; zero data frozen out)

The fork of doc 32 PROBE 2, in operational form. The natural variable
for accumulation is L = log X (the loci flow as the family grows) and
the natural frequencies are the zero ordinates gamma (the EF places
oscillations e^{i gamma log x} on the prime side; GG's renormalized
survivor is the sigma = 0 shell). Pre-registered channels:

```text
CHANNEL RAW (the trivial channel, sanity only): F_raw(tau, X) =
    n_-(M(w,X) + tau I) - n_-(surrogate at same X). At tau = 0+ and
    Lorentzian signature this is just the atom-count difference
    Pi(X) - Pi~(X): any dimension count "sees the zeros" the way
    pi(x) does. A gamma-peak here is NOT a hit; it is the pipeline
    sanity check (if even this channel has no power, the probe is
    resolution-limited and the verdict is INCONCLUSIVE-POWER, not s-b).

CHANNEL INT (the decision channel): the dimension-NORMALIZED flow
    F_int(tau, X) = n_-(M + tau I) - (N(X) - 1) * f~(tau, X), where
    f~ = surrogate fraction of loci above tau at matched dimension.
    This subtracts the trivial counting channel; what remains is the
    INTERNAL spectral shape of the loci. WKB heuristic (recorded at
    registration time, not assumed): the level counting at tau > 0
    weights atom x = log n by ~ sqrt(x) e^{-x/2} - the n^{-1/2}
    EF-shell weighting - so a surviving gamma signal here would mean
    the signature flow transmits the sigma = 0 shell NONTRIVIALLY
    (beyond counting); its absence means the spectral functional
    smooths the oscillations away.

CHANNEL STATIC (descriptive): frozen loci t_k(w, X) at fixed X vs
    rank-matched surrogate loci; residual r_k; coherence check
    (r_k/|t_k| ~ const would mean the loci shift coherently and all
    zero content lives in the X-flow, reducing STATIC to INT).
```

READINGS (decision table, fixed in advance; z = normalized spectral
amplitude at gamma vs background median/MAD over gamma in [5, 60],
computed only after the freeze):

```text
(s-a) HIT: CHANNEL INT prime-carrier z >= 4 at >= 3 of the first 5
      gammas, AND the same statistic on the Epstein carrier and the
      jitter control stays z < 3 there (discrimination): first
      integer object touching the zeros beyond counting; escalate to
      the G-INT2 comparison identity.
(s-b) CLEAN NO-GO (full value): CHANNEL RAW sanity passes but
      CHANNEL INT prime z < 3 across the first 5 gammas, and the INT
      residual is noise-grade or log p-comb-grade: the integer
      signature flow at this level is supply-blind beyond the trivial
      dimension count; record which structure is missing
      (effectivity/h^0).
(s-c) PARTIAL: anything between - e.g. INT carries the density/li
      layers (slow trends separating the li-surrogate from a cruder
      PNT surrogate) but no gamma oscillations, or 1-2 isolated gamma
      peaks: measure exactly which EF layer the integers see.
FAIL-CLOSED: if Epstein/jitter ALSO show zeta-gamma peaks in their
      INT channels, the statistic measures geometry, not arithmetic:
      any prime-carrier hit is DEMOTED to artifact and the verdict
      reverts to no-go-with-flag (gate II5).
```

## 2. PRE-REGISTERED SCAN GRID AND METHOD (G-INT6: the grid is a choice - logged)

```text
weights        w in {1, 2, 4, 8}; full X-flow at w in {1, 4};
               static loci at all four w.
X              flow: 480 log-uniform samples, X in [200, 10^4]
               (principal submatrices of the X = 10^4 matrix);
               static: X in {10^3, 10^4} all w; X = 3*10^4 at w = 1
               (N ~ 3500, float-grade). X = 10^5 flow is OUT OF
               BUDGET (recorded as a limit, not silently dropped).
t              the loci are the full spectrum, so every t is covered;
               decision panel tau(w) = log2 + {0.3, 1, 3} w (fixed in
               the witness docstring BEFORE the first run, with the
               design reason: the loci bulk sits at log2 + w mu_k with
               mu_k the MIN-kernel spectrum, so tau <= log2 only
               re-counts the dimension; the panel probes the WKB
               regime k ~ S sqrt(w/(tau - log2))/pi); RAW sanity at
               tau = 0+; W-window edges reported at the static
               instances.
surrogate-A    (prime carrier only, density diagnostics): smooth
               prime-power count Pi~(x) = sum_{m<=16} li(x^{1/m}),
               atoms at Pi~ = k - 1/2; PLUS the cruder PNT surrogate
               (li(x) -> x/log x) to separate density layers.
surrogate-B    (ALL carriers, the discrimination-fair smooth model):
               Gaussian-smoothed counting staircase in L = log n,
               sigma_L = 0.4 (suppresses frequency gamma by
               e^{-gamma^2 sigma^2/2}, i.e. kills gamma >= 14 by
               > e^{-15}, keeps all density layers); surrogate atoms
               at smoothed-count = k - 1/2; edge buffer: atoms
               enumerated to X e^{1.2} for the smoothing tail.
carriers       PRIME: prime powers <= X (the object). EPSTEIN:
               distinct represented values of x^2 + 5y^2 (AA's
               carrier; norm-Gram formable, Lorentzian per AA E1; no
               multiplicativity). JITTER: Poisson resample from the
               smoothed prime density, seed 20260610 (noise floor).
               DH-style perturbed ladder: NOT FORMABLE as a degree
               multiset (DH coefficients are not nonnegative counts;
               no atom monoid) - recorded, consistent with AA/GG
               precedent that DH dies at the carrier level.
spectra        F(L) resampled on a uniform L-grid, detrended by its
               own sigma = 0.4 Gaussian smoothing, Hann-tapered,
               amplitude spectrum on a fine gamma grid; z-scores
               against median/MAD of the gamma in [5, 60] background
               (probe gamma's +-1.5 band excluded from background).
               Resolution: Delta L = log(10^4/200) ~ 3.9 ->
               d(gamma) ~ 2pi/3.9 ~ 1.6; first gammas separable
               (gaps ~ 7).
exactness      atom data, factorizations, p^a != q^b, norm masses:
               integer-exact. Decisive small instances: certified arb
               LDL inertia (prec 300, reversed order, AA's method) at
               N <= 220, cross-checked against numpy eigh signatures
               (must agree exactly). Large-N spectra: numpy eigh,
               FLOAT-GRADE (flagged; entries are logs of integers,
               rel error ~ 1e-16; loci used only through window-scale
               statistics, never through sign decisions tighter than
               1e-8 - any such decision would be gated to arb).
freeze         sha256 of all computed series/spectra printed BEFORE
               the first import of zeta zero data; hash logged in
               sec 4.
```

Evaluation rules fixed: gates II1 (assembly exact), II2 (certification
+ n_+ <= 2 + Lorentzian census), II3 (grid computed + freeze logged),
II4 (post-freeze comparison computed), II5 (discrimination guard),
II6 (verdict printed per the sec-1 table; the verdict value is not a
pass/fail - structural gates are). Exit 0 only if II1-II5 pass.

---- verdict sections written after the runs ----

## 3. VERDICT: s-c, EXACTLY THE REGISTERED DENSITY/OSCILLATION SPLIT -
## the integer signature flow sees the EF's density tower and is blind
## to the oscillatory (zero) layer; the controls discriminate

ALL PASS (8/8 gates), exit 0. FREEZE sha256 = 25653c15ab1775c020c824a6
17adc9183c9f8ade64cf41416bb6fd5d1b2ca48e - IDENTICAL across runs 2-4
(the pipeline is deterministic; sec 5 has the engineering record).
Measured decision numbers, exactly as the registered table consumed
them:

```text
SANITY (raw/trivial channel, prime, w=1, tau=0+): z at gamma_1..5 =
    8.3, 3.9, 5.0, 3.9, 3.8 - the dimension count Pi(X) sees the first
    zeros, as any prime-counting staircase does; the pipeline has
    power.  Epstein raw channel against ZETA gammas: z <= 1.5 (its
    dimension count carries NO zeta content); jitter raw z <= 2.2.
    The gamma peaks are arithmetic, not pipeline geometry.
INT (decision channel, dimension-normalized internal loci structure):
    prime w=1: z = 0.3, 1.1, 0.9, 1.1, 1.3 at gamma_1..5 (max 1.7 over
    the first 12).  ZERO hits (threshold 4).  w=4 row IDENTICAL to
    w=1: the w-dial is inert (rank-one interlacing pins the panel
    counts; measured: equal arrays) - the loci family is ONE
    w-rescaled object; the only real dial is X.
DENSITY: max|D_int| = 2.63 >= 2: the dimension-normalized loci
    counting SEPARATES the li-density model from the crude x/log x
    model (dimension-level separation 168 atoms; spectral-level 2.6
    counts).  The loci see the smooth density tower beyond mere
    dimension.
CONTROLS (II5 PASS): epstein INT z <= 1.1, jitter INT z <= 2.2 at the
    first 5 gammas - clean as registered.
VERDICT (registered table): s-c - the jump loci carry the density/PNT
    layer of the EF and NOT the oscillations.
```

## 4. WHAT THE FLOW MEASURED STRUCTURALLY

1. GLOBAL LORENTZIAN: n_+(M(w,X)) = 1 at EVERY flow sample, carrier,
   weight, and static instance up to N = 3321 (X = 3*10^4); n_+ <= 2
   is EXACT (M + tI = U B U^T - (w MIN_l + (log2-t)I), U = [D, 1], B
   of signature (1,1), plus Weyl) - the glued all-places family keeps
   the Castelnuovo shape W/AA certified per place.  arb ball-certified
   at 5 instances (N <= 131, prec 300, every pivot).
2. THE JUMP-LOCI ACCUMULATION POINT IS log 2 - THE CC-NORM CONSTANT,
   NOT A ZERO POSITION: median locus 0.6944 (X = 10^4) -> log 2 =
   0.69315; window edge t_hi = -lambda_2 = 0.6940, 0.6932, 0.6932 at
   X = 10^3, 10^4, 3*10^4.  The global t-window of the (1, N-1)
   signature is asymptotically (-lambda_1, log 2): n-stable, contains
   0 with margin -> log 2 (W's per-place window globalizes; the edge
   is set by the norm constant - arithmetic-only, reading (s-b) for
   the loci POSITIONS themselves).
3. WKB LAW OF THE COUNTING: n_-(tau) at tau = log2 + a*w scales as
   sqrt(1/a) (measured 46/25/14 at a = 0.3/1/3; ratios 1.84, 1.79 vs
   sqrt ratios 1.83, 1.73) - the level counting is the Sturm-Liouville
   count of the MIN kernel on the degree density.
4. THE BOUNDARY, measured + design-grade explanation: the level
   counting weights the atom at x = log n by ~ sqrt(x) e^{-x/2} (WKB
   density of the MIN kernel) - the EF's sigma = 0-shell CRITICAL
   weight.  Under it each zero's oscillation enters with BOUNDED
   amplitude ~ 1/(gamma sqrt(L)) ~ 0.02 counts (EF balance), while the
   density layers grow ~ e^{L/2}: the integer observable (quantization
   floor O(1) per jump) keeps the growing layers and buries the
   bounded one.  Consequence (design-stage derivation, not theorem):
   MORE X DOES NOT HELP - the oscillatory amplitude stays bounded
   while the floor stays O(1).  The blindness is structural to
   "signature of the norm-Gram", not a power shortfall of this scan.
   The cheapest discreteness-sees-spectrum claim dies (doc 32 PROBE 2
   "miss" reading), while the density tower IS transmitted (s-c, not
   s-b).
5. DISCRIMINATION: the construction is formable for Epstein (AA E1)
   and the probe runs on it; its loci flow shows NO zeta content in
   either channel - so the zeta-gamma content in the prime carrier's
   trivial channel is carried by the ARITHMETIC staircase, and the
   probe is not measuring geometry.  DH: not formable (negative
   coefficients, no atom multiset) - dies at the carrier, AA/GG
   precedent.

## 5. WITNESS-ENGINEERING RECORD (disclosed, CC/GG-style)

- Run 1 (dense eigh per flow sample) was KILLED for cost (~12 s per
  1000x1000 eigh on this host's LAPACK; 10+ h projected); it never
  flushed any output - no verdict was produced or seen.
- ENGINE SWAP (pre-verdict): the flow inertia is computed from the
  program's own W6d split via the Haynsworth quotient formula with a
  Sturm/LDL count on the tridiagonal MIN'^{-1} and two tridiagonal
  solves - O(N) per sample, 14 flows x 480 samples in ~8 s.  GATED:
  exact agreement with dense eigh on 16 random samples (all panel
  taus) and with dense + arb LDL on the 5 certified instances; 0
  dense fallbacks taken.
- Run 2 (first complete run): 7/8 - all channels, freeze, comparison,
  controls, verdict computed (s-c); the arb certification clause
  returned None (uncertifiable pivots).  Run 3: a precision-escalation
  attempt FAILED (wrong diagnosis).  Run 4: real bug - arb_gram built
  its input balls at the AMBIENT precision (53 bits) before the
  working precision was raised; building at the working precision
  certifies all 5 instances at prec 300 on the first try.  No gate
  semantics, channel, threshold, or grid changed at any step; the
  freeze hash and every decision number are IDENTICAL across runs 2-4.
- The tau-panel was refined (log2 + {0.3,1,3}w replacing the draft
  {0.25,1,4}w) BEFORE the first run, design reason logged in sec 2.

## 6. G-INT6 LEDGER

```text
input                        choices spent
family + Gram                0 (AA Thm AA.1 cross-place; W6d; GG's
                             unit-weight survivor normalization; unit
                             once = GG's continuum unit)
norm formula 2max(A,B)       0 (AA's representative generalizes;
                             integer-exact, II1)
grid, tau-panel, sigma=0.4,  registered BEFORE first run (sec 2 +
seed, thresholds, channels   witness docstring); never changed
zero data                    COMPARISON ONLY, post-freeze (II3/II4)
engine + arb repairs         numerical method only; gated by exact
                             agreement; verdict-invariant (sec 5)
```

## 7. HONEST LIMITS

- The INT channel's a-priori power against the oscillatory layer is
  LOW (sec 4.4: bounded amplitude vs O(1) quantization floor) - the
  no-go is for this observable class, with the boundedness argument at
  design grade (WKB + EF balance), not theorem grade.  A hit was
  detectable had the loci responded at the trivial channel's strength.
- Flow X <= 10^4 (static to 3*10^4); X = 10^5 flow out of budget.  By
  sec 4.4 the verdict is not expected to change with X; not witnessed.
- Large-N inertia is float-grade (validated exactly on samples,
  certified at N <= 131); no asymptotic claim (doc 13 wall).
- The STATIC channel was reduced to the witnessed static data (t_hi,
  lambda_1, median, census); the quantile-residual refinement was not
  run (descriptive only, no decision weight).
- Epstein is tested for zeta-blindness only; its OWN L-function zeros
  were not used as a positive control.  Jitter is one seed.
- No spectrum-level object; no RH input anywhere; the EF enters only
  as the frozen comparison.

## 8. HAND-OFF (doc 32 PROBE 2 answer)

The integer signature flow of the certified Lorentzian count-pairing
family does NOT see the zeros: the jump loci accumulate at log 2 (the
norm constant) and their internal flow carries exactly the EF's smooth
density tower (li-layer separation witnessed) and nothing of the
oscillatory shell, with the suppression mechanism identified (critical
sigma = 0-shell weighting + integer quantization).  The cheapest
discreteness-sees-spectrum claim is DEAD at this level, as a
structural matter rather than a power shortfall.  What an integer
object would need to touch the zeros: an observable whose zero
response GROWS with the family - the effectivity/h^0 count (doc 32's
ROAD terminus), not the signature.  PROBE 2 closes; G-INT2 escalation
not triggered.

## 9. Witness (exit-gated, lead can rerun; ~50 s)

    python3 -m scripts.numerics.witness.prime_int_ii_signature_flow

Inherited, rerun before work: prime_int_gc_k3_barnes_rank (ALL PASS),
prime_cc_thh_norm_filtration (ALL PASS).
