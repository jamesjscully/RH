# Contributing

## Before you write anything

Check the work against [STRATEGY.md](STRATEGY.md) — especially §5 (kill-tests) and §6
(the do-not list). The project's failure mode is drifting back into RH-neutral
reformulations. A new direction is admissible only if it could carry a **forcing
structure** (reverse force), not just another equivalence to RH.

## Atomic commit policy

Each commit is one logical, self-contained change that leaves the repo working.

1. **One concern per commit.** A single experiment, fix, doc change, or refactor.
2. **Each commit is consistent.** The kept python modules import and run; no half-deleted
   state. Run the relevant module (`python3 -m scripts.numerics.witness.<name>`) before
   committing.
3. **No futility.** A commit that adds an RH-equivalent reformulation with no path to
   reverse force, or that resurrects the deleted NB-Beurling / forward-convergence
   apparatus, is not progress — see STRATEGY.md §2/§6.
4. **Message format.** Imperative subject ≤ ~72 chars, area-prefixed
   (`numerics:`, `research:`, `docs:`); a body explaining *why* when it isn't obvious.
5. **AI-assisted commits** include a `Co-Authored-By:` trailer for the assisting model.

A clean history *is* the loss ledger — each commit independently reviewable and revertible.

## Enforcement (tracked git hooks)

Enable once per clone: `git config core.hooksPath .githooks`

- **pre-commit** — `scripts/automation/guard.sh`: fails if any deleted futility file
  (NB-BD docs, `hardy.py`/`forward_bound.py`/`power_test.py`, the Lean witness tree)
  reappears. Fast, no dependencies.
- **pre-push** — the guard plus an import smoke-test of the kept modules.

Bypass in a genuine emergency with `--no-verify`, then restore a clean state.

## Prerequisites

```bash
pip install --user --break-system-packages python-flint numpy   # mpmath/scipy optional
```

Run an experiment:
```bash
python3 -m scripts.numerics.witness.harness        # kill-test gates
python3 -m scripts.numerics.witness.descent_test   # nerve criterion
python3 -m scripts.numerics.witness.jensen_nerve   # Jensen cover nerve
```
