# NF-C1 — characteristic 1 as a NATIVE foundation carrying a scale: is the q→1 dequantization FORCED, or is there a non-degenerate scale-bearing char-1? [NEW-FOUNDATIONS · DEF · theorem + anchor · DEGENERATE / FORCED]

2026-06-06. New-foundations frontier (charter `research/new-foundations.md`, direction C1), after the `𝔽₁`-construction program (`research/f1-construction.md`) exhausted and bottomed on the char-0/char-p divide. Builds on and SHARPENS F1-T (`F1-T-tropical-char1.md`, SCALE_FREE empirically), R3 (scaling = continuum), PA-char1 (homogeneous fixed-point), PA-q-to-1 (slope = exponent not radius), QD. Lit (web-searched, quoted): Connes–Consani *Characteristic one, entropy and the absolute point* (0911.3537); *Riemann–Roch for $\overline{\mathrm{Spec}\,\mathbb Z}$* (2205.01391), *On the Jacobian of Spec ℤ* (2602.15941); the finite-semifield classification (Lescot; 0911.3537 §2.6). Numerics: inline mpmath 40dps (this log).

## The mandate (charter C1)

Characteristic 1 (idempotent/tropical addition, `a⊕a=a`, so `1+1=1`) is a GENUINE new additive structure — a native finite-characteristic-style addition, not char 0. The charter's three sharp questions:
1. **Is the `q→1` dequantization FORCED, or is there a non-degenerate char-1 geometry where a scale survives?** In char 1, what plays the role of `|𝔽_q|=q` — is there a finite char-1 "size" that is NOT 1?
2. **Deepest version:** does the char-1 Frobenius `x↦x^λ` admit a DISCRETE arithmetic sublattice of `λ` carrying a scale, rather than the full continuum `ℝ₊^×` (R3 found the continuum)?
3. **Anchor:** an `𝔽_q` reduced to char 1 — does `q` survive or go to 1? Falsify DH.

This pass answers all three at THEOREM grade (not just empirically as F1-T did).

---

## What the literature ESTABLISHES — the finite-semifield classification (the decisive new fact)

**[lit·1 · THEOREM] A finite semifield is EITHER a finite field (char `p`) OR the Boolean semifield `B={0,1}` (char 1).** [Connes–Consani 0911.3537 §2.6; Lescot] (web-search-quoted)
> "The multiplicative group of a finite strict semifield is finite and torsion-free so it is trivial. … We have `1+1=1` … Therefore we get the Boolean semifield. … There is only one finite semifield which is not a field. If a semifield contains a non-trivial root of unity it is a field. The only finite semifield which is not a field is `B`."

This is the load-bearing result F1-T did not have in theorem form. It says: **the only finite characteristic-1 semifield is `B`, whose multiplicative group `B^×={1}` has order 1.** There is NO finite char-1 object of "size" anything but 1 (multiplicatively). The `q→1` dequantization is therefore **not incidental — it is the classification theorem.** A finite char-1 size that is `≠1` does not exist.

**[lit·2] The proof mechanism IS the char-divide, native.** [0911.3537, mechanism]
- Char 1: addition idempotent ⟹ `n·1 = 1` for all `n` (the additive "order" of 1 is replaced by IDEMPOTENCE — `1` is its own sum). This forces the multiplicative group `G` to be TORSION-FREE (a nontrivial root of unity would make it a field). **Finite + torsion-free abelian ⟹ trivial.** So `|G|=1`.
- Char `p`: `n·1` cycles with additive order `p`; the multiplicative group is `ℤ/(q−1)`, cyclic of order `q−1` (HAS torsion); `|𝔽_q|=q` finite `>1`. The finite scale `q−1` (mult torsion) and the finite additive order `p` come together because **one Frobenius `x↦x^q` respects `+` and `×` at once.**

**The exact contradiction:** the finite ADDITIVE characteristic at `∞` (idempotence, `n·1=1`) — which is *precisely what the charter asks char 1 to supply* — is the SAME structure that **kills the finite multiplicative scale** (torsion-free ⟹ trivial). Carrying a finite scale `q≠1` REQUIRES mult torsion (a root of unity), which REQUIRES being a FIELD (char `p`). **Char-1-finite and scale-bearing are mutually exclusive, by theorem.**

**[lit·3] `ℤ_max` — the unique char-1 semifield with infinite-cyclic mult group `q^ℤ` — has size `∞`, not a finite `q`.** [web-search-quoted] "The only semifield whose multiplicative group is infinite cyclic is `ℤ_max`." A DISCRETE `λ`-lattice DOES exist here (`λ∈ℤ`, the exponent lattice `t^ℤ`) — answering charter Q2 — but it is the **infinite** exponent lattice of the Frobenius, with a FREE generator `t` (rescale `t↦t^k`, no marked value), NOT a finite cardinality `|𝔽_q|=q`. The discrete sublattice is the `q^ℤ` of the exponent, scale-free; `q` itself (the base) is unmarked.

**[lit·4] Connes–Consani Riemann–Roch for `\overline{Spec ℤ}` (2205.01391, 2602.15941): the DEGREE is REAL-valued (continuum); only the COUNT (`h^0`, Euler characteristic) is integer.** [web-search-quoted abstract] "the (integer valued) Euler characteristic … a slight modification … in terms of the sum of the **degree of the divisor and the logarithm of 2**." The Arakelov degree of `a·[∞]` is `a∈ℝ` (logs). So the deepest current char-1 arithmetic geometry, even with its genuine Riemann–Roch, gives: **dimension/`h^0` = INTEGER (the count), degree/scale = REAL ℝ (continuum)**. The "scale" at `∞` is the continuum `ℝ` (the char-1 `R_max` constant), never a finite `q`. This is the count/radius decoupling (the-complete-account §5) realized in the most advanced char-1 object: the count is finite (integer), the scale is the continuum.

---

## What got COMPUTED (mpmath 40dps, FF-anchored)

**[1 · forced] The char-1 finite size is 1; `q≠1` requires mult torsion ⟹ a field.** [computed/structural]
`1+1 = max(1,1) = 1` (idempotent): `n·1=1 ∀n` — `1` additively idempotent (NOT order-`p`). `|B^×|=1`. Contrast `𝔽_5`: `1+1+1+1+1=0` (additive order 5 = char), `𝔽_5^×=ℤ/4` (torsion `q−1=4`), `|𝔽_5|=5`. **The finite char-1 size is forced to 1 by the classification theorem.**

**[2 · ANCHOR] `𝔽_q → char 1` (`q→1`): `q` and radius `√q` EVAPORATE.** [computed]
`√q` for `q=25,9,5,3,2,1.5,1.1,1.001 → 5,3,2.236,1.732,1.414,1.225,1.049,1.0005 → 1`. The char-1 limit IS `q→1`; the radius collapses to 1. **`q` is the dequantization parameter sent to 1 to REACH char 1.**

**[3 · ANCHOR-finite] At a genuine finite prime, `q` survives — `Frob=x^q`, `|α|=√q` MARKED.** [computed, anchor PASS]
`(q,a)=(5,1),(7,3),(11,−2),(13,4)` → `|α|=√q={2.236,2.646,3.317,3.606}`, pure. Here `q` is the integer cardinality of the constant field, `Frob=x^q` one ring map doing `+,×` at once (mult torsion `q−1` AND additive char come together). **The discreteness the char-1 continuous `λ` lacks — and the char-1 finite size cannot have.**

**[4 · RR] Connes–Consani degree is REAL (continuum), dim is INTEGER (count).** [computed/structural]
`deg(a·[∞]) = a ∈ ℝ` for `a=0.5,1,log2,π` — the scale lives in the continuum `ℝ`; only `h^0` is integer. No finite `q`: the residue at `∞` is the char-1 `B/R_max`, `|·|∈{1, continuum}`.

**[5 · DH] DH falsified — unposable.** [structural] No Euler product ⟹ no `#X(𝔽_{p^n})` point-count ⟹ Soulé's `𝔽₁`-zeta condition fails ⟹ no char-1 curve / `q→1` limit / Frobenius `x↦x^λ` (the arithmetic/scaling site is built on `(ℕ^×,·)` = the primes, which DH's coefficients do not factor through). DH dies — inherited Euler-product kill.

---

## THE ANSWER to the three charter questions

**Q1 — Is `q→1` FORCED, or is there a non-degenerate scale-bearing char-1?** **FORCED. No non-degenerate scale-bearing finite char-1 exists.** The classification theorem ([lit·1]): the only finite char-1 semifield is `B`, `|B^×|=1`. A size `≠1` requires multiplicative torsion (a root of unity) ⟹ a field (char `p`). The finite char-1 "size" is `1`, by theorem, not by accident. **There is NO char-1 analogue of `|𝔽_q|=q` between `1` and the continuum.**

**Q2 — Discrete `λ`-sublattice carrying a scale?** **The discrete sublattice EXISTS (`ℤ_max`: `λ∈ℤ`, `t^ℤ`) but does NOT carry a finite `q`.** It is the INFINITE exponent lattice of the Frobenius (`q^ℤ`), with a FREE rescalable generator — the count/index half, scale-free (= R3b-BC's discreteness ≠ base size, now at the semifield root). The continuum `ℝ₊^×` (R3) and the discrete `ℤ` (`ℤ_max`) are the only two char-1 Frobenius options; NEITHER marks a finite base `q`.

**Q3 — Anchor / DH.** `𝔽_q`: `q` integer ≥2, `|α|=√q` MARKED (computed, PASS). `𝔽_q→`char-1 is `q→1`: `q` and `√q` EVAPORATE (computed). DH: unposable (no Euler product). **Anchor recovered at the finite prime; char-1 limit kills it.**

---

## The deepened result — char 1 SUCCEEDS at the additive characteristic, and that is EXACTLY why it FAILS at the scale

The charter's sharp target was: give `∞` a FINITE ADDITIVE CHARACTERISTIC (a sense of `p·1=0` at `∞`) carrying a scale `q`. Char 1 is the one direction that **genuinely supplies a finite additive characteristic** — idempotence `n·1=1` is a real new additive structure, not char 0's torsion-free addition. **So the additive half SUCCEEDS** (this is char 1's genuine appeal, and it is more than F1-T credited). But:

> **THE CONTRADICTION [theorem-grade].** The very additive structure that gives char 1 its finite characteristic — IDEMPOTENCE (`a⊕a=a`, replacing additive order `p` by `n·1=1`) — is PRECISELY the structure that forces the multiplicative group torsion-free, hence TRIVIAL (`|G|=1`), hence the scale `q→1`. Over `𝔽_q` the finite additive characteristic (`p·1=0`) and the finite multiplicative scale (`q−1` torsion, `|𝔽_q|=q`) coexist because `n·1` CYCLES (additive ORDER `p`), and one Frobenius `x↦x^q` carries both. Char 1's additive characteristic is the DEGENERATE one (`n·1=1`, idempotent, no order), and idempotence ⟹ no mult torsion ⟹ no finite scale. **`p·1=0` at `∞` via idempotence is the `p→1` corner where the scale is identically `1`.** The two halves the charter needs TOGETHER — finite additive characteristic AND a finite scale — are, in char 1, MUTUALLY EXCLUSIVE by the finite-semifield classification.

This is the char-0/char-p divide re-derived from the characteristic-1 ROOT, now as a theorem about what a "number" can be: a finite additive characteristic at `∞` *of the idempotent kind* is not contradictory with `ℚ` (it is the dequantized shadow), but it carries NO scale — it is the `q→1` degenerate characteristic. The non-degenerate finite characteristic that carries a scale is char `p`, which `∞` provably is not.

---

## Verdict — DEGENERATE (`q→1` FORCED by theorem; the additive characteristic succeeds but is scale-free)

> **[DECISION · NF-C1].** Characteristic 1 (idempotent addition) IS a genuine new additive structure giving `∞` a finite additive characteristic (`n·1=1`, not char 0) — the charter's additive target is met. **But the `q→1` dequantization is FORCED, not incidental:** the finite-semifield classification theorem (Connes–Consani / Lescot) proves the only finite char-1 semifield is `B` with `|B^×|=1`; a finite scale `q≠1` requires multiplicative torsion (a root of unity), which makes the object a FIELD (char `p`). The idempotence that GIVES the additive characteristic is the SAME structure that KILLS the scale (torsion-free ⟹ trivial mult group). The discrete `λ`-sublattice exists (`ℤ_max`, `t^ℤ`) but is the infinite, free, scale-free exponent lattice — not a finite `q`. The deepest current char-1 object (Connes–Consani Riemann–Roch for `\overline{Spec ℤ}`) has INTEGER dimension (the count) but REAL degree (the continuum scale) — `ℝ`, never a finite `q`. Anchor: `q` MARKED at the finite prime (`|α|=√q`, computed), EVAPORATES (`q→1`) in the char-1 limit. DH unposable. **DEGENERATE: char 1 gives a finite additive characteristic but a scale-free one (`q→1`), and the scale-freeness is a THEOREM, not a gap — strengthening F1-T from empirical to forced.**

## Falsifier verdict (NF-C1 — terminus characterizer, Euler-silent by design)
- **EULER-BORNE — NO, by design.** Type-checks char-1 finiteness against the anchor; not a standalone ℤ-positivity. DH: unposable (no Euler product ⟹ no point-count ⟹ no char-1 curve).
- **SEES-ZEROS — YES** only via the Connes–Consani spectral realization (RH = spectrum on the self-dual axis `½`), which the continuum scaling does not force.
- **INDEPENDENT — NO** (the `½` is the FE-fixed DH-shared locus; the finite `q` it lacks IS RH over `𝔽_q`).
→ DISPERSING-by-design. Registered as a new-foundations terminus: the char-1 root gives the **finite additive characteristic at `∞` (real, new) but provably scale-free** — the count (`χ`/`h^0`/`ℤ_max` index) survives, the scale (`q`) is forced to 1 by the finite-semifield classification.

## Residual / blueprint
The precise residual: a finite char-1 object whose multiplicative group has TORSION (a marked finite `q−1`) WITHOUT collapsing to a finite field — provably impossible by the classification theorem ([lit·1]). The only way to get finite mult torsion is a root of unity ⟹ char `p`. So the blueprint is **self-defeating in char 1**: re-importing the finite scale means re-importing char `p`, i.e. a finite constant field at `∞`, which `Spec ℤ` lacks (R8). Char 1 is the cleanest statement of WHY: it is the `p→1` corner where the additive characteristic is idempotent (free) and the multiplicative scale is forced to 1. **The finite additive characteristic at `∞` is COMPATIBLE with `ℚ` (the dequantized shadow), but it cannot be the SCALE-BEARING (char-`p`) kind — that requires the multiplicative torsion char 1 structurally forbids.** Candidate C1 CLOSED — DEGENERATE, by theorem.
