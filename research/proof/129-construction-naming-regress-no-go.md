# 129 - The construction-naming regress (autopsy + standing no-go)

Status: terminal no-go + operating-discipline correction, 2026-06-14.
This doc replaces deleted docs 129-196 (the candidate-driven "assault"
era and the entire PFV2 thread). It is the full-value negative for that
era, recorded here per the fail-closed rule (negatives are full value;
refuted registrations are recorded, never silently relocated).

This is the one doc in `research/proof/` permitted to name the dead
PFV2 lineage, as the cautionary example. The discipline guard
(`scripts/automation/check_proof_targets.py`) bans that lineage from
every other proof doc.

## 1. What was deleted and why

Between 2026-06-11 and 2026-06-12 the program ran 68 documents
(129-196) and one state-machine "witness"
(`pfv2_gate_calibration.py`) on a single line of attack: build a
concrete two-place product-formula source object (PFV2) that carries
the Euler product structurally into a trace value. The target name grew
one qualifier per document:

```text
PFV2-FIRST -> PFV2-ADELIC-LOCAL -> PFV2-COMP-REFLECT -> PFV2-REL-FIRST
  -> PFV2-REL-UPROP -> PFV2-REL-REFLECT -> PFV2-REL-DESCENT
  -> PFV2-DESC-SELECT -> PFV2-DESC-RESIDUAL -> PFV2-RHO-SELECT
  -> PFV2-RHO-NONTRIVIAL -> PFV2-RHO-SURVIVES -> PFV2-TOR-SELECT
  -> PFV2-TOR-NATIVE -> PFV2-TOR-CARRIER -> PFV2-TOR-EULER-BAND
  -> PFV2-EULER-OP -> PFV2-EULER-TOWER-OP -> PFV2-TOWER-EFFECTIVE
  -> PFV2-TOWER-GLOBAL -> PFV2-GPF-LOCAL -> PFV2-GPF-SELECT
  -> PFV2-GPF-RESIDUAL -> PFV2-GPF-RMON-SELECT -> ... ->
  PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-SELECTIVE-TRACE-SENSITIVE
```

Outcome at deletion: **zero proved theorems, zero numerical witnesses,
66 of 68 docs terminating in `HOLD` / "no witness licensed".** Every
"Theorem" in the era is a target to be proved, never a result. The one
executable artifact (`pfv2_gate_calibration.py`) did not compute
anything about zeta, primes, or any carrier; it was the rejection chain
itself transcribed as a boolean state machine that classified toy
records by which adjective they lacked.

## 2. The mechanism of failure (the no-go)

The era is a textbook violation of the program's own degrees-of-freedom
gate (G-INT6, doc 21 sec 3): a derivation is admissible only if the
number of independently matched constraints exceeds the number of free
modeling choices; otherwise it is calibration, not derivation.

```text
Lemma 129.1 (naming regress).
Let a "shot" propose an object schema by listing properties it must
have, and let a "collapse" reject the schema by naming one more
property it lacks, appending that property to the target name. The
shot/collapse loop:

  (a) matches zero external constraints at every step (no witness, no
      identity, no comparison to the explicit formula is ever run);
  (b) adds one free naming choice at every step (the new qualifier);

so #constraints - #choices is monotonically DECREASING. By G-INT6 the
process is pure calibration with negative information content. It can
neither produce a witness (no object is ever constructed) nor a no-go
(no impossibility is ever proved: each "collapse" only rejects a
strawman the loop itself invented).
```

Two corollaries that make this a standing guard, not just a postmortem:

```text
Cor 129.2 (length is a stopping signal). The number of hyphenated
qualifiers in a live target name is an upper bound on the depth of the
naming regress, not a measure of progress. A target with >= 6 ALLCAPS
hyphen segments is presumptively inside the regress and must be
refactored into either (i) a runnable witness or (ii) a stated
impossibility theorem before any further document is written about it.

Cor 129.3 (shape is not object, restated). AB's split (doc, work/AB)
already says shape data is not object data. The regress is AB's split
iterated: an unbounded tower of shape constraints with no object under
it. No quantity of shape constraints converges to an object.
```

## 3. Why the *whole branch* (construction-chasing) was the error

The pivot was doc 129's predecessor (the deleted "candidate-driven
assault ledger"): the program switched from **proving no-go theorems
and narrowing the spec** to **chasing a concrete construction in the
hope of stumbling onto the missing object**. That switch removed the
only thing that had been generating information:

```text
- A no-go theorem matches a constraint: it proves a named class CANNOT
  supply a doc-45 clause. That is a permanent, citable reduction of the
  search space (docs 51-70 are the bank).
- A construction shot with no witness and no impossibility proof
  matches nothing. It only renames the wish.
```

The substantive arc (docs 00-70) made progress precisely because every
step was either (i) a certified numerical witness or (ii) a no-go
theorem with a named mechanism. The construction era abandoned both.

## 4. Standing correction (the restored discipline)

```text
1. Every cycle produces a certified witness OR a no-go theorem with a
   named mechanism. Nothing else is "progress".
2. No-go theorems are the primary product. They narrow the doc-45 spec
   monotonically and are banked in docs 51-70 + this file's successors.
3. A construction is admitted to the record only when it ships a
   runnable, exit-gated witness (STRATEGY.md sec 8). A schema with no
   witness is not a document.
4. Target names do not grow by qualifier accretion. If a target needs a
   new qualifier, that is a signal to STOP and either run a witness or
   prove the impossibility (Cor 129.2).
5. The two genuine open frontiers (STRATEGY.md sec 7) are the missing
   arithmetic object (Connes-Consani C x C / scaling site) and forcing
   Lambda <= 0 (de Bruijn-Newman). Construction work re-enters only
   against one of those, with a witness.
```

This correction is mirrored as a banned futility attractor in
STRATEGY.md sec 6 and enforced by the discipline guard.

## 5. What survived the deletion

Nothing from 129-196 is salvaged (no theorem, no witness existed).
The surviving no-go bank is docs 51-70 plus the genuine theorems kept
from the 71-128 band: **74, 79, 80, 82, 85, 93, 97, 100, 107, 108,
109, 111, 112, 118, 125**. The deleted 71-128 docs were ledgers,
routers, admission matrices, status boards, dispatch/expert packets,
and response rubrics - process artifacts that foreshadowed the regress.

If any future work wants the deleted content, it is recoverable in git
history at the checkpoint commit immediately preceding the reset.
