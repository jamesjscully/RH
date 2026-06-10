# J - C5'' executed (first pass): the ladder data against the actual homotopy theory - transcription, reconciliation, corrections to doc 20, and the archimedean gap posed

Status: C5'' front (doc 20 sec 5), fresh-context pass 2026-06-10. Primary
sources fetched and archived (research/proof/refs/): Hesselholt
arXiv:1602.01980 (hesselholt2016-thh-hasse-weil.pdf, full text read);
Bhatt-Morrow-Scholze arXiv:1802.03261 (bms2018-thh-padic-hodge.pdf);
Deninger Invent. math. 104 (1991) 245-261 (deninger1991-gamma-factors.pdf,
GDZ scan, read page-by-page) and Invent. math. 107 (1992) 135-150
(deninger1992-local-l-factors.pdf, ditto); Connes-Consani arXiv:1211.4239
(connes-consani2012-cyclic-serre-local-factors.pdf); Connes-Consani
arXiv:2205.01391 and arXiv:2306.00456 (Riemann-Roch over S;
connes-consani-2022-riemann-roch-specZbar.pdf,
connes-consani-2023-riemann-roch-ring-Z.pdf);
Dotto-Moi-Patchkoria-Reeh arXiv:1711.10226 (THR); Rognes-Sagave-
Schlichtkrull arXiv:1410.2170 (log THH). New witness (ALL PASS, exit-code
gated): prime_int_deninger_convention.py.

HEADLINE (fail-closed finding, witness-verified): doc 20's W3 closed form
is NOT Deninger's identity. Deninger's regularized determinant of the full
ladder (Invent. 107, Prop. 2.3; the identity Hesselholt's Theorem A runs
on, via his Prop. 7.1 = Deninger [Motives PSPM 55] Cor. 2.8) is

    det_inf( (log q/2 pi i)(s - Theta) | full ladder ) = 1 - lambda q^{-s}

WITHOUT the self-dual prefactor. The prefactor q^{(s-alpha)/2} - doc 20's
"KMS-1/2 emergence" - is exactly the difference between two regularization
SCHEMES, and the homotopy-theoretic theorem that exists (Hesselholt) forces
the scheme WITHOUT it. KMS-1/2 is therefore still underived; it has moved
from "duality datum" to "global-duality datum that no local regularization
supplies". Details, transcription, and the archimedean survey below.

## 1. (a) Finite places: exact transcription of Hesselholt's mechanism

Hesselholt, "Topological Hochschild homology and the Hasse-Weil zeta
function" (arXiv:1602.01980v2; Contemp. Math. 708). For X smooth and
proper over k = F_q, q = p^r, W = W(k), iota: W -> C an embedding:

    Theorem A.  zeta(X, s) = det_inf(s id - Theta | TP_od(X) (x)_{W,iota} C)
                           / det_inf(s id - Theta | TP_ev(X) (x)_{W,iota} C),

Theta a C-linear graded derivation with q^Theta = Fr_q^* and
Theta(v) = (2 pi i / log q) v on the periodicity class v in TP_{-2}(k).

### 1.1 (i) Where the vertical ladder comes from - and what is choice

The chain, with his numbering:

- Tate spectral sequence (Section 1): E^2 = S{t^{+-1}} (x) pi_*(X) =>
  TP_{*}(X), periodicity operator t = c_1(O(1)) in H^2(P^infty(C), Z).
  Over a finite field t is an infinite cycle represented by a preferred
  class v in TP_{-2}(k) (Section 4): v = inverse of the image of the
  DIVIDED BOTT element alpha_eps = mu_eps^{-1} beta_eps in
  TF_2(O_C; p, Z_p) (Definition 4.1), descended to F_p (Proposition 4.2).
  This is where Bokstedt periodicity is load-bearing (his closing remark
  of the introduction: no divided powers on THH, unlike HH - "It is this
  basic periodicity theorem in conjunction with the cyclotomic structure
  ... that makes Theorem A possible").
- TP_*(k) = S_W{v^{+-1}} (Section 4), TP_0(k) = W via the explicit
  isomorphism tau; TP_*(X) is a 2-periodic graded W-algebra/module over
  it. So TP_{2m+j}(X) (x) C = (TP_j(X) (x) C) . v^{-m}, and a graded
  DERIVATION Theta acts on x v^{-m} by alpha - m (2 pi i / log q) if
  Theta(x) = alpha x. As m runs over Z this is the full vertical ladder
  alpha + (2 pi i / log q) Z. (Proposition 7.1 + Remark 7.2 then convert
  the ladder back: det_inf(s id - Theta | T_{2*+j}) =
  det(id - q^{-s} Fr_q^* | T_j).)
- The cyclotomic structure supplies the Frobenius: phi is meromorphic on
  TP (Section 2, Section 4), with phi(v) = p v (Proposition 4.2), and on
  the weight-w part of the Hodge spectral sequence Fr_q^* = q^w phi^r
  (end of Section 7).

HONESTY POINT (this is the precise boundary of "derived"): the homotopy
theory delivers the MULTIPLICATIVE data - the periodicity class v, the
finite-dimensional TP_j(X) (x) C, the linear Frobenius Fr_q^* with
Fr_q^*(v) = v. The vertical ladder appears in SOLVING q^Theta = Fr_q^*:
the log is multivalued with ambiguity group (2 pi i / log q) Z (Remark
7.2's exact sequence 0 -> (2 pi i/log q) Z -> C -> C^* -> 0), and
Hesselholt CHOOSES Theta(v) = (2 pi i/log q) v ("the most general
solution to q^Theta = Fr_q^*", intro). So: spacing 2 pi i / log p at
finite places = the character lattice of the orbit circle R/(log q)Z,
entering through the passage from the multiplicative Frobenius (which IS
homotopy-theoretic) to its additive infinitesimal generator (which is a
log choice). Doc 20's "compact orbit of circumference log p" is exactly
this, and it is as derived as it can be: the ladder is the fiber of
q^(-) over a Frobenius eigenvalue.

### 1.2 (ii) Where properness is used - all four entry points

- P-i (transfer/carrier): Section 3 - for PROPER f: X -> Y, right derived
  restriction gives f_*: THH(X) -> THH(Y) as cyclotomic THH(Y)-modules.
- P-ii (finite dimensionality = det_inf typechecks): Theorem 6.8 /
  Corollary 6.9 - the Hodge spectral sequence
  E^2_{i,j} = (+)_m lim_{n,F} H^{-i}(X, W_n Omega^{j+2m}_X) => TP_{i+j}(X)
  has finitely generated E^2 BECAUSE X is proper (Illusie, Prop. II.2.1,
  invoked verbatim in the proof); this feeds the Mittag-Leffler/strong
  convergence argument AND gives the degree-wise finite-dimensional
  TP_j(X) (x) C that Deninger's det_inf definition (his conditions (1)-(2),
  reproduced in Hesselholt Section 7) requires. Without properness the
  eigenspaces are infinite-dimensional and det_inf does not typecheck -
  this is doc 18/19's wall, on the nose.
- P-iii (comparison): Berthelot's cohomological interpretation
  [Berthelot, These, Thm. VII.3.2.3] - crystalline cohomology of proper X
  is finite over W and computes zeta(X, s). The conjugate spectral
  sequence (Theorem 5.1/Corollary 5.2, Illusie-Raynaud III.2.2) again
  needs proper.
- P-iv (smoothness, separately): Lemma 6.1 / Prop. 6.6 ("analogue of
  analytic continuation") need smooth of finite relative dimension; the
  descent results (Prop. 6.4, Remark 6.5) are only known for smooth X.

So in doc 19's decomposition: Hesselholt uses PF (finiteness) at P-ii/P-iii
and the module/transfer structure at P-i; PD/PR/PS (duality, RR, sections)
do NOT appear - the zeta identity is supply-side only, poles included, and
the FF zeros enter through Berthelot's H^1 weights, imported whole. The
"properness = Poisson" face of doc 19 is not exercised by his proof at all;
properness enters as FINITENESS, not as duality.

### 1.3 (iii) The W3 question: discrepancy found and certified

Doc 20 W3 claimed prod_reg over the full ladder = 2 sinh((log p)s/2) =
p^{s/2}(1 - p^{-s}) "= Deninger's local-factor-as-regularized-determinant
identity". The actual identity in the sources:

- Deninger, Invent. 107 (1992), Proposition 2.3 (he flags it: "To me the
  following observation is a miracle"):
  det_inf((log q/2 pi i)(s - Theta) | L_lambda) = 1 - lambda q^{-s}.
  His convention (2.1)-(2.2): rotate the ladder real by the COMPLEX scale
  log q/(2 pi i); choose arg(z + a_nu) in (-3 pi/2, pi/2] for |nu| >> 0,
  i.e. arg(z - nu) = arg(nu - z) - pi on the negative half. His proof
  splits the rotated ladder into prod_{nu>=0}(z+nu) = sqrt(2 pi)/Gamma(z),
  the phase e^{-i pi (zeta(0,-z)-1)}, and prod_{nu>=1}(nu-z) =
  sqrt(2 pi)/Gamma(1-z), assembling to 2 i e^{-i pi z} sin(pi z) =
  1 - e^{-2 pi i z} = 1 - lambda q^{-s}.
- Hesselholt Section 7 reproduces Deninger's det_inf definition verbatim
  (branch -pi < Arg <= pi) and uses Proposition 7.1 (special case of
  Deninger PSPM 55 Cor. 2.8) + Remark 7.2: "In its most basic form,
  Deninger's formula expresses the inverse non-archimedean Euler factor
  1 - lambda q^{-s} ... as the regularized product of the s - alpha with
  alpha ranging over all solutions to q^alpha = lambda."

So doc 20's W3 closed form does NOT appear in Hesselholt or Deninger; what
appears is the SAME ladder with a DIFFERENT regularization scheme and the
value 1 - lambda q^{-s}, i.e. WITHOUT the KMS-1/2 prefactor.

Witness (prime_int_deninger_convention.py, gates G4, all to ~5e-16 rel):

```text
Deninger rotated convention (his proof steps, Hurwitz-assembled):
                          det = 1 - lambda q^{-s}        (NO prefactor)
vertical principal branch (-pi, pi], independent continuation:
                          det = 1 - lambda q^{-s}        (same value)
doc 20 symmetric scheme (pair n with -n, regularize moduli):
                          det = q^{(s-alpha)/2} (1 - lambda q^{-s})
ratio symmetric/Deninger  = q^{(s-alpha)/2}  EXACTLY (verified on a
                            (q, s, alpha) grid incl. complex s)
```

The discrepancy factor q^{z/2} = e^{(log q) z / 2} is the HALF-SUM of the
ladder - the vacuum-energy / Weyl-vector term (theta-regularized
Tr e^{-zH} with H = (log q)(N + 1/2) vs (log q)N). Two further hard
consequences:

- CONSISTENCY KILL: with the symmetric scheme, Hesselholt's Theorem A
  would be FALSE already for X = Spec F_q: TP_od = 0, TP_ev = the bare
  ladder, and zeta(Spec F_q, s) = 1/(1 - q^{-s}), not
  1/(q^{s/2}(1 - q^{-s})). The theorem that exists SELECTS the
  Deninger-arg scheme. (Equivalently: the q^{s/2} factors of the
  symmetric scheme do not cancel between od and ev - for a curve they
  would total q^{s(2-2g)/2 - ...} != 1.)
- RELOCATION: doc 20's reading "duality completion GENERATES the KMS-1/2
  normalization" must be downgraded to: "the full ladder TOGETHER WITH
  the conjugation-symmetric regularization scheme generates KMS-1/2; the
  arg-convention scheme on the same ladder does not; the existing
  homotopy-theoretic theorem uses the latter." The missing fourth
  realization input is again open - it is now precisely "WHO CHOOSES THE
  SCHEME", a global question (sec 4 below), not a local one.

### 1.4 (iv) H^0/H^2 and the pole factors

In Hesselholt's framework there is no H^0/H^2 as such; the crystalline
H^od/H^ev enter via the conjugate spectral sequence and land in
TP_od/TP_ev. For a curve, H^0 (Frobenius eigenvalue lambda = 1) and H^2
(lambda = q) sit in TP_ev and contribute det-factors 1 - q^{-s} and
1 - q^{1-s} to the DENOMINATOR - the pole ladders at s in 0, 1 +
(2 pi i/log q) Z. They are full ladders like everything else; nothing is
one-dimensional at finite level. The s, s-1 BARE factors are a feature of
the conjectural compactified object only: Deninger 1992, p. 146 (Spec Z
section): "H^0 and H^2 must be one-dimensional ... det_inf((1/2 pi)(s -
Theta) | H^i) = s/2 pi for i = 0, (s-1)/2 pi for i = 2. Note that
H^2 = H^0(-1) as C[Theta]-modules." So doc 20's "(c) rank factors = pi_0
excess" matches Deninger's normalization with the dictionary: pi_0 excess
<-> the lambda in {1, q} eigenclasses (finite level: full ladders) <->
one-dimensional H^0, H^2 = H^0(-1) with eigenvalues 0, 1 (compactified
level: bare factors s/2 pi, (s-1)/2 pi). The (2 pi)^{-2} prefactor of his
(3.2) is the 1/(2 pi) scale on the two rank factors.

## 2. (b) The integers: what TP(Z)/TC^-(Z) actually provides

Source: BMS, arXiv:1802.03261 (final, 88pp). All statements p-complete.

- Definitions/intro: TC^-(A) = THH(A)^{hT}, TP(A) = THH(A)^{tT}; for
  connective A, pi_0 TC^-(A; Z_p) = pi_0 TP(A; Z_p) via can; the
  cyclotomic Frobenius phi_p: THH(A) -> THH(A)^{tC_p} induces
  phi = phi_p^{hT} on TC^-; "this map is the ultimate source of the
  endomorphism phi" (Section 1.2).
- Perfectoid base (Theorem 1.6 + Section 6): for R perfectoid,
  pi_0 TC^-(R; Z_p) = A_inf(R); pi_* TP(R; Z_p) = A_inf[sigma, sigma^{-1}]
  (2-periodic; Tate spectral sequence degenerates); A_inf{1} :=
  pi_2 TP(R; Z_p) free of rank 1 (Breuil-Kisin-Fargues twist); phi on
  pi_{-2} becomes an isomorphism only after inverting xi. This is the
  exact mixed-characteristic analogue of TP_*(F_p) = Z_p[v^{+-1}], with
  W(F_p) replaced by A_inf and "phi(v) = p v" replaced by a xi-divisor.
- Motivic filtration (Theorem 1.12): for quasisyntomic A (Z_p qualifies:
  p-complete regular), Fil^n TP(A; Z_p) with
  gr^n TP(A; Z_p) = Dhat_A{n}[2n], where Dhat_A = gr^0 TC^- = gr^0 TP is
  NYGAARD-COMPLETED (absolute) PRISMATIC COHOMOLOGY, plus the descent
  spectral sequence E_2^{ij} = H^{i-j}(Dhat_A{-j}) => pi_{-i-j} TP(A;Z_p).
  So pi_* TP(Z_p; Z_p) is built from the cohomology of prismatic twists
  (the prismatic identification attributed via BMS Remark 1.3 to [BS];
  BMS 1802.03261 itself phrases Thm 1.12 via Nygaard-filtered Dhat) -
  a filtration, not a ladder; no closed form like W[v^{+-1}].
- Breuil-Kisin (Theorem 1.2 / Section 11, Theorem 11.2): the arithmetic
  refinement lives in RELATIVE THH: THH(-/S[z]), S = W(k)[[z]],
  theta-tilde(z) = pi, E(z) Eisenstein (for Z_p: E = z - p). For proper
  smooth formal X/O_K: RGamma_S(X) a perfect S-complex with phi-LINEAR
  (i.e. phi_S-semilinear) Frobenius, an isomorphism after inverting E.

LADDER READING: exists at F_q, fails at Z_p, for an identifiable reason.
At F_q the Frobenius phi^r = Fr_q^* is LINEAR over the constants
TP_0(F_q) = W ⊂ C: finite-dimensional C-spaces, eigenvalues, Deninger's
det_inf applies. Over Z_p the Frobenius is only phi-semilinear over the
base (S with phi(z) = z^p, or Dhat with its Frobenius), and NO finite
power of phi is linear - the "constants" of the prismatic base are F_p's
Witt vectors only after killing z, i.e. only at the special fiber. A
semilinear operator on an infinite S-module has no eigenvalue ladder; the
weight structure survives only as the motivic FILTRATION. So the precise
obstruction ladder for a global statement:

```text
O-b1 (p-completion): the entire technology is p-complete - Bokstedt
     periodicity, quasisyntomic descent, and above all the cyclotomic
     Frobenius phi_p: THH -> THH^{tC_p}, which exists for each finite
     prime and for nothing else. TP(Z; Z_p) ~ TP(Z_p; Z_p) sees one
     residue characteristic; there is no phi_infty.
O-b2 (semilinearity): eigenvalue ladders need Frobenius LINEARITY over
     embeddable constants (Deninger's conditions (1)-(2)); this holds
     exactly over finite fields, where q^Theta = Fr* can be solved. Over
     Z_p, det_inf does not typecheck even p-adically: the ladder is
     replaced by the Nygaard filtration. (Same lesson as 1.3: the
     regularized-determinant layer is ANALYTIC superstructure that the
     homotopy theory only meets over F_q.)
O-b3 (the missing archimedean corner): integrally, the arithmetic
     fracture square glues TP(Z) from prod_p TP(Z; Z_p) and a rational
     corner. Doc 18's invariant prod_reg_k |THH_{2k-1}(Z)| = sqrt(2 pi)
     = e^{-zeta'(0)} is a GLOBAL quantity: each p-completion sees only
     the p-part Z/p^{v_p(k)} of Z/k, and sum_k v_p(k) log p regularizes
     to the p-Euler-factor data, never to log sqrt(2 pi). The
     archimedean constant lives in the integral torsion tower exactly
     where no completion looks. No integral computation of TP(Z) is in
     the literature (UNVERIFIED beyond absence-of-evidence; the
     p-complete computations are Bokstedt-Madsen Asterisque 226 (1994)
     p odd / Rognes p = 2, in pre-NS notation).
```

So (b) in one line: BMS deliver the finite-place half of doc 20's program
in the strongest known form (TP = prismatic cohomology with Frobenius,
p-adically), and simultaneously prove the point that the ladder/det layer
is special to F_q; the global object is blocked at O-b1-O-b3, and O-b3 is
the program's wall restated.

## 3. (c) The archimedean gap: candidate survey

What is needed (doc 20 sec 3): a circle-equivariant object attached to
the compactified Spec Z over S whose Tate-type construction at the
infinite place yields the DEGENERATE ladder - spacing 2, start 0,
half-line - i.e. eigenvalues s + 2n, n >= 0, at scale 1/(2 pi).

### 3.1 (i) Deninger's own conventions (primary source, now exact)

Invent. 104 (1991): for X/K smooth projective, v | infty, he constructs
H_ar^w(X_v) (via B_ar = (Sym R(1))[R(-1)] ~ R[T, T^{-1}], the
"archimedean B_dR", with derivation Theta_{B_ar} = T d/dT) and proves
(intro + Sect. 4): L_v(H^w(X), s) = det_inf((s/2 pi) - (Theta/2 pi) |
H_ar^w(X_v))^{-1}. The ladder conventions, Proposition 2.1 (arguments in
(-pi/2, pi/2) for nu >> 0; proof via Hurwitz zeta, zeta(0, z) = 1/2 - z,
d_s zeta(0, z) = log Gamma(z) - (1/2) log 2 pi):

```text
prod_{nu>=0} (nu + z)              = ( Gamma(z) / sqrt(2 pi) )^{-1}
prod_{nu>=0} ((nu + z)/(2 pi))     = Gamma_C(z)^{-1},  Gamma_C = (2pi)^{-z} Gamma(z)
prod_{nu>=0} ((2 nu + z)/(2 pi))   = Gamma_R(z)^{-1},
        where HIS Gamma_R(z) := 2^{-1/2} pi^{-z/2} Gamma(z/2)
```

NOTE the 2^{-1/2}: Deninger's Gamma_R is NOT the classical
pi^{-z/2} Gamma(z/2); with his normalization the duplication is clean:
Gamma_C(z) = Gamma_R(z) Gamma_R(z+1) (classically it is 2 Gamma_C). His
global formula (1992, (3.2)) carries the constant visibly:
2^{-1/2} (2 pi)^{-2} pi^{-s/2} Gamma(s/2) zeta(s) s(s-1) =
det_inf((1/2 pi)(s - Theta) | H^1(Spec Z bar)).

Eigenvalue conventions, reconciled with doc 20 (witness gates G1-G3, G5,
G6, all PASS):

```text
- ladder SET: identical (Theta-eigenvalues -2 nu, nu >= 0: spacing 2,
  start 0). Doc 20's degenerate-ladder claim is confirmed against the
  primary source.
- SCALE: Deninger divides by 2 pi; doc 20's prod_reg(n + s/2) is the
  unscaled (entries (s+2n)/2) version. Because the half-ladder has
  ANOMALOUS DIMENSION zeta_H(0, s/2) = (1-s)/2 != 0, the value is
  scale-DEPENDENT, and the ratio is exactly pi^{(1-s)/2}:
      doc20 ladder        = sqrt(2 pi)/Gamma(s/2)
      Deninger ladder     = sqrt(2) pi^{s/2}/Gamma(s/2).
  At finite places the full ladder has anomalous dimension 0 - scale-
  free. THIS is the content of Hesselholt's remark that the scaling
  factor "is essential" only in the archimedean case ([CC14] reference
  in his intro): the place dichotomy is also a dichotomy of anomalous
  dimension (0 at finite places, (1-s)/2 at infinity).
- EF COMPLETION (new, witness G6): the scale anomaly GENERATES the
  -(1/2) log pi term of the explicit formula's archimedean density:
  -d/ds log det_scaled = -(1/2) log pi + (1/2) psi(1/4 + it/2) on the
  critical line - HALF of doc 09's density term '-log pi +
  Re psi(1/4 + it/2)' (the s <-> 1-sbar pairing of the two EF half-
  ladders supplies the 2 Re; bookkeeping, not a discrepancy), whereas
  doc 20's unscaled
  ladder produced only the digamma. The "-log pi" loose end of docs
  09/19 is the anomalous-dimension term, and it exists ONLY at the
  archimedean place.
- CONSTANTS: the 2^{+-1/2} mismatches are EF-invisible (constant
  log-derivative zero) normalization freedom; record, don't fix.
```

What Deninger delivers/lacks for C5'': delivers the exact target
conventions and the unconditional zero-side counterpart (1992, Theorem
3.3 + (3.3.1): 2^{-1/2}(2 pi)^{-2} pi^{-z/2} Gamma(z/2) zeta(z) z(z-1) =
exp(-d_s xi(s, z)|_{s=0}) with xi(s,z) = sum_rho ((z-rho)/2 pi)^{-s},
proved from the Weil/Barner explicit formula - the regularized
characteristic function of the ZEROS exists unconditionally; what is
missing is the cohomology under it). Lacks: any carrier - H_ar is built
from the Hodge structure of X(C), i.e. the archimedean fiber is INPUT.

### 3.2 (ii) Connes-Consani

Two distinct deliverables.

- arXiv:1211.4239 (J. K-Theory 14 (2014) 1-45), Theorem 1.1: for X
  smooth projective over a number field, nu | infty:
  prod_{0<=w<=2d} L_nu(H^w(X), s)^{(-1)^{w+1}} =
  det_inf((1/2 pi)(s - Theta) | HC^ar_even(X_nu)) /
  det_inf((1/2 pi)(s - Theta) | HC^ar_odd(X_nu)),
  with Theta = cyclic-homology grading + LAMBDA-OPERATIONS:
  k^Theta |_{HC_n} = Lambda(k) k^{-n}. This is the PROVEN archimedean
  mirror of Hesselholt's Theorem A (Hesselholt cites it as such, and
  takes from it the delta = 1/2 pi remark). Frobenius at infinity = the
  lambda/Adams flow - converging exactly with C6's psi^k family on
  ku ^ ku (same operations, different home). Missing: the input is
  X_nu = X x_K K_nu, an R/C-variety - the archimedean place is inserted,
  not produced; the theory is cyclic homology over the archimedean
  coefficients, not THH over S; and there is no single object containing
  both this and TP(X/F_q).
- arXiv:2205.01391 (Riemann-Roch for Spec Z bar) and arXiv:2306.00456
  (Riemann-Roch for the ring Z): using Segal Gamma-rings ("absolute
  algebra over S"), they prove INTEGER-VALUED Riemann-Roch statements
  for Arakelov divisors on Spec Z bar - the Euler characteristic equals
  deg D + log 2-corrected resp. deg D + 1 terms (their S-module
  cohomology). This is the nearest existing theorem to doc 19's missing
  PR/PS package over S (vdGS theta-RR made integer-valued by changing
  the base to S). Caveats: their S is the Gamma-ring sphere
  (combinatorial), not ring spectra; no circle action, no ladder, no
  zeta zeros; the carrier discipline (dies on DH: needs the ring Z)
  appears to hold but the connection to THH is not made anywhere.

### 3.3 (iii) Real THH (THR) and the C_2 at infinity

Inventory of what exists: Dotto-Moi-Patchkoria-Reeh arXiv:1711.10226
(JEMS 2021): THR as the C_2-equivariant norm refinement of THH; THR(F_p)
computed (bigraded polynomial); THR(Z) computed AWAY FROM 2; the
geometric fixed points Phi^{C_2} THR(Z) computed as a ring. Real
cyclotomic spectra and TCR exist (Quigley-Shah arXiv:1909.03920;
Hogenhaven arXiv:1611.01204); THR of perfectoids (arXiv:2310.11183) and
computational tools (arXiv:2408.07188) are active. Nothing in print
connects THR to archimedean L-factors (checked; mark: program-level
reading only).

Why this candidate is structurally RIGHT for doc 20's dichotomy: THH of a
commutative ring is an O(2)-spectrum (the reflection acts because Z has a
trivial anti-involution; THR records this genuinely). Inside O(2):

```text
- the rotation subgroups C_n, T act FREELY on the circle: their
  Tate constructions are the finite-place machine (C_{p^n} -> TP,
  full ladders, Frobenius orbits = free orbits);
- the REFLECTIONS are the only subgroups with FIXED POINTS on the
  circle (each reflection fixes two points);
- the character ladder folds: T-characters z^n, n in Z (full ladder,
  Gamma_C) vs reflection-invariant combinations indexed n >= 0
  (half-ladder) with the even/odd split (Gamma_R vs Gamma_R(s+1)) -
  exactly Serre's recipe at a real place, where F_infty = complex
  conjugation splits Hodge classes into +-.
```

So "Frobenius at the infinite place = the circle action degenerating at a
fixed point" (doc 20's open piece) has a literal candidate: the
archimedean place is the REFLECTION sector of the O(2)-action on THR(Z),
and the degenerate spacing-2 ladder is the folded character lattice. What
is missing is everything quantitative: no theorem produces Gamma_R (or
the anomalous dimension (1-s)/2, sec 3.1) from a C_2- or O(2)-Tate
construction of THR(Z).

### 3.4 (iv) Rognes's logarithmic THH

Rognes, "Topological logarithmic structures" (Geom. Topol. Monogr. 16
(2009)); Rognes-Sagave-Schlichtkrull arXiv:1402.1317 (localization
sequences for log THH), arXiv:1410.2170 (log THH of topological
K-theory). What the technology provides: for a log ring spectrum (A, M)
the log THH sits in cofiber/RESIDUE sequences interpolating between
THH(A) and THH of the localization (e.g. THH(ku) -> THH(ku | KU) ->
Sigma THH(Z)-type sequences, proved for ku, l, and DVR-like cases) - i.e.
exactly the "compactify by adding a boundary, get duality-grade exact
sequences" mechanism that properness needs, in homotopy theory, today.
What is missing for us: a log structure "at the infinite prime" on
HZ (or on S -> HZ) is not defined anywhere; the existing log structures
compactify chromatic/p-adic directions (Bott element, p), not the
archimedean one. Candidate role: the properness VEHICLE for C5''' (the
residue sequence whose boundary term is the sec-3.3 reflection sector),
not the source of the ladder itself.

## 4. Consequences: corrections to doc 20 + the relocated burden

Proposed correction notes (lead to apply; doc 20 sec 2 and sec 5):

```text
C1 (W3 attribution): the closed form 2 sinh((log p)s/2) is NOT
   "Deninger's identity". Deninger 1992 Prop. 2.3 / Hesselholt Prop.
   7.1 + Rem. 7.2 give 1 - lambda p^{-s} for the SAME ladder under the
   arg-convention scheme (branch conventions differ between Hesselholt
   Sec 7, args in (-pi, pi] following Deninger PSPM 55, and Deninger
   1992 Conv (2.1), args in (-3pi/2, pi/2]; witness G4 shows BOTH yield
   1 - lambda q^{-s}, so cite both rather than conflating); the p^{s/2}
   prefactor is the property of the
   symmetric scheme alone (witness G4; ratio exactly p^{(s-alpha)/2} =
   the ladder's half-sum/vacuum term). Hesselholt's Theorem A is
   consistent ONLY with the scheme WITHOUT the prefactor (Spec F_q
   check). Therefore "duality completion generates KMS-1/2" must be
   weakened: the completion generates the full ladder; KMS-1/2 is
   generated by the full ladder PLUS the conjugation-symmetric
   regularization, and that scheme choice is NOT yet supplied by any
   homotopy-theoretic theorem. Doc 10's fourth realization input is
   reopened at the derivation level (supply-level numerics unaffected).
C2 (archimedean dictionary): doc 20's degenerate ladder is confirmed
   against Deninger 1991 Prop. 2.1, but the dictionary to Gamma_R needs
   the 1/(2 pi) scale: the half-ladder has anomalous dimension (1-s)/2,
   the value is scale-dependent, the ratio is pi^{(1-s)/2}, and the
   scale anomaly is exactly the EF's -(1/2) log pi supply term (witness
   G5-G6) - which the unscaled doc-20 ladder lacks. New invariant for
   the place dichotomy: anomalous dimension 0 (finite) vs (1-s)/2
   (infinity); "the scaling factor is essential" only at infinity.
C3 (constants): Deninger's Gamma_R carries 2^{-1/2} (his definition,
   1991 sec. 2; duplication then reads Gamma_C = Gamma_R Gamma_R(+1)).
   EF-invisible; record as normalization freedom.
```

The relocated derivation burden, sharpened by 1.1-1.3: the homotopy
theory (Hesselholt + BMS) derives, at finite places, (1) the 2-periodic
module structure, (2) the Frobenius with phi(v) = p v, (3) hence the full
ladder as the log-fiber of the Frobenius flow - but the ANALYTIC layer on
top (which regularization scheme, hence whether KMS-1/2 appears) is not
homotopy-theoretic anywhere: Deninger's scheme is selected by consistency
with the crystalline determinant, and the symmetric scheme (which the
program wants, since it alone produces the self-dual normalization) must
be selected by a structure that pairs the ladder with its conjugate -
i.e., by a REAL/self-dual structure. Note the convergence: the symmetric
scheme is precisely the regularization that respects an underlying real
structure (eigenvalues paired with conjugates), and the real structure on
the circle action is the C_2 of sec 3.3. The scheme question and the
archimedean question appear to be the SAME question.

## 5. The missing archimedean theorem, in gate language

GATE C5''-infty (open; the sharpest statement this pass can certify):

```text
Required: a genuine O(2)-equivariant (real-cyclotomic) refinement X of
THH(Z) - carrier: exists iff the input is a commutative ring (DH/Epstein
die by non-existence: no ring => no THR, P2-grade kill inherited) -
together with a compactness/log-boundary datum over S, such that:

(infty-1) LADDER: the Tate-type construction of X at a REFLECTION
   subgroup C_2 < O(2) (the only subgroups with fixed points on the
   circle; finite places = free rotation orbits) carries a weight
   grading whose regularized characteristic function is the half-ladder
   {(s + 2n)/(2 pi)}_{n>=0}: spacing 2, start 0.
(infty-2) SCALE: the construction canonically produces the 1/(2 pi)
   scale - equivalently the anomalous dimension (1-s)/2 and with it the
   EF's -(1/2) log pi term (witness G5/G6). At finite places scale-
   freedom is automatic (anomalous dimension 0); at infinity the scale
   is DATA the object must supply.
(infty-3) SCHEME: the regularized determinant arising from the homotopy
   theory must be identified as a scheme; the finite-place theorem
   forces the arg-convention scheme (no KMS-1/2), so the self-dual
   normalization must come from the global real/self-dual structure
   (infty-1's C_2), not from any local regularization - fail-closed: if
   the C_2-structure does NOT induce the symmetric scheme on ladders,
   the realization-spec input KMS-1/2 has no carrier in this approach.
(infty-4) RANK: the pi_0-excess delivers the bare rank factors
   s/(2 pi), (s-1)/(2 pi) with H^2 = H^0(-1) (Deninger 1992 p. 146).
Then C5''' (the zeros) = Poisson/Serre duality for the compactified
object, with the log-THH residue sequence (sec 3.4) as the candidate
exactness vehicle and CC's S-valued Riemann-Roch (sec 3.2) as the
nearest existing global statement.
```

FEASIBILITY VERDICT. No candidate currently delivers (infty-1)-(infty-4);
the assignment of roles, by evidence:

- (iii) THR/real-cyclotomic is the only candidate whose symmetry group
  CONTAINS the required fixed-point geometry intrinsically (reflections
  = fixed points; doc 20's orbit dichotomy is literally the subgroup
  structure of O(2)), and sec 4's finding makes it double-duty: the same
  C_2 is the only visible source of the symmetric scheme = KMS-1/2.
  VERDICT: primary candidate.
- (ii) CC 2014 is the only PROVEN archimedean det_inf theorem and fixes
  the flow (Theta = grading + lambda-operations = the Adams flow,
  converging with C6). Use as the calibration target the THR-side
  construction must reproduce.
- (i) Deninger fixes all conventions (this doc + witness); his (3.3.1)
  shows the zero side exists unconditionally as a regularized product.
- (iv) Rognes log THH is the properness vehicle for the C5''' step, not
  the ladder source.

FIRST CONCRETE STEP (posed, finite, computable with existing inputs):
compute the reflection-Tate ladder of THR. Concretely: for the genuine
C_2-spectrum THR(F_p) (fully computed, DMPR) and THR(Z) away from 2
(DMPR), determine the RO(C_2)-graded structure of the C_2-Tate
construction THR^{tC_2} and of the O(2)-relative constructions, and test
two pre-registered readings: (r1) the weight grading folds Z -> {n >= 0}
with spacing doubled (the Gamma_C -> Gamma_R fold); (r2) the associated
regularized characteristic function has anomalous dimension (1-s)/2
rather than 0. A positive (r1)+(r2) at F_p would already be decisive
orientation (the fold is local, not archimedean-specific); the
archimedean statement is then the same computation for the compactified
object, which does not yet exist. If (r1) fails on THR(F_p) - i.e. the
C_2-Tate does NOT fold the ladder - the THR candidate dies and the
archimedean carrier must be sought in CC's Gamma-ring geometry instead.

## 6. Witness record

prime_int_deninger_convention.py (ALL PASS): G1-G3 Deninger Prop 2.1
(three identities incl. the sqrt(2), to 1.5e-15 rel); G4 the three-scheme
comparison on the full ladder (Deninger-rotated, vertical principal
branch, doc-20 symmetric; values 1 - lambda q^{-s}, 1 - lambda q^{-s},
q^{(s-alpha)/2}(1 - lambda q^{-s}); to 5.5e-16); G5 anomalous dimensions
(0 full / (1-s)/2 half; doc20/Deninger ratio pi^{(1-s)/2}); G6 the scale
anomaly = the EF's -(1/2) log pi (1.2e-9, fd-limited); G7 duplication
guards. Pre-registered readings R1-R5 in the docstring; every reading
came out on the "discrepancy is real" branch. Invalidation: any of G1-G4
failing under an independent implementation of Deninger's conventions
(e.g. exact arb enclosures of the Hurwitz derivatives) would reopen doc
20's attribution; the conventions themselves are pinned to scanned
primary text (refs/deninger1991-gamma-factors.pdf p. 247-248 = Prop 2.1;
refs/deninger1992-local-l-factors.pdf p. 142-143 = Prop 2.3, p. 146-147
= (3.1)-(3.2)).

Unaffected by the scheme finding: doc 18's <Delta,Delta> = zeta'(0) and
doc 19's D(s) = sqrt(2 pi)/Gamma(s+1) (positive-real half-ladders, no
branch ambiguity); doc 20's W4 digamma claim (log-derivative on a
half-ladder; only the -(1/2) log pi completion was missing, now located).
