# PA2 — the EQUALITY-CLAUSE attack: is the per-eigenvalue radius the Hard-Lefschetz/primitivity equality, or = F F† = q·Id (RH)? [DECIDED · circular-terminus]

`[BUILT + CONJ on the II₁ side · coherence-checked vs F_q]` — 2026-06-06
Module: `scripts/numerics/witness/equality_clause_lefschetz.py`
(run: `python3 -m scripts.numerics.witness.equality_clause_lefschetz`). The ONE not-yet-tried synthesis
named by `PA-synthesis.md` §"The ONE not-yet-tried synthesis", attacked and DECIDED.

## The mandate (the decidable test)

RH = the AM–GM **EQUALITY case** `|αᵢ| = q^{w/2}` for EVERY `i` (zero variance of the moduli), NOT the
geometric mean `det/count` (free). Classical Hodge–Riemann carries an **inequality** (the signature /
Weil positivity) AND an **equality clause** classically tied to the **Hard-Lefschetz isomorphisms** /
the **primitive (Lefschetz) decomposition**. The test: is the per-eigenvalue radius equality

- **(i)** `F F† = q·Id` (= Weil positivity itself = RH) → **CIRCULAR**, terminus; OR
- **(ii)** a **SEPARATE** coherence — a Hard-Lefschetz / primitivity equality NOT equal to Weil
  positivity (the sl₂ iso `L^j : H^{w−j} ≅ H^{w+j}` as a STRUCTURAL equality that forces
  `|αᵢ|=q^{w/2}` per-eigenvalue WITHOUT assuming a positivity) → the **first genuine lead**.

## What got BUILT (the equality-clause object, two anchors, exact)

The cleanest carrier of BOTH a Hard-Lefschetz iso AND a Hodge–Riemann form is the **monodromy/Lefschetz
sl₂** (Jacobson–Morozov, R1): `e = L` (raising / cup-with-ample), `f = N` (lowering / monodromy log),
`h` the weight grading. Built `(e,h,f)` exactly on a Jordan-3 irrep (weights `{−2,0,+2}`, a centre).

**[1] The HL iso — equality of DIMENSIONS, no moduli.** `e^j : (h=−j) → (h=+j)` is an exact
isomorphism (`dim gr_{−j} = dim gr_{+j} = rank`, COMPUTED). This is pure sl₂ representation theory — a
**structural/combinatorial** equality, using no eigenvalue, no modulus. So **(ii)'s premise is real**:
HL *is* a separate equality from the positivity form.

**[2] THE DECISIVE PROBE — does HL-compatibility force the radius?** Built a Frobenius `F` satisfying the
**arithmetic Hard-Lefschetz compatibility** `F·e = q·e·F` (cupping with an ample class raises Frobenius
weight by 2 = scales by `q`; the geometric Frobenius–Lefschetz relation), parametrized by its action on
the **primitive (lowest-weight) seed** (free) and **propagated up each sl₂ string** by `F e = q e F`.

| seed | `‖F e − q e F‖` (HL-compat) | per-weight `|eig|` vs `q^{k/2}` | radius matched? |
|---|:--:|---|:--:|
| **pure** (seed modulus `q^{wmin/2}`) | `0.00e+00` | `k=−2:0.111, k=0:1.0, k=+2:9.0` = `q^{k/2}` | **YES** |
| **impure** (seed pushed off circle, ×e^{0.4}) | `0.00e+00` | `k=−2:0.166, k=0:1.49, k=+2:13.4` ≠ `q^{k/2}` | **NO** |

> **An HL-compatible-but-IMPURE Frobenius EXISTS** (the relation `F e = q e F` holds to machine zero for
> BOTH, yet the impure one is off the per-eigenvalue circle). **Hard-Lefschetz compatibility fixes the
> RATIO of moduli across a string (a factor `q` per `e`-step = the symmetric centering = the COUNT) but
> leaves the PRIMITIVE seed's ABSOLUTE modulus FREE.** HL propagates the primitive modulus
> `q`-equivariantly; it does NOT pin it. **The radius is NOT forced by HL alone.**

**[3] II₁/Connes continuous-dimension version `[CONJ]`.** HL becomes `τ(P_{+j}) = τ(P_{−j})` (equal
Murray–von Neumann dimension of the weight projections; COMPUTED `=0.333` both, `τ(1)=1`). `τ` reads the
normalized **COUNT** and is **sl₂-invariant** — same blindness as the trace (R8/R10/von_neumann_typeII1):
it CANNOT see a per-eigenvalue modulus. The probe [2] carries over verbatim — the `τ`-equality fixes the
symmetric continuous COUNT, never the primitive's absolute modulus. (Marked `[CONJ]`: argued by the
invariance of `τ` under the sl₂, not separately re-instantiated on a genuine `II₁` factor — the finite
model already exhibits the mechanism and the trace-invariance is the standard `II₁` fact.)

**[4] CIRCULARITY AUDIT — the HR equality clause, written out.** The two-sided Weil/Hodge–Riemann bound
SQUEEZES `|α|` to `q^{w/2}` **exactly when** `F F† = q·Id` on the primitive part (COMPUTED: the q-isometry
holds for the pure config, fails the instant one eigenvalue leaves the circle). **The HR-positivity
equality clause IS the q-isometry of Frobenius = purity = Weil II = RH.** Substituting it is circular.

## The decision: (i), with a NEW decomposition of WHY

The attack does NOT collapse to a bare restatement. It **locates** the radius inside the Hodge–Riemann
package and proves a genuine structural split:

- **Hard-Lefschetz / primitivity IS a separate equality from Weil positivity** — `(ii)`'s premise is
  vindicated: the sl₂ iso is real, structural, positivity-free. **But it delivers the COUNT, not the
  radius**: it fixes the symmetric multiplicities and the per-string `q`-ratio (the centering), and is
  blind to the primitive's absolute modulus.
- **The radius equality is the OTHER half** — the HR **inequality's equality clause** `F F† = q·Id`,
  which is exactly purity = Weil II = RH.

So the count↔radius decoupling that R8/R10/PA-synthesis isolated **recurs one level deeper**, *inside* the
Hodge–Riemann relations themselves: HL/primitivity (the iso) carries the COUNT; the polarization
inequality's equality clause carries the RADIUS, and that clause is the isometry = RH. The two
Hodge–Riemann ingredients **partition exactly along the count/radius fault line**. That is the new
content — not a lead, but a sharper terminus: it answers *which* Hodge-theoretic datum the radius is
(`F F†=q·Id`) and proves the *other* candidate (HL iso) provably cannot supply it.

## Anchor / DH / falsify

- **ANCHOR (recover `q^{1/2}` on the FF curve w/o zeros):** recovered **only** with the pure primitive
  seed `[2a]`; the HL iso alone admits the impure seed `[2b]` at zero compatibility-residual. So HL does
  NOT recover the radius without assuming the isometry. (The pure-seed recovery itself ASSUMES the very
  modulus it would derive — the circularity, made visible.)
- **DH:** **unposable** — no Euler product ⟹ no Frobenius `F` ⟹ no operator to test; the sl₂ `(e,h,f)`
  EXISTS for DH (DH-shared archimedean Hodge/Γ structure, R2) but carries no `F`, no `q`. Consistent with
  R1's (N3)-vacuity. **The radius-bearing half is exactly the DH-distinguishing half DH lacks.**
- **`falsify.py` three axes:** EULER-BORNE **NO** (Euler-silent terminus-characterizer like R1/R2/R8/R10;
  type-checks the FF anchor, not a standalone ℤ-positivity) → **DISPERSING-by-design**. SEES-ZEROS
  **YES** (the radius = even split = where zeros sit). INDEPENDENT **NO** (the equality clause =
  `F F†=q·Id` = Weil II = the solved case). Were it Euler-borne it would classify **CIRCULAR** — the
  load-bearing INDEPENDENT axis fails. Registered as the **47th wall confirmation**.

## Verdict

`[circular]` — **CIRCULAR (terminus confirmed), with new structural content.** The per-eigenvalue radius
is **(i)** `F F† = q·Id` = Weil positivity = RH, NOT a separate Hard-Lefschetz/primitivity equality.
**New content (not a bare restatement):** Hard-Lefschetz/primitivity IS a genuinely separate equality
from the polarization positivity — but it is the **COUNT** (the symmetric multiplicities + the per-sl₂-
string `q`-ratio / centering), provably **blind to the primitive's absolute modulus** (an HL-compatible-
but-impure Frobenius exists at zero compatibility-residual). The radius lives in the **equality clause of
the HR inequality**, and that clause is exactly the q-isometry `F F†=q·Id`. The count↔radius decoupling
recurs *inside* Hodge–Riemann: the two ingredients (HL iso / polarization positivity) partition along the
count/radius fault line. PA-synthesis's predicted ~85–90% circular outcome is **confirmed and explained**.

**The next step IF one still hunts (the residue, re-sharpened):** the only remaining handle would be a
structure forcing the **primitive seed** modulus to `q^{wmin/2}` *non-positively* — but [2]+[4] prove that
forcing IS the isometry. The honest read: this closes the equality-clause route; the radius is the
isometry `F F†=q·Id`, the irreducible open ingredient (R8 constant-field cardinality / R10 purity-on-
the-spectrum), now shown to be the HR equality clause and NOT manufacturable from the HL iso.
