# Contributing

## Atomic commit policy

This repository uses **atomic commits**. Each commit is one logical, self-contained
change that leaves the repo in a working state.

**Rules**

1. **One concern per commit.** A commit does exactly one thing: a single feature, fix,
   refactor, doc change, or experiment. Don't mix unrelated changes. Don't split one
   logical change across several commits.
2. **Each commit builds green.** At every commit, `lake build` succeeds and
   `scripts/automation/check-stubs.sh` passes (no `:= True` spine stubs, no
   `sorry`/`axiom`). Never commit a known-broken state "to fix later".
3. **Proof discipline carries over.** A commit that adds a "theorem" proving `True`, or
   a numeric claim with no path to a certified inequality, is not a self-contained unit
   of progress — see `research-program.md` §12.
4. **Message format.** Imperative subject ≤ ~72 chars, optionally area-prefixed
   (`lean:`, `numerics:`, `research:`, `automation:`); a body explaining *why* when it
   isn't obvious. Example:

   ```
   lean: de-tautologize the contradiction theorem

   The old theorem assumed an `incompatible` hypothesis equal to its
   conclusion. Replace with `forward_reverse_incompatible`, which derives
   False from order facts on a rational distance sequence.
   ```

5. **AI-assisted commits** include a `Co-Authored-By:` trailer for the assisting model.

**Why atomic.** Each commit is independently reviewable, revertible, and bisectable —
which matters here because the program advances by small, falsifiable steps and
regularly converts failures into obstruction results. A clean history *is* the loss
ledger.

## Enforcement (tracked git hooks)

Hooks live in `.githooks/` (tracked, shared). Enable them once per clone:

```bash
git config core.hooksPath .githooks
```

- **pre-commit** — runs `scripts/automation/check-stubs.sh` (fast, no deps): blocks
  `:= True` spine stubs, `sorry`, and `axiom`.
- **pre-push** — runs the stub guard and `lake build` (requires `lake exe cache get`
  first, since the Lean library depends on Mathlib): blocks pushing code that doesn't
  build.

Bypass in a genuine emergency with `git commit --no-verify` / `git push --no-verify`,
but the next commit must restore a green state.

## Prerequisites

- **Lean**: `lake exe cache get` then `lake build` (Mathlib dependency).
- **Numerics**: `pip install --user --break-system-packages python-flint mpmath scipy`
  (numpy preinstalled); run `python3 -m scripts.numerics.witness.harness`.
