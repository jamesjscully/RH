# Automation Dependencies

This project uses two local tool repositories to manage a fully automated research program:

- WhippleScript: durable multi-agent workflow orchestration.
- Loft: event-sourced local issue/work tracking with leases and evidence.

The local paths are recorded in [tools.toml](tools.toml):

```text
../whipplescript
../loft
```

## Dependency Check

```bash
scripts/tools/check-deps.sh
```

This verifies that both local repos exist, their Cargo manifests load, and their CLIs can be run from source or from installed binaries.

## Optional Local Install

```bash
scripts/tools/install-local-tools.sh
```

This installs `whip` and `loft` from the local repos using Cargo. The project scripts also work without installation by running the CLIs from source.

## Project Check

```bash
scripts/automation/check.sh
```

This runs:

1. `lake build RH`
2. WhippleScript workflow validation for [workflows/research-program.whip](../workflows/research-program.whip)
3. `loft doctor`

## Runtime State

WhippleScript runtime state is stored under `.whipplescript/` and ignored by Git.

Loft canonical state lives under `.loft/config.toml` and `.loft/tx/**/*.json`. Loft SQLite projections and local runtime files are ignored by Git.
