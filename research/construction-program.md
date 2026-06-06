# Construction mode — building the object (the charter, 2026-06-06)

We shift from audit to **construction**. We do the categorical work; we invent language where the
existing language can't hold the object; we are patient and we accept the risk. The audit phase is
done — every reformulation converges on one wall — and its job was to hand construction a **sharp
target, a hard no-go, and a falsifier.** We now build the object the spec demands. Posture: we intend
to go further than the existing programs, and the way we earn that is by exploiting what they didn't
start with — a *constructive constraint* the audit proved.

---

## 0. The decisive gift the audit hands construction (our actual advantage)

The audit's terminal no-go: **any form that encodes RH as a `*`-congruence of a fixed (DH-shared)
archimedean background is Sylvester-inertia-locked** — RH-silent, for real OR complex structures. We
spent this whole program reading that as a wall. *In construction mode it is a design law:*

> **CONSTRUCTIVE COROLLARY (the spine of the plan): the polarization must be CATEGORICAL — a duality
> pairing — NOT a metric.** Any object built as "a space with a metric" yields a `*`-congruence form
> and dies by Sylvester. Therefore the object must be built in a category whose **duality is structural
> (Verdier/Serre-autonomous)** and whose polarization is the *canonical pairing of that duality*, which
> is ζ-intrinsic by construction and cannot be reduced to a congruence of the archimedean data.

This rules out the metrized-Arakelov approach *a priori* and points at a single target shape: a
**polarized arithmetic Hodge category** (Tannakian, with duality). That redirection — from *metrized
space* to *polarized category* — is the one genuinely new strategic input we own, and it is forced,
not chosen.

## 1. The target, as a universal property (the contract — not a construction yet)

Build a category `𝒞` and a cohomology functor `H: 𝒞 → grVect_dual` with a distinguished object
`𝕊_ℤ = H^•(\overline{Spec ℤ})` such that **[the spec, sharpened by the whole program]**:
1. an endomorphism (Frobenius/flow) `F` with `Tr(F^t \mid H^1) = Σ_ρ e^{tρ}` (zeros = `spec F`);
2. a **(p,q)/Hodge grading at `∞`** where complex conjugation is part of the structure;
3. a **structural duality** `D: 𝒞 → 𝒞^{op}` with `D(𝕊_ℤ) ≅ 𝕊_ℤ` realizing the functional equation;
4. a **polarization** `⟨·,·⟩` = the canonical pairing of `D` (categorical, not metric);
5. `⟨·,·⟩ > 0` on the primitive part **iff RH** (the Hodge index of the polarized category);
6. **no such object for Davenport–Heilbronn** (no Euler product ⟹ `𝕊_DH` is not in `𝒞`).

`𝕊_ℤ` is to be *constructed as the representing object of this functor*, not built by hand.

## 2. The strategy — three pillars

**Pillar A — the category & the language (invent it).** A category of **ζ-equivariant objects over
`\overline{Spec ℤ}`**, fusing the three frameworks the audit already singled out, each carrying one
required structure: the **sphere spectrum / Segal Γ-rings** (the `𝔽₁` base — Connes–Consani 2023 gives
the curve's `H^•` + Serre duality here), **condensed/analytic geometry** (the archimedean place — the
coherent duality Arakelov lacks), and a **Hodge `(p,q)` enrichment** (the reality/phase structure).
The new language is the glue: *a `D`-polarizable, `(p,q)`-graded `𝕊`-linear category with a condensed
archimedean structure.* Notation to be coined as we go (§5, M3).

**Pillar B — the object by descent (force the gluing, don't choose it).** Build `𝕊_ℤ` by **descent**:
local data (the Euler factor / Frobenius-conjugacy at each prime `p`; the `Γ_ℝ`-factor `(p,q)` datum at
`∞`) glued by a **duality-descent condition** (a stack/topos gluing), so the cross-place coupling
`W_∞≥Σ_p W_p` is *a descent constraint the construction imposes*, not an inequality we hope for. The
polarization is then the **global duality pairing** of the glued object — ζ-intrinsic by construction,
evading the §0 no-go because it is not a congruence of any single place's data.

**Pillar C — positivity from coherence (the payoff).** In a genuinely *polarized* category, the Hodge
index `⟨·,·⟩>0` on primitives is a **formal consequence of `D`-self-duality + the polarization axiom**
— exactly as over `𝔽_q`, where projectivity ⟹ Hodge index. So RH becomes the statement *that the
constructed category is polarizable*, and the hard residue is concentrated in proving the polarization
axiom holds — a coherence property of the build, not an external estimate.

## 3. The method (from `research/method.md`, in build mode)
Definition-first; `axioms ⟹ RH` formal (it is — Pillar C); push all hardness into *constructing a model
of the polarized category*; construct by **representability**, not by hand; validate on the minimal
model (function fields) before betting on `ℤ`; falsify every candidate. We are always either choosing a
definition or measuring a coherence failure that names the next definition.

## 4. The load-bearing discipline (why this won't drift)
- **Anchor first.** No structure is admitted for `ℤ` until it is *built for function fields in the same
  language and shown to reproduce the Weil/Hodge-index proof.* If our category can't redo the solved
  case, the language is wrong — back up. (This is the move Grothendieck's étale cohomology had to pass.)
- **Falsify every piece.** Each constructed object/pairing runs `falsify.py`: does its polarization
  depend on the zero *locations* (sees-zeros), and does the construction *fail to exist* for DH? A
  metric-reducible or DH-admitting candidate is dead on contact.
- **Coherence over target.** Most labor is internal: is `D` a duality, is the gluing a descent, is the
  `(p,q)` grading functorial. RH is the distant consequence; we judge by internal inevitability.

## 5. First moves (NOW — concrete, ordered)
- **M1 [DEFINE].** Write the universal property of `𝕊_ℤ` (§1) as a precise functor of points / a
  representability statement. Output: the contract, formally.
- **M2 [ANCHOR-BUILD — load-bearing].** Build the polarized arithmetic Hodge category **for a function
  field** in this language, and check it reproduces the Weil RH proof (the Hodge index as the categorical
  polarization). *This validates the language before we deform to `ℤ`.* The minimal working model.
- **M3 [INVENT].** Define the *one* genuinely new structure: the **archimedean Hodge polarization** —
  the `(p,q)`/condensed duality datum at `∞` that supplies the reality/phase. Coin its notation; state
  its axioms; check it is NOT a `*`-congruence (passes §0 by construction).
- **M4 [DESCENT].** Specify the duality-descent gluing (Pillar B): how `{Euler factors} ∪ {Γ_ℝ (p,q)}`
  glue, and why the glued polarization is the explicit-formula quadratic form.
- **M5 [FALSIFY].** Run M2–M4's objects through the falsifier; confirm zero-dependence + DH-failure.

## 6. The engine
The autonomous loop is re-pointed from audit to **construction** (`research/AGENDA.md` re-seeded with
M1–M5 and their successors). The loop builds minimal models, checks coherence, invents and tests
notation, and runs the falsifier; I make the categorical choices and supervise. We expect to be wrong
several times — each wrong definition *names the next one*. That is not drift; it is the construction
converging on the object the audit proved must exist.
