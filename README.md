# RH Witness-Constraint Program

This repository supports a Lean 4-based research program aimed at an unconditional proof of the Riemann hypothesis.

The project has two synchronized tracks:

1. A Lean 4 formalization track for definitions, theorem stubs, toy models, and eventually analytic proof components.
2. A research-log track for theorem agendas, informal mathematics, numerical experiments, failures, and bibliography notes.
3. A local automation track using WhippleScript for durable agent orchestration and Loft for event-sourced issue/work state.

The corrected strategy is described in [research-program.md](research-program.md); the live work breakdown, status, and discipline are in [research/tracker.md](research/tracker.md), which is the source of truth. The raw source conversation is preserved in [chat.md](chat.md).

## Build

The Lean library now depends on Mathlib (for the analytic toy theorems). Fetch the
prebuilt Mathlib cache first, then build:

```bash
lake exe cache get   # download Mathlib oleans (first time / after a Mathlib bump)
lake build
```

Numerics use a Python stack (FLINT/Arb): `pip install --user --break-system-packages
python-flint mpmath scipy` (numpy preinstalled). Run the refutation harness with
`python3 -m scripts.numerics.witness.harness`.

## Automation Dependencies

The automation layer depends on two local sibling repositories:

```text
../whipplescript
../loft
```

Check those dependencies and the project automation surface with:

```bash
scripts/tools/check-deps.sh
scripts/automation/check.sh
```

See [automation/README.md](automation/README.md) for details.

## Contributing

This repo uses an **atomic-commit policy** with tracked git hooks — see
[CONTRIBUTING.md](CONTRIBUTING.md). Enable the hooks once: `git config core.hooksPath
.githooks`.

## Layout

```text
RH/
  Basic/          foundational names and placeholders
  Witness/        abstract witness-constraint systems
  HardyModule/    Hardy/module proof-spine targets
  Strategy/       Theorem A/B/C and contradiction mechanism
  Experiments/    Lean hooks for toy and finite experiments

research/
  log/            daily research logs
  agenda.md       ordered work queue
  definitions.md  informal definitions and Lean status
  theorem-stubs.md theorem tracker
  bibliography.md reference notes
  failure-modes.md known failure modes
  questions.md    open questions

scripts/
  gram_matrix/    numerical finite Gram experiments
  numerics/       general numerical exploration
  references/     reference-processing helpers

notebooks/
  finite_gram_experiments/
  reverse_packet_experiments/

automation/
  tools.toml      local WhippleScript/Loft dependency manifest

workflows/
  research-program.whip
```

## Immediate Goal

The corrected architecture (see [research/tracker.md](research/tracker.md)) recognizes
that **reverse visibility is the easy, classical direction** (an `N`-uniform evaluation
bound), while the **forward/arithmetic convergence theorem is the bottleneck and is RH**
— so it must be powered by the **Euler product**, validated against the
**Davenport–Heilbronn barrier** (any argument blind to the Euler product would "prove"
RH for DH, which is false).

The first two milestones are therefore:

1. **Refutation harness** — a test-object battery (ζ, Davenport–Heilbronn, a
   planted-zero "fake ζ", a truncated Euler product) plus four cheap checks that keep
   the forward search from proving false or RH-neutral statements.
2. **Power test** — demonstrate the machinery can unconditionally reprove a *known*
   result (the classical zero-free region, a zero-density estimate, or
   `M_N → 1/ζ` for `Re s > 1`) before aiming at RH.
