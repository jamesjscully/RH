# 135 - The phase certificate collapses: arg m positivity is the zero cross-correlation / Weil positivity, RH-equivalent

Status: no-go + characterization, 2026-06-16. Fifth post-reset cycle. It
closes the single surviving frontier object doc 134 sec 6 isolated --
PHASE-CERT, the Euler-borne argument-principle certificate for arg m -- by
showing it is NOT a new door: it reduces literally and term-by-term to the
doc-13 zero cross-correlation (= Weil positivity), it holds verbatim for the
genuine Davenport-Heilbronn function (RH-silent) or detects DH's off-line
zero only at RH-strength, and no strictly-weaker Euler-borne phase statement
escapes. With this, BOTH analytic faces of the missing object (modulus, doc
132/133; phase, doc 134/135) are RH-equivalent, and the program residue
reduces to a single construction: build End(S^2/Z) with a positive Rosati
involution.

Witnesses (lead-reran this cycle, all exit 0):
`probe_pb_dh_phase_killtest` (GENUINE DH, rho0=0.8085+85.699i: FE_ok=True;
on-line min w_DH=0.6456>0 verbatim for the RH-false DH => FE-shared,
RH-SILENT; winding around rho0=+1 at Re=0.8085 off-line, detection needs the
location => RH-strength; DH prime side has negative / off-prime-power coeffs
=> no unconditional escape; verdict (a)+(b), no escape),
`probe_pa_argm_to_tau` (the phase functional int w g reduces to the Weil
explicit formula sum_gamma g(gamma)==arch(g)-prime(g) to rel 5e-12, three
independent computations; dual-positive zero side == 2 sum khat^2 = the
doc-13 r self-norm; escape=False; DH detection lives only in the zero-side
difference, archimedean cancels),
`probe_pc_weaker_phase_escape` (phase firewall: C1/C3 modulus-in-disguise,
C2 FE/arch-shared RH-neutral, C4 positive-proportion is a partial count that
tolerates an off-line set; no candidate is weaker + Euler-borne + DH-detecting),
`phase_winding` (w = w_arch - w_zeros; total winding zeta 12.96 vs off-line
14.92, Delta 1.96 -- count sees the zero; density_discriminates=False, w>=0
on the line for BOTH; w_arch / Gamma_R phase DH-shared, not Euler-borne),
`off_diagonal` (the DH-detecting object is the Weil/Li Gram: PSD on true
zeros, INDEFINITE with a planted off-line zero = RH itself),
`explicit_formula` (zeta prime side = von Mangoldt to 2.5e-60, nonneg,
prime-power-supported; DH negative / off-prime-power -- a MODULUS-side
discriminator, the wrong half for a phase certificate).

## 1. Purpose

Doc 134 sec 6 narrowed the program's UNKNOWN residue to ONE named,
zero-free, attackable object: PHASE-CERT -- an Euler-borne
argument-principle positivity for arg m (the winding / the line Re s = 1/2),
NOT a modulus / norm-square. The banked unconditional positivity (sym^2
|h|^2) controls the modulus / edge, the wrong half (KILL-REAL.2); PHASE-CERT
must control the phase from prime data directly. This doc attacks PHASE-CERT
head-on and asks: is the argument-principle / winding positivity a genuinely
new handle on arg m, or does it reduce to the banked conserved difficulty
(doc 13 zero cross-correlation / doc 09 R1 zero-side oscillation)?

## 2. Covered Class

```text
- any Euler-borne argument-principle / winding positivity for arg m: the
  winding density w(t) = -(1/2pi) d/dt arg S(1/2+it), S(s)=Lam(2s-1)/Lam(2s),
  one-sided winding w>=0 on the line, the signed/total winding (= zero count);
- averaged-argument statements: Littlewood int_0^T S(t)dt = O(log T), and any
  S_1(T) / mean-argument bound;
- Lindelof-on-average / 2k-th moment phase statements;
- positive-proportion-on-the-line statements (Selberg / Levinson / Conrey
  mollifier counts) read as a phase / resonance-location positivity.
```

It does NOT cover (sec 6) the construction of End(S^2/Z) with a positive
Rosati involution -- the single remaining non-analytic target this no-go
hands off to.

## 3. Lemma

```text
PHASE-CERT REDUCTION. Let w(t) = -(1/2pi) d/dt arg S(1/2+it) be the winding
density and g an even Schwartz test. Then:

(L1) [explicit-formula identity] the zero-counting part of int w(t) g(t) dt
     equals the Weil explicit formula
        sum_gamma g(gamma) = arch(g) - prime(g),
     arch(g) the Gamma_R archimedean phase (Euler-FREE, DH-shared, RH-silent)
     and prime(g) = sum_n Lambda(n) g-hat(log n) the SIGNED von-Mangoldt sum.

(L2) [no Euler-borne lower bound] prime(g) is order-1 and takes both signs;
     arch(g) is DH-shared. Neither piece, alone or summed, has an Euler-borne
     sign that forces int w g >= 0. Manifest positivity of the zero side is
     available ONLY through a dual-positive test g-hat = k-hat^2, for which
     the zero side IS 2 sum_{gamma>0} k-hat(gamma)^2 = the doc-13 tracking
     residual r (self-norm). Hence int w(autocorr) >= 0 <=> r >= 0 for all
     tests <=> uniform tau < 1 (doc 13) <=> RH.

(L3) [DH dichotomy on the genuine function] for the genuine DH function with
     proven off-line zero rho0: (a) w_DH(t) >= 0 holds verbatim on Re s = 1/2
     (FE / archimedean-shared) -- RH-SILENT; (b) the only phase object that
     sees rho0 is the argument-principle winding COUNT, which flags 'off-line'
     only by supplying the location Re(rho0)/2 != 1/4 = the zero = RH-strength;
     (c) DH's prime side is not a positive prime-power object (no Euler
     product), so the prime-borne phase is signed and forces nothing
     unconditionally -- NO escape.

Therefore PHASE-CERT is RH-EQUIVALENT: it holds for DH (RH-silent) or detects
DH only at RH-strength; it is the zero cross-correlation in winding-density
clothing.
```

## 4. Proof

```text
(L1) phase_winding decomposes w = w_arch - w_zeros: w_arch = (1/pi) d theta/dt
  is the Riemann-Siegel / Gamma_R phase, monotone, positive, Euler-FREE, and
  reproduced by the archimedean-only scattering S_inf (carried verbatim by DH,
  same Gamma factor). probe_pa_argm_to_tau verifies the identity
  sum_gamma g(gamma) == arch(g) - prime(g) to rel 5.3e-12 / 2.7e-12 / 1.3e-12
  across three test bumps from THREE independent sources (FLINT zeros,
  archimedean phase derivative, von-Mangoldt sum). An independent re-derivation
  with disjoint code (textbook Riemann-Weil factor Omega(t) =
  (1/2pi)[Re psi(1/4+it/2) - log pi] via mpmath digamma) reproduces it to
  rel ~1e-16 -- ruling out shared-code circularity. This is doc 09 sec 6''''
  exactly: (1/2pi) int |h-hat|^2 D_R = 2 sum_{gamma>0} h-hat(gamma)^2.

(L2) probe_pa [3] reports escape=False: prime(g) values -0.52/-0.18/-0.34 are
  comparable in magnitude to arch 0.48/0.96/0.66 and oscillate in sign, so the
  DH-shared archimedean piece cannot force the sign without the zero sum. The
  dual-positive zero side reduces algebraically to a manifest sum of k-hat^2
  (probe_pa [2], rel exactly 0.0; magnitudes degenerate by underflow but the
  identity g-hat=k-hat^2 is exact). off_diagonal [B] independently corroborates:
  the Weil Gram is PSD on true zeros (min eig -3.4e-16, Cauchy-Schwarz holds)
  and INDEFINITE with a planted off-line zero (min eig -2.29, worst minor
  -0.84) -- PSD-ness <=> all gamma real <=> RH = doc-13 uniform tau<1.

(L3) probe_pb_dh_phase_killtest builds the GENUINE DH function
  f_DH(s)=5^{-s} sum a_r zeta(s,r/5) (odd character mod 5), verifies the FE
  |Lam_DH(s)/Lam_DH(1-s)|=1.0 to 1e-12 (FE_ok=True), and verifies by argument
  principle that rho0=0.8085+85.699i is a real off-line zero (winding +1). (a)
  on-line scan: min w_DH=0.6456>0 on the band straddling Im(rho0)/2=42.85; a
  wide [5,95] sweep (this cycle's adversarial verification) gives 0 negative
  samples, global min 0.298>0 -- w_DH>=0 holds verbatim for the RH-FALSE DH.
  A single off-line denominator zero at Re=0.404 produces a POSITIVE Lorentzian
  bump on the line (w=+1.66 at t=42.85), not a negative one: the backward
  winding (w=-242.6 at Re=0.404) lives OFF the line, only its positive tail
  reaches Re=1/2. So (a) is FE-shared, RH-silent. (b) detection of rho0 requires
  evaluating at Re=0.404 = supplying the location = the zero = RH-strength.
  (c) explicit_formula: DH c_DH(n) has negative coeffs and off-prime-power
  support [6,12,14,18,21,24,26,28], so the DH prime phase is signed, no
  Euler-borne lower bound, no unconditional escape.

PHASE FIREWALL (probe_pc, sec 6 disposal of weaker statements). Every
genuinely-weaker Euler-borne phase statement falls in one of three RH-neutral
buckets: (M) MODULUS-IN-DISGUISE -- Littlewood S_1(T) = -(1/pi) int_{1/2}^inf
log|zeta(sigma+iT)| d sigma + O(1) is the harmonic conjugate of log|zeta|, and
|zeta|^{2k} moments are modulus by definition: both are the KILL-REAL.2 wrong
half; (B) FE/ARCH-SHARED -- one-sided w>=0 on the line holds for BOTH zeta
(min 8e-4) AND the off-line plant (min 0.042), density_discriminates=False, and
the dominating w_arch is DH-shared; (K) PARTIAL COUNT -- positive-proportion
(Levinson) is genuinely weaker, Euler-borne, and location-flavoured, but it is
the argument-principle integer count (doc 16 R-SQ) that lower-bounds on-line
cardinality while tolerating a positive-density off-line exceptional set; it
detects no SPECIFIC DH zero, and forcing proportion->1 IS RH. No candidate is
simultaneously weaker + Euler-borne + DH-detecting-through-the-phase.
```

## 5. The unification: both analytic faces are now RH-equivalent

```text
The post-reset cycles are faces of ONE missing object -- the positive-Rosati
correspondence algebra End(S^2/Z) (Connes-Consani C x C / scaling-site
Jacobian):

  doc 130       SECOND EVALUATION  the odd slot is self-supplied without a
                                   properness / Poincare-duality truncation;
  doc 132/133   RADIUS (MODULUS)   the even split |alpha|=|beta| is the acting
                                   map's own modulus; the EDGE / FE is free;
  doc 134       REALITY (PHASE)    theta F theta = F* is arg m / the line;
                                   positivity-by-axiom = RH (KILL-REAL.1);
  doc 135       PHASE-CERT         the argument-principle positivity for arg m
                                   IS the zero cross-correlation / Weil
                                   positivity; holds for DH or RH-strength.

Doc 134 left PHASE-CERT as the one analytic door still ajar. Doc 135 shuts it:
in EVERY face the FE / edge / modulus / relation half is FREE and DH-shared
(RH-silent), and the RH content is the split / phase / positivity half, which
in the phase face is provably the doc-13 zero cross-correlation. Both analytic
faces of the missing object -- modulus (132/133) and phase (134/135) -- are
RH-equivalent. There is no analytic shortcut on either face. The program's
whole residue is the ONE algebra End(S^2/Z) with positive Rosati involution
F^dag = (deg) F^{-1}, present over F_q (Frobenius) and absent over Z.
```

## 6. Surviving Escape

```text
The analytic escapes are CLOSED. What survives is NOT an analytic certificate
but a CONSTRUCTION:

  END(S^2/Z). Build the self-product correspondence algebra End(S^2/Z) (the
  Connes-Consani C x C / scaling-site Jacobian) carrying a POSITIVE Rosati
  involution F^dag = (deg) F^{-1} -- the operator-side object whose self-norm
  is the sum over zeros (RH). This is the common target of all four faces; it
  is geometric / arithmetic, not a phase or modulus inequality on the line.

The ONLY residual analytic seam (not an escape, a standing open question): a
hypothetical LEVEL-3+ Euler-borne phase functional detecting DH off-line
without routing through the signed prime phase or the integer count. No
constructed candidate occupies it; probe_pc and probe_pb rule out all level-2
(mollified-linear) and local phase objects. Per doc 134 sec 6 this is a
relocation of the wall, not an unconditional impossibility theorem -- but it
is the program-wide frontier, not a defect specific to the phase face.
```

## 7. Kill Conditions

```text
KILL-PHASE.1 holds-for-DH (RH-silent)
  the phase positivity holds verbatim for the genuine RH-false DH on the line
  (FE / archimedean-shared). The on-line winding density w_DH(t)>=0 (min 0.298
  over [5,95]) is the positive Lorentzian tail of an OFF-line resonance.
  Witness: probe_pb_dh_phase_killtest (a_holds_for_DH=True), phase_winding
  (density_discriminates=False).

KILL-PHASE.2 zero-cross-correlation-in-disguise (RH-equivalent)
  the certificate's only route to manifest positivity is a dual-positive test,
  whose zero side IS 2 sum k-hat^2 = the doc-13 tracking residual r; its
  nonnegativity for all tests is uniform tau<1 = RH. Witness:
  probe_pa_argm_to_tau (dual-positive == 2 sum k-hat^2; escape=False),
  off_diagonal (Weil Gram PSD on zeros, indefinite off-line).

KILL-PHASE.3 modulus-for-phase / FE-shared background
  the statement is an averaged / moment argument (Littlewood S_1 = harmonic
  conjugate of log|zeta|; |zeta|^{2k}) controlling the modulus / edge, OR it
  rests on the dominating w_arch = Gamma_R phase, DH-shared and Euler-free.
  Either way RH-silent for arg m. Witness: probe_pc_weaker_phase_escape (C1/C3
  modulus-in-disguise, C2 FE/arch-shared), explicit_formula (Euler fingerprint
  is a MODULUS-side discriminator).

KILL-PHASE.4 partial-count evasion
  the statement lower-bounds the on-line count (positive proportion) while
  tolerating a positive-density off-line set; it detects no specific DH zero
  and forcing it to full measure IS RH. Witness: probe_pc (C4 PARTIAL-COUNT).
```

Do not apply this no-go to a construction of End(S^2/Z) with a positive Rosati
involution (sec 6) -- that is the surviving, non-analytic frontier.

## 8. Board

```text
Phase certificate, cycle 5:
  PHASE_CERT_COLLAPSES__ARG_M_POSITIVITY_IS_ZERO_CROSS_CORRELATION.
  The argument-principle / winding positivity for arg m reduces term-by-term
  to the Weil explicit formula (probe_pa, rel 5e-12, independently ~1e-16):
  arch (Euler-free, DH-shared, RH-silent) minus prime (signed, no lower bound),
  manifest positivity only via the doc-13 zero cross-correlation r = RH. On the
  GENUINE DH function (probe_pb, exit 0) w_DH>=0 holds verbatim (RH-silent);
  rho0 is seen only by the count at its off-line location (RH-strength). No
  strictly-weaker Euler-borne phase statement escapes (probe_pc firewall).
  Adversarial verification 0/4 refuted: the RH_EQUIVALENT verdict survived.

Unification (both analytic faces closed):
  modulus (docs 132/133) and phase (docs 134/135) are BOTH RH-equivalent.
  In every face the FE / edge / modulus is free and DH-shared (RH-silent);
  the RH content is the split / phase / positivity. No analytic shortcut on
  either face.

Program residue (the single remaining target):
  build End(S^2/Z) with a positive Rosati involution F^dag = (deg) F^{-1}
  (Connes-Consani C x C / scaling-site Jacobian) -- a geometric / arithmetic
  construction, NOT a phase or modulus inequality. Present over F_q, absent
  over Z.

Next valid work:
  construct End(S^2/Z) with the positive Rosati involution, with a runnable
  witness. Do NOT propose: an argument-principle positivity for arg m
  (KILL-PHASE.1/2), a modulus / moment / averaged-argument certificate
  (KILL-PHASE.3), or a positive-proportion count (KILL-PHASE.4).
```
