# global-frobenius — index

A greenfield arc toward the F_1 / Connes–Deninger object, reframed as a single
primitive: a **global/archimedean Frobenius** on the compactified Spec Z, from
which the square correspondence, its duality, and the Rosati positivity
(<=> RH) are derived. Opened 2026-06-29 from the synthesis of the prior
End(S^2/Z) arc (research/proof/), keeping its proven discipline and discarding
its two failure modes.

## Read in order
1. `CHARTER.md`   — the original target, layers, foundation, success spec.
2. `05-dichotomy-pivot-charter.md` — **the committed pivot** (current primary goal).
3. `ATLAS.md`     — the living map of the far side of the wall (the dual product).
4. `DISCIPLINE.md`— the operating rules (deliverables, anti-regress, guards).
5. `00`–`04`      — the cycle trail that led here (CC ground → dichotomy → W2 closed).

## Pivot in one line (2026-06-29)
After W2 closed (doc 04, no leak), the arc COMMITTED to proving the
integrality–summability dichotomy **fundamental** (bounded-negative), with the
far-side **ATLAS** as a standing dual product so a stall stays productive. The
unifying fact: the wall's only door = the program's original target (a canonical
multiplicative Frobenius at ∞), so proving the wall and mapping the missing
object are the same activity. Phase 1 (bounded): close **W1** + pin class **C**;
hard checkpoint (A→draft theorem / B=leak→swing positive / D=RH-equivalence→bank
wall + full atlas).

**Phase-1 checkpoint reached (docs 06+07).** (T) **W1 proved** — the
staircase-defect pole is shape-independent (residue ∝ 1/log b for *every* effective
integer dimension, not just CC's ceiling; `gf_w1_residue_offset_independence` exit
0), so side A holds for the whole class. (M) **Class C pinned** = integer-valued
additive/localizing invariants; its boundary = the additive/multiplicative line =
the F1 door. **Honest correction to doc 03:** "canonical" does *not* force
"additive" — canonical *multiplicative* structures (norm/Frobenius/δ) are canonical
yet non-additive, so the squeeze does not close; it *locates* the door precisely =
a canonical multiplicative structure at the archimedean place = the program's
original target. The two-sided theorem is now assembled within C (side A = W1 +
doc 04; side B = Efimov), modulo routine Euler–Maclaurin write-up. Checkpoint reads
toward **A** (no RH-input was needed — not D). Live question is entirely far-side:
**F1** — does a canonical multiplicative integer structure exist at ∞?

**Phase 2 done both ways (docs 08+09).** (Theorem) The bounded-negative result is
**drafted** (additive form), assembled from the certified witnesses + Efimov; its
one real gate is obligation **O1** (self-intersection = additive tower sum, general
form). (Door) Walking through F1: it's **occupied** by the canonical multiplicative
structure at ∞ — the scaling flow / Deninger's Θ — but that has **continuous
spectrum**, so it does *not* escape (self-intersection = the transcendental
−ζ′(0)). **Lindemann anchor:** −ζ′(0)=½log2+½logπ, and ½logπ is provably *not*
finite-place type (else π algebraic) — so the transcendental horn is now a theorem
(`gf_archimedean_no_finite_q` exit 0). The program has **collapsed to one
question Q:** does a canonical *discrete* (finite-q) Frobenius exist at ∞ — a
discretization of Θ? YES ⇒ the missing object ⇒ RH; NO ⇒ the door shuts and the
theorem extends to the full canonical class. Two live fronts: close **O1**
(theorem rigor) and the **multiplicative-extension target** (canonical archimedean
multiplicative ⇒ continuous spectrum; Lindemann = brick 1).

**Terminus reached (docs 10+11).** **O1 reduced** to a trace theorem —
⟨Δ,Δ⟩ = tr(id) = Euler characteristic (Ponto–Shulman additivity of traces);
non-dualizability over Z̄ forces regularization; the sharp residual is
regularization-uniqueness via S1. **The multiplicative door is shut** for all known
canonical structures — named mechanism: **R₊^* has no canonical generator** (a
discrete archimedean Frobenius = a canonical "q at ∞" = a non-canonical choice,
forbidden by S1; finite places have a canonical Frobenius generator, ∞ does not).
So the bounded-negative branch is **complete over the known canonical class**
(additive 08+10, multiplicative 11). The wall is fully drawn; there is exactly
**one door = a canonical q at ∞ = the F_1 problem**, which the program can't
adjudicate from inside. Two named residuals: (O1-iv) regularization-uniqueness;
(F_1) an unknown canonical archimedean discretization (the positive escape). Two
end-states: **(a)** bank the combined theorem (recommended — the durable mapped
wall); **(b)** attack F_1 directly (open frontier, unbounded).

## One-paragraph state
Target: the global Frobenius `F` with purity `|eig F| = N^{w/2}` (CHARTER sec 2).
Foundation to build ON (a theorem): Connes–Consani curve-level Riemann–Roch +
Pontryagin–Serre duality for compactified Spec Z (arXiv:2205.01391, 2306.00456)
+ the Pic/Jacobian infrastructure. The gap = the self-product / square joint
(R1), where CC departs from the function-field analogy. Primary named wall:
the carrier wall — multiplicativity (the Euler product) must be STRUCTURE, not
a property. Cycle 0 LANDED (doc 01, no-go "Frobenius-free RR"): CC reproduce the
FE-layer (RR/duality/Jacobian) via Pontryagin duality as a Frobenius surrogate
and route to a rank-1 adele-class Jacobian, not a square — so build-on-CC is the
right foundation but inherits only the RH-neutral layer; the RH-grade primitive
(integer intersection form on a self-product) is the omitted residue. Convergence
check FIRED (three venues, one wall; p-local artifact shed). Cycle 1 LANDED
(doc 02, no-go "integrality–summability dichotomy"): CC's integer dimension is a
ceiling (`dim = ⌈log₃(2n+1)⌉`, Prop 3.3) — integral level-wise but the
regularized tower diverges (simple pole at s=0, residue −1/(2 log 3); finite
part rational, scheme-laden). An integer intersection form on a self-product
needs BOTH integrality AND a summable pairing; the dichotomy forbids both, so
CC's integer-dim has no Künneth extension. Convergence FIRED again (four venues,
one wall — now a certified pole, first candidate structural CAUSE). Investigation (doc 03) scoped whether the
dichotomy is FUNDAMENTAL: plausibly a bounded theorem over C = additive/
localizing integer invariants (contains every tested construction). Two-sided —
(A) scale-aware ⇒ geometric jumps (density 1/log b, Census-certified universal,
`gf_dichotomy_jump_density` exit 0) ⇒ s=0 pole ⇒ divergent total; (B) scale-blind
⇒ no intersection content (Efimov, already a theorem). Side A reduces to one
elementary Dirichlet lemma. The squeeze: fundamentality meets rigidity spec S1
⇒ bounded-negative terminus. Decisive weak link **W2**: does a 2-variable
self-product zeta escape the s=0 pole? **Cycle 2 closed W2 (doc 04, no leak):**
all three natural 2-variable models are polar on the diagonal (M1 product
H¹⊗H¹: double pole; M2 additive: simple pole; M3 normal-bundle: double pole),
and the only finite value is the certified *non-integer* transcendental
−ζ′(0)/log b — finite⟺alternating⟺transcendental, integer⟺divergent
(`gf_selfproduct_pole_escape` exit 0). The square supplies no properness; it
double-diverges the genuine 2-dim content. **The fork resolved toward
bounded-negative.** Only **W1** (an elementary Mellin sawtooth lemma, combinatorial
core already Census-certified) now stands between here and writing the
fundamentality theorem. Current target: prove W1, then draft the theorem (the
charter's bounded-negative branch — does NOT disprove RH; the lone open escape, a
canonical-but-non-additive form, is in tension with rigidity spec S1).

## Why this reframe (the inheritance, one line each)
- Three walls = one: no Frobenius on bar(Spec Z); radius/properness/carrier are
  its three faces. The carrier wall is primary.
- Wrong venue retired: p-local homotopy (TCR(F_2)/DMP) sees only the shadow;
  the Z/2 Weyl-shear obstruction is a p-local artifact. Use it only as a probe.
- One durable residue kept: the rigidity blueprint (terminal/contractible/
  dagger-pivotal/exact-K0/Hecke) = the success spec (CHARTER sec 4).
- Scope fixed: existence => RH (not iff); no "unknowable" branch (RH is Pi_1).

## Witnesses
`scripts/numerics/witness/`, run `python3 -m scripts.numerics.witness.<name>`,
exit 0 = claim reproduces. python-flint + numpy. Naming under DISCIPLINE sec 2.

## Ledger
`ledger.json` — the no-go bank + verified sub-objects, registered as they land
(starts empty; one entry per theorem-grade deliverable).
