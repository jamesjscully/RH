# RF — the Rosati/theta realization: ruthless circularity skeptic [DECIDED · circular-terminus]

`[BUILT + computed]` — 2026-06-06
Module: `scripts/numerics/witness/rosati_circularity_skeptic.py`
(run: `python3 -m scripts.numerics.witness.rosati_circularity_skeptic`).

## The mandate (the decidable question)

The count/radius meditation says `psi_infinity` should be a CANONICAL FINITE-DEGREE SELF-MAP `F` of a
polarized archimedean abelian variety, with `|alpha|=sqrt(deg)` FORCED by Rosati positivity (a free
theorem over C, NOT RH). Rosati positivity `Tr(phi phi^dagger)>0` and `F.F^dagger=[deg]` are
tautological. So IF the radius is forced, ALL the RH content must hide in the SPECTRAL REALIZATION.

DECISIVE: does an OFF-LINE eigenvalue OBSTRUCT the EXISTENCE of the polarized-AV-with-endomorphism
realization?
- YES → genuine forcing (no AV with off-line `F` exists → radius FORCED → RH).
- NO → realization possible off-line too → radius datum ASSUMED → CIRCULAR.

Tested all three named candidate obstructions: (a) FE/pairing, (b) integrality/endomorphism, (c)
positivity. Built a 2x2 'Frobenius' with off-line eigenvalues and COMPUTED whether it admits a positive
Rosati polarization.

## What got BUILT (the decisive toy, exact)

A 1-dim complex torus `R^2=C`, a real endomorphism `F`, the unique-up-to-sign complex structure `J`
commuting with `F` (`[F,J]=0` to machine zero), the area-form polarization `E` with sign chosen so
`H(x,y)=E(Jx,y)+iE(x,y)` is positive-definite, the Rosati adjoint `F^dagger = E^{-1} F^T E`, and the
Rosati trace form `Tr(phi phi^dagger)` on the basis `{I,F}`.

**[B] The crux — PLANT an off-circle conjugate pair `alpha = r e^{it}`, `r != sqrt q`, q=7 fixed
(= a genuine off-line zeta zero, `Re rho != 1/2`):**

| case | `\|alpha\|=r` | off-circle | polarization H pos-def? | Rosati form pos-def? | `F.F^dagger` | `=r^2=detF` | `=q` |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| ON-CIRCLE r=sqrt q | 2.646 | no | **YES** | **YES** | 7.000 | yes | **yes** |
| OFF r=1.3 sqrt q (Re ρ>½) | 3.440 | yes | **YES** | **YES** | 11.830 | yes | **no** |
| OFF r=0.7 sqrt q (Re ρ<½) | 1.852 | yes | **YES** | **YES** | 3.430 | yes | **no** |
| OFF r=2.0 sqrt q | 5.292 | yes | **YES** | **YES** | 28.000 | yes | **no** |

> **An OFF-CIRCLE Frobenius admits a positive Rosati polarization at zero obstruction.** Every 1-dim
> complex torus IS an abelian variety (it always carries a positive polarization), regardless of where
> `F`'s eigenvalues sit. The Rosati form `Tr(phi phi^dagger)` is positive-definite for the off-circle
> `F` too. **No existence obstruction. Candidate (c) — positivity forces the line — is FALSE.**

The free theorem fires exactly as advertised: `F.F^dagger = r^2 = det F = |alpha|^2`, ALWAYS scalar,
ALWAYS positive. **But that scalar is `r^2`, the polarization degree, which is `|alpha|^2` read off
alpha — it equals the externally-prescribed `q` ONLY when `r=sqrt q`, i.e. only on the line.** The
identity `F.F^dagger = deg` is tautological and on-line-blind; the equation `deg = q` is the entire RH
content, and it is an EXTERNAL constraint never supplied by the AV/polarization data.

**[A] companion `x^2-ax+q` confirms the same:** for nonreal eigenvalues the polarization exists and
`F.F^dagger = q` — but ONLY because the companion HARD-CODES `det F = q` into its bottom-left entry.
That `det=q` is the assumption, not a derivation; it is the choice of which matrix to call "the"
Frobenius. (Real-eigenvalue companions `a^2>4q` carry no commuting `J` — not the AV case at all.)

**[C] Integrality / endomorphism (candidate b) — the subtlest, and it ALSO does not force q:** an
imaginary-quadratic integer `alpha` IS an endomorphism of `C/O_K` with `det(F on H_1) = N(alpha) =
alpha·alpha-bar = |alpha|^2`. So integrality FORCES `|alpha| = sqrt(deg)` — but `deg = N(alpha)` is
alpha's OWN norm, a tautology (`N = |·|^2` BY DEFINITION of the complex modulus). An off-circle integral
endomorphism with `|alpha|^2 != deg` is IMPOSSIBLE — but the "deg" it is forced relative to is `N(alpha)`,
NOT an independently given `q`. The radius is forced relative to the WRONG (self-referential) degree.
**Integrality does not obstruct an off-line realization; it only re-confirms `|alpha|=sqrt(|alpha|^2)`.**

## Where RH enters (the EXACT circularity step)

The free Rosati positivity genuinely fires and the radius genuinely drops out: `|alpha| = sqrt(F.F^dagger)
= sqrt(deg)`. **This is FORCED, not assumed.** The circularity is NOT in the positivity, NOT in the FE
(candidate a, pairing is automatic), NOT in integrality (b), NOT in existence-of-polarization (c).

The RH content sits in ONE step, the **anchoring of the degree**:

> `deg(F) = F.F^dagger = q`, where `q` is the *externally prescribed* radius² (the critical-line radius).

For `F` to be "THE canonical/geometric Frobenius with `F.F^dagger = q·Id`" for a *prescribed* `q`, one
must SELECT, among all the off-circle endomorphisms (each with its own `det = |alpha|^2`), the one whose
degree is `q`. That selection = the constraint `|alpha|^2 = q` = `Re rho = 1/2` = **RH itself**. The
spectral realization "put the zeta zero `rho` at `alpha = q^{rho}` as an eigenvalue of a degree-`q`
endomorphism `F`" PRESUPPOSES `|alpha| = sqrt q`, i.e. presupposes the zero is on the line, the moment it
demands `F.F^dagger = q` (not just `= some scalar`). **An off-line `rho` realizes equally well — it just
lands on a degree-`|alpha|^2`(≠q) endomorphism.** The `q` is not intrinsic to the archimedean AV; over
`F_q` it is intrinsic (the constant field's cardinality, the one arithmetic `q` doing double duty as both
the q-th-power-map scaling AND the count — `M2`/`PA-synthesis` §2). At infinity there is no such field, so
`q` must be imported, and importing `deg = q` is importing the radius is importing RH.

## anchor over F_q / complex over C

- **over F_q (`anchor_Fq`): PASS — `F.F^dagger = q` IS forced, by the geometric Frobenius being the
  q-th-power map.** It is a ring endomorphism whose single arithmetic `q` is simultaneously the constant
  field cardinality (the count / `Tr`-source) and the q-th-power scaling (the radius / modulus). The
  polarization is the cup product on the EXISTING surface `C×C`; the Rosati involution permutes actual
  correspondences; `F.F^dagger = deg(Frob) = q` because `Frob∘Frob^t = [q]` is the degree of the
  q-Frobenius, a geometric fact (`M2-ff-hodge-datum.md` C3a/C3b). The radius IS forced — by the geometry
  of the q-power map, not by RH. (`rosati_reflection.py`, `edge_to_centre_chain`, confirms: positivity
  tracks the line for all planted cases.)

- **over C (`complex_check`): PASS on positivity, but it does NOT deliver the radius.** The Rosati form
  IS positive-definite WITHOUT assuming RH — computed pos-def for EVERY off-circle `F` (table [B]). And
  `F.F^dagger = deg` holds for the canonical adjoint, also without RH. BOTH free theorems fire. **But
  `deg` is `|alpha|^2`, self-referential** — the positivity that is free is blind to the prescribed `q`;
  it pins `|alpha| = sqrt(deg(F))` and is silent on `deg(F) = q`. The complex-analytic AV has NO canonical
  `q`: there is no archimedean field-endomorphism `x↦x^q` to source one (`PA-synthesis` §2). The very fact
  that makes positivity free (it works for any `F`) is the fact that makes it RH-silent (it cannot select
  the `deg=q` `F`).

## DH litmus / falsify

- **DH:** unposable as a forcing — no Euler product ⟹ no `q` ⟹ no `F.F^dagger=q` to demand. The
  polarized-torus + endomorphism structure EXISTS over any spectral data (an off-line DH zero realizes on
  a degree-`|alpha|^2` torus just as well), so the realization is **DISPERSING** in the existence question
  (consistent with `PA-synthesis`: every archimedean structure exists over DH too).
- **`falsify.py` axes for "RH ⟸ existence of polarized-AV-with-deg-q-endomorphism":**
  EULER-BORNE **NO** (the polarized torus exists for any spectral multiset, DH included — the existence is
  not Euler-borne; only the *value* `q` is, and that value is imported); SEES-ZEROS **YES but vacuously**
  (the realization tracks the zero, but accommodates it ON OR OFF the line, landing it on the matching
  degree); INDEPENDENT **NO** (demanding `deg=q` IS the on-line condition). Same box as the equality-clause
  attack `PA2`: the radius is the equality clause `F.F^dagger=q`, here re-derived as the *degree-anchoring*
  step. Runs clean; framework-consistent.

## Verdict

`[circular]` — **CIRCULAR (terminus confirmed), with a sharpened locus.** The skeptic's hypothesis is
CONFIRMED in its decidable form: the FREE Rosati positivity genuinely forces `|alpha| = sqrt(deg(F))`
(FORCED, not assumed — a real theorem over C, computed pos-def for off-circle `F`), but `deg(F) = F.F^dagger
= |alpha|^2` is SELF-REFERENTIAL — it equals the prescribed critical radius² `q` **iff** the eigenvalue is
already on the line. **None of (a) FE-pairing, (b) integrality, (c) positivity OBSTRUCTS an off-line
realization** — the computation shows the off-circle Frobenius admits a positive Rosati polarization at
zero obstruction, with `F.F^dagger = r^2 ≠ q`. So the radius is **forced to `sqrt(deg)` but NOT to
`sqrt(q)`**; the equation `deg = q` — the anchoring of the abstract degree to the *prescribed* arithmetic
radius — is the EXACT step where RH enters. Over `F_q` that step is FREE (the geometric q-power map is its
own degree-`q` source); over C there is no archimedean `x↦x^q`, so `deg=q` must be imported, and importing
it is importing RH. The spectral realization does NOT obstruct off-line zeros (it accommodates them on
their own circle), so it is **RH-silent / circular**, not a forcing.

**Tag:** `radius_forced_or_assumed = PARTIAL` — the *radius-relative-to-own-degree* is FORCED (free
Rosati, genuinely not RH); the *radius-equals-prescribed-q* is ASSUMED (the degree-anchoring = RH). The
forcing and the assuming are cleanly separated by this computation, which is the new content.

**Next step IF one still hunts:** the only non-circular escape would be a CANONICAL archimedean source for
`q` itself — a structure forcing `deg(F) = q` for an externally prescribed `q` without already knowing
`|alpha|=sqrt q`. That is precisely R8's irreducible open ingredient (the missing finite constant-field
cardinality at ∞), now re-localized as "the degree-anchoring of the canonical endomorphism." This route
does not open it; it re-confirms it from the AV/Rosati direction and proves the obstruction is NOT in any
of the three candidate places (existence/integrality/positivity) but solely in the degree=`q` anchor.
