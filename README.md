# RH — forcing-structure search

A research project on the Riemann hypothesis. After a long detour through a
Nyman–Beurling / witness-constraint reformulation (now deleted as futility — see the
autopsy in [STRATEGY.md](STRATEGY.md) §2), the project is organized around one principle:

> A route to RH is viable only if it carries a **forcing structure** — a property provable
> on its own terms that *forces* the zeros onto the line — not an equivalence that merely
> restates RH. Everything is filtered by **kill-tests** (Davenport–Heilbronn, Epstein, Weil
> positivity) and a **descent nerve criterion**.

**[STRATEGY.md](STRATEGY.md) is the single source of truth.** Read it first.

## What's here

```
STRATEGY.md                  the charter (forcing structures, kill-tests, do-not list)
scripts/numerics/witness/    the gates + experiments (python-flint / numpy)
  explicit_formula.py        DH discrimination (prime side != Lambda for DH)
  li_positivity.py           Weil/Li positivity (>=0 for zeta, detects DH off-line zeros)
  second_wall.py             Epstein wall (Euler product yet RH-false)
  descent_test.py            nerve-cohomology criterion (cech_h1)
  jensen_nerve.py            Jensen cert/tail/bridge cover — descent teeth?
  harness.py                 runs the kill-test gates on a candidate
  objects.py                 test-object battery (zeta, DH, Epstein, ...)
research/log/                dated record of what was tried and why it was abandoned
```

## Run

```bash
pip install --user --break-system-packages python-flint numpy   # mpmath/scipy optional
python3 -m scripts.numerics.witness.harness          # kill-test gates
python3 -m scripts.numerics.witness.descent_test     # nerve criterion
python3 -m scripts.numerics.witness.jensen_nerve     # Jensen cover nerve
```

## Discipline

Atomic commits, each leaving the tree working — see [CONTRIBUTING.md](CONTRIBUTING.md).
Before proposing work, check it against [STRATEGY.md](STRATEGY.md) §5 (kill-tests) and §6
(do-not list). The point of the gates is to **kill** dispersing candidates, not to defend one.
