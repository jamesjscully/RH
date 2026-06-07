# RH — a forcing-structure search, and where it landed

A research project on the Riemann Hypothesis. It began as a search for a **forcing structure** (a property
provable on its own terms that *forces* the zeros onto the line, not an equivalence that merely restates RH),
filtered by kill-tests (Davenport–Heilbronn, Epstein, Weil positivity). That discipline is intact and is the
reason the project reached a definite, honest result rather than a pile of equivalent reformulations.

## Result

The search reduced RH to a single **reality condition** `F† = F̄` and then proved **two no-go theorems** for
the geometric ("import Weil's function-field proof") strategy:

- **Theorem A (Foundational No-Go).** A finite additive characteristic at the archimedean place of `ℚ` is
  *contradictory* with `ℚ` being characteristic 0 — the definitional identity *archimedean ≡ characteristic 0*
  (Ostrowski + the definition of characteristic + the finite-semifield classification). The finite ground
  Weil's proof needs at `∞` is not missing but **forbidden**.
- **Theorem B (Geometric No-Go).** A similitude `F·F† = [deg]` **underdetermines the signature** of its
  invariant form; positive-definiteness — which *is* RH — is independent of the duality and forced by no
  coherence structure (Tannakian, `C*`, o-minimal, …). RH-violating spectra are consistent objects in each.

We neither prove nor disprove RH. We establish that **if RH is provable, the proof cannot route through a
finite ground at `∞`** — it must live on the analytic/characteristic-0 side. (The analytic side is mapped too:
de Branges is the one scoped no-go; Weil/Connes are circular; Hilbert–Pólya, Berry–Keating, Beurling–Nyman are
open roads.)

**The paper:** [`research/preprint/geometric-obstruction-RH.tex`](research/preprint/) (build with `pdflatex`
×2; see the preprint README). Prose account: [`research/WRITEUP-geometric-obstruction.md`](research/WRITEUP-geometric-obstruction.md).

## The arc (read in this order)

| stage | document |
|---|---|
| the charter / methodology | [`STRATEGY.md`](STRATEGY.md), [`research/method.md`](research/method.md) |
| the audit (every reformulation → one wall) | [`research/positivity-program.md`](research/positivity-program.md) |
| the construction (polarized arithmetic Hodge category) | [`research/construction-program.md`](research/construction-program.md), `research/construction/M*.md` |
| the full arc, end to end | [`research/the-complete-account.md`](research/the-complete-account.md) |
| the `𝔽₁`-ground exhaustion | [`research/f1-construction.md`](research/f1-construction.md) |
| the foundational no-go | [`research/new-foundations.md`](research/new-foundations.md) |
| the analytic-side map | [`research/analytic-strategies-map.md`](research/analytic-strategies-map.md) |
| the preprint + arXiv packet | [`research/preprint/`](research/preprint/) |

## Reproducible witnesses

The constructive claims have numerical witnesses (`python-flint` / `numpy`); the paper's cited numbers
reproduce exactly:

```bash
python3 -m scripts.numerics.witness.theorem_B_similitude_signature   # Thm B: on-line (4,0,0) vs off-line (4,2,0) Krein, residual 1.8e-15
python3 scripts/numerics/witness/cstar_hermitian_witness.py          # the (6,0) vs (3,3) signature flip
python3 -c "from scripts.numerics.witness.jensen_real import exact_bw_slack; print(exact_bw_slack(20))"  # P1: BW slack (refutes (3/2)ln2)
python3 -m scripts.numerics.witness.falsify                          # the 3-axis falsifier (Euler-borne / sees-zeros / independent)
```

Setup: `pip install --user --break-system-packages python-flint numpy` (mpmath/scipy optional).

## Discipline

Atomic commits, each leaving the tree working — see [CONTRIBUTING.md](CONTRIBUTING.md). The forcing-structure
filter and the kill-tests (`STRATEGY.md` §5–6) are why the project converged on a *theorem about why the
geometric strategy fails* instead of another equivalent restatement of RH. Calibration is stated everywhere:
Theorem A is a theorem; Theorem B is a theorem plus a per-framework table; RH itself is open.
