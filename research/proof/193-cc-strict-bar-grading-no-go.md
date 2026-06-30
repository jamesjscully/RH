# 193 - Strict bar grading does not construct the square carrier

Status: no-go + CC strict bar/character grading repair deletion, 2026-06-20.
Fifty-sixth cycle of the doc-137 construction arc. Doc 188 killed promoting
strict Gamma-set square divided-power/character data itself to End(S^2/Z).
Docs 189-192 then killed the CC-ceiling graded-tolerance aggregation repairs.
This document tests the sharper strict-square repair: grade the strict
character/divided-power invariants by the cyclic bar direction and use that
graded object as the diagonal/Bokstedt bridge.

Witness, lead-reran this cycle:
`prime_int_n1b_cc_strict_bar_grading_no_go` (SBG1-SBG10 ALL PASS) -- strict
cyclic-bar grading formability on character data, free monoid-ring character
algebra, per-prime probe artifact, nonclosed divided-power probes, zero
character-shaped H^1 in the verified window, missing degree-3 Bokstedt slot
in the tested character span, required evasion by joint-shape invariants or
derived replacement, missing square H^2/intersection/correspondence/Rosati
data, missing Laurent boundary/torsor/DD.4 data, and residual R1
carrier-guard checks.

Adjacent heavy witnesses from the V record:
`prime_cc_grading_invariant_kernel` (V-B1-V-B4 ALL PASS) and
`prime_cc_grading_bar_degree` (V-A1-V-A4 ALL PASS).

## 1. Purpose

Doc 188 left one honest repair:

```text
The strict square HZ ^ HZ has real square-only data.
Maybe the cyclic bar direction grades that data into the Bokstedt tower.
```

This repair is stronger than simply promoting the ungraded invariants. It
uses a real construction: the strict cyclic bar object has levels

```text
N^cy_q(HZ) = HZ ^ ... ^ HZ  (q+1 factors),
```

with faces given by multiplication of adjacent slots. The V record shows
that subset characters are compatible with this bar grading.

The repair still fails for the known strict character/divided-power algebra.
The universal invariant at level 1 is a free monoid-ring character algebra,
not the torsion Bokstedt tower. The mod-p divided-power probes are not closed
cochains under the strict bar differential. The character-shaped H^1 is zero
in the verified window, and the degree-3 Bokstedt Z/2 slot is absent in the
tested character span.

This document is local. It does not reject a future invariant of genuinely
new joint/cell shape, nor a derived replacement such as a cofibrant or
tolerant smash construction. It rejects the strict cyclic-bar grading of the
known character/divided-power algebra as construction-grade End(S^2/Z).

## 2. Lemma

```text
Lemma 193.1 (Strict character bar grading does not supply the square carrier).

In the strict Gamma-set square HZ ^ HZ, the universal column/row character
data descends to the coend and is multiplicative:

  chi_col(x * y) = chi_col(x) * chi_col(y)

with values in the free monoid ring on nonzero integers.

The cyclic bar direction is formable on this character data. The V witness
checks subset-character invariance under 571536 per-slot move instances and
checks the face dictionary on 180000 instances.

However, the resulting strict bar complex does not reproduce the Bokstedt
diagonal tower:

  strict character side: degree 0 = free monoid-ring excess,
                         H^1 = 0 in the verified character window,
                         degree 3 empty in the tested character span;

  Bokstedt target:       pi_0 THH(Z) = Z,
                         pi_1 THH(Z) = 0,
                         pi_3 THH(Z) = Z/2.

The divided-power probes that looked like the Bokstedt torsion are not
closed strict-bar cochains. In the V enumeration, the nonclosed counts are:

  Phi'_2: 14016,
  Phi_2 : 95280,
  Phi'_3: 111370,
  Phi_3 : 125017.

Thus the strict bar grading is formable but not construction-grade
End(S^2/Z). A surviving strict-square route must either construct new
joint/cell-shape invariants beyond the classified character shape, or replace
the strict smash by a derived/tolerant square construction, and in either
case must construct square H^2, intersection, correspondences, Laurent
boundary data, and Rosati.
```

Verdict label:

```text
N1B_CC_STRICT_BAR_GRADING__CHARACTER_COMPLEX_NOT_BOKSTEDT_DIAGONAL__NO_GO.
```

## 3. Proof

`prime_int_n1b_cc_strict_bar_grading_no_go` verifies the R1 carrier gate
from the V record.

SBG1 records the positive fact: strict cyclic-bar grading is formable on
subset-character data. This repairs the weaker objection that "degree" is
unformable in the strict world.

SBG2 records the first mismatch: the universal strict character algebra is a
free monoid-ring object. At degree 0 it is larger than the Bokstedt
`pi_0 THH(Z)=Z`; it remembers bilinear factorization excess before the
diagonal evaluation.

SBG3 records that the old per-prime resonance was a probe artifact: the
character algebra carries mod-m data for every m, not just one Z/p per prime.

SBG4 records the decisive divided-power failure. The probes
`Phi'_2`, `Phi_2`, `Phi'_3`, and `Phi_3` are not closed cochains for the
strict bar differential. Therefore they do not define classes in any strict
bar degree.

SBG5 records that the character-shaped H^1 kernel is the zero functional in
the verified window. This matches `pi_1 THH(Z)=0`, but it supplies no positive
square carrier data.

SBG6 records the bounded degree-3 failure: the tested subset-character span
does not produce the Bokstedt `Z/2` slot.

SBG7 records the exact evasion condition: any surviving strict-square bridge
must construct genuinely new joint/cell-shape invariants, or replace the
strict smash by a derived/tolerant construction. Neither is supplied here.

SBG8-SBG9 record the carrier failure: no square H^2, intersection form,
correspondence algebra, Frobenius graph, positive Rosati, Laurent axis,
boundary map, torsor splitter, or DD.4 weight>=1 datum is constructed.

SBG10 records that the base R1 obstructions and carrier guard remain.

## 4. Impact on R1

```text
R1 after docs 138-193:
  NEWLY CLOSED THIS CYCLE:
    - strict cyclic-bar grading of the known strict-square character/
      divided-power algebra as End(S^2/Z), the Bokstedt diagonal, square
      H^2/intersection/correspondence data, Frobenius graph, Laurent
      boundary data, torsor splitter, or positive Rosati (doc 193).

  STILL ADMISSIBLE:
    - a future joint/cell-shape invariant not classified by the character
      computation, or a derived/tolerant square construction that replaces
      the strict smash and constructs square H^2, intersection,
      correspondences, Laurent boundary data, and Rosati.

  STILL OPEN:
    - a genuinely different carrier whose first
      correspondence/multiplication constructs the square data internally
      and finishes DD.4 weights>=1.
```

R1 is still open. The strict bar grading is a measured failure, not the
target object. R2 remains locked.

## 5. Kill Conditions

```text
KILL-SBG.1 strict bar grading as Bokstedt bridge
  A proposal grades the known strict character/divided-power invariants by
  cyclic-bar degree and claims the Bokstedt diagonal. Kill it: the probes are
  not closed and the tested degree-3 character slot is empty.

KILL-SBG.2 per-prime divided-power resonance
  A proposal reads Phi_p or Phi'_p as the THH degree 2p-1 class. Kill it:
  the probes are not strict-bar cochains, and the per-prime pattern was a
  probe artifact.

KILL-SBG.3 monoid-ring character algebra as pi_0
  A proposal identifies the strict degree-0 character algebra with
  pi_0 THH(Z)=Z. Kill it: the strict side is the free monoid-ring excess
  before diagonal evaluation.

KILL-SBG.4 character grading without new invariant shape
  A proposal stays within column/row/subset-character shape. Kill it unless
  it supplies a new verified degree-3 class; the recorded span does not.

KILL-SBG.5 bar grading without square H2/intersection
  A proposal gives strict bar character data but no H^2, intersection form,
  or correspondence algebra. This is not the square carrier.

KILL-SBG.6 bar grading without Rosati/Laurent boundary
  A proposal gives strict bar character data but no Frobenius graph, positive
  Rosati, Laurent boundary map, torsor splitter, or DD.4 weight>=1 datum.
  This does not unblock R2.
```

## 6. Board

```text
doc-137 R1, cycle 56 = doc 193:
  N1B_CC_STRICT_BAR_GRADING__CHARACTER_COMPLEX_NOT_BOKSTEDT_DIAGONAL__NO_GO.

What got built: no End object. The value is a deletion: the strict cyclic-bar
grading exists on character data, but the character complex is not the
Bokstedt diagonal and constructs no square correspondence algebra.

What remains: construct a genuinely new joint/cell-shape invariant,
construct a derived/tolerant square functor, or return to the in-house
PFD/Xbar DD.4 weight>=1 obstruction.
```
