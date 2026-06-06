# The Arakelov candidate for the missing object — arithmetic surface, intersection theory, and the precise gap to RH

**Scope.** This file characterizes, as precisely as the literature allows, the
**Arakelov-geometric** candidate for "the missing object" (`state-of-search.md` §5.1):
`Spec ℤ` compactified to the arithmetic curve `\overline{Spec ℤ} = Spec ℤ ∪ {∞}`,
the arithmetic surface and the would-be `\overline{Spec ℤ} ×_{𝔽₁} \overline{Spec ℤ}`,
their arithmetic intersection theory, and the **positivity** that would prove RH. The
governing discipline is STRATEGY §8: every statement below is tagged **THEOREM**
(proven, with reference), **CONJECTURE** (open, named), or **ANALOGY** (a structural
correspondence, not a proof). The whole point of the exercise is that the *proven*
positivity is the **wrong sign / wrong object**, and the positivity RH needs is open.

Sources read directly: Bost–Gillet–Soulé 1994 (`research/papers/`, full text);
Connes–Consani, *Weil positivity and Trace formula, the archimedean place*, arXiv
2006.13771 (`research/papers/`, full text). Web: Yuan–Zhang, *Arithmetic Hodge index
theorem for adelic line bundles I*, arXiv 1304.3538 / Math. Ann.; Moriwaki 1996;
Faltings 1984 / Hriljac 1985; Connes–Consani, *The Weil proof and the geometry of the
adèles class space*, arXiv math/0703392.

---

## 0. The template being imitated (function fields — the proven case)

Over a function field, RH for a curve `C/𝔽_q` is **THEOREM** (Weil 1948; Deligne 1974
in general). The forcing structure is intersection-positivity on the **surface
`C × C`** (product over `𝔽_q`):

- Frobenius acts; its graph is a **correspondence** (a divisor) on `C × C`. The zeros
  of the zeta function are the eigenvalues of Frobenius on `H¹`.
- The **Hodge index theorem** on the surface `C × C` gives the intersection pairing on
  divisors signature `(+1, −1, …, −1)` — positive on one class (a polarization), and
  **negative definite on its orthogonal complement (the primitive / degree-0 part)**.
- Applied to the Frobenius correspondence via the **Castelnuovo–Severi inequality**
  (`d ∘ d` self-intersection bound), negative-definiteness forces
  `Tr(Z ∘ Z') ≥ 0` (**Weil positivity** of correspondences), which pins
  `|α| = q^{1/2}` for every Frobenius eigenvalue `α` — i.e. RH. (Connes–Consani
  math/0703392 reconstruct exactly this; the eigenvalue bound is the geometric
  incarnation of the explicit formula.)

So the template is: **a surface, a self-intersection / correspondence, and a Hodge-index
positivity on the primitive part.** The number-field problem is to build the `ℤ`-analogue
`\overline{Spec ℤ} × \overline{Spec ℤ}` and the corresponding positivity. There is **no
field below `ℤ`** to take the product over — this is the `𝔽₁` problem (STRATEGY §1).

---

## 1. The arithmetic surface and its intersection theory (THEOREM — fully developed)

### 1.1 The arithmetic curve `\overline{Spec ℤ}`

`Spec ℤ` is a 1-dimensional regular scheme; its closed points are the primes `p`
(finite places). **Arakelov's** insight (Arakelov 1974) is that to get a *complete*
(proper) object with good intersection theory, one **compactifies by adding the
archimedean place** `∞`, equipping the picture with a hermitian metric there:
`\overline{Spec ℤ} = Spec ℤ ∪ {∞}`. This is the arithmetic analogue of a smooth
*projective* curve. An "Arakelov divisor" on `\overline{Spec ℤ}` is
`D = Σ_p n_p [p] + x_∞ [∞]` with `n_p ∈ ℤ`, `x_∞ ∈ ℝ`; its degree
`\widehat{deg} D = Σ n_p log p + x_∞` is the archimedean-completed degree. This is BGS
§2.1.3, the degree map `\widehat{deg} : \widehat{CH}^1(Spec 𝒪_K) → ℝ`.

### 1.2 The arithmetic surface (a relative curve over `Spec ℤ`)

The **arithmetic surface** in the literal, proven sense is `X → Spec 𝒪_K` (BGS §2.1.1
"arithmetic variety"): `X` is a 2-dimensional regular scheme, flat and projective over
`S = Spec 𝒪_K`, with regular generic fiber `X_K` a curve of genus `g ≥ 1`. The fiber
over a prime `𝔭` is a (possibly singular/reducible) curve over the residue field; the
"fiber at `∞`" is the Riemann surface `X(ℂ)` with a chosen Kähler/Arakelov metric. This
is `X × X`-style geometry **for genus-`g` curves**, *not* the self-product of
`Spec ℤ`. The self-product `\overline{Spec ℤ} × \overline{Spec ℤ}` (the object the RH
analogy actually wants — `C×C` with `C = \overline{Spec ℤ}`) **does not exist as a
scheme**; only the relative-curve surfaces `X → Spec ℤ` do. This distinction is the
crux of §3.

### 1.3 Arithmetic Chow groups and the intersection pairing (THEOREM — Gillet–Soulé)

For a regular arithmetic variety `X` (BGS §2.1.1, quoting the text I read):

- **Arithmetic cycles.** `\widehat{Z}^p(X)` = pairs `(Z, g)`, `Z ∈ Z^p(X)` an algebraic
  cycle of codimension `p`, and `g` a **Green current** for `Z`: a current on `X(ℂ)`
  with `dd^c g + δ_Z` smooth (`δ_Z` = integration on `Z(ℂ)`). The Green current is the
  **archimedean datum**; it carries the metric/potential-theoretic information.
- **Arithmetic Chow group.**
  `\widehat{CH}^p(X) = \widehat{Z}^p(X) / \widehat{R}^p(X)`, where `\widehat{R}^p`
  is generated by `(0, ∂u + \bar∂ v)` and by
  `(\mathrm{div}(f), -\log|f|^2)` — the arithmetic analogue of rational equivalence
  (the `-\log|f|^2` is the Green current of a principal divisor).
- **Maps** (BGS §2.1.1): `z: \widehat{CH}^p → CH^p` (forget the metric),
  `ω: \widehat{CH}^p → A^{p,p}` (`(Z,g) ↦ dd^c g + δ_Z`, the curvature form), and
  `a: A^{p-1,p-1} → \widehat{CH}^p` (`η ↦ (0,η)`), with `ω∘a = dd^c`. **Lemma 2.1.1**
  (Hodge theory): if `z(x)=0` and `ω(x)=0` then `x = a(η)` with `η` harmonic — the
  "purely archimedean" classes are the harmonic forms.
- **Intersection product** (BGS §2.1.1, eq. (2.1.1)):
  `\widehat{CH}^p(X) ⊗ \widehat{CH}^q(X) → \widehat{CH}^{p+q}(X)_ℚ`,
  `[(Z_1,g_1)]·[(Z_2,g_2)] = [(Z_1·Z_2,\ g_1 * g_2)]`, where `g_1 * g_2` is the
  **star product** of Green currents (BGS §1.3; associative — BGS Thm 1.3.2). For a
  regular arithmetic *surface* `X` (`dim_{Krull} X = 2`), two arithmetic divisors pair
  to a class in `\widehat{CH}^2(X)_ℚ`, and the **degree map**
  `\widehat{deg}: \widehat{CH}^2(X)_ℚ → ℝ` produces a real number:

  > `(\overline{D_1} · \overline{D_2}) = Σ_{p\ finite} (\text{local intersection mult.}) \log \#(\text{residue}) \;+\; \frac{1}{2}∫_{X(ℂ)} g_1 * g_2`.

  **The pairing is a sum of finite-place (geometric) contributions and one
  archimedean Green's-function contribution.** This is exactly the form
  `state-of-search.md` invokes ("finite places + archimedean Green's-function term").

### 1.4 Heights and the self-intersection `\overline{ω}·\overline{ω}` (THEOREM)

A hermitian line bundle `\overline{L} = (L,h)` defines `\widehat{c}_1(\overline{L}) ∈
\widehat{CH}^1(X)` (BGS §2.1.2: the class of `(\mathrm{div}(s), -\log\|s\|^2)`). The
**height** of a `d`-dimensional cycle is the iterated arithmetic intersection
`h_{\overline{L}}(X) = \widehat{deg}\big(\widehat{c}_1(\overline{L})^{d+1} \cap [X]\big)`
(BGS §3, the central definition). For an **arithmetic surface** `X/S` the load-bearing
example (BGS §3.3.3, which I read) is the self-intersection of the relative dualizing
sheaf with the **Arakelov metric**:

> `(\overline{ω}_{X/S} · \overline{ω}_{X/S})` — the **Arakelov–Faltings invariant**,

the height attached to `\overline{ω}_{X/S}`, a single real number invariant of the
arithmetic surface (BGS: independent of the semistable model; Moret-Bailly; Faltings
1984). This `\overline{ω}·\overline{ω}` is the arithmetic analogue of `ω·ω = 4g-4` /
the self-intersection on a geometric surface, and is the prototype "self-intersection"
the RH analogy wants. **Faltings 1984 proved `\overline{ω}·\overline{ω} ≥ 0`** and the
arithmetic Noether formula relating it to the Faltings height of the Jacobian and the
analytic torsion — all proven, all genuinely about genus-`g` curves, none of it touching
`Spec ℤ × Spec ℤ`.

---

## 2. The arithmetic Hodge index theorem (THEOREM — and exactly where the analogy breaks)

### 2.1 Faltings–Hriljac (n=1, arithmetic surfaces) — PROVEN

**THEOREM (Faltings 1984; Hriljac 1985, independently).** Let `X → Spec 𝒪_K` be a
regular arithmetic surface with smooth projective generic fiber `X_K` of genus `g ≥ 1`.
On the arithmetic divisor classes whose generic fiber has **degree 0** (more precisely
on `\widehat{Pic}` of the Arakelov divisors that are *flat*/orthogonal to the fibral and
archimedean polarization), the **Arakelov intersection pairing is negative definite**,
and it **equals the negative of the Néron–Tate canonical height pairing** on
`Pic^0(X_K) = J(K)`:

> for `D, E` degree-0 divisors on `X_K` with disjoint support,
> `\widehat{⟨D,E⟩}_{\mathrm{Ar}} = -\, \hat h_{NT}(D,E) = -Σ_{v∈M_K} ⟨D,E⟩_v`.

Equivalently: the arithmetic intersection form on
`\widehat{CH}^1(X)_ℝ` has signature `(+,−,−,…,−)` — **positive on the polarization,
negative (semi-)definite on its orthogonal complement** (the primitive part), with the
kernel exactly the pullbacks from the base. This is the literal arithmetic analogue of
the geometric Hodge index theorem of §0. (Sources: Faltings, *Calculus on arithmetic
surfaces*, Ann. Math. 119 (1984); Hriljac, *Heights and Arakelov's intersection
theory*, Amer. J. Math. 107 (1985).)

### 2.2 Moriwaki (higher dimension) — PROVEN

**THEOREM (Moriwaki 1996).** For a higher-dimensional regular arithmetic variety
`X → Spec 𝒪_K` of relative dimension `n`, with an **arithmetically ample** hermitian
line bundle `\overline{L}` and a hermitian line bundle `\overline{M}` whose generic
fiber is **numerically trivial** (`c_1(M_K)·c_1(L_K)^{n-1} = 0` on `X_K`):

> `\widehat{c}_1(\overline{M})^2 · \widehat{c}_1(\overline{L})^{n-1} ≤ 0`.

The sign is again **negative**: the form is negative (semi-)definite on the
`L`-primitive part of codimension-1 arithmetic classes.

### 2.3 Yuan–Zhang (adelic line bundles) — PROVEN

**THEOREM (Yuan–Zhang 2017, Math. Ann.; arXiv 1304.3538).** The same inequality and
equality condition hold for **adelic line bundles** on projective varieties over a
number field (and over finitely generated fields). Stated: with `\overline{L}`
arithmetically ample (nef) and `\overline{M}_K` numerically trivial on the generic
fiber, `\widehat{c}_1(\overline{M})^2 · \widehat{c}_1(\overline{L})^{n-1} ≤ 0`, with
**equality iff `\overline{M} = π^* \overline{M}_0`** for a hermitian line bundle
`\overline{M}_0` on the base `Spec 𝒪_K` (up to torsion / `ℚ`-linear equivalence).
Consequences they extract: uniqueness in the non-archimedean Calabi–Yau theorem, and
the **rigidity** of preperiodic points of polarizable dynamical systems. (Higher-degree
/ function-field versions: Carney–Hindes–Yuan–Zhang-style work, arXiv 1810.06342.)

### 2.4 The sign — the precise place the analogy breaks (ANALOGY → obstruction)

Compare §0 and §2.1–2.3. In **both** the geometric (`C×C`) and the arithmetic
(`X/S`) settings the Hodge index pairing is **negative definite on the primitive /
degree-0 part**. In the **function-field** proof this negative-definiteness is the
**source** of RH-positivity: applied to the *Frobenius correspondence* on `C×C` via
Castelnuovo–Severi, the correct sign falls out and forces `|α| = q^{1/2}`. **The
arithmetic Hodge index theorem is the same statement, with the same sign — and it is
PROVEN.** So why no RH?

Because the proven arithmetic Hodge index theorem lives on the **wrong surface and
about the wrong divisor**:

1. It is a theorem about a relative curve `X → Spec ℤ` (a genus-`g` *geometric* curve
   fibered over the arithmetic base), **not** about the self-product
   `\overline{Spec ℤ} × \overline{Spec ℤ}`. The Frobenius-correspondence / diagonal
   self-intersection that carries the zeta zeros has **no home** here, because the
   second factor `Spec ℤ` is the base, not a curve.
2. Its content — negativity of the height pairing on `J(K)` — is a statement about the
   Mordell–Weil / Néron–Tate height, **logically independent of RH for `ζ`**. There is
   no Frobenius on `Spec ℤ` whose eigenvalues are the `ζ`-zeros, so the index theorem
   has nothing to be applied *to* in the RH direction.

So: **the positivity that IS proven (Faltings–Hriljac–Moriwaki–Yuan–Zhang) is the
arithmetic analogue of the function-field Hodge index theorem, but on the relative-curve
surface, where it does not see `ζ`.** RH needs the same kind of positivity on the
missing self-product surface, applied to a Frobenius/diagonal class whose self-pairing is
the explicit-formula sum over zeros.

---

## 3. The explicit formula as a self-intersection — the analogy, made precise (ANALOGY)

The bridge that makes "the missing object" concrete is the **Weil explicit formula** read
as an intersection number. Schematically (Weil; Connes–Consani math/0703392, 2006.13771):

> `\widehat f(0) + \widehat f(1) - Σ_{ρ:\ ζ(ρ)=0} \widehat f(ρ) = Σ_v \int (\text{local Weil distribution } W_v)(f)`.

In the function-field case **each side is literally an intersection number on `C×C`**:
the left is `(Δ · Γ_f)` for the diagonal `Δ` and a Frobenius-twisted correspondence
`Γ_f`; the sum over zeros is `Tr` of Frobenius on `H¹`; **Weil positivity** is
`(Γ_f · Γ_f) ≤ \text{(self-intersection bound)}` from Hodge index — and that single
inequality is RH. The dictionary the program needs is therefore:

| function-field object | sought `ℤ`-analogue | status |
|---|---|---|
| surface `C × C` over `𝔽_q` | `\overline{Spec ℤ} × \overline{Spec ℤ}` over `𝔽₁` | **does not exist as a scheme** — `𝔽₁` problem |
| diagonal `Δ`, Frobenius graph `Γ` | divisor of the **Frobenius correspondence** on the Scaling-Site square | conjectural (Connes–Consani, "in development") |
| `Tr(Γ·Γ')` = sum over zeros | RHS of the **Riemann–Weil explicit formula** | the analytic object — exists |
| Hodge-index negativity on primitive part ⇒ Weil positivity | **archimedean Green-form / Weil positivity** | **OPEN** (the missing positivity) |
| self-intersection `(Δ·Δ)`, `ω·ω` | `(\overline{ω}·\overline{ω})` / archimedean diagonal contribution | partial; the small-square `∆` archimedean term is the obstruction (CC §2) |

**Connes–Consani 2006.13771** (read directly) make this exact: they show the Schwartz
kernel of the scaling operator `f(x)↦f(λx)` is `k(x,y)=δ(λx-y)`, i.e. it
**"corresponds geometrically to the divisor of the Frobenius correspondence"**; the
trace `\int k(x,x)dx` **"corresponds geometrically to the intersection with the
diagonal"**; and the explicit formula splits over the **two squares `Δ` and `Σ`** in the
first quadrant (their Fig. 1). Their **main positivity** (Theorem 1, Thm 6.11) is
`W_∞(g * g^*) ≥ Tr(ϑ(g) S ϑ(g)^*)` at the **archimedean place only**, and they prove
(their §2, Prop. 2.2) that **the obstruction to full Weil positivity is the specific
contribution of the small square `∆`** — the *archimedean diagonal self-intersection*.
This is precisely the *archimedean Green's-function term* of the BGS arithmetic
intersection pairing (§1.3), reappearing as the one term whose positivity is not free.

**BGS §6.3 (read directly) is the abstract obstruction theorem behind this.** BGS prove
(Cor. 6.3.2): a positive Green form for a cycle `Y` need **not exist** — if there is a
subvariety `Z` with `⟨p^*c_{r-1}(Q),[Z]⟩ < 0` then **no Green form positive off `Y`
exists**, and they exhibit explicit `(Y=`curve, `F=`rank-2 bundle with `\deg F < \deg L
≤ -g)` counterexamples. So **positive Green forms are not automatic**: the archimedean
positivity that the RH analogy needs is exactly the kind of object BGS show can be
*obstructed*. This is `state-of-search.md`'s "BGS §6.3 positive-Green-form obstruction =
RH-hard," now pinned to the theorem: **the missing positivity is a positive Green form /
positive archimedean diagonal contribution, and BGS §6.3 is the proof that its existence
is a genuine (sometimes false) condition, not a formality.**

---

## 4. The precise gap (the bottom line)

**What is proven.**
- The arithmetic surface `X → Spec 𝒪_K`, its arithmetic Chow groups
  `\widehat{CH}^•(X)`, the intersection pairing `=` (finite places) `+` (archimedean
  Green's-function term), and the height `\overline{ω}·\overline{ω}` — **all rigorously
  constructed** (Arakelov, Gillet–Soulé, BGS). [THEOREM]
- The **arithmetic Hodge index theorem**: the pairing is **negative definite on the
  degree-0 / `L`-primitive part**, equal to `-\hat h_{NT}` (Faltings–Hriljac, `n=1`;
  Moriwaki, all `n`; Yuan–Zhang, adelic), with equality only for base pullbacks.
  [THEOREM]

**Why it does not give RH.**
1. **Wrong surface.** The proven index theorem is about a *relative curve* `X → Spec ℤ`.
   RH's analogy needs the *self-product* `\overline{Spec ℤ} × \overline{Spec ℤ}`, which
   **does not exist** (no `𝔽₁`). The Frobenius correspondence / diagonal whose
   self-intersection is the explicit-formula sum-over-zeros has no scheme to live on.
   [the `𝔽₁` gap]
2. **Wrong divisor.** Negativity of `\hat h_{NT}` on `J(K)` is logically independent of
   RH for `ζ`; there is no Frobenius on `Spec ℤ` with eigenvalues `= ζ`-zeros for the
   index theorem to constrain.
3. **The archimedean term is unfree.** Even granting the object, the positivity needed is
   a **positive Green form / positive archimedean diagonal self-intersection** (the small
   square `∆`, CC §2), and **BGS §6.3 proves such positivity can fail** in general — so it
   must be *established*, not assumed.

**Exactly what stronger positivity RH would need (CONJECTURE — open).**

> RH `⟺` an **arithmetic Hodge index / Weil positivity on the missing self-product
> object** `\overline{Spec ℤ} × \overline{Spec ℤ}` (Connes–Consani Scaling-Site square),
> namely: the self-intersection of the diagonal-minus-Frobenius correspondence is
> negative on the primitive part — equivalently, the **archimedean local Weil
> distribution `W_∞` is positive** on test functions (a positive Green form for the
> diagonal whose `∆`-square contribution does not violate Cor. 6.3.2).

This is the **arithmetic standard conjecture** in this setting: the analogue of the
function-field Hodge-index step, but on an object whose **construction is itself the open
problem**. It is *not* the Faltings–Hriljac theorem (that is the index theorem on the
*base-relative* surface and has the right sign for the *wrong* application). It is the
**unproven** positivity of the archimedean diagonal self-intersection on the unconstructed
`ℤ × ℤ`. Connes–Consani prove its **archimedean-place** instance up to an explicit
finite, RH-irrelevant defect (their `c`, `13<c<17`, eq. (5)–(6)) — which is real progress
on one place but **not** the global positivity, and not via the missing object.

**Consistency with the program's map.** This is the same endpoint reached independently
by the Jensen/metric route (`metric-arakelov-probe.md`): the slack is an Arakelov height
(condition-number = height of the discriminant), its leading energy is GUE-universal
(= archimedean / dispersing), and the RH content sits in the **subleading Euler-product /
positive-Green-form** structure — i.e. the **same** BGS §6.3 / archimedean-Weil-positivity
obstruction. Every geometric route lands here; none of them constructs the object.

---

## 5. One-line summary

- **Object:** the arithmetic surface `X → \overline{Spec ℤ}` (proven) and the *desired,
  unconstructed* `\overline{Spec ℤ} × \overline{Spec ℤ}` / Scaling-Site square (the
  missing object).
- **Proven positivity:** arithmetic Hodge index theorem — pairing negative-definite on
  the primitive part `= -\hat h_{NT}` (Faltings–Hriljac, Moriwaki, Yuan–Zhang).
- **Gap:** that theorem is the right *kind* of positivity on the *wrong* surface (a
  relative curve, blind to `ζ`); RH needs the same negativity for the
  **diagonal–Frobenius self-intersection on the missing `ℤ×ℤ`**, equivalently
  **positivity of the archimedean local Weil distribution / a positive Green form for the
  diagonal** — which BGS §6.3 shows is a genuine (obstructable) condition and which
  remains **OPEN**.

---

### References (load-bearing, as cited above)

- **S. Arakelov**, *Intersection theory of divisors on an arithmetic surface*, Math.
  USSR Izv. 8 (1974) — compactification `Spec ℤ ∪ {∞}`, archimedean Green's functions.
- **G. Faltings**, *Calculus on arithmetic surfaces*, Ann. of Math. 119 (1984) —
  `\overline{ω}·\overline{ω} ≥ 0`, arithmetic Hodge index (`n=1`), Noether formula.
- **P. Hriljac**, *Heights and Arakelov's intersection theory*, Amer. J. Math. 107
  (1985) — index theorem `= -` Néron–Tate, independently of Faltings.
- **H. Gillet, C. Soulé**, *Arithmetic intersection theory*, Publ. IHÉS 72 (1990);
  *An arithmetic Riemann–Roch theorem*, Invent. Math. 110 (1992) — `\widehat{CH}^•`,
  the pairing, arithmetic RR.
- **J.-B. Bost, H. Gillet, C. Soulé**, *Heights of projective varieties and positive
  Green forms*, J. AMS 7 (1994) — `research/papers/`; §2 intersection theory, §3.3.3
  `\overline{ω}·\overline{ω}`, **§6 positive Green forms, §6.3 the obstruction (Cor.
  6.3.2)**.
- **A. Moriwaki**, *Hodge index theorem for arithmetic cycles of codimension one*, Math.
  Res. Lett. 3 (1996) — higher-dimensional index theorem.
- **X. Yuan, S.-W. Zhang**, *The arithmetic Hodge index theorem for adelic line bundles
  I*, arXiv 1304.3538, Math. Ann. (2017) — adelic index theorem, equality condition.
- **A. Connes, C. Consani**, *The Weil proof and the geometry of the adèles class space*,
  arXiv math/0703392 — explicit formula as intersection on `C×C`, Weil positivity.
- **A. Connes, C. Consani**, *Weil positivity and Trace formula, the archimedean place*,
  arXiv 2006.13771 — `research/papers/`; Frobenius correspondence = scaling kernel,
  diagonal = trace, the small square `∆` archimedean obstruction, Thm 1 / Thm 6.11.
