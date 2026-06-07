# AN-synthesis: the analytic side of the RH-strategy map, completed (2026-06-06)

Companion to `WRITEUP-geometric-obstruction.md` (geometric side, FORECLOSED: Theorem A char-0
contradiction; Theorem B′ a similitude underdetermines the signature). This document closes the
**two-sided map**. Per-strategy detail: `AN-{HP,dB,BN,W,BK,C}-*.md`. Sources: the 6 strategy-verdicts.

---

## 0. The forcing axis (Theorem B′, restated as a litmus)

Theorem B′ proved the RH-positivity (`F†=F̄`, the `(d,0)` signature) is **not forced by any structural
datum** — duality, functional equation, similitude/scaling, coherence are all satisfied by off-line
worlds (Davenport–Heilbronn is the witness: ζ-type `Γ_ℝ` functional equation, self-dual axis ½, GUE-ish,
but no Euler product and zeros off the line). So a genuine proof must supply the positivity **from
analysis**, from a source that is simultaneously:

- **(i) Euler-borne** — sees the prime/Euler-product data (else it is DH-shared, RH-neutral); and
- **(ii) zero-bearing** — its sign actually moves when a zero leaves the line (else it cannot exclude
  off-line zeros); and
- **(iii) independent** — not the Weil/trace positivity it is trying to prove (else circular).

**The pin (the wall):** in every classified strategy, *no single object is all three at once.* The
archimedean piece (`W_∞`, `Γ_ℝ`/digamma, Riemann–Siegel θ, smooth Weyl count `N̄`) is Euler-blind and
DH-shared (fails i). The Euler-borne prime piece (`Λ(n)`, Bost–Connes KMS, the Euler product itself) is
zero-independent — it has no "plant-a-zero knob" (fails ii). The one form that is both Euler-borne and
zero-bearing is the **Weil functional itself**, which is circular (fails iii). This is the analytic
shadow of Theorem B′.

---

## 1. The classification (all 6)

| Strategy | Prereq status | Positivity source | DH litmus | Verdict |
|---|---|---|---|---|
| **dB** de Branges / Conrey–Li | CONTRADICTORY | REDUCES_TO_WEIL | FAIL | **REAL_NOGO** (scoped) |
| **W** Weil positivity / explicit formula | CIRCULAR | REDUCES_TO_WEIL | FAIL | **CIRCULAR** (the wall) |
| **C** Connes adele-class trace formula | CIRCULAR | REDUCES_TO_WEIL | FAIL | **CIRCULAR** |
| **HP** Hilbert–Pólya | UNCONSTRUCTED | REDUCES_TO_WEIL (floor) | FAIL\* | **OPEN_ROAD** (circular floor) |
| **BK** Berry–Keating / quantum chaos | UNCONSTRUCTED | NONE | FAIL | **OPEN_ROAD** (degenerate) |
| **BN** Beurling–Nyman / Báez-Duarte | UNCONSTRUCTED | NONE | **PASS** | **OPEN_ROAD** (faithful, inert) |

\* HP's *bare* self-adjointness / unitary-scaling realization is DH-shared (FAIL); the only *constructed*
HP (Connes–Moscovici prolate operator) is circular. The non-circular HP is unconstructed.

### (a) The no-gos — and exact scope
**Only one** strategy is contradictory: **de Branges (dB)**, via Conrey–Li (IMRN 2000,
math/9812166). They prove de Branges's *specific strong positivity hypothesis* (3.1) is **false** for ζ's
own space: the necessary conclusion `Im{Ē′(w)E(w+i)/2πi} ≥ 0` is **violated at the 34th zero**
ρ = ½ + i·111.0295…, where the quantity equals `−ξ′(ρ)ξ(1+ρ) = −5.389…×10⁻⁶⁹ < 0` (companion
(3.4) = −1.32×10⁻⁴ < 0). This is a **strict logical contradiction** (one bad zero refutes the hypothesis),
not a heuristic — reproduced independently at 40 digits.

**Scope (decisive):** this closes **one labelled door, not the corridor.** By the Lagarias coincidence the
de Branges norm IS the Weil Hermitian form, so de Branges's (3.1) is **stronger than RH-positivity**
(it over-proves) — which is *why* it is refutable. A weaker de Branges space / canonical system / Krein
string whose positivity comes from a *different* source is **untouched**. The no-go is scoped to the named
1986–1994 positivity conditions, and it **confirms Theorem B′ from the analytic side**: the kernel/FE
(Step A) is free; the posited positivity (Step B) is the unforced — here false-as-stated — extra.

### (b) The circular ones — = Weil positivity restated
**W (Weil positivity)** and **C (Connes trace formula)** are both **CIRCULAR**: their prerequisite *is* RH
in quadratic-form clothing.
- **W**: `W(f) = Σ_ρ \hat f(ρ) ≥ 0` is manifestly ≥0 **iff** every γ_ρ is real = RH (`weil_form.py`: min
  eig −3.4e-16 on true zeros; −1.49 with a planted off-line zero). Bombieri–Lagarias (1999) is the
  non-circularity killer: Li's λ_n ≥ 0 follows for an *arbitrary* multiset on Re=½, so positivity is a
  *consequence* of on-line-ness, not a source forcing it. The only unconditional positivity (Bombieri
  2000 / Yoshida, small support) is an **edge result that provably does not reach the line.**
- **C**: Connes geometrized the explicit formula into a real trace formula and realized the zeros as an
  **absorption** spectrum — genuine theorems — but the positivity `Σ_v W_v ≥ 0` is Weil's criterion
  transported *verbatim* onto the adèle class space, **not derived from it**. The one analytic input
  (conditional one-place `W_∞ ≥ 0` via prolate-spheroidal/Sonin analysis, arXiv:2006.13771) is built from
  the `Γ_ℝ`/Riemann–Siegel θ apparatus = the DH-shared archimedean datum: RH-silent.

Anything reducing to `Σ_v W_v ≥ 0` (incl. the dB norm, the HP Connes–Moscovici floor) lands here. **This
is the wall, not a road.**

### (c) The open roads — unconstructed, not contradictory
**HP, BK, BN.** None has a Conrey–Li-type no-go; each genuinely encodes RH but leaves an **unconstructed
object**.
- **HP** — a canonical self-adjoint `H` with spec **exactly** {γ}, self-adjointness forced by an
  *independent* positivity. No general no-go (the function-field anchor proves consistency). But the only
  essentially-constructed HP (Connes–Moscovici prolate operator, 2021/22) is **circular**: the zeros
  appear only as a UV/absorption asymptotic in the Sonin space, and `H=H*` ⟺ Weil positivity ⟺ RH. The
  non-circular HP is unbuilt — and **coincides with the program's missing cross-place object.**
- **BK** — same operator dream via xp/quantum chaos. **Degenerate / RH-silent**: every actual
  construction yields only the *smooth Weyl count* `N̄(E)` (Berry–Keating/Sierra — DH-identical, Euler-blind),
  or an absorption spectrum (Connes), or a *non-self-adjoint* operator (Bender–Brody–Müller 2017, refuted
  by Bellissard 2017: it is the dilation generator in a non-unitary basis, with ζ smuggled in via the
  boundary condition). positivity_source = NONE.
- **BN** — RH ⟺ `dist(1_{(0,1)}, span{1/(nx)})_{L²} = 0` ⟺ `d_N² → 0`. **Faithful and concrete**, the only
  open road that **PASSES the DH litmus** (DH has zeros Re>½, so its BN-density genuinely fails — the
  criterion discriminates ζ from DH). But it carries **NO positivity** (RH is encoded as a distance=0,
  orthogonal to the B′ axis), and the known distance asymptotics only **bound `d_N` below** and re-encode
  the off-line obstruction without removing it. Inert.

---

## 2. THE KEY FINDING: is there a GENUINE_ANALYTIC positivity source?

**No — none of the six supplies a positivity source that is (i) Euler-borne, (ii) zero-bearing, AND
(iii) independent of the Weil positivity.** Of the four with a positivity facet (dB, W, C, HP-floor) **all
four are `REDUCES_TO_WEIL`**. The two remaining roads (BN, BK) have **positivity_source = NONE** — they do
not even traffic in positivity (BN is an approximation; BK is a spectrum). So on the decisive Theorem-B′
axis:

> **GENUINE_ANALYTIC positivity source found in 0 of 6 strategies.** Every positivity on the analytic side
> either *is* the Weil positivity (circular) or is absent. This is the analytic confirmation of Theorem B′:
> the structure (Step A) is everywhere free; the positivity (Step B) is everywhere either circular,
> contradictory-as-specifically-stated, or absent.

**The single named missing object — shared by HP, BK, W, C, and the geometric program:** a positivity that
is the **cross-place coupling `W_∞(f) ≥ Σ_p W_p(f)`** (archimedean term dominates the prime term for every
test function), supplied by an **Euler/Hecke (not Eisenstein/archimedean) source** that **sees zero
locations** — concretely an archimedean Kähler / Hodge–Riemann form on the missing arithmetic surface
`S²/ℤ` (the q→1 shadow of the Hodge index theorem on `C×C`), or a reflection-positive prime-place
involution. The HP operator is the **shadow** of this surface positivity; HP and the geometric program
**converge on the same object.** It is unbuilt, and in its literal finite-ground form forbidden at ∞ by
Theorem A — which is exactly why no road yet supplies it.

---

## 3. The two-sided picture — is anything foreclosed-as-a-whole?

| Side | Status | Mechanism |
|---|---|---|
| **Geometric** (FF transport, Frobenius, Hodge index → ℚ) | **CLOSED / FORECLOSED** | Theorem A: char-0 contradiction; Theorem B′: similitude underdetermines signature |
| **Analytic — dB specific** | NO-GO (scoped) | Conrey–Li contradiction at the 34th zero |
| **Analytic — W, C** | CIRCULAR | = Weil positivity restated |
| **Analytic — HP, BK, BN** | OPEN (unconstructed) | no contradiction; missing object as hard as RH |

**Is any analytic road foreclosed *as a whole*?** **No.** The single contradiction (dB) is **scoped** to
de Branges's specific 1986–94 positivity hypotheses — it refutes a Step-B *over-statement*, not the
de Branges *corridor*, and not HP/BK/BN/W/C. **There is no analytic theorem forbidding RH-positivity to
exist.** Indeed the function-field anchor exhibits the whole stack as a **theorem** over `𝔽_q(C)`
(self-adjoint Frobenius, de Branges positivity, BN-density, Weil ≥0 — all true, supplied by the Hodge
index over the finite ground). The obstruction over ℚ is the **absence of the finite ground at ∞**
(Theorem A), not a contradiction in the target.

So the honest situation is exactly as posed: **every analytic road either reduces to the same Weil
positivity (circular) or is unconstructed (open); NONE is contradictory-as-a-whole.** This is the
signature of a problem that is **true-and-provably-open, not foreclosed** — the analytic side does **not**
close, unlike the geometric side.

---

## 4. The deepest honest meaning + the single most concrete live road

**The analytic side confirms RH is OPEN, not foreclosed.** The asymmetry is the whole content of the
two-sided map: the geometric side ends in a *contradiction* (you cannot have the finite ground at ∞), but
the analytic side ends in *unconstructed objects with no contradiction* (you have not yet built the
positivity, but nothing forbids it). RH is therefore most likely **true and provably open**: the proof, if
it exists, is the construction of the one missing positivity object — it is not blocked, merely unbuilt.

**Two candidate "most concrete" roads, and the honest ranking:**

- **HP / the cross-place positivity** is the road whose missing object is *correctly aimed* (it IS an
  RH-positivity source) but whose obstruction is *maximal* — it coincides with the geometric program's
  missing `S²/ℤ` Hodge form, forbidden in literal form by Theorem A. Deepest, hardest.
- **BN** is the road whose missing object is *most concrete and constructive* — an explicit family of
  Dirichlet polynomials `A_N(s) = Σ_{n≤N} a_n n^{−s}` with an **unconditional** estimate
  `(1/2π)∫|1 − ζ(½+it)·A_N(½+it)|² dt/(¼+t²) → 0`. It is the **only road that passes the DH litmus**, it
  *sees zero locations faithfully*, and its object is **fully explicit** (no need to invent a Hilbert
  space, an operator, or a new positivity — just a sequence of coefficients and one analytic estimate).

> **The single most concrete live road is BEURLING–NYMAN.** Its missing object — an explicit `A_N` with an
> unconditional `d_N² → 0` (equivalently: a constructive proof that `1_{(0,1)}` is in the L²-closure of
> `span{1/(nx)}`) — is the **least apparently-obstructed** unconstructed object on the entire two-sided
> map: it requires no positivity certificate, only an approximation, and it is the unique road that
> discriminates ζ from DH.

**The honest caveat (no false hope):** "most concrete" ≠ "easiest." BN carries **no positivity lever**, so
it offers no *new analytic input* — its missing `A_N` controls putative off-line zeros only by a mechanism
that **does not yet exist** and is, on current evidence, **no easier than RH itself** (the known `d_N`
asymptotics sum only over on-line zeros and bound below). It is the most concrete *target*, not a *shortcut*.
HP names the *right* object (a genuine positivity) but is maximally obstructed; BN names the *most explicit*
object but supplies no positivity. The two open roads are the two faces of the same gap.

---

## 5. Bottom line (two-sided)

**Geometric side: CLOSED (contradiction).** **Analytic side: OPEN (unconstructed, none contradictory).**
The only analytic no-go (de Branges/Conrey–Li) is **scoped** to a Step-B over-statement; W and C are the
**circular Weil wall**; HP, BK, BN are **open roads** with no general no-go. **Zero** strategies supply a
GENUINE_ANALYTIC (non-Weil) positivity source — confirming Theorem B′ analytically. The single most
concrete live road is **Beurling–Nyman** (an explicit `A_N` with unconditional `d_N² → 0`); the single
deepest-aimed object is the **cross-place positivity `W_∞ ≥ Σ_p W_p`** on the missing surface `S²/ℤ`,
shared by HP and the geometric program. RH reads as **true-and-provably-open**: the proof is a
construction, not foreclosed.
