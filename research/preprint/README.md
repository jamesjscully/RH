# Preprint — build instructions

**`geometric-obstruction-RH.tex`** — *Two no-go theorems for the geometric strategy on the Riemann Hypothesis.*

**`count-ladders-index-boundary.tex`** — *Count ladders, duality renormalization, and the
exact boundary of the index attack on the Riemann Hypothesis* (DRAFT, 2026-06-11): the
homotopy-theory/index-attack arc. Assembled from `../proof/` documents 17–37 and the
`../work/` worker records cited at each statement (SS, KK, HH, EE, S, O, W, DD, BB, LL, QQ,
TT, UU, II, NN, and others); every labeled claim carries a grading tag
(Theorem / Certified / Census / Reading), the program's corrections are reproduced *as*
corrections, and the witness scripts backing each certified claim are named inline and
indexed in Appendix B. 25 pp. Builds clean with `tectonic count-ladders-index-boundary.tex`
(zero warnings); also builds with the two-pass pdflatex recipe below (inline
`thebibliography`, no BibTeX needed).

**`tracking-equivalence-RH.tex`** — *RH as a tracking inequality* (DRAFT, 2026-06-09): the
exact finite-dimensional reduction along the prime filtration. Front matter, the five main
theorem statements, the no-go map and the bibliography are complete; the proof-body sections
were transcribed from `../proof/` documents 00, 00a, 09, 11, 12, 13 (each
pointer in a `%` comment at the section head). Numerical gates:
`../../scripts/numerics/witness/certify_chain.py`. Builds with `tectonic` as below.

## Build

```sh
pdflatex -interaction=nonstopmode geometric-obstruction-RH.tex
pdflatex -interaction=nonstopmode geometric-obstruction-RH.tex   # 2nd pass: refs + bibliography
```

(Or `latexmk -pdf geometric-obstruction-RH.tex`.) The bibliography is inline
(`thebibliography`), so no BibTeX/biber pass is needed. Output: `geometric-obstruction-RH.pdf`.

## Requirements

Standard `amsart` + these packages (all in `texlive-latex-recommended` / a full TeX Live):
`amsmath`, `amssymb`, `amsthm`, `geometry`, `booktabs`, `hyperref`.

## Source

Built from `../WRITEUP-geometric-obstruction.md` (the prose account). The load-bearing results are
self-contained in the `.tex`:
- **Theorem A** (Foundational No-Go) — a theorem (Ostrowski + definition of characteristic + the
  finite-semifield classification);
- **Theorem B** (Geometric No-Go) — a structural theorem (a similitude underdetermines the signature),
  proved in full, with the per-framework exhaustion in Table 1.

Numerical witnesses for the constructive claims live in `../../scripts/numerics/witness/`
(`theorem_B_similitude_signature.py`, etc.). Calibration is stated in-text: Theorem A is a theorem,
Theorem B is a theorem plus a case-by-case table, and RH is neither proved nor disproved.
