# HANDOFF - Prime-Toeplitz / R-INT program: lead-agent onboarding

Written 2026-06-11 by the outgoing lead (Claude, full license granted by
the user 2026-06-09). Read this first; then doc 45; then docs 46-48 for
the three live branches; then docs 38-44 as needed.

## 1. What this is

An unconditional-RH research program. The original arc (docs 00-16)
produced the TRACKING EQUIVALENCE (RH <=> uniform tau < 1; doc 13,
preprint research/preprint/tracking-equivalence-RH.tex) and a no-go
map. The current arc (docs 17-40) reconstructed the SUPPLY SIDE of the
completed zeta function from integer cardinalities (THH count ladders,
no zeta input), realized a compactified local object as a spectrum,
executed the Weil-positivity index attack to its exact boundary, and
reduced everything to ONE missing object with a complete specification.
Second preprint: research/preprint/count-ladders-index-boundary.tex
(25pp, draft, awaiting user submission decision).

## 2. The mathematical state (entry points)

THE SPEC, FINAL FORM (doc 45, consolidating doc 40 sec 3, docs 41-44,
and MM's liquid LS1-LS6): the missing object = a class- and
scale-coupled archimedean unit satisfying
  OC1 integer charge dichotomy   OC2 threading-as-structure
  OC3 the depth wall (unit-free) OC4 carrier (Euler product)
  BC13 index positivity + exhaustion of the doc-00 core
  BC-E3' nonempty odd slot with UNFORCED eigenvalues.
Everything else measured so far is SLOT DATA (the inserted test
function's own image - doc 40 sec 2's reconciliation).
Address: the liquid/condensed layer (XX's ladder: circle blind /
solenoid place-addressed-scale-free / liquid = where log p must live).
Type: liquid/metrized Euler-product carrier with candidate-native
unit, forced-positive index/Gram over the full Frobenius cone, and
P3-grade odd-slot second evaluation. Equivalence: BC1-12 + BC13 <=>
RH at stated grade (AC; the zero-shortcut is formally confirmed - no
discount exists). LS3 at adoption grade (the communicable conjecture
for the condensed community) is in research/work/XX-b1-liquid.md sec 4.

KEY THEOREMS BANKED (worker docs in research/work/): SS.1-SS.5 (the
ku-face inequality package), KK.L1 (effectivity, exact), HH.1 (Lambda =
-<d,d>), EE.1 (DD.4's Lin clause), S.1 (THR(F_2)^{tC_2}), the max-Gram
lemma (W), O's A0-A6 (scheme rigidity), BB.1 (FE kappa-blindness),
II's suppression mechanism, AB's split, AC's implication map.

THE QUEUE (doc 45 sec 8, now split into docs 46-48): no banked
finite-window probe remains. M-C, M-A, and M-B are accounted for.
Doc 46 gives the construction-facing blueprint: start with the B0
Tate-curve/liquid-RR calibration and Epstein replacement before any
claim of a live carrier. Doc 47 gives field-native external questions
for liquid geometry, trace theory, and arithmetic topology. Doc 48
gives theorem-shaped no-go targets for scale-blind traces, carrier-blind
Poisson/Epstein formalisms, inserted units, strict-face positivity, and
transport/self-supplied second evaluations. Background: cross-edge
certificates, C6', AHL verification debt, the (A'') spherical delta-ring
hunt.

## 3. How to navigate the record

research/proof/00-16: the tracking arc. 17-40: the R-INT arc (each doc
is a cycle synthesis; CORRECTIONS ARE IN PLACE - docs 18/20/23/24/25
carry dated correction sections; never read an early claim without its
corrections). research/proof/TODO.md: the risk ladder (historical +
live). research/work/[G..AC]-*.md: worker records (theorem statements
live HERE; the proof docs cite them). research/proof/refs/: ~40
archived primary sources (+ .txt extractions). scripts/numerics/
witness/: ~80 fail-closed witnesses, run via
  python3 -m scripts.numerics.witness.<name>
(exit 0 = the recorded claim reproduces; stack: python-flint, numpy;
tectonic at /home/jack/.cargo/bin/tectonic for preprints; NO pdflatex).

## 4. The operating system (how the program is run)

LEAD ROLE: design cycles, dispatch FRESH-CONTEXT background workers
(3-5 per cycle), verify every landing (rerun the witness yourself
before committing), apply errata across docs, write the cycle
synthesis, keep TODO + the memory file current, commit atomically with
the Co-Authored-By trailer (a futility-guard hook runs per commit).
Workers NEVER commit; they write to research/work/<ID>-*.md + witnesses
only. Worker briefs must include: required reading list, pre-registered
readings, fail-closed framing, output discipline (incremental writes,
<600-word final message), G-INT6 ledger, carrier guard.

STANDING DISCIPLINE (non-negotiable):
- Pre-registration before computation; refuted registrations are
  recorded, never relocated.
- Fail-closed: negatives are full-value; every kill names its mechanism.
- Witnesses: exit-gated, deterministic, rerun by the lead at landing.
- FREEZE PROTOCOL for any zero contact (II's template: loci computed
  and hashed BEFORE fork_lib.zeta_gammas is imported; comparison only).
- Fork protocol (doc 14): F1 value fork, F2 deformation kill, P1 extra
  information, P2 carrier non-existence, P3 second-evaluation
  independence (YY's criterion; state audit level number-vs-structure).
- Gates G-INT1-6 (doc 17 + 21: esp. G-INT6 DOF ledger - #constraints
  must exceed #choices or it is calibration) and G-CH1-4 (doc 38:
  lesson elevation each cycle; full-ledger scoring on arrival;
  second-evaluation arrival test; STANDING CRITIC every cycle).
- Elevations E1-E8 (docs 39-40): BC1-conformance necessary-not-
  sufficient, with the candidate's OWN unit; BC-E3' arrival question
  "who supplies the slot's eigenvalue?"; label registry (BC names are
  program-global).
- Carrier guards: every construction must die on DH (no carrier) and
  Epstein (dies at multiplicativity/effectivity/address - the exact
  death point must be exhibited, and a PD-layer PASS for Epstein is
  expected and is itself the lesson).
- Claims grading everywhere: Theorem / Certified / Census / Reading.

OPERATIONAL CAUTIONS (learned the hard way):
- TODO edits: ALWAYS assert-guarded python replaces (two silent no-ops
  happened; fixed 52c7477).
- Worker output limits: cap single Writes (~400 lines); bulk to /tmp.
- Workers dying on transport errors / session limits: check for
  partial artifacts (git status), relaunch with a pickup note;
  artifacts are the dead worker's, to be validated not trusted.
- SendMessage to agents is NOT available in this environment; workers
  that background their own runs resume on their own watchers - do not
  duplicate their jobs (check ps before taking over).
- The memory file (~/.claude/projects/-home-jack-code-RH/memory/
  prime-toeplitz-proof-track.md) is the cross-session state; update it
  every cycle.

## 5. What NOT to do

Do not insert the unit (zero-slack is a theorem: LL/NN - it must be
derived; any insertion is logged and demotes the result). Do not trust
shape data as object data (AB's split). Do not re-litigate the
provably-dead list (OO sec 3 + appendix A of the preprint). Do not
read zero data before freezing. Do not claim RH progress from FE-layer
results (BB.1 is the guard). The user sets strategy at decision
points; execute autonomously between them and report outcome-first.
