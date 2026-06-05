# RH Witness-Constraint Program

This repository supports a Lean 4-based research program aimed at an unconditional proof of the Riemann hypothesis.

The project has two synchronized tracks:

1. A Lean 4 formalization track for definitions, theorem stubs, toy models, and eventually analytic proof components.
2. A research-log track for theorem agendas, informal mathematics, numerical experiments, failures, and bibliography notes.
3. A local automation track using WhippleScript for durable agent orchestration and Loft for event-sourced issue/work state.

The current proof spine is described in [research-program.md](research-program.md). The raw source conversation is preserved in [chat.md](chat.md).

## Build

```bash
lake build
```

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

The first formal milestone is an abstract Lean contradiction theorem:

> forward convergence + same-coordinate reverse obstruction + positive reverse gap rules out a hypothetical off-critical zero.

The first analytic milestone is to derive the finite half-plane Gram matrix and raw evaluation-kernel lower bound for the Hardy-module witness spaces.
