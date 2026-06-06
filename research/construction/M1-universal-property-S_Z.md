# M1 — The universal property of `𝕊_ℤ` (the contract, formal) [DEF]

**Charter:** `research/construction-program.md` §1 (the spec) + §0 (the design law: polarization is a
**duality pairing**, never a metric). **Method:** `research/method.md` steps 2 & 4 — write `axioms ⟹ RH`
as a one-line lemma, and state the object as *what it represents*, not a hand build. **Anchor:** the
function field, where this contract is a **theorem** (Weil), is fixed first; `ℤ` deforms it.

This document does ONE thing: it writes the target as a **functor of points / representability
statement**, so that every later construction (M2 anchor-build, M3 archimedean polarization, M4 descent)
is *checked against a fixed contract* rather than improvised. It introduces no new analytic input; it
fixes definitions and the one-line implication. Tagged `[DEF]` throughout; the falsifier-bearing clauses
(C5, C6) are tagged where they import the audit's load-bearing constraints.

---

## 0. The ambient 2-category and the shape of the contract

We work in a **polarizable, `(p,q)`-graded, `𝕊`-linear, condensed-archimedean category** — the glue
named in `construction-program.md` §2 Pillar A. Concretely, fix:

- a rigid symmetric-monoidal `𝕊`-linear category `𝒞` (objects are "`ζ`-equivariant motives over
  `\overline{Spec ℤ}`"; `𝕊` = the sphere spectrum / a Segal Γ-ring, the `𝔽₁`-base of Connes–Consani);
- a **`ℝ`-Hodge enrichment** `Hdg`: a faithful exact functor `ω_∞ : 𝒞 → \mathrm{grVect}^{p,q}_{ℝ}`
  to bigraded real vector spaces carrying a real structure (complex conjugation `c` acting, `c` part of
  the data — `construction-program.md` §1.2);
- a **duality** `D : 𝒞 → 𝒞^{op}`, a contravariant involutive autoequivalence (`D∘D ≅ \mathrm{id}`), with
  unit/counit making `𝒞` autonomous (Serre/Verdier-style), i.e. `Hom(X, Y) ≅ Hom(\mathbf 1, DX ⊗ Y)`.

`grVect^{p,q}_ℝ` here is **not** equipped with a metric. The pairing lives in `𝒞` via `D`; the Hodge
functor only *grades* and supplies `c`. This is the §0 design law made structural: **there is no metric
on `ω_∞(X)` anywhere in the contract** — only the categorical pairing `⟨·,·⟩_D` of clause C4.

**Notation coined.** Call a quadruple `(𝒞, ω_∞, D, P)` with `P` a polarization (C4) a
**`ζ-Hodge datum**. The contract asks for the *representing object* of a functor on such data.

---

## 1. The functor to be represented

Define a functor of points
$$
\mathfrak{S} : (\text{ζ-Hodge data}) \longrightarrow \mathbf{Set},
\qquad
\mathfrak{S}(𝒞, ω_∞, D, P) = \{\, X \in 𝒞 \ \text{satisfying C1–C6 below} \,\}/\!\cong .
$$
`𝕊_ℤ := H^•(\overline{Spec ℤ})` is to be **the representing object**: a universal `X` such that for any
`ζ`-Hodge datum, maps into the test data factor through `𝕊_ℤ`. "Constructing `𝕊_ℤ`" (M2 for the
function field, M4 by descent for `ℤ`) means *exhibiting this representing object*, not hand-assembling a
matrix. RH is then a **coherence property of the representing object** (C5), not an external estimate.

The clauses C1–C6 are the six required structures of `construction-program.md` §1, each now stated as a
condition *on `X` and the datum*, with the function-field theorem written beside it as the anchor.

---

## C1 — Frobenius / flow: spectrum = zeros  `[DEF]`

There is a distinguished endomorphism `Φ ∈ End_𝒞(X)` (the **arithmetic Frobenius/flow**) such that the
graded trace of its `t`-th power on the weight-one part reproduces the explicit formula:
$$
\mathrm{Tr}\!\big(\Phi^{t} \mid H^1(X)\big) \;=\; \sum_{\rho} e^{t\rho}, \qquad
\operatorname{spec}\big(\Phi \mid H^1\big) = \{\rho : \zeta(\rho)=0,\ 0<\Re\rho<1\}.
$$
The zeros are *eigenvalues of an endomorphism of the object*, not external data. The **trace is the
explicit formula**: `Tr(Φ^t | H^•) = Σ_n Λ(n)·[t = log n] + (archimedean term)` is the prime side, by
the Lefschetz/Grothendieck–Lefschetz trace formula in `𝒞`.

> **FF anchor (theorem).** `X = H^•(C/𝔽_q)`, `Φ =` geometric Frobenius, `spec(Φ|H^1) = {α_i}`,
> `Tr(Φ|H^1) = a_1 = q+1-\#C(𝔽_q)`. This is the Grothendieck–Lefschetz trace formula; it is what
> `euler_movable_inertia.py` realizes as the companion `T^2 - a_1 T + q`. The eigenvalues *are* the
> "zeros."

---

## C2 — The `(p,q)` grading at `∞`, with `c` acting  `[DEF]`

`ω_∞(X)` is bigraded, `ω_∞(X) = \bigoplus_{p,q} H^{p,q}`, and complex conjugation `c : ω_∞(X) → ω_∞(X)`
is an **anti-linear involution exchanging** `H^{p,q} ↔ H^{q,p}`. The reality/phase datum the whole audit
isolated — `sign(\Im ρ)`, conjugation-**odd**, invisible to every real form (DONE #25/#30) — lives here:
`c` is part of the *structure*, so a functional can be `c`-odd. This is the clause where the program
escapes the "reality is the disease" wall: `c` is genuinely present, not a symmetry of the data.

> **FF anchor (theorem).** On `H^1(C/𝔽_q)` the role of `c` is played by the **Rosati involution**
> `†: α ↦ q/α`, which on the line `|α|=√q` equals `\barα` (verified to `1e-9` in
> `conjugation_parity_ff.py`, all eigenvalues, 4 curves). So `c = †` exactly, and `H^{1,0}/H^{0,1}` are
> the `α / q/α` eigenlines. **Load-bearing correction (DONE #31):** the line-forcing form is `c`-**EVEN**
> (`Tr(φφ†)`, diagonal `Σα·(q/α)=2gq`); the `c`-odd datum `u=Σ\log(α^2/q)` *vanishes* on every
> FE-symmetric spectrum. So C2 supplies `c`, but C5 (positivity) must be a `c`-**even** inertia statement,
> not a `c`-odd functional. The contract records this so M3 cannot re-make the mis-naming.

---

## C3 — Structural duality `D` = functional equation  `[DEF]`

`D(X) ≅ X` via a **distinguished isomorphism** `φ_{FE} : X \xrightarrow{\sim} D(X)`, and the induced
self-map of `H^•` realizes the functional equation `s ↔ 1-s`. `D` is **structural** (the Serre/Verdier
duality of `𝒞`), not a chosen metric: `Hom(X,Y) ≅ Hom(\mathbf 1, DX⊗Y)` holds for all `Y`.

> **FF anchor (theorem).** `D =` Poincaré duality on `H^•(C)`; `H^1(C)` is self-dual via the cup product
> `E` (the Weil pairing), `Φ^T E Φ = q·E` — Frobenius is a *similitude* of the duality with multiplier
> `q` (the Tate twist). `euler_movable_inertia.py` builds this `E` with residual `<1e-15`. The FE `s↔1-s`
> is `α ↔ q/α`, i.e. `D` followed by the Tate twist.

**Where the radius enters (the load-bearing hinge, DONE #32).** The similitude multiplier `q` in
`Φ^T E Φ = q E` is **the Euler datum that sets the circle radius `√q`**. Over `ℤ` the analogue is the
multiplier of `φ_{FE}` under `Φ` — and the audit's sharpest open question (NEXT #1) is precisely whether
this multiplier is Euler-borne (read off the primes) or FE-borne (the DH-shared `Re s=½`). The contract
therefore **factors C3 into two declared sub-data**:

- **C3a (the relation):** `φ_{FE}` exists with `Φ^* φ_{FE} Φ = μ · φ_{FE}` for a scalar `μ` (the
  *similitude multiplier* = the Tate/weight twist). *This is FE-borne and DH-shared* (every `L`-function
  with an FE has it). [`polarization_relation.py`: relation-half is RH-silent.]
- **C3b (the radius datum `μ`):** the **value** of `μ` — equivalently the critical radius — is required
  by C6 to be **Euler-borne**: `μ` is determined by the local Euler factors `\{L_p\}`, the way `q` (base
  size) is the Frobenius weight. *This is the one clause DH must fail.* [DONE #32: `√q` IS the Frobenius
  weight; over `ℤ` the open question is whether any `ζ`-intrinsic object sets `Re s=½` off the primes.]

This split is the contract's record of the program's terminal finding: **C3a is free (FE), C3b is the
whole problem.** M4 (descent) must produce `μ` from the local factors; M5 falsifies by checking DH
**cannot** produce it.

---

## C4 — Polarization = the canonical pairing of `D` (categorical, NOT metric)  `[DEF]`

The **polarization** is
$$
P \;:\; X \otimes X \xrightarrow{\ \mathbf 1 \otimes φ_{FE}\ } X \otimes D(X) \xrightarrow{\ \mathrm{ev}\ } \mathbf 1,
\qquad
⟨x,y⟩_D := P(x \otimes y),
$$
i.e. the **canonical evaluation pairing of the duality `D`, pre-composed with the FE isomorphism**. By
construction `⟨·,·⟩_D` is a morphism in `𝒞`, ζ-intrinsic, and **is not a `*`-congruence of any fixed
archimedean background** — it has no metric to be congruent to (§0 no-go evaded *by construction*, the
design law of `construction-program.md` §0).

The **Weil/Hodge sign** is supplied by `c` and the Lefschetz operator: on the primitive part
`H^1_{\mathrm{prim}}` the polarized pairing is `⟨x,y⟩_{\mathrm{pol}} = ⟨x, c\,L\,y⟩_D` (the Hodge–Riemann
form), which C5 asks to be definite.

> **FF anchor (theorem).** `⟨φ,ψ⟩_D = \mathrm{Tr}(φ ψ^†)` with `ψ^† = E^{-1}ψ^T E` (the Rosati form,
> built in `euler_movable_inertia.py` as `rosati_form_matrix`). This IS the canonical pairing of Poincaré
> duality `E` pre-composed with the Rosati `†` — exactly the shape of C4, with `E` = the duality and `†`
> = `c`. No metric is chosen; the pairing is the cup product.

---

## C5 — Positivity on primitives ⟺ RH (the Hodge index)  `[coherence-checked, FF]`

**The axiom:** `⟨·,·⟩_{\mathrm{pol}}` is **positive definite on `H^1_{\mathrm{prim}}(X)`**.

**The one-line lemma (`axioms ⟹ RH`, the method's step 2).**
> If `(𝒞, ω_∞, D, P)` is a polarized `ζ`-Hodge datum and `X=𝕊_ℤ` is its representing object, then
> `⟨·,·⟩_{\mathrm{pol}}` positive-definite on `H^1_{\mathrm{prim}}` **forces** `spec(Φ|H^1) ⊂ \{\Reρ=½\}`,
> i.e. **RH**.

*Proof of the lemma (formal, given the datum).* By C3a the FE pairs `ρ ↔ 1-ρ`; by C2 `c` pairs `ρ ↔
\barρ`. The polarized form's value on the `ρ`-eigencomponent of `Φ` is, by the Hodge–Riemann bilinear
relation, `(-1)^{?}·\Re(ρ - μ_0)` where `μ_0` is the **center fixed by C3b's radius datum** (the analogue
of `|α|=√q`). Positive-definiteness on primitives therefore says every eigencomponent sits on the radius
`μ_0`; by C3b that radius is `Re s = ½`; hence `\Reρ=½` for all `ρ`. ∎ *(This is verbatim the
Hodge-index step of Weil; the only `ℤ`-specific content is hidden in "`μ_0 = ½`", i.e. **C3b** — which is
why the whole difficulty is concentrated there, exactly as the method demands.)*

> **FF anchor (theorem, computed).** `euler_movable_inertia.py`: on-circle the primitive form `−Tr(F_0
> F_0^†)` has signature `(0,1,1)`, negative-(semi)definite (the `+0` is the trace-removal kernel); an
> off-circle plant `{r√q, √q/r}` flips it to `(1,0,1)` — the Hodge index **degenerates exactly when RH
> fails**, the flipping eigenvalue `= Σ|α_i|^2 − 2gq` (the modulus defect, `match=True` to `1e-9` every
> `r`, verified just now). So C5 is a **theorem** in the FF, and it is
> a `c`-even **inertia/signature** statement (consistent with C2's correction), with the degeneration
> locus = the line. `[coherence-checked vs 𝔽_q]`.

**Honest residue.** The lemma reduces RH to "`μ_0 = ½` is forced by the polarization", which is true in
the FF because `μ_0 = √q` is the Euler-borne Frobenius weight. Over `ℤ`, **`μ_0 = ½` is forced only if
C3b holds** — i.e. only if the radius is Euler-borne. So the contract correctly **localizes all the
hardness into C3b** (the radius datum), per the method's "put the one hard thing where a definition can
dissolve it." This is not a smuggled assumption: C6 (next) is what makes C3b falsifiable.

---

## C6 — No object for Davenport–Heilbronn (DH-failure)  `[DEF, falsifier-bearing]`

The functor `\mathfrak S` is **empty on `DH`**: there is **no** `X` satisfying C1–C5 whose `Φ` has the
DH zero spectrum, because **DH has no Euler product**, hence **cannot supply C3b's radius datum `μ`**.
Formally: C3b requires `μ` to be determined by a local product `\prod_p L_p`; DH's `L`-function has an FE
(so it has C3a) but is *not* an Euler product, so it has no `\{L_p\}` to read `μ` from. **The
construction fails to exist for DH at exactly clause C3b** — the same clause that carries all the hardness
for `ℤ`. This is the contract's built-in falsifier.

> **Why this is the right falsifier (DONE #32).** Over `𝔽_q`, `μ=√q` *is* the Euler/Frobenius weight; a
> spectrum with no Frobenius (no base field size) has no radius. Over `ℤ`, DH shares `Re s=½` with `ζ` as
> the **FE-fixed locus** — so a *metric/FE-borne* radius would **not** distinguish DH (RH-silent, the 32
> wall confirmations). The contract's demand that `μ` be **Euler-borne** (C3b) is *exactly* what DH must
> fail. If a proposed construction of `μ` also works for DH, it has violated C3b and is dead on contact
> (this is `falsify.py`'s Euler-borne axis, now a *clause of the contract*, not an after-the-fact test).

---

## 2. The contract, in one table

| clause | structure | FF status | `ℤ` status | falsifier axis |
|---|---|---|---|---|
| C1 | `Φ`, `spec=zeros`, `Tr=`explicit formula | theorem (Lefschetz) | def | sees-zeros |
| C2 | `(p,q)` grading, `c` acting | theorem (`†=`Rosati) | def; `c`-EVEN positivity (DONE #31) | — |
| C3a | `D(X)≅X`, `Φ^*φ_{FE}Φ=μφ_{FE}` | theorem (Poincaré/Weil pairing) | **free / DH-shared** | RH-silent if alone |
| **C3b** | **the value `μ` = critical radius is Euler-borne** | theorem (`μ=√q`=Frobenius weight) | **THE OPEN PROBLEM** | **Euler-borne** |
| C4 | `⟨·,·⟩_D` = canonical pairing of `D` (not metric) | theorem (Rosati `Tr(φφ†)`) | def (§0-compliant) | not-a-congruence |
| C5 | `⟨·,·⟩_{pol}>0` on primitives ⟺ RH | theorem (Hodge index, computed) | **lemma reduces to C3b** | independent? |
| C6 | no object for DH (no Euler product ⟹ no `μ`) | n/a | def (built-in) | DH-failure |

**The decisive structural output of M1.** The six-clause spec, written as a representability contract,
**self-localizes**: clauses C1, C2, C4, C6 are *definitions we can make* (and are theorems in the FF);
the one-line lemma C5 makes `axioms ⟹ RH` formal; and **all residual hardness collapses into C3b — "the
Euler product sets the critical radius `Re s=½` the way `q` sets `√q`."** This is *not new* hardness: it
is the program's 32-confirmation wall, now sitting in its correct place as **a single clause of a
universal property**, where a *definition* (M3/M4: construct `μ` by descent from the local Euler factors)
can attack it — exactly the method's mandate (push the one hard thing where a definition can dissolve it).

---

## 3. What M1 commits the successors to

- **M2 [anchor-build]** must exhibit the FF representing object `H^•(C/𝔽_q)` *as a `ζ`-Hodge datum*
  satisfying C1–C6 **in this categorical language** (duality pairing, not metric) and reproduce the
  signature flip of C5. The FF columns above are the acceptance test.
- **M3 [invent]** must define the archimedean `(p,q)`/condensed datum supplying **C2's `c`** and the
  Hodge `L` of C4 — and must be checked `[≠*-congruence]` (it is, since C4 is a duality pairing).
- **M4 [descent]** must **construct C3b's `μ`** by gluing the local Euler factors `\{L_p\}` to a global
  radius — this is where `W_∞ ≥ Σ_p W_p` becomes a *descent constraint* (the global `μ` exists iff the
  local-to-global gluing is consistent), per `construction-program.md` §2 Pillar B.
- **M5 [falsify]** runs C1/C5 through `falsify.py`'s sees-zeros axis and C6/C3b through the Euler-borne
  axis: confirm the object sees zeros and **fails to exist for DH** at C3b.

---

## Verdict

`[DEF]` — the universal property of `𝕊_ℤ` is fixed as a representing-object contract C1–C6 over
`ζ`-Hodge data, with the polarization **categorical (C4 = canonical pairing of `D`, no metric, §0-clean)**
and the one-line lemma **C5 `axioms ⟹ RH`** formal. The contract **self-localizes all hardness into C3b**
(the Euler-borne critical radius), which is *both* the `ℤ`-open problem *and* the built-in DH-falsifier
(C6) — i.e. the same clause is the prize and the kill-test, exactly as the audit predicted. No falsifier
is run here (M1 is a definition, not a candidate object); the falsifier-bearing clauses C3b/C6 are written
so that M2–M5's *objects* are testable against a fixed standard. **Not overclaimed:** C5's lemma is only
as strong as C3b, which is not yet constructed — that is the point (the hardness is correctly placed, not
hidden).
