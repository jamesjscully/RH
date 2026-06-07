# Preprint — build instructions

**`geometric-obstruction-RH.tex`** — *Two no-go theorems for the geometric strategy on the Riemann Hypothesis.*

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
