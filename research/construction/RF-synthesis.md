# RF-synthesis — Rosati / polarized-AV canonical endomorphism as the radius-forcer [DECIDED · CIRCULAR, with one empty escape]

**Lead under judgment.** `psi_infinity` (RH's irreducible residue) realized as a CANONICAL endomorphism
`F` of a polarized archimedean abelian variety / theta object, with the radius `|alpha|=sqrt(deg F)`
FORCED by Rosati positivity — claimed as a FREE theorem over C (`F.F^dagger=[deg F]` tautological from
the dual isogeny; `Tr(alpha alpha^dagger)>0` is Mumford, not RH). Question: genuine escape from the
count/radius decoupling, or does the spectral realization assume RH?

Three angles were built and run; all numerics reproduced live (numpy/cmath, machine-exact).
Verdicts: `rosati-positivity-free` → CIRCULAR; `cm-shimura-taniyama` → PARTIAL_LEAD; `circularity-skeptic`
→ CIRCULAR.

---

## (1) Is `F.F^dagger=[deg]` genuinely tautological/free — radius forced given F? PARTIALLY, AND IT IS THE WRONG "FORCING".

**The tautology is REAL but VACUOUS for the radius.** Confirmed over both regimes, machine-exact:

- **Over C, the dual-isogeny identity holds with NO RH input.** `F.F^vee=[deg F]` as endomorphisms; on
  each F-eigenline `eig(F)*eig(F^vee)=deg F`. This fires for EVERY F. Rosati POSITIVITY
  (`Tr(phi phi^dagger)>0`) is likewise a genuine free theorem over C (Mumford/Hodge–Riemann): the
  skeptic toy computes the Rosati Gram on `{I,F}` positive-definite for EVERY off-circle F (table B:
  `r=0.7, 1.3, 2.0 × sqrt q` all pos-def). **Both free theorems fire and the radius genuinely DROPS OUT
  as `|alpha|=sqrt(deg F)`.** This is FORCED, not assumed — a real structural fact over C.

- **BUT `deg F` is self-referential.** `deg F = det F = |alpha|^2` BY DEFINITION of the complex modulus
  on a conjugate pair. So `|alpha|=sqrt(deg F)` says `|alpha|=sqrt(|alpha|^2)` — a tautology relative to
  F's OWN degree. The skeptic table B makes this exact: planted off-circle pair `alpha=r e^{it}`,
  `r != sqrt q`, gives `F.F^dagger = r^2 = det F` (machine-exact), **equal to the polarization degree but
  NOT to the prescribed q.** The radius is forced relative to the WRONG (self-referential) degree.

- **The machine-exact off-line counterexample to the tautology-as-radius-forcer** (test3): take the
  off-line companion of `T^2-6T+7` (a=6 > 2√7, Hasse-violating). Its Rosati adjoint `F^dagger=E^{-1}F^T E`
  gives `F.F^dagger = 7.I` EXACTLY (the tautology `F.F^dagger=[deg]` HOLDS), **yet the eigenvalues are
  REAL {1.586, 4.414}, `|eig|^2={2.52, 19.49} != 7`.** The tautology controls the Rosati-dual PRODUCT
  `alpha*(deg/alpha)=deg` (says deg=deg, vacuous), NOT the modulus `alpha*conj(alpha)=|alpha|^2`. These
  agree iff `conj(alpha)=deg/alpha` iff `beta=conj(alpha)` iff `a^2<=4q` = **RH for the curve.** The
  conjugacy `beta=conj(alpha)` IS RH.

**Verdict on (1).** The count/radius decoupling is NOT broken by the tautology. The Rosati involution
couples `alpha` to `deg/alpha` (the FE-pairing partner), NOT to `conj(alpha)` (the modulus). x^q over F_q
couples them because the q-power map identifies the dual partner with the conjugate (the geometric
Frobenius IS the q-power ring map, supplying a single arithmetic q that is simultaneously count-source
and radius-source). Over C there is no archimedean `x->x^q`, so the dual-partner identity and the
conjugation identity are DIFFERENT identities; the tautology gives the first, RH is the second.

---

## (2) ALL RH content is in the REALIZATION — does an off-line zero OBSTRUCT it? NO. It realizes equally well. CIRCULAR.

This is the decisive, decidable test (skeptic toy, table B). The hope was: if an off-line Frobenius
admits NO positive Rosati polarization, then the realization EXISTS iff RH — a genuine forcing.

**It admits one at zero obstruction.** For every planted off-circle conjugate pair (a genuine off-line
zeta zero, `Re rho != 1/2`):
- a commuting complex structure J exists (`[F,J]=0`, `J^2=-I` machine-exact);
- a positive-definite polarization H exists (every 1-dim complex torus IS an abelian variety, regardless
  of where F's eigenvalues sit — the free fact);
- the Rosati form on `{I,F}` is positive-definite;
- `F.F^dagger = r^2 = det F` (its own degree), simply NOT the prescribed q.

None of the three named candidate obstructions fires:
- **(a) FE/pairing** is automatic (`alpha <-> deg/alpha` always pairs).
- **(b) integrality** only re-confirms `|alpha|=sqrt(N(alpha))` with `N=|.|^2` BY DEFINITION for an
  imaginary-quadratic integer — forced relative to alpha's OWN norm, never an externally prescribed q.
  (An off-circle integral endomorphism with `|alpha|^2 != N(alpha)` is impossible because the field norm
  IS the complex modulus-squared — so integrality forces the self-referential circle, not the q-circle.)
- **(c) positivity** is FALSE as a line-forcer: pos-def for ALL off-circle F (table B).

**The obstruction lives SOLELY in the `deg=q` anchor** — selecting, among all off-circle endomorphisms
each with its own `det=|alpha|^2`, the one whose degree equals the externally prescribed q. That equation
`deg F = q` IS `|alpha|^2=q` IS `Re(rho)=1/2` IS RH. It is never supplied by the AV/polarization data
over C. Off-line zeros realize equally well; they just land on a degree-`|alpha|^2(!=q)` torus.

**Therefore the realization is RH-silent / circular**, NOT a forcing. The new problem "construct the
archimedean polarized AV with the zeros as a canonical endomorphism" does not obstruct off-line — so it
is not a different+easier residue; it re-imports `deg=q` = RH.

---

## (3) HONEST VERDICT: CIRCULAR — with the radius-forcing relocated cleanly, and ONE genuine-but-empty escape (CM).

**VERDICT: CIRCULAR.** Where RH re-enters, exactly: the degree-anchoring step `deg(F)=q`, i.e. the
demand that `F.F^dagger=q.Id` be the SCALAR q (every `|rho|^2` equal to the prescribed q) rather than a
positive operator with its own spread spectrum `r^2`. On the conjectural archimedean spectrum
(zeros = eigenvalues), "`F^dagger.F=[deg].Id` is the scalar q" literally says every `|rho|^2` is the same
number = RH restated. Same terminus as **PA2** (the HR equality-clause `F F†=q·Id`, not the HL-iso) and
**PA-synthesis** (the missing finite constant-field cardinality `|kappa(t=0)|=q>1` at infinity), now
re-derived from the AV/Rosati direction and localized to the single operator identity `F^dagger.F=[deg].Id`.

**What is genuinely settled / a real structural shift worth stating loudly:** the radius IS free GIVEN
the degree — `|alpha|=sqrt(deg F)` is FORCED by Rosati positivity over C, a real theorem, no RH. The
count/radius coupling on an AV is tautological *relative to F's own self-referential degree*. So the
radius was NEVER the hard part on an AV. **But "free relative to own degree" is not "free relative to the
prescribed q".** The entire RH content has been shown — by three independent machine-exact toys — to live
in ONE place and one place only: anchoring the abstract self-referential degree to the externally
prescribed arithmetic q. The realization does NOT obstruct off-line zeros, so it is not a different,
easier problem; it is the SAME `deg=q` anchor wearing a Hodge/spectral costume.

**What is genuinely DIFFERENT from the dead positivity branch.** The dead branch said "find an
archimedean positivity that forces the line." This synthesis proves that positivity is the WRONG target
twice over: (i) Rosati positivity is FREE and fires for every off-circle F, so it cannot be the
obstruction; (ii) the obstruction is not a positivity at all but a DEGREE-ANCHORING — manufacturing a
canonical scalar q as the degree of the archimedean endomorphism. That is a sharper, different terminus:
not "the radius is `F F†=q`" but "the degree-anchoring `deg(F)=q` of the canonical endomorphism, with no
archimedean `x->x^q` to supply q." This coincides with R8's irreducible open ingredient (the missing
finite residue-field cardinality `q>1` at the archimedean place) and PA-synthesis's "degree raising never
raises the base `1^d=1`."

**The one genuine-but-empty escape: CM / Shimura–Taniyama (PARTIAL_LEAD).** The `cm-shimura-taniyama`
angle is NOT a circular terminus. For a CM (imaginary-quadratic) endomorphism field, the Rosati
involution is FORCED `= complex conjugation` (a structural fact of CM fields), which identifies the free
norm `N(pi)=q` (the degree) with `|pi|^2` — so `|alpha|=sqrt q` is forced WITHOUT RH (verified exact on
9 (d,p) pairs; `a^2 = 4q - d b^2 < 4q` forced whenever `b!=0`). This is exactly the missing identity
`F^dagger = conj` that the general case lacks — **supplied for FREE by a large archimedean-typed
endomorphism algebra, not assumed.** So the radius CAN drop out of an archimedean infinity-type
non-circularly. The catch that makes it empty for zeta: zeta is GL(1) (motive Q(0), Hodge type (0,0)) —
NO Frobenius pi, NO endomorphism field for an infinity-type to act on; and the relevant weight-2
Rankin–Selberg / NS carrier is non-CM (CM forms are measure-zero, generic End=Z). The very feature that
forces the radius (a CM endomorphism algebra) is precisely what zeta lacks. **This is WHY the CM case is
easy and zeta is hard**, and it relocates the wall to a concrete, decidable, strictly-sharper place.

**DH litmus.** All three angles falsify on Davenport–Heilbronn: DH has no Euler product → no Frobenius pi
→ no endomorphism field → no CM type → the radius-forcing is UNPOSABLE for DH. The free Rosati positivity
is Euler-silent (fires for any F), so it correctly does NOT force the line for DH. Consistent: the only
non-circular forcing (CM) is Euler-borne and DH-failing by design.

**Honest odds.** ~3% that the Rosati/AV direction opens RH. The realization is RH-silent (proven by the
off-line toy), so the AV direction adds no forcing beyond `deg=q` = RH. The single non-vacuous handle is
the CM-lift question below, predicted hard/likely-impossible (CM is measure-zero).

**Next step (the strictly sharper, decidable terminus).** Do NOT chase "an archimedean positivity"
(dead) nor "does off-line obstruct the realization" (now answered: NO). Instead the one untried,
non-circular-IF-it-works handle: **can zeta's weight-2 NS / Rankin–Selberg carrier be given an enlarged
archimedean-typed endomorphism algebra in which the Rosati involution is FORCED `= complex conjugation`
(the motivic-CM-lift)?** Concretely: probe whether the self-product NS lattice `gr^W_2(S^2)` of a
CM-modular-form factor inherits a CM endomorphism structure making purity automatic, and whether that
structure can be transported OFF the CM locus by deformation/degeneration. The missing object is a CM
endomorphism algebra on the carrier (= a canonical `F^dagger=conj`), NOT a missing positivity and NOT a
missing realization. Predicted: hard/likely-impossible, but it is the one place where "self-duality /
archimedean infinity-type forces it" genuinely separates from "RH assumed."
