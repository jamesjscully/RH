# AN-C — Connes' trace formula / spectral realization (the adèle class space)

*Analytic-side strategy map, strategy (C). 2026-06-06. Verdict: **CIRCULAR** (the adelic
trace positivity = the Weil positivity, geometrized; no new analytic positivity source).*

Sibling: `connes-consani-scaling-site.md` (the geometric-square / Riemann–Roch facet, already
mapped). This note maps the **operator/trace-formula** facet head-on against the unifying question
of `analytic-strategies-map.md` and Theorem B′ of `WRITEUP-geometric-obstruction.md`.

---

## 0. The strategy in one line

Connes (1999, *Trace formula in NCG and the zeros of the Riemann zeta function*, Selecta Math.):
realize the explicit formula as a **trace formula** for the action of the idele class group (the
scaling action `R_+^*`) on the adèle class space `A_Q/Q^*` (resp. `Q^*\A_Q/\hat Z^*`). The critical
zeros appear as an **absorption spectrum** — the frequencies *missing* from the continuous spectrum
of the scaling action on `L²` of the adèle classes (and eventual off-critical zeros would appear as
**resonances**). RH is then reduced to the **positivity of the Weil distribution** `Σ_v W_v`,
re-read as a trace positivity on this noncommutative space. [established — these are theorems.]

> **Prerequisite (what the strategy needs to prove RH):** the positivity of Connes' trace
> functional / the Weil distribution `W(f) = Σ_ρ \hat f(ρ) = Σ_v W_v(f) ≥ 0` on the adèle class
> space, for `f = g ⋆ g^♯`.

---

## 1. The prerequisite IS the Weil positivity (CONFIRMED)

This is not an interpretive claim; it is what Connes proves. The two load-bearing theorems are:

1. **The trace formula = the explicit formula** [established, Connes 1999; Connes–Consani–Marcolli,
   *The Weil proof and the geometry of the adèles class space*, arXiv:math/0703392]. The geometric
   trace of the scaling action equals `Σ_v ∫_{Q_v^*} h(u^{-1})/|1−u| d^*u` = the sum of the
   Riemann–Weil **local distributions** `W_v`. This is a genuine achievement: the explicit formula
   is *geometrized* as a Lefschetz/Atiyah–Bott trace.

2. **RH ⟺ the trace is positive** [established as a reduction, = Weil's criterion]. Connes' RH
   criterion is *literally* `Σ_v W_v(g ⋆ g^♯) ≥ 0` (the form normalized so positivity ⟺ all zeros on
   the line). This is **Weil's positivity criterion** (Weil 1952), transported verbatim onto the
   adèle class space. It is the **same** functional that `weil_form.py` certifies as `PSD ⟺ RH`
   (`positivity-program.md` table B, row "Hodge index"; row "Weil/Li positivity": *PSD ⟺ RH —
   circular*).

So step (1) is real new mathematics (a trace realization); step (2) — the **positivity that is RH**
— is imported unchanged. The NCG/adelic framework supplies a magnificent **stage** for the Weil
positivity, not a new **proof** of it.

**Why the framework cannot add positivity (Theorem B′ applied).** Theorem B′ says: a similitude /
duality datum (`F·F† = [deg]`, the functional equation, the Frobenius graph) **underdetermines the
signature** — off-line spectra carry a perfectly consistent *indefinite (Krein)* invariant form;
positive-definiteness ⟺ all `|α| = √c` ⟺ RH is an **independent** condition. Connes' trace formula
supplies exactly the Step-A datum: the scaling action is the `R_+^*`-similitude, the graph of
scaling is the proposed Frobenius correspondence (CCM math/0703392 name it as such), and `Σ_v W_v` is
the invariant pairing. The framework constructs the pairing; it does **not** construct the metric
that makes it positive-definite. The Hilbert space `L²(adèle classes)` is positive by fiat — but the
*trace* `Σ_v W_v` on it is a **difference** (archimedean `W_∞` minus prime `Σ_p W_p`, the small-square
`Δ` minus the big-square `Σ` in 2006.13771's Figure 1), and *that* difference's sign is unforced.
Connes' object is the textbook instance of B′'s "presents Step A, silent on Step B."

> **Conclusion of §1.** The adelic/NCG framework does **NOT** supply a new analytic positivity. The
> prerequisite is the Weil positivity verbatim. positivity_source = **REDUCES_TO_WEIL**.

---

## 2. Spectral realization: does it FORCE positivity or ASSUME it? (ASSUMES)

The absorption-spectrum picture is the heart of the "spectral realization." Honest status:

- **What is forced [established].** The zeros *are* realized: as the absorption spectrum (Connes
  1999), and most recently as the spectrum of a **prolate wave operator** (Connes–Consani–Moscovici,
  *Zeta zeros and prolate wave operators*, arXiv:2310.18423, accepted Aug 2024) — the low-lying zeros
  from its positive spectrum, the UV behaviour from the Sonin space = its negative spectrum. The
  scaling Hamiltonian is the Berry–Keating `xp`/`(x∂+∂x)/2` made rigorous on the right space
  (arXiv:1910.14368). These are real spectral-realization theorems.

- **What is NOT forced [established as a gap].** A spectral realization is **RH-neutral by
  construction** — this is the project's "stone 1" (`positivity-program.md` C, row self-adjointness:
  *reflects not forces; resonances ≠ self-adjoint eigenvalues*). The absorption picture realizes the
  zeros **wherever they are**; an off-critical zero is *also* realized, as a **resonance** (Connes'
  own word). Nothing in the construction of the space or the action excludes resonances. The
  exclusion of resonances ⟺ self-adjointness of the relevant operator ⟺ positivity of the trace ⟺
  RH — and that step is exactly where every Connes paper since 1999 stops and *assumes* (or, in the
  archimedean paper, proves only at one place, conditionally). The "Hilbert–Pólya operator" the
  realization gives is **not manifestly self-adjoint**; making it self-adjoint is RH, not an input
  the construction delivers.

- **The "scaling Hamiltonian" paper's own admission** [established]: arXiv:1910.14368 uses quantized
  calculus to analyze **X.-J. Li's attempt to prove Weil positivity and to understand its *limit*** —
  i.e. the paper's contribution on positivity is to *diagnose why an attempt fails*, not to supply
  one. Positivity remains the wall, not the output.

> **Conclusion of §2.** The spectral realization **assumes** the positivity (excludes resonances by
> hand = assumes RH); it does not **force** it. The audit's "Bost–Connes RH-silent" finding
> (`positivity-program.md` table B, row Bost–Connes QSM: *free energy is RH-silent*; Worker A
> `qsm_free_energy.py`: KMS positivity certified, Euler-borne, DH-refusing, **but RH-SILENT** — does
> not see the zeros) is the same conclusion on the statistical-mechanics facet of the same NCG.

---

## 3. The anchor: function fields (where the trace IS positive, by geometry)

[established] Over a function field `F_q(C)` the *same* adelic trace formula is the **Weil/Lefschetz
trace formula** on `C`, and the positivity is **Weil's theorem** — supplied by the **Hodge index
theorem** on `C ×_{F_q} C` (a genuine geometric positivity, because the surface is projective over
the *finite* field `F_q`). CCM (math/0703392) make the dictionary explicit: scaling-graph ↔ Frobenius
correspondence, `Σ_v W_v` ↔ the intersection pairing, RH-positivity ↔ Hodge index.

So the anchor's analytic content is **a theorem there** (not vacuous) — but it is a theorem *because
of the finite ground*, i.e. exactly the resource Theorem A proves is **forbidden at `∞`** for `Q`
(*archimedean ≡ characteristic 0*; no finite residue field at `∞`). Over `Q` the trace `Σ_v W_v` is
positive **iff RH**, with no geometric Hodge-index theorem available to make it so. The anchor
therefore *confirms* the diagnosis: the framework transports everything **except** the one thing
(the finite-ground positivity) that cannot transport. The trace formula is the part that survives the
`q→1` limit; the positivity is the part that does not.

---

## 4. The honest achievement vs. the wall

| ingredient | status | who supplies the positivity |
|---|---|---|
| explicit formula = geometric trace (`Σ_v W_v`) | **theorem** [Connes 99; CCM 07] | n/a (an identity, not a positivity) |
| zeros = absorption spectrum / prolate-operator spectrum | **theorem** [Connes 99; CCM 2310.18423] | none — realizes zeros wherever they are |
| off-critical zeros = resonances | **theorem** (their framing) | the realization *permits* them; RH = their absence |
| `RH ⟺ Σ_v W_v ≥ 0` | **theorem** (= Weil's criterion, geometrized) | **this is the Weil positivity** — the wall |
| archimedean `W_∞(g⋆g^♯) ≥ 0`, `supp g ⊂ (1/2,2)`, `\hat g(±i/2)=0` | **theorem, conditional, one place** [2006.13771] | prolate/Toeplitz analysis — analytic, but `Γ_R`/archimedean = **DH-shared** (see §5) |
| semilocal `{∞,2,…,p}` positivity ⟹ RH | **program, not carried out** [2006.13771 abstract] | the missing object |
| Riemann–Roch / `H¹` on the square `S²` (forcing structure) | **open** [1805.10501] | would be the new source — **unbuilt** |

The single genuinely *analytic* positivity Connes produces — the archimedean `W_∞ ≥ 0` of 2006.13771
via prolate-spheroidal/Hermitian-Toeplitz analysis — is real and is an **estimate** (a true new
analytic input at one place). But by the project's own diagnosis (`connes-consani-scaling-site.md`
§5; `positivity-program.md` Worker C `semilocal_2.py`) it is built from the **Riemann–Siegel `θ` /
`Γ_R` / Sonin** apparatus, which is the **archimedean datum shared verbatim with Davenport–Heilbronn**
— so it is **RH-neutral / RH-silent**: it certifies the place where ζ and DH *agree*, not the
Euler-product content that separates them. The RH content sits in the **prime side** `Σ_p W_p` and the
cross-place coupling `W_∞ ≥ Σ_p W_p` — the unbuilt part.

---

## 5. DH litmus

[established] **FAIL** for the spectral-realization positivity *as a forcing mechanism*; more
precisely, **the realization itself does not even discriminate** (the absorption-spectrum / scaling
construction is built on the archimedean scaling action and the functional equation, both of which
Davenport–Heilbronn shares — DH has the same `Γ_R`, the same approximate functional equation). The
audit's harness records: `semilocal_2.py` — the `{∞,2}` Gram form *sees* the Euler product in its
matrix **entries** (`Λ(2)=0.693` vs `c_DH(2)=0.197`) but **both stay PSD** (RH-SILENT at one place);
`qsm_free_energy.py` — Bost–Connes KMS positivity is Euler-borne and DH-*refusing* but **RH-silent**
(blind to zero locations). So Connes' positivity inputs pass the *cheap* axis (Euler-borne /
DH-refusing on the prime side) but **fail the decisive `sees-zeros` axis** — exactly the `falsify.py`
RH-SILENT verdict. The one place it would have to discriminate (force the line, not the edge) is
where the construction stops.

DH verdict: **FAIL** — the spectral realization is RH-silent; the positivity it reduces to is the
Weil positivity, which is `≥0 ⟺ RH` by definition (CIRCULAR, not falsifiable by DH because it simply
*is* the statement).

---

## 6. Verdict

**CIRCULAR.** Connes geometrized the explicit formula into a trace formula (a real theorem) and gave
the zeros a spectral realization (real theorems, up to the 2024 prolate-operator work). But the
**positivity** that is RH — `Σ_v W_v ≥ 0` — is the **Weil positivity verbatim**, transported onto the
adèle class space, *not* derived from it. The NCG/adelic framework is a **stage** for the Weil
positivity, not a new **source** of it:

- **positivity_source = REDUCES_TO_WEIL.** The prerequisite IS the Weil positivity (geometrized
  adelically). The framework supplies the Step-A similitude datum (scaling action / functional
  equation) and is, by Theorem B′, structurally **silent on the signature** (Step B = positivity). The
  one genuinely analytic input (archimedean `W_∞ ≥ 0` via prolate/Toeplitz) is **DH-shared /
  RH-silent** — it certifies the archimedean place, not the line.
- **prerequisite_status = CIRCULAR.** The prerequisite is RH restated: `trace ≥ 0 ⟺ RH` is a
  *definition-level* equivalence (Weil 1952), with no independent analytic source on the `Q` side
  (the function-field anchor's source — the Hodge index theorem — needs the finite ground forbidden
  at `∞` by Theorem A).
- **The spectral realization assumes positivity** (excludes resonances by hand) **rather than forcing
  it.** Self-adjointness of the realized operator ⟺ RH is not delivered by the construction.

**Is there *any* open road inside this strategy?** Yes, but it is the **geometric** facet already
mapped, not the trace-formula facet: the **unbuilt Riemann–Roch / `H¹` on the square `S²`**
(`connes-consani-scaling-site.md` §4, 1805.10501) — *that* would be a forcing structure (a real
positivity source, the `q→1` shadow of the Hodge index theorem). It is **OPEN/UNCONSTRUCTED** there
and **forbidden** by Theorem A in its literal finite-ground form. The **trace-formula / spectral-
realization** facet examined here is **CIRCULAR**: it restates the wall analytically, beautifully, and
diagnoses (Li) why a positivity attempt fails — it does not give a road.

> **One line.** Connes gave the Weil positivity a *spectacular stage* (the adèle class space, the
> scaling/Frobenius flow, the absorption spectrum) and a real one-place analytic estimate — but the
> positivity itself is still **Weil's, assumed**: the trace is positive **iff RH**, with the only
> non-circular source (the Hodge index theorem) living over the finite ground that `∞` is forbidden
> (Theorem A). He **restated the wall analytically**, he did not breach it.

---

## Sources
- A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*,
  Selecta Math. 5 (1999) 29–106. [the original trace formula + absorption-spectrum realization]
- A. Connes, C. Consani, M. Marcolli, *The Weil proof and the geometry of the adèles class space*,
  arXiv:math/0703392. [explicit formula as trace; scaling-graph ↔ Frobenius; Weil-positivity dictionary]
- A. Connes, C. Consani, *Weil positivity and Trace formula, the archimedean place*, arXiv:2006.13771.
  [one-place conditional `W_∞ ≥ 0`; prolate-spheroidal / Hermitian-Toeplitz; "semilocal case where
  Weil positivity implies RH" = stated program]
- A. Connes, C. Consani, *The Scaling Hamiltonian*, arXiv:1910.14368. [Berry–Keating link; analyzes
  X.-J. Li's Weil-positivity attempt **and its limit** — positivity is diagnosed, not supplied]
- A. Connes, C. Consani, H. Moscovici, *Zeta zeros and prolate wave operators*, arXiv:2310.18423
  (accepted Aug 2024). [zeros from the prolate operator's positive spectrum, UV from Sonin = negative
  spectrum — the current state of the spectral realization; still no global positivity]
- Repo cross-refs: `connes-consani-scaling-site.md` (geometric square / RR(S²) facet);
  `positivity-program.md` (Workers A `qsm_free_energy.py`, C `semilocal_2.py`; tables B/C);
  `WRITEUP-geometric-obstruction.md` (Theorem A finite-ground forbidden at `∞`; Theorem B′ similitude
  underdetermines signature); `weil_form.py` (`PSD ⟺ RH`).
