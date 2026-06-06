# Worker A — QSM free-energy reflection positivity (the convergent lead 1+5+6)

*(opened 2026-06-06; §8 discipline. [THM] proven, [PROG] program, [CONJ] conjecture,
[AN] analogy. Numerics certified in python-flint acb ball arithmetic where they bear on
the spine. Module: `scripts/numerics/witness/qsm_free_energy.py`, run
`python3 -m scripts.numerics.witness.qsm_free_energy`.)*

**The target** (positivity-program.md §F): a reflection-positive continuation of the
Euler-product free energy `F(β) = −log ζ(β)` from the real `β`-axis (KMS/convexity
positivity, Euler-borne, DH-refusing) to the critical line — *made to see the zeros*,
with a DH surrogate that *breaks* it.

**Verdict up front.** Real-axis positivity is **confirmed and certified**, it is
**genuinely Euler-borne**, and the DH surrogate **breaks it** (this is a real, new,
Euler-borne falsifier — promote it). **But the continuation does NOT see the zeros.**
The only reflection-positive (OS/Bochner) object the QSM free energy produces is positive
*automatically* from the Euler-borne nonnegativity `Λ(n)log n ≥ 0` and is **completely
independent of where ζ vanishes** — it holds whether or not RH is true. The naive analytic
continuation of the susceptibility off the real axis is **not** OS-positive (indefinite
Hankel form). **QSM free-energy positivity stalls on the real axis: RH-SILENT** — the
audit's standing classification (thread 5) is confirmed, now mechanically.

---

## 1. Real-axis KMS/Gibbs positivity [CONFIRMED, certified]

Thermodynamics with `β` = inverse temperature, `H` = BC Hamiltonian, `Z(β)=ζ(β)`:

| quantity | formula |
|---|---|
| free energy | `F(β) = −log Z(β) = −log ζ(β)` |
| mean energy | `U(β) = F'(β) = −(d/dβ) log ζ(β)` |
| **energy variance** | `Var_β(H) = −F''(β) = (log ζ)''(β)` |

The Gibbs/KMS state-positivity `φ_β(a^*a) ≥ 0` manifests, for the energy observable, as
`Var_β(H) ≥ 0`. Certified for ζ (acb, prec 300):

```
beta   F         U         Var = −F''      [certified lower bound > 0]
1.2   −1.72126  +4.45834  +24.831493       True
1.5   −0.96026  +1.50524  + 3.854963       True
2     −0.49770  +0.56996  + 0.884482       True
3     −0.18403  +0.16482  + 0.172281       True
5     −0.03626  +0.02756  + 0.022127       True
10    −0.00099  +0.00070  + 0.000491       True
```

`F` is **concave** (`F'' < 0`), equivalently the variance is positive — the standard
thermodynamic-stability / KMS positivity.

**Why it is Euler-borne (the load-bearing identity).**
```
Var_β(H) = (log ζ)''(β) = Σ_n Λ(n) (log n) n^{−β} = Σ_{p,k} (log p)(k log p) p^{−kβ}.
```
Every coefficient `a_n = Λ(n) log n ≥ 0` **because** ζ has an Euler product: the von
Mangoldt function is the log-derivative of `∏_p(1−p^{−s})^{−1}`, hence supported on prime
powers with nonnegative weight. So `Var_β(H) ≥ 0` *termwise* — the positivity is not an
accident of the value, it is a manifest consequence of the product. Confirmed numerically
(every term `≥ 0`, partial sums match `−F''`).

**Phase transition at `β = 1` [THM, Bost–Connes].** `Z = ζ` has a pole at `β=1`; `F → −∞`.
Certified divergence: `Z(1.1)=10.58, Z(1.01)=100.58, Z(1.001)=1000.58`,
`F(1.001) = −6.908`. This is the BC spontaneous-symmetry-breaking transition at inverse
temperature 1 (the boundary of the KMS-convergence half-line).

---

## 2. The crux — the continuation does NOT see the zeros [HONEST NEGATIVE]

The question: is there a reflection `β ↦ 1−β` (the FE symmetry) or an analytic continuation
under which a continued free-energy / two-point function is reflection-positive (OS), and
does that positivity constrain `Re ρ = ½`? **Three tests, all negative.**

### (a) The functional-equation reflection `β ↦ 1−β` does not carry the positivity.
The KMS positivity lives on the *convergent* half `β > 1`. The FE reflection maps it to
`β ∈ (−1,0)` — outside convergence — where the susceptibility flips sign:
```
beta   Var(beta)     Var(1−beta)
1.5   + 3.85496     − 0.14504     ← negative
2     + 0.88448     − 0.93799     ← negative
```
There is **no** `β ↦ 1−β` orbit on which `−F''` stays positive. The reflection that
*would* reach the critical strip is exactly the one that destroys the positivity, because
the positivity is a property of absolute convergence (the Euler product converging),
which the reflection leaves.

### (b) The naively continued susceptibility is NOT OS-positive.
Continue the susceptibility to imaginary time: `G(t) = (log ζ)''(σ + i t)` on a vertical
line `Re s = σ > 1`. Osterwalder–Schrader / reflection positivity demands the Hankel form
`M_{jk} = G(t_j + t_k)` be PSD. It is **indefinite** (σ=2, Hermitized):
```
eigenvalues = [−0.8007, −0.1464, −0.0, 0.0001, 0.0056, 1.4148]   → NOT OS-positive
```
So the obvious analytic continuation of the free-energy susceptibility off the real axis
carries **no** reflection positivity. (The continued `G(σ+it)` *does* have the zeros as
singularities once `σ ≤ 1` — `(log ζ)''` has double poles at the zeros — but no positivity
accompanies them.)

### (c) The GENUINE KMS correlator IS reflection-positive — and that is precisely why it is RH-silent.
The honest KMS/Wightman two-point function of the energy observable is
```
C(t) = Σ_n a_n e^{−i t log n},   a_n = Λ(n)(log n) n^{−β} ≥ 0.
```
Because `a_n ≥ 0` (Euler-borne), `C` is the Fourier transform of a **nonnegative** spectral
measure, hence (Bochner) positive-definite; the Toeplitz/OS matrix `M_{jk}=C(t_j−t_k)` is
PSD:
```
eigenvalues = [0.0005, 0.013, 0.0813, 0.2576, 0.7179, 1.7338, 3.3663]   → OS-positive ✓
```
**This is honest reflection positivity** — but it is *automatic* from `a_n ≥ 0` and is
**completely independent of the location of the zeros of ζ**. The spectral measure
`Σ_n a_n δ_{log n}` lives on `{log n}` (the "energy levels" `log p^k`); the zeros never
enter. The correlator is positive whether or not RH holds. The reflection positivity is
real, the partition function is `ζ`, the primes are visibly in the spectrum — and **none of
it constrains `Re ρ`.** This is the sharpest statement of why thread 5 stalls: QSM hands you
a genuine OS-positive theory whose positivity is built from the *coefficients* (Euler
product on the real axis), not the *zeros* (critical line).

---

## 3. DH kill-test — QSM REFUSES DH [the new Euler-borne falsifier]

`F_DH(β) = −log L_DH(β)`, `L_DH = L(χ_{5,2}) + L(χ̄_{5,2})` (objects.py `DavenportHeilbronn`:
same `Γ_ℝ`/FE, **no Euler product**, off-line zeros). "QSM refuses DH" made precise:

- **Structurally:** a BC/QSM partition function is *by construction* an Euler product
  `∏_p(1−p^{−β})^{−1}`. `L_DH` is a sum of two such, **not** a product — so it is not the
  partition function of any BC-type crossed product. QSM cannot even form the object.
- **Computationally (the sharp test):** because `L_DH` has no Euler product, the Dirichlet
  coefficients of `−L_DH'/L_DH` are **signed** (not `Λ(n) ≥ 0`). Hence `(log L_DH)''` is
  **not** a nonnegative measure, and the "energy variance" goes **NEGATIVE** on a real-β
  interval where ζ's stays positive:

```
beta   Var_zeta     Var_DH
1.1   +99.82237    −0.190651   ← DH NEGATIVE (no Gibbs/partition-function rep)
1.5   + 3.85496    −0.113117   ← DH NEGATIVE
2     + 0.88448    −0.058465   ← DH NEGATIVE
3     + 0.17228    −0.013169   ← DH NEGATIVE
4     + 0.05606    −0.001005   ← DH NEGATIVE
4.5   + 0.03466    +0.000738
5     + 0.02213    +0.001343
```

**This is a genuine discriminator** and the right kind: unlike Nyman–Beurling / RTF (which
evaluate `≥ 0` on DH and are therefore dispersing), the QSM free-energy convexity **breaks
for DH exactly where it holds for ζ**, and breaks *for the right reason* (no Euler product
⟹ no nonnegative spectral measure ⟹ no Gibbs state). It passes legs (a) Euler-borne and
(b) fails-for-DH of the standing kill-test **cleanly**.

**But** — and this is the whole point — this discrimination lives on the **real axis /
convexity**, exactly where the positivity is RH-silent (§2). DH is excluded at the
partition-function stage, not at a zero-forcing stage. The falsifier separates
"has an Euler product" from "doesn't"; it does **not** separate "zeros on the line" from
"zeros off the line." (Indeed ζ and DH differ in §3 not because of where their zeros are but
because DH has no product at all.)

---

## 4. Verdict + most concrete next step

**Real-axis positivity confirmed?** Yes — certified, concave `F`, positive energy variance
`−F'' = (log ζ)'' > 0`, manifestly Euler-borne (termwise `Λ(n)log n ≥ 0`), phase transition
at `β=1`.

**Does the continuation see the zeros?** **No.** The FE reflection `β↦1−β` destroys the
positivity (§2a); the naive continued susceptibility is OS-indefinite (§2b); the one
genuinely OS-positive object (the KMS correlator) is positive *because* `a_n ≥ 0`,
independent of the zeros — **RH-silent** (§2c). This confirms thread 5's verdict
mechanically: a new *kind* of positivity (thermodynamic, state-level), but **not** a new
lever on RH.

**DH kill-test result.** **DH BREAKS the convexity** (negative energy variance on
`β ∈ (1, ~4.3)`) where ζ keeps it — a real, new, Euler-borne, DH-refusing falsifier. The
right *kind* of object; but it falsifies "no Euler product," not "off-line zeros," so it is
not yet a zero-forcing positivity.

**Honest framing.** The QSM free energy is a clean specimen of the program's central
finding (positivity-program.md §E.1): *the Euler product is the sole discriminator, but the
discrimination it provides on the real axis is RH-silent.* The free energy sees the primes
(coefficients) beautifully and sees the zeros not at all. The gap between "Euler-borne
positivity of the *coefficients* on `β>1`" and "positivity that forces the *zeros* onto
`Re s=½`" is **the same wall** as CC20/thread-0: it is crossed only by carrying the prime
data across the functional equation, which the free-energy convexity cannot do.

**Single most concrete next step.** Stop deforming the *real-axis convexity* (it is
RH-silent by §2) and instead test the **off-diagonal / cross-place** structure where the
zeros do enter. Concretely:

> The continued susceptibility `(log ζ)''(s)` has the zeros as **double poles** (§2b). On the
> critical line its imaginary part is the **derivative of the scattering phase**
> `d/dt arg S(½+it)` (Birman–Krein), the thread-6 object. The free energy's only contact with
> the zeros is through this phase. **Build the Hankel form not from `(log ζ)''` on a `σ>1`
> line (RH-silent, §2b) but from the explicit-formula pairing `W = W_∞ + Σ_p W_p`** — i.e.
> hand the free-energy / KMS data to worker B's prime-place reflection `θ` on `weil_form.py`,
> and run the same DH kill-test there. The §3 falsifier ("DH has signed log-derivative
> coefficients") is exactly the ingredient that should make worker B's Gram matrix lose
> positive-definiteness for DH **at the level of the zeros**, not the coefficients. That hand-off
> — real-axis Euler-borne positivity (here) → prime-place OS form on the zeros (worker B) — is
> the place-crossing the convergent lead is really after.

If worker B's prime-place Gram form is OS-positive for ζ and indefinite for DH *at the
zeros*, the convergent lead has its zero-forcing object. If it too is RH-silent, the QSM
branch closes as real-axis-only (fall back to thread 0, globalising CC20).

---

## Auditor rows to fold back into `positivity-program.md`

- **§C tracker**, row `QSM / KMS (Bost–Connes)`: refine to — *real-axis KMS/Gibbs positivity
  CONFIRMED & certified (concave `F=−log ζ`, `−F''=(log ζ)''=Σ Λ(n)log n · n^{−β} ≥ 0`,
  Euler-borne termwise), and it is the program's cleanest **DH-refusing falsifier** (DH's
  energy variance goes negative — signed log-derivative coefficients, no Gibbs rep). **But the
  continuation is RH-silent:** the FE reflection `β↦1−β` destroys the positivity, the
  naive continued susceptibility is OS-indefinite, and the genuine KMS correlator
  `C(t)=Σ a_n e^{−it log n}` is OS-positive *only* by `a_n≥0`, independent of the zeros.
  Real-axis-only, mechanically confirmed.*
- **§B auditor**, new row:
  | function-field structure | over ℤ | status / breakpoint |
  |---|---|---|
  | QSM free energy `F(β)=−log Z(β)`, convexity/KMS positivity | `−F''=(log ζ)''=Σ Λ(n)log n·n^{−β}` | **transfers on `β>1`** (Euler-borne, ≥0 termwise; DH breaks it ⟹ falsifier). **breaks at the line**: FE reflection destroys positivity; the OS-positive KMS correlator is built from coefficients (`a_n≥0`), not zeros — RH-silent |
