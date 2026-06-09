# 10 - The realization spec (post-R1 front)

Status: specification, not theorem. This converts the R1 findings (09) into the precise
construction target. Per 09 section 6'''', the phenomenology phase is complete; what
remains is to BUILD one object. This document fixes what that object must be and what
it must not be.

## 1. The object

A passive (contractive) realization of the nested Prime-Toeplitz family:

```text
For every 0 < L < R, exhibit the transfer operator K_{L,R} = A^{-1/2} C D^{-1/2}
as the transfer function of a dissipative state-space system whose energy-balance
identity is the explicit formula, constructed from PRIME-SIDE data only.
Passivity of the system  =>  ||K_{L,R}|| <= 1  =>  the Schur target  =>  RH (doc 00).
```

KYP equivalence: contractivity <=> existence of a PSD storage Pi satisfying the chain
LMI. The realization is what SUPPLIES Pi. The first probe (TODO R-KYP) showed Pi is
genuinely path-dependent (the frozen-response closed form fails by O(debt)) - the
state must carry the evolving response map X_j, not just the future residual.

## 2. What the realization must encode (each item now individually evidenced)

```text
E1. Globality in the places. Every place and every prime-power atom is
    individually load-bearing (6'); subset realizations cannot exist. The system
    must be built on the FULL free abelian semigroup N^x ~ multiplicative
    structure of the integers, not on local factors composed one at a time.
E2. The critical KMS weight. Atom weights 2 Lambda(n) n^{-1/2} are the beta=1/2
    KMS weights on that semigroup; positivity fails for beta != 1/2 in BOTH
    directions (6'). The realization lives exactly at the critical temperature -
    any construction with an adjustable inverse-temperature knob that works in
    an open interval is therefore wrong (it would over-prove).
E3. The archimedean supply. W_inf alone funds positivity only to gmax ~ 2.3
    (6'''); past that the system is energy-deficient archimedean-side and the
    prime interference is the only source of the missing positivity. The
    realization's supply rate is the digamma density; its interconnection must
    EXTRACT positivity from the atom phases (equidistribution of {log p},
    resonance dictionary 6'').
E4. Exactness. Margins are e^{-1.5R} below the natural scale of every term
    (Finding 1); the realization's energy identity must be exact algebra - any
    construction whose passivity proof needs an estimate with slack dies.
```

## 3. What the realization must NOT be (graveyard guards, each with its kill)

```text
G1. A de Branges chain whose structure function is fitted to zeta: Conrey-Li.
G2. The Connes trace / zero-side spectral realization: circular (AGENDA).
G3. A composition of one-place or finitely-many-place passive systems: refuted
    2026-06-09 (prime_single_place_passivity.py).
G4. A smooth-density (PNT-surrogate) system with atoms as perturbation:
    permanently indefinite (prime_margin_law.py).
G5. Anything whose mechanism survives Davenport-Heilbronn coefficients or
    beta != 1/2 weights: over-proves, hence wrong (kill-test discipline).
```

## 4. The sharpest available framing

The Bost-Connes system is the canonical C*-dynamical system on exactly the E1 semigroup
with exactly the E2 critical line: its partition function is zeta, beta=1 is its phase
transition, and the Weil weights n^{-1/2} sit at beta=1/2 INSIDE the critical region
(no KMS state, type III behavior) - which matches the project's finding that the
positivity at beta=1/2 is not a state-positivity of the BC system itself (worker A:
real-axis KMS is RH-silent) but something sharper. The spec question, stated once:

```text
What completion / dilation of the BC-type semigroup structure at beta=1/2,
coupled to the digamma supply through the Sonin support filtration,
has the explicit formula as its exact energy-balance identity?
```

The support filtration (the only admissible induction coordinate, 6') plays the role of
TIME for the dissipative system; the chronological cells are its discrete time steps;
the Riccati identity (05) is its exact local energy ledger; the storage Pi is its
internal energy. Every piece of the proof track built so far is a component of this
one system. What does not yet exist is the system itself.

## 5. First falsifiable sub-targets

```text
S1. Construct the state space for the FINITE chain explicitly: the state at
    step j must determine (S_j, X_j) and be updated by cell data alone. Measure
    its minimal dimension along the ladder - if it grows like the full window
    dimension, the "system" view adds nothing (fail-closed); if it stays small
    or has multiplicative structure, that structure IS the realization's germ.
S2. Test E2 sharply in the realization frame: the BC algebra has a canonical
    dilation at beta=1/2 (the GNS/Toeplitz dilation of the semigroup of
    isometries V_n with weights n^{-1/2}). Compute whether the V_n-dilation
    compresses to the witness atoms exactly (the atom B_{log n} should be
    <h, (V_n + V_n^*) h>-shaped on the Sonin window). If yes, the witness
    family literally IS a compression of a semigroup-isometry system and
    passivity has a candidate home; if the compression has a defect term,
    that defect is the next object to control.
S3. O3/O4 paper work (doc 00) continues in parallel - the reduction must be
    certified before any realization claim can matter.
```

## 6. S2 outcome (2026-06-09, fail-closed)

The exact even-model decomposition (verified to grid error 4e-4 per atom):

```text
<h, tau_U h> = 2 corr(U) + conv(U),
corr(U) = int_0^inf h_+(v+U) h_+(v) dv     (half-line shift/semigroup channel),
conv(U) = int_0^U  h_+(v) h_+(U-v) dv      (corner/autoconvolution channel),
and for U > sup supp h_+ the atom is PURE corner (correlation empty) - the
doc-07 edge-convolution regime is exactly the corner channel.
```

Measured on the ladder (gmax 2.30 -> 4.96):

```text
eigmin(W - P_shift):  -0.07 -> -0.29   (indefinite everywhere tested)
eigmin(W - P_corner): -0.41 -> -1.61   (indefinite everywhere tested)
eigmin(W - P_full):   +2.3e-2 -> +2.9e-4  (positive)
corner share of edge atoms (log n >= gmax/2): 0.67 -> 1.000
```

Conclusions:

```text
- the hopeful version of S2 ("shift channel passive against W_inf, corner
  carries the knife-edge") is FALSE: the two channels repair EACH OTHER; the
  half-line semigroup part alone is not dominated. Add to the guards (G6):
  any realization treating the shift semigroup as a passive backbone with
  corner corrections dies the same way the subset inductions died;
- the corner channel - the autoconvolution (h_+ * h_+)(log n) sampled at prime
  powers with critical weights, a Beurling-Nyman-flavored pairing - is the
  DOMINANT channel for edge atoms, and the full-line even model is precisely
  the unitary dilation of the half-line system with the corner as boundary
  radiation. Passivity, if constructible, lives in the dilated (even, full-
  line) picture where translations are unitary, with W_inf as the supply.
  The collectivity results (6') say its energy balance cannot be localized in
  any sub-channel: place-global AND channel-global.
```
