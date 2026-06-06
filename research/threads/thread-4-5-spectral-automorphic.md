# Threads 4 + 5 — spectral / automorphic positivity (opened 2026-06-06)

Audit of the two "spectral positivity" levers in `positivity-program.md` §A against the standing
kill-test (`positivity-program.md` §B): a candidate forcing positivity must be **(a) Euler-product-
borne**, **(b) fail for Davenport–Heilbronn** (a linear combination `L(s,χ_{5,2}) + L(s,χ̄_{5,2})` of
two modulus-5 Dirichlet L-functions — *same `Γ_ℝ`, functional equation, but no Euler product and
provably zeros off the line*), and **(c) not reduce to the assumed `λ_n ≥ 0`** (circular with Weil
positivity) or a graveyard route.

Tagging per `STRATEGY.md` §8: **[THM]** proven, **[CONJ]** conjectured/hypothesised, **[PROG]** an open
program/research direction, **[AN]** formal analogy. Quotes are verbatim from the cited sources; nothing
is fabricated.

Primary sources:
- Sarnak/Beuzart-Plessis school — *The relative trace formula in analytic number theory*
  (arXiv:1912.08137); ARCC workshop *Relative trace formula and periods of automorphic forms*.
- Jacquet, Guo, Waldspurger — RTF and central-value positivity (Waldspurger's formula; Guo's
  `L(1/2,π) ≥ 0`).
- Frenkel–Langlands–Ngô; *Local and global questions "beyond endoscopy"* (arXiv:2310.02438) — poles,
  not zeros.
- Bombieri — *Remarks on Weil's quadratic functional…* (the explicit-formula quadratic form, PSD ⟺ RH).
- Connes, *An essay on RH* [Ce]; Connes–Consani [CC20] (arXiv:2006.13771) — archimedean Weil positivity.
- Bost–Connes (1995), *Hecke algebras, type III factors and phase transitions…*; Connes–Marcolli
  (Q-lattices / GL₂ system); *Riemann hypothesis and Quantum Mechanics* (arXiv:1012.4665).

---

## Thread 4 — Langlands / relative trace formula (RTF)

### 4.1 The most concrete positivity the RTF offers — and it is the WRONG positivity

The relative trace formula (Jacquet) equates two period-distributions; its spectral side, after the
Waldspurger / Jacquet–Rallis matching, produces an **honest nonnegativity of central special values**:

> **[THM, Guo / via RTF].** `L(1/2, π) ≥ 0` for the relevant automorphic representations — proved by
> Guo using the relative trace formula, *independently of RH*. Waldspurger's formula expresses a toric
> period as `|period|² ∝ L(1/2, π × χ)`, forcing `L(1/2, π × χ) ≥ 0` (a square is nonnegative).

This is the genuine, load-bearing positivity of the automorphic spectral side: **a period is an
`L²`-norm, and `|period|² ≥ 0` gives `L-value ≥ 0`.** It is real, and Euler-product-compatible. **But it
constrains the *value at the central point `s = 1/2`*, not the *location of the zeros*.** The
search-confirmed status of the converse:

> "The Generalized Riemann Hypothesis implies that `L(1/2, π × χ) ≥ 0`, but Waldspurger's formula is
> not explicit enough to conclude this directly… the nonnegativity of central L-values *follows from*
> the Riemann hypothesis [and] does not, conversely, imply the zeros lie on the critical line — the
> nonnegativity is a weaker consequence than what the full Riemann Hypothesis would provide."

So the RTF positivity sits **orthogonal** to RH: `L(1/2) ≥ 0` is a *downstream consequence* of RH, and
positivity of the period proves it *unconditionally* — which means it cannot, even in principle, be the
forcing input for RH. It does not see zeros at all.

**Verdict (1): NOT a new lever for RH; not circular with Weil positivity either — it is a *different,
weaker* positivity (central-value, not zero-location). It is "new" only in the trivial sense of being a
distinct true statement that does not bear on the line.** `[THM]` for what it proves; `[—]` for RH.

### 4.2 Beyond endoscopy — poles, not zeros; no RH positivity

Langlands' beyond-endoscopy weights the trace formula by `L`-functions and takes **residues at poles**
(Frenkel–Langlands–Ngô removing the trivial rep; Venkatesh/Sarnak via Kuznetsov for `Sym²` on GL(2)):

> "weighing the trace formula by L-functions, and taking residues *at the poles* of those, one could
> detect the images of functorial lifts… One had to introduce L-functions 'by hand,' whose *poles* had
> the role of picking up the images of functorial lifts." (arXiv:2310.02438)

The program is about the **pole at `s = 1`** (functoriality / order of pole of `L(s, π, ρ)`) and
Ramanujan bounds — *not* about zeros, and **carries no positivity inequality bearing on the critical
line**. Confirmed: the survey "contains no discussion of positivity conditions, Riemann Hypothesis, or
zero locations." **[PROG]; RH-neutral.**

### 4.3 Arthur trace formula spectral-side positivity — and Bombieri's quadratic functional

- Arthur's spectral side is a sum over cuspidal data of distributions built from truncated Eisenstein
  series; recent work (Finis–Lapid–Müller) gives **absolute convergence**, but the spectral side is an
  *identity of distributions*, **not** a positive form. No spectral-side positivity of Arthur's TF is
  known that specializes to Weil positivity. `[THM]` (convergence); no RH positivity.
- **Bombieri's quadratic functional is exactly Weil's explicit-formula form**: PSD ⟺ RH `[THM]`. In the
  automorphic setting this is precisely `Σ_v 𝒲_v(g ∗ ḡ^♯) ≤ 0` ([CC20] eq. (2)). So when the RTF/Arthur
  side *does* carry a positivity that bears on zeros, **it is the Weil functional itself** — i.e.
  **circular** (= assumed `λ_n ≥ 0`), not a new lever.

### 4.4 Is Weil positivity a shadow of an automorphic period positivity?

**No — not as the RTF supplies it.** The two automorphic positivities are:
- **period positivity** `|period|² ≥ 0 ⟹ L(1/2) ≥ 0` — load-bearing, Euler-product-friendly, but a
  *central-value* statement, blind to off-line zeros (§4.1);
- **Weil/Bombieri positivity** `Σ_v 𝒲_v ≤ 0 ⟺ RH` — bears on zeros, but is RH restated (§4.3).

There is no proven bridge making the second a *shadow* of the first; the bridge would itself be RH. The
Sarnak "RH for L-functions in families" program is **statistical** (one-level densities, low-lying
zeros match a symmetry-type random-matrix ensemble) — strong *evidence*, and it correctly predicts
different behaviour for families with vs. without an Euler product, but it is **not a positivity
forcing structure**; it describes the *distribution* of zeros assuming, or testing, RH.

### 4.5 Kill-test (thread 4)

- **Euler-product-borne?** The *period/Waldspurger* positivity is **not** Euler-product-borne — it is
  `L²`-norm positivity of a period and holds for any automorphic `π` whether or not its `L` has the
  forcing structure. It therefore **fails the kill-test at (a)**: it does not know about the Euler
  product, hence cannot exclude DH.
- **Davenport–Heilbronn:** DH `= L(s,χ_{5,2}) + L(s,χ̄_{5,2})` is a **linear combination** of two GL(1)
  automorphic `L`-functions, each of which *individually* satisfies its own (G)RH and is a genuine
  period/`L²` object — so the automorphic period positivity **holds for each summand and says nothing
  about the sum**, which has no Euler product and provably has zeros off the line. The RTF positivity
  **does not exclude DH** because it never operated on the combined object at all. **Fails the
  DH-falsifier** exactly as Nyman–Beurling does (`positivity-program.md` §C: "holds for DH ⟹
  dispersing").
- **Circular?** The only RTF/Arthur positivity that *does* bear on zeros is the Weil/Bombieri functional
  = assumed `λ_n ≥ 0`. **Circular.**

### 4.6 Where it stalls
The RTF manufactures the *easy* positivity (central values, the consequence of RH) with great success,
and is silent on the *hard* one (zero location). Beyond endoscopy reaches the **pole at `s=1`**
(functoriality) but the analytic machinery to weight by log-derivatives and isolate the *zeros* is, in
Langlands' own framing, "prohibitively difficult to manage," and even then would only re-derive the
explicit formula — the RH-neutral identity.

### 4.7 Most concrete next step (thread 4)
A *falsification-first* experiment, runnable in the existing `weil_form.py` / `explicit_formula.py`
scaffold: take the DH function as a degree-2 automorphic-type object (`L(χ_{5,2}) + L(χ̄_{5,2})`) and
**confirm that every RTF-style positivity candidate (period-norm, Waldspurger central value) evaluates
nonnegative on DH** — i.e. mechanically certify that RTF positivity is DH-blind. If (as expected) it
passes for DH, thread 4 is **closed as dispersing**, and the auditor row is set. The only RTF avenue
that survives is *globalising the Sonin/Weil operator positivity* (§5.4), which is thread 0, not a new
automorphic lever.

---

## Thread 5 — Noncommutative geometry (Connes) + Bost–Connes / QSM

### 5.1 Where the NCG positivity stalls — exactly

The spectral realization ([C99]; [Ce]) is **engineered around the critical line, not forcing it**: the
absorption spectrum on `L²_δ(X_K)₀` is visible only after inserting the Sobolev weight
`ρ(x)=(1+log²|x|)^{δ/2}`, and ([Ce] p.13, quoted in `deninger-spectral-cohomology.md` §2.2) "δ
artificially cuts the multiplicities of the zeros" and the construction "only sees the zeros on the
critical line." Off-line zeros would show as **resonances**, not missing absorption lines — so the
Hilbert-space statement **does not by itself prove RH**. RH ⇔ **Weil positivity** `Σ_v 𝒲_v(g∗ḡ^♯) ≤ 0`
([CC20] eq. (2)).

> **[THM, CC20].** The single archimedean inequality `W_∞(g∗g^*) ≥ Tr(ϑ(f) 𝐒 ϑ(f)^*) ≥ 0` holds: the
> Sonin-space compression `𝐒` makes the trace **positive by construction**, and differs from `−W_ℝ` by
> a **compact** operator.

**The stall is sharp and unchanged since 2020:** positivity is `[THM]` only **at `∞` and in the
simplest semilocal cases** `{∞, 2, …, p}`. The **global** Weil positivity over *all* places
simultaneously — which is RH — is **open**, and the missing geometry is, in Connes' own boxed words,
"an **intersection theory and a Riemann–Roch theorem on the square of the arithmetic site `Â × Â`**…
no Serre duality or good cohomological version of `H^{j≠0}`." That `Â × Â`-Hodge-index positivity is
the **same wall** as `λ_n ≥ 0` (`positivity-program.md` §B last row). So the NCG operator positivity,
where it bears on zeros, **is** Weil positivity — **circular**, not a new lever. `[THM]` at `∞`;
`[CONJ]/[PROG]` globally.

### 5.2 The Bost–Connes / QSM lever — is KMS/Gibbs positivity a *genuinely different* lever?

The BC system: `C*`-algebra `C*(ℚ/ℤ) ⋊ ℕ^×`, time evolution `σ_t`, with

> **[THM, Bost–Connes 1995, Thm 5(c)].** the **partition function is `ζ(β)`**; there is a **phase
> transition at inverse temperature `β = 1`** with **spontaneous symmetry breaking**: for `β ≤ 1` a
> unique KMS state; for `β > 1` the extremal KMS_β states are indexed by embeddings (`Gal(ℚ^ab/ℚ)`
> acts), partition function `ζ(β)`; the system sits on a **type III₁ factor**.

The thermodynamic positivity here is the **KMS / Gibbs positivity**: `φ_β(a^* a) ≥ 0`, the positivity
of an equilibrium state (a state is a positive functional). The pole of `ζ` at `β = 1` is the
**partition-function divergence** = the phase transition. This is genuinely a *different kind* of
positivity (state-positivity / convexity of the free energy) than the explicit-formula quadratic form.

**But the decisive question — does it see the *zeros*?** The answer from every source is **no, not the
zeros' location**:

- The BC partition function being `ζ(β)` is a statement about `ζ` on the **real axis `β > 1`** (the
  region of absolute convergence / the pole at `1`). KMS/Gibbs positivity `φ_β(a^*a) ≥ 0` is automatic
  for *any* `C*`-dynamical system with a trace and **does not encode where `ζ` vanishes**. The BC
  construction "realizes `ζ` as a partition function + the Galois symmetry (`Hilbert 12`)" — it is a
  triumph about **special values / class field theory**, and **RH is not addressed within the BC
  framework itself**: it is neither theorem nor even a clean conjecture there; it is a *hope* ("there
  might be a way to shed insight on RH").
- The only route from QSM *to the zeros* (Connes–Marcolli; *RH and Quantum Mechanics* arXiv:1012.4665)
  re-expresses RH as an **inequality on the same `ζ`-data** (e.g. a Robin/Lagarias-type
  `N_q|φ_β(N_q)|ζ(β−1) > e^γ log log N_q` for primorials, or — in the adele-class-space incarnation —
  "the Riemann hypothesis becomes equivalent to the **positivity of the relevant trace pairing**,
  mirroring Weil's proof"). **Every version that touches the zeros routes back through the Weil/trace
  positivity** or an elementary `ζ`-inequality. The thermodynamic positivity does **not** independently
  constrain the zeros.

**Verdict (QSM): the KMS/Gibbs positivity is a genuinely *different* positivity (state-positivity, on
the real `β`-axis, about the pole and Galois symmetry), but it is NOT a different lever on RH — it is
RH-silent.** When the QSM framework is pushed to say anything about zeros (Connes–Marcolli's adele class
space), the positivity it produces **reduces to Weil positivity** (`Σ_v 𝒲_v ≤ 0`). So: a new
*thermodynamic positivity*, **yes**; a new lever *on the location of the zeros*, **no**. `[THM]` for the
phase transition and partition function; `[CONJ]/hope` for any RH bearing.

### 5.3 Kill-test (thread 5)

- **Euler-product-borne?** The BC partition function `ζ(β) = Π_p (1−p^{-β})^{-1}` **is** the Euler
  product on the real axis — so QSM is *Euler-aware* in a way the RTF period positivity is not. This is
  the one genuinely encouraging feature. **But** the Euler product enters as the **partition function on
  `β > 1`** (convergence region), where it says nothing about the line `Re s = 1/2`. The Euler structure
  is present but **not deployed against the zeros**.
- **Davenport–Heilbronn:** here is the sharp test. DH = `L(χ_{5,2}) + L(χ̄_{5,2})` has **no Euler
  product ⟹ no partition-function / QSM interpretation as a single Bost–Connes-type system** (a BC/QSM
  system's partition function is *by construction* an Euler product; a sum of two `ζ`-type functions is
  not the partition function of a crossed-product of the required form). **So QSM correctly *refuses to
  represent* DH** — it cannot even form the object. This is the structurally correct exclusion: unlike
  Nyman–Beurling/RTF which *evaluate positive on DH*, QSM **does not admit DH at all**. *However*, this
  exclusion lives entirely in the **partition function (real axis), not in a zero-forcing positivity** —
  QSM excludes DH for the right reason (no Euler product) but at a stage that does not yet force the
  zeros. It passes (a) and (b) **in spirit** but only because it never reaches the zeros (c is moot /
  collapses to Weil when it does).
- **Circular?** Connes–Marcolli's adele-class-space positivity = Weil positivity ⟹ **circular** at the
  point of contact with the zeros.

**Net:** QSM is the **only** candidate in this audit that is *both* Euler-product-borne *and* DH-
refusing — but it achieves this on the **partition-function / real axis**, and the bridge from there to
a positivity that forces the zeros is exactly the unbuilt `Â×Â` intersection theory of §5.1. The
Euler-awareness is real and is the reason QSM is worth keeping; the zero-forcing is absent.

### 5.4 Where it stalls
Identical wall to CC20 / thread 0: positivity proven **only at `∞` / semilocally**; the **global** Weil
positivity (= the `Â×Â` Hodge index) is unconstructed. QSM adds a real-axis Euler-borne positivity but
no mechanism carries it across the functional equation onto the critical line.

### 5.5 Most concrete next step (thread 5)
The lever worth testing is the **`β`-deformation**: the BC/QSM positivity is a *one-parameter family*
of states `φ_β` with a phase transition at `β=1`. The unexplored question is whether the **KMS
state-positivity, transported under the functional-equation / scaling symmetry, can be made to
interpolate to a positivity at the symmetric point** (the analogue of `β = 1/2`), i.e. whether the
thermodynamic convexity of the free energy `F(β) = −log Z(β) = −log ζ(β)` has a reflection-positive
continuation through `β = 1` (this is the natural meeting point with **thread 1, reflection
positivity**, and thread 6). Concretely, in the scaffold: model `F(β)` and its Legendre/convexity
structure and **test whether the convexity survives for the DH partition function surrogate** — if DH
(no Euler product) breaks the convexity/KMS structure where `ζ` keeps it, that is a *new* Euler-borne
falsifier worth promoting through `weil_form.py`. This is the single most concrete way to find out if
the thermodynamic positivity is a real lever rather than a restatement.

---

## Summary verdicts

**RTF positivity verdict.** The relative trace formula carries a real, load-bearing positivity —
`|period|² ≥ 0 ⟹ L(1/2, π) ≥ 0` (Waldspurger/Guo) — but it is the **central-value** positivity, a
*consequence* of RH, **blind to zero location**. It is **not Euler-product-borne** (it is `L²`-norm
positivity of a period), and it therefore **fails the DH kill-test** (it holds termwise for the two
Dirichlet `L`-summands of DH and says nothing about their off-line sum) exactly like Nyman–Beurling —
**dispersing**. Beyond endoscopy reaches **poles** (functoriality at `s=1`), not zeros, and is
RH-neutral. The only RTF/Arthur/Bombieri positivity that *does* bear on zeros **is** the Weil
explicit-formula functional — **circular** with the assumed `λ_n ≥ 0`. **No new lever.**

**QSM / NCG positivity verdict.** NCG's operator positivity is `[THM]` **only at `∞`** (CC20 Sonin-space
compression); the **global** positivity is open and **is** the `Â×Â` Hodge-index wall = `λ_n ≥ 0`
(**circular**). The **Bost–Connes / QSM KMS–Gibbs positivity is a genuinely *different* positivity**
(equilibrium-state positivity / free-energy convexity, on the real `β`-axis), and it is the **only**
candidate here that is simultaneously **Euler-product-borne** (partition function `= Π_p(1−p^{-β})^{-1}`)
and **DH-refusing** (DH has no Euler product, so it is not the partition function of any BC-type system).
**But** this positivity lives on the **real axis / partition function and is silent about the zeros**;
every QSM route that reaches the zeros (Connes–Marcolli adele class space) **reduces to Weil positivity**.
So: a new *thermodynamic* positivity, **yes**; a new *lever on RH*, **not as currently built**.

**Are either a new lever?** Thread 4: **no** (dispersing or circular). Thread 5: **the QSM KMS
positivity is the one genuinely new *kind* of positivity surfaced in this audit and the only
Euler-borne / DH-refusing one — but it does not yet reach the zeros; at the point it would, it
collapses to Weil positivity.** Keep thread 5 (QSM) live; demote thread 4 (RTF) to dispersing.

**Kill-test summary.**

| lever | Euler-borne? | excludes DH? | reaches zeros? | verdict |
|---|---|---|---|---|
| RTF period / Waldspurger positivity | no (`L²`-norm of period) | **no** (holds termwise on DH summands) | no (central value `L(1/2)`) | **dispersing** |
| beyond endoscopy | n/a (poles at `s=1`) | n/a | no | RH-neutral |
| Arthur / Bombieri quadratic form | yes (= explicit formula) | yes | yes — but **is** Weil form | **circular** (`= λ_n≥0`) |
| NCG operator positivity (global) | yes | yes | yes — but **is** `Â×Â` Hodge index | **circular** (`= λ_n≥0`) |
| **BC / QSM KMS–Gibbs positivity** | **yes** (partition function) | **yes** (no Euler product ⟹ no BC system) | **no** (real axis only) | **new kind, RH-silent** — keep |

**Single most concrete next step.** Test whether the **free-energy convexity / KMS positivity of
`F(β) = −log ζ(β)`** (the genuinely new, Euler-borne, DH-refusing thermodynamic positivity) admits a
**reflection-positive continuation through the phase transition `β=1` toward the symmetric point**, and
whether the **DH partition-function surrogate breaks that convexity where `ζ` preserves it**. If so, QSM
yields a *new* Euler-borne falsifier — promote it through `weil_form.py` and meet thread 1 (reflection
positivity) / thread 6 there. If the convexity is DH-blind too, close thread 5's QSM branch as
real-axis-only and fall back to thread 0 (globalising the CC20 Sonin positivity).

## Auditor rows to fold back into `positivity-program.md`
- §C tracker: `automorphic / RTF positivity` → **dispersing** (period positivity = central-value
  `L(1/2)≥0`, not Euler-borne, holds for DH); the only zero-bearing RTF form is the Weil functional
  (circular).
- §C tracker: `QSM / KMS (BC system)` → **new kind of positivity (thermodynamic, Euler-borne,
  DH-refusing) but RH-silent**; reduces to Weil positivity at the adele-class-space point of contact.
  Keep live pending the `β`-convexity / reflection-positivity test (§5.5).
- §B auditor: add row — *BC/QSM partition function `Z(β)=ζ(β)=Π_p(1−p^{-β})^{-1}`* → over `ℤ`
  **transfers on the real axis `β>1`** (Euler product + Galois `Hilbert-12` symmetry, `[THM]`);
  **breaks** at the critical line — no construction carries the KMS positivity across the functional
  equation to `Re s = 1/2`.
