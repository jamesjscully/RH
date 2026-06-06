# Thread 1 — Reflection positivity / QFT / stat-mech as the source of the Weil positivity

*(opened 2026-06-06; §8 discipline: [THM] proven, [PROG] partial/program, [CONJ] conjecture,
[AN] analogy-only. Sources quoted; results vs. analogy distinguished.)*

**The bet.** The Weil positivity `Σ_ρ ĥ(γ) ≥ 0` (⟺ `λ_n ≥ 0` ⟺ RH) is the
**Osterwalder–Schrader / reflection positivity** of a Euclidean field theory, or the positivity
of a stat-mech partition function — a positivity *automatic from physics* rather than assumed.
The GUE/random-matrix statistics of the zeros are the loud hint a physical/probabilistic model
underlies them.

**Verdict up front.** Every concrete model surveyed is **RH-neutral or circular**: it either
*reformulates* the positivity it needs (lattice gas, Berry–Keating, BBM Hamiltonian), or it is a
statement *conditional on / equivalent to* RH about the zeros once they are already on the line
(determinantal/GUE statistics). **No surveyed model exhibits a reflection positivity that is
(a) Euler-product-borne, (b) genuinely independent of the Weil positivity, and (c) fails for
Davenport–Heilbronn.** This matches the program's standing classification of reflection positivity
as *untested but unexplored as a true OS construction* (`positivity-program.md` §C). Below: the four
candidate families, where each dies on the kill-test, and the one move that is genuinely new.

---

## 1. The candidate physical / probabilistic models (a),(b),(c)

### (a) "Hamiltonian for RH" literature — Berry–Keating, Bender–Brody–Müller, Connes
- **Berry–Keating `H = xp`** [CONJ/AN]. Heuristic semiclassical match of the zero-counting smooth
  term; the operator "is symmetric but not necessarily self-adjoint … may have nontrivial deficiency
  indices," "breaks time reversal invariance," and "it is not known a quantization of `H = xp`
  yielding … the Riemann zeros as eigenvalues" (search synthesis of Sierra et al.,
  arXiv:1012.4264, math-ph/0702034). **No positivity is constructed**; this is the Hilbert–Pólya
  *reflection* hope, not a forcing.
- **Bender–Brody–Müller (2017, PRL 118:130201; arXiv:1608.03679)** [CONJ]. Build `H` with
  eigenvalues `E_n` s.t. zeros are `z_n = ½(1 − i E_n)`; `iĤ` is "PT symmetric with broken PT
  symmetry, thus allowing for the possibility that all eigenvalues are real." Quote: *"If the
  analysis can be made rigorous to show that the Hamiltonian is manifestly self-adjoint, then this
  implies that the Riemann hypothesis holds true. However, the property that maximally broken PT
  symmetry would guarantee real eigenvalues … remains to be proved."* The positivity (reality of
  spectrum) is **assumed, not derived** — and the construction was challenged (arXiv:1704.02644).
- **Connes' scattering / "absorption spectrum"** is the program's own Stone 1
  (`scattering.py`, `the-lift-program.md` §7): `S(s)=Λ(2s−1)/Λ(2s)`, unitary on `Re ½`. Already
  kill-tested **RH-neutral**: the self-adjoint/unitary structure holds verbatim for an off-line-zero
  function (Lax–Phillips obstruction). This is the same wall every Hilbert–Pólya operator hits.

**Why this whole family is RH-neutral:** self-adjointness/PT-reality is exactly the conclusion one
wants, so positing it is circular; nothing in these constructions *forces* it. The program already
records this as **stone 1 / "reflects not forces"** (`positivity-program.md` §C row "self-adjointness
(Hilbert–Pólya): RH-neutral").

### (b) Random-matrix / determinantal-process angle
- **Montgomery–Dyson + Keating–Snaith** [THM, conditional] + [CONJ]. Under RH the zero correlations
  match the **sine-kernel determinantal point process**, `K_sin(x,y)=sin(πν(x−y))/(π(x−y))`; "all
  orders correlations of the ζ zeros coincide with determinants of the sine kernel" (Bourgade,
  CIMS notes; Rodgers, *Arithmetic consequences of the GUE conjecture*). Bourgade–Kuan proved (under
  RH) linear statistics → Gaussian field with `H^{1/2}` covariance (strong-Szegő analogue,
  CPA 2013).
- **Is the zero process determinantal, hence positive, hence forcing the line?** *No.* The sine
  kernel is a determinantal process **on the line ℝ after the zeros are already assumed real (RH)
  and unfolded**. Its positivity (a valid correlation kernel, `0 ⪯ K ⪯ I`) governs **spacings along
  the critical line**; it says nothing about a zero leaving the line. The determinantal positivity is
  **a consequence of / conditional on RH**, not a lever onto it. Rigidity results (Ghosh–Peres;
  Sine_β, arXiv:1804.01216) are likewise *intra-line*.

**Why (b) is RH-neutral:** the positivity is real and beautiful but lives on the wrong axis — it
constrains the horizontal arrangement of points that are *postulated* to be on the vertical line.
There is no kernel positivity here whose failure would push a zero off the line.

### (c) Genuine reflection-positive / stat-mech model whose OS-positivity = `Σ_ρ ĥ(γ) ≥ 0`
- **Lattice gas of primes (Mussardo–LeClair / "A lattice gas of prime numbers and the RH",
  arXiv:1211.6621, 2012)** [AN/CONJ]. Primes as occupied sites of a 1-D lattice gas; the real parts
  of the zeros **extremize a grand potential `Ω`**, "the critical point being located at 1/2 as the
  Riemann Hypothesis claims." But the analysis (WebFetch): *"reformulative rather than forcing … it
  restates RH in thermodynamic language without providing an independent positivity argument … that
  would rigorously enforce the zeros on the critical line."* It **does** use the Euler product
  (the prime/`ζ=∏(1−p^{-s})^{-1}` structure is the input) — so it is not DH-blind — **but** the
  positivity is the extremization it imports, i.e. circular.
- **Reflection positivity proper (Osterwalder–Schrader; Jaffe; Neeb–Ólafsson)** [THM, but
  *unconnected*]. RP is a mature, powerful positivity ("imaginary-time analog of unitarity",
  arXiv:1802.09037; "Reflection Positive Doubles", Jaffe–Janssens arXiv:1607.07126; RP ↔ Hankel
  operators, Neeb–Ólafsson arXiv:2105.08522). **Crucially: in none of the located RP literature is
  there a Euclidean field theory or RP-double whose reflection-positivity specializes to the Weil
  explicit-formula functional.** The Hankel/RP connection (positive Hankel forms ↔ RP) is the closest
  structural bridge to Weil's quadratic form (Connes–Consani control the archimedean Weil functional
  precisely via **Hermitian Toeplitz/Hankel matrices** — see §2), but **the bridge has not been
  built**: no one has exhibited the explicit formula as an OS reconstruction.

---

## 2. The kill-test verdict

**Standing kill-test** (`positivity-program.md` §B): a candidate must (a) be Euler-product-borne,
(b) fail for Davenport–Heilbronn (same `Γ_ℝ`, but no Euler product ⟹ off-line zeros) and Epstein,
(c) not reduce to the assumed `λ_n ≥ 0`. DH is the litmus: *"a zeta function possessing a functional
equation but no Euler product, with … non-trivial zeros wide of the critical line … shows a
functional equation is insufficient for RH"* (search synthesis; arXiv:2503.24275, 1602.06328).

| model | Euler-product-borne? | fails for DH? | independent of Weil pos.? | verdict |
|---|---|---|---|---|
| Berry–Keating `xp` / BBM `H` | no (FE/counting only) | **no** (DH-blind) | no (assumes reality) | **RH-neutral** |
| Connes scattering `S(s)` (Stone 1) | no (FE only) | **no** | no | **RH-neutral** (proven, Stone 1) |
| sine-kernel determinantal process | no (intra-line) | **no** (DH zeros also have spacings) | no (conditional on RH) | **RH-neutral** |
| prime lattice gas (Mussardo–LeClair) | **yes** | plausibly yes (no Euler prod ⟹ no gas) | **no** (imports extremization) | **circular** |
| generic OS / RP double | n/a — no model built | — | — | **untested (not yet a model)** |

**Net:** the only candidate that even *sees* the Euler product (prime lattice gas) fails leg (c) —
its positivity is the conclusion. Every RH-neutral candidate fails legs (a)+(b): being built from
`Γ_ℝ`/FE/counting data alone, it would hold verbatim for DH. This is the **4th–5th confirmation** of
the program's recurring finding: *archimedean/FE/spectral data is RH-neutral; only the Euler product
discriminates* (`the-lift-program.md` §7, Stones 1–2).

---

## 3. Is reflection positivity a genuine NEW lever, or tried-and-stalled?

**It is genuinely under-explored as an OS construction — but with one decisive caveat that downgrades
the bet.** Findings:

1. **Not yet tried in the strong form.** No located work realizes the Weil explicit-formula
   functional as the OS reconstruction of an honest reflection-positive Euclidean theory. The
   "physics of RH" corpus (Schumayer–Hutchinson, *Rev. Mod. Phys.* 83:307 (2011), arXiv:1101.3116)
   catalogues lattice gases, quantum chaos, BEC analogies — **all reformulations**, none an RP model
   with automatic OS-positivity. So as a *construction*, RP is new here.

2. **But the structural bridge already exists on the Connes–Consani side, and it stalls exactly where
   the program already stalls.** RP ↔ **positive Hankel/Toeplitz forms** (Neeb–Ólafsson
   arXiv:2105.08522). Connes–Consani (*Weil positivity and trace formula, the archimedean place*,
   Selecta 2021; arXiv:2006.13771) prove archimedean Weil positivity precisely by *"the theory of
   Hermitian Toeplitz matrices as a key device,"* via the Sonin-space compression of the scaling
   action — and "All the ingredients … make sense in the general semi-local case, where Weil
   positivity implies RH." **So the Weil functional is already a (Hankel/Toeplitz) positivity
   problem.** RP would, at best, give a *physical reason* for that Toeplitz positivity. The hard step
   — extending the archimedean positivity to **dominate the prime sum, globally and equivariantly** —
   is identical to the program's open **Stone 3** (`the-lift-program.md` §7). RP does not obviously
   supply the global/prime domination any more than CC20 does.

3. **The decisive caveat (why RP likely inherits the same RH-neutrality):** OS positivity is a
   property of the *measure/action* of a Euclidean theory and is, in itself, **insensitive to the
   Euler product** unless the prime data is *built into the reflection*. A reflection on the
   archimedean/scaling geometry (the natural one) would be RH-neutral — it would equally certify DH.
   For RP to be a *new* lever it must be a **reflection whose positivity is destroyed by the absence
   of the Euler product** — i.e. the reflection must act on the *prime* (adelic, finite-place)
   structure, not the archimedean one. **That is the open, unbuilt object.** This is the same demand
   as the program's condition 4 (`the-lift-program.md` §5).

**Status update for the trackers** (auditor + candidate tracker):

- *Candidate tracker* `positivity-program.md` §C, row "reflection positivity (OS/QFT): untested" →
  refine to: **RP-as-reformulation = RH-neutral (lattice gas circular); RP-as-honest-OS-construction
  = genuinely unbuilt, but only a new lever if the reflection acts on the prime/adelic structure
  (not the archimedean one) so its OS-positivity fails for DH.**
- *Auditor* `positivity-program.md` §B, new row:
  | function-field structure | over ℤ | status / breakpoint |
  |---|---|---|
  | (QFT analogy) OS reflection on Euclidean time | reflection on the adelic/prime structure | **breaks/open**: archimedean reflection is RH-neutral (certifies DH); a *prime* reflection whose RP fails for DH is unbuilt |

---

## 4. The most concrete next step

**Do not build another Hilbert–Pólya operator or lattice-gas reformulation** — both are kill-tested
RH-neutral/circular above. The single move that could turn RP into a real lever:

> **Test whether the Connes–Consani archimedean Weil-positivity (Toeplitz/Hankel form) is the OS
> reconstruction of a reflection acting on the *prime* (finite-adelic) places, and whether that
> reflection's positivity is destroyed for Davenport–Heilbronn.**

Concretely, three checkable sub-steps using the existing scaffold
(`scattering_forcing.py`'s `λ_n`, `S_offline`; `weil_form.py`'s PSD⟺RH; `harness.py`):

1. **Identify the reflection.** Write the Weil quadratic form `W(h,h)=Σ_ρ ĥ(γ)` as a Gram/Hankel
   matrix in a basis adapted to the adelic decomposition `W = W_∞ + Σ_p W_p` (CC20's splitting). Ask:
   is there an involution `θ` (a reflection: `t ↦ −t` on the explicit-formula variable, i.e.
   `u ↦ u^{-1}` under the `ℝ₊^*`-scaling of `the-lift-program.md` §2) such that `W(h,h)=⟨θh, h⟩`
   is manifestly an OS-type pairing `⟨θh,h⟩ ≥ 0`? The conformal corner kernel `−1/(2|u|)` is
   scale-invariant — exactly the kind of two-point function a reflection-positive scale-invariant
   (CFT-like) boundary theory has. This connects Thread 1 directly to the conformal-scattering spine.

2. **Run the DH kill-test on the reflection.** Feed DH's data (same `Γ_ℝ`, no Euler product) through
   the same Gram/Hankel construction. If `θ` and the OS-pairing exist for DH too (with its off-line
   zeros), the reflection is **archimedean/RH-neutral — dead**, confirming RP inherits the wall. If
   the Gram matrix loses positive-definiteness *only* when the Euler product is removed, the
   reflection genuinely sees the primes and we have the first OS-positive object that discriminates.
   This is mechanically the `S_offline` test already wired in.

3. **If (2) discriminates, locate the OS reconstruction theorem** that would upgrade
   "Gram-PSD for ζ, indefinite for DH" into "Re ρ = ½," i.e. an OS → unitary-time reconstruction
   whose unitarity is the critical line. (This is where RP's machinery — Neeb–Ólafsson RP↔Hankel —
   would do real work, *if* step 2 passes.)

**Falsifier (honest framing):** step 2 is the whole bet. If the Hankel/OS positivity of the Weil form
is present for DH, reflection positivity is the **6th confirmation** that archimedean/reflection data
is RH-neutral, and Thread 1 collapses into Stone 3 (the global/prime domination) with nothing added.
The *only* way RP is new is if the reflection is genuinely a **prime-place reflection**, and that
object does not yet exist in the literature.

---

## Sources

- Connes–Consani, *Weil positivity and Trace formula, the archimedean place*, Selecta Math. 2021 —
  https://arxiv.org/abs/2006.13771 (Hermitian Toeplitz device; "semi-local case, Weil positivity
  implies RH").
- Connes–Moscovici, *The UV prolate spectrum matches the zeros of zeta*, PNAS 2022 —
  https://www.pnas.org/doi/10.1073/pnas.2123174119 (negative eigenvalues reproduce squares of zeros).
- Bender–Brody–Müller, *Hamiltonian for the Zeros of the Riemann Zeta Function*, PRL 118:130201
  (2017) — https://arxiv.org/abs/1608.03679 ; Comment: https://arxiv.org/pdf/1704.02644.
- Sierra et al., *A physics pathway to RH* (arXiv:1012.4264), *Dirac-type xp* (arXiv:1205.6755),
  *xp with interaction* (math-ph/0702034) — `xp` not self-adjoint / RH-neutral.
- Mussardo–LeClair, *A lattice gas of prime numbers and the Riemann Hypothesis* —
  https://arxiv.org/abs/1211.6621 (grand potential extremized at Re=½; reformulative).
- Schumayer–Hutchinson, *Physics of the Riemann Hypothesis*, Rev. Mod. Phys. 83:307 (2011) —
  https://arxiv.org/abs/1101.3116 (review; all reformulations).
- Montgomery pair correlation / GUE: Rodgers, *Arithmetic consequences of the GUE conjecture*
  (http://user.math.uzh.ch/rodgers/ArithmeticGUE.pdf); Bourgade CIMS notes
  (https://cims.nyu.edu/~bourgade/papers/PoincareSeminar.pdf); Bourgade–Kuan CPA 2013.
- Reflection positivity: Jaffe–Janssens, *Reflection Positive Doubles* (arXiv:1607.07126);
  *Reflection Positivity* survey (arXiv:1802.09037); Neeb–Ólafsson, *RP and Hankel operators*
  (arXiv:2105.08522).
- Bost–Connes / Connes–Marcolli QSM: Bost–Connes system (Wikipedia; partition function = ζ);
  Connes–Marcolli–Ramachandran (Q-lattices) — KMS positivity is Thread 5, not a forcing of RH.
- Davenport–Heilbronn (FE, no Euler product, off-line zeros): arXiv:2503.24275, arXiv:1602.06328.
- Morán Ledezma, *A probabilistic interpretation of Weil's explicit sums and arithmetic spectral
  measures* (2023) — https://arxiv.org/abs/2311.08519 (covariances on Bohr compactification; does
  **not** claim a positivity that forces RH).
