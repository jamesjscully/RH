# RF — Rosati positivity as the FREE forcing of the radius: is `F.F†=[deg F]` a tautology that forces `|α|²=deg`? [DECIDED · circular, with an exact new split]

`[computed · 4 exact tests over F_q and C]` — 2026-06-06
Test harness: `/tmp/rosati_free_test{,2,3,4}.py` (numpy/cmath; results inlined below). The angle:
Rosati positivity is a REAL free theorem over C (Mumford / Hodge–Riemann on the AV, NOT RH); does it
FORCE the radius `|α|=√deg`, moving all RH content to the realization (is there a canonical archimedean
endomorphism `F` whose eigenvalues are the zeros)?

## The claim under test (the seductive version)

> `F.F† = [deg F]` is a TAUTOLOGY (the dual isogeny DEFINES degree). On `H¹`, `eig(F†) = deg/eig(F)`,
> so `eig(F)·eig(F†) = deg` for every eigenline — free, no RH. Hence `|α|²=deg` is FORCED for ANY
> isogeny on ANY polarized AV including over C, and the entire RH difficulty is the (different,
> possibly easier) realization problem.

**This claim is FALSE in the load-bearing step.** The tautology is VACUOUS for the radius.

## The four exact computations

**(1) ANCHOR over F_q [computed].** Elliptic `E/F_q`, geometric Frobenius `F` (companion of
`T²−aT+q`). `F.F^vee = q` on each eigenline tautologically (`α·(q/α)=q`). For on-line curves
(`a=1,5` at `q=7`; `a=3,q=11`; `a=4,q=13`) `|α|²=q` holds. **But for the off-line plant `a=6,q=7`
(`a²=36>4q=28`): `α=4.414, β=1.586` REAL, `F.F^vee=7` STILL HOLDS, yet `|α|²=19.49 ≠ 7`.** The
tautology survives off-line; the radius does not. → **the tautology does NOT force the radius.**

**(2) COMPLEX CM [computed].** `E/C` with CM by `ℤ[i]`, principal polarization, Rosati `†` = complex
conjugation on `ℚ(i)`. Rosati Gram on `{1,i}` is `[[2,0],[0,2]]`, eigenvalues `{2,2}` —
**positive-definite, NO RH input** (pure `2×`Euclidean norm). And `|eig(F)|²=Nm(F)=deg F` holds for
every CM endomorphism `F=a+bi` (`|α|²=a²+b²=deg`). **Both "free over C" facts confirmed.** But note:
this `|α|²=deg` is the *analytic* `Nm`, true for EVERY `F` — it does not single out a critical radius.

**(3) THE CRUX [computed — decisive].** Built a Rosati adjoint `F† = E⁻¹FᵀE` (symplectic cup form
`E=J`) for `F=`companion`(T²−6T+7)` (the OFF-LINE `a=6` case). Machine-exact result:
`F.F† = 7·I` (the tautology `F.F†=[deg F]` HOLDS), `det F = 7 = deg F`, **yet eigenvalues are REAL
`{1.586, 4.414}`, `|α|² = {2.52, 19.49} ≠ 7`.** So an isogeny with `F.F†=[deg F]` exact AND eigenvalue
OFF the circle `|α|²=deg` EXISTS. **The tautology controls the PRODUCT `α·(deg/α)=deg` (which says
`deg=deg`), NOT `|α|²=α·conj(α)`.** They coincide iff `conj(α)=deg/α` iff `|α|²=deg` — i.e. iff
`β=conj(α)` (the two eigenvalues are complex-conjugate, `a²≤4q`) — **which is exactly RH for the curve.**

**(4) WHERE THE FREE POSITIVITY ENTERS, AND WHAT IT FORCES [computed].** Separate two facts both free
over C:
- **(A) tautology** `F.F†=[deg F]` — free, but VACUOUS for the radius (test 3).
- **(B) Rosati POSITIVITY** `<u,v>=Tr(u v†)` positive-definite — free over C (Hodge–Riemann), NOT RH.
The Hasse/Weil radius comes from **(B), not (A)**: with `F†=[a]−F`, `F F†=[q]` (`a=Tr F ∈ ℤ`),
positivity of the integer form `Q(m,n)=Tr((m+nF)(m+nF)†)=2m²+2amn+2qn²` `⟺ a²≤4q ⟺ |α|=√q`. Verified:
`a=1,5 (q=7)` pos-def, `a=6,7 (q=7)` NOT, `a=4 (q=13)` pos-def — tracks the line exactly.

## The exact verdict on the angle's question

**Is the radius FORCED (tautological, all difficulty in realization) or does `deg F` secretly encode RH?**

Neither of the angle's two framings is right; the truth is a third, sharper thing:

1. **The tautology (A) `F.F†=[deg F]` does NOT force the radius** (test 3, machine-exact off-line
   witness). It is VACUOUS — it controls a Rosati-dual PRODUCT `α·(deg/α)`, not a modulus `α·conj(α)`.
   The angle's "the radius is FREE given F via the tautology" is **FALSE**.

2. **Rosati POSITIVITY (B) DOES force the radius — and IS free over C** (tests 2,4). For a *genuine*
   endomorphism `F` of a *genuine* polarized AV over C, `F†F=[deg F]` is positive-self-adjoint, its
   eigenvalues are positive reals `=|eig F|²`, and positivity + the integral trace relation pin them to
   `deg F`. This is a real, RH-free theorem. **So the radius is FORCED — by positivity, not the
   tautology.**

3. **WHERE RH HIDES (the exact circular step).** The forcing (B) requires `F†F` to be the SCALAR
   `[deg F]` (one radius, all `|ρ|²` equal) rather than a positive operator with SPREAD spectrum
   (`|ρ|²` not all equal). For the function field that scalarity is the integral trace relation
   `F+F†=[a]`, `FF†=[q]` *inside `End(AV)`* — a genuine endomorphism of a genuine polarization. For the
   conjectural archimedean `F` (zeros = eigenvalues), **`F†F = [deg]·Id` (scalar) is precisely RH**:
   it says every `|ρ|²` equals the same number `deg`. Whether `F†F` is the scalar `[deg]` or a positive
   operator with eigenvalues `|ρ|²` spread off `1/4 + t²` IS RH, restated. The positivity is free; the
   SCALARITY of `F†F` (= the realization of `F` as a true endomorphism of a true polarized archimedean
   AV) is RH.

So: the **radius IS forced by free Rosati positivity** — but the input that positivity consumes is
`F†F = scalar`, i.e. `F` is a genuine endomorphism of a genuine polarized AV with `End` containing the
integral relation. **`deg F` does not "secretly encode RH"; the SCALARITY `F†F=[deg]·Id` does.** The
difficulty is the realization, exactly as the angle hoped — BUT the realization obstruction is not
"merely different/easier": it is `F†F=[deg]·Id` = **RH itself**, because making `F†F` a scalar on the
archimedean space is making every `|ρ|²` equal = RH. The realization is RH-EQUIVALENT, not weaker.

## Anchor / complex / DH

- **ANCHOR (F_q, recover √q w/o zeros):** the radius is recovered ONLY through positivity (B) +
  `F†=[a]−F`, `a∈ℤ` (the integral endomorphism). The tautology (A) alone recovers NOTHING (test 3:
  off-line `F` satisfies it). So the F_q recovery is REAL but routes through `F†F=[q]·scalar ∈ End`,
  which is the integral polarization datum, not a free archimedean fact.
- **COMPLEX (C, positive-definite w/o RH):** PASS — Rosati form `[[2,0],[0,2]]` positive-definite, free
  (test 2). `F†F=deg` for a *canonical* `F` (CM `Nm`) holds tautologically over C — but every `F`
  satisfies it, including ones whose "eigenvalue spread" off a critical line would be RH-violating IF
  the zeros were realized as the spectrum. The positivity is free; it does not by itself constrain a
  GIVEN infinite operator to be a polarized-AV endomorphism.
- **DH:** unposable — no Euler product ⟹ no Frobenius/integral `F` ⟹ no `F†F=[deg]·Id` scalar to
  demand. The radius-bearing datum (scalarity of `F†F`) is exactly the DH-distinguishing piece DH lacks.

## `falsify.py` three axes

- **EULER-BORNE:** the scalarity `F†F=[deg]·Id` is sourced by the Frobenius/Hecke integral structure;
  DH supplies no such `F`. **Euler-silent terminus-characterizer**, same box as M2/M4A/PA2.
- **SEES-ZEROS:** YES — `F†F` scalar `⟺` all `|ρ|²` equal `⟺` on the line (test 4 tracks the line for
  all planted `a`).
- **INDEPENDENT:** NO — the load-bearing input (scalarity of `F†F`, = `F` a genuine polarized-AV
  endomorphism) is RH-equivalent. **The new, sharper content:** the circularity is now pinned to a
  SINGLE precise statement — not "Rosati positivity over ℤ" (the rosati_reflection.py off-diagonal
  framing) but **"`F†F = [deg]·Id` is a SCALAR"** — and the FREE part (positivity itself) is cleanly
  isolated as NOT the obstruction.

## Verdict

`[CIRCULAR]` — but with a clean, decisive new decomposition that corrects the angle's premise. **The
radius is NOT forced by the tautology `F.F†=[deg F]`** (machine-exact off-line counterexample: tautology
holds, `|α|²≠deg`). **The radius IS forced by Rosati positivity, which IS free over C** — confirming the
angle's instinct that positivity is a real RH-free theorem. **But the input that the free positivity
consumes is `F†F = [deg]·Id` (a SCALAR), and on the conjectural archimedean spectrum that scalarity —
every `|ρ|²` equal — IS RH.** So: positivity is free (real escape from one half), the tautology is
vacuous for the radius (the angle's mechanism fails), and the realization obstruction is precisely
`F†F = scalar` = RH-equivalent, not easier. The decoupling recurs as: **POSITIVITY (free) vs SCALARITY
(=RH)**, where prior work (PA2, rosati_reflection) had it as **HL-iso (count) vs HR-equality-clause
(radius=RH)** — the same fault line, now localized to the single operator identity `F†F=[deg]·Id`.

**Next step IF one still hunts:** the only remaining handle is whether `F†F = scalar` can be FORCED by a
structure on the archimedean space OTHER than "`F` is a genuine polarized-AV endomorphism" — e.g. a
self-duality/principal-polarization condition that forces `F†F` to be central. But tests 3–4 show the
scalarity is exactly the integral relation `F+F†=[a]∈End`, and an off-line `F` with `F†F=[deg]·I` (a
scalar!) yet REAL spread eigenvalues EXISTS (test 3 — note `F†F=7·I` there IS scalar, yet off-line,
because the integral relation `F+F†=[a]` had `a=6` violating `a²≤4q`). So even scalarity of `F†F` alone
is NOT enough — the FULL Rosati positivity of the integral form (test 4, `a²≤4q`) is required, and that
positivity over the integral `End` is RH. The honest read: this closes the "tautology forces radius"
route, isolates the genuinely-free piece (Rosati positivity over C, a theorem), and proves the
irreducible residue is `F` being a genuine endomorphism of a genuine polarized archimedean AV whose
integral Rosati form is positive — which is RH, not a weaker realization problem.
