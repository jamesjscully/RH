# 28 - The product-formula determinant structure (PFD): spec for the compactified archimedean object

Status: 2026-06-10, spec (lead-authored after the doc 27 cycle; user-
approved direction). This is a DEMAND SHEET with a defining structure,
not a construction: the program's repeated lesson is that imposing a
known formalism (TP, branch conventions, tolerance) yields the right
ladders in the wrong layer. The two structures that have never failed
a kill-test are the count identities and the product formula; the
object is therefore POSED as the thing they define.

## 1. The structure

A PFD object D consists of:

```text
(local data)   for each prime p: the full determinant ladder
               (V_p, Theta_p) of the p-local Tate/TPR square (the
               objects of docs 20/24/25: spacing 2 pi i/log p, the
               2-primary sector carrying t with t^2 = vertical
               periodicity);
(degenerate    (V_oo, Theta_oo): the reflection/fixed-point sector
 sector)       (half-ladder, spacing 2, start 0; at 2 the computed
               Gamma_C degeneration and the Barnes Gamma_2 rank-2
               tower of doc 25);
(gluing)       THE PRODUCT FORMULA AS STRUCTURE: for each eigenvalue
               family lambda of the underlying count data, the trace/
               determinant layer is equipped with an identification
               whose shadow on absolute values is prod_v |lambda|_v = 1
               - i.e. the p-adic MIN faces and the archimedean MAX
               face of the W-doc pairing are declared two readings of
               ONE object (W-doc W6d is the local model);
(duality =     POISSON AS DEFINING PROPERTY: the finite-truncation
 compactness)  residue pairings (U-doc: perfect, weight flip
               m <-> N-m, dying in completion) EXTEND to D - the
               compactification is whatever makes the finite-level
               negation-duality global. Conjecture U.2 (the disk glued
               to its divided-power dual along the Lin line) is the
               p = 2 instance.
```

Existence/consistency of D is the mathematics. The analogy to how
cyclotomic spectra were defined (Frobenius as structure, existence as
theorem) is deliberate; Hesselholt's iota: W -> C (the "archimedean
move", W-doc) becomes part of the gluing datum rather than an
insertion.

## 2. Kill-test battery (all pre-registered; any failure kills or
## reshapes the spec - the tests must come OUT of D, never in)

```text
K1 (scale): the 1/(2 pi) scale - equivalently the EF's -(1/2) log pi
    supply term via anomalous dimension (1-s)/2 - must EMERGE from the
    gluing (doc 20 C2 / gate infty-2). Inserted scale = failure.
K2 (negation): the duality of D must restore s -> -s exactly where U
    proved the z-adic completion breaks it; by O's rigidity theorem
    this FORCES KMS-1/2 - realization input 4 regains a carrier, and
    the scheme question closes. The extension of U's finite residue
    pairings is the testable core.
K3 (rank 2): the Barnes Gamma_2 / s(s-1) sector (doc 25, gate infty-4)
    must appear as the rank part of the degenerate sector.
K4 (Q's pole): any integer-dimension layer of D must not be exact on
    a b-adically geometric set (else Sum_reg does not exist - Q-doc).
    D's integer layer must break the strict tolerance <-> derived
    dichotomy in exactly the recorded way.
K5 (carrier): no ring => no local data => no D. DH/Epstein die at the
    object. The O_K family must yield xi_K's data (doc 22's bench).
K6 (G-INT6): the only gluing inputs are the product formula and the
    residue pairings - both theorem-sourced, ZERO free choices. Any
    additional choice demotes the construction to calibration.
```

## 3. Execution plan

```text
Step 1 (worker Z, dispatched): the U.2 instance at p = 2 - construct
    the glued object from S's computed Tate square + U's witnessed
    finite-level pairings; run K2 (does the gluing extend the residue
    pairing past the completion?) and K1 (does the scale emerge?).
    Everything needed is banked and witnessed.
Step 2: odd-p instances (the fold is theorem-grade there; the gluing
    should be EASIER - no Euler tower); then the global assembly
    demand (all places + product formula) posed precisely.
Step 3: the zeros test - the global sections / H^1 of D against the
    EF's spectral side. NOT part of this spec's burden; recorded so
    the target stays visible. The standing guard (doc 21 sec 4): a D
    that reproduces only the functional equation is PD-grade and
    vacuous for RH - the index/Riemann-Roch layer (K3 + the W-doc
    Lorentzian face) is what must do work.
```

## 4. Failure modes, named in advance

- F-a (circularity): the gluing secretly encodes zeta's analytic
  continuation. Guard: K6 + the fork protocol (doc 14) on every
  emergent identity.
- F-b (vacuity): D exists but its duality is carrier-blind (every
  lattice passes - the BK/Ngo failure mode, doc 21 sec 4). Guard: K5
  with Epstein run explicitly.
- F-c (the wrong layer again): D's ladders are right but the scheme is
  still applied not forced. Guard: K2 is the forcing test; doc 25's G5
  weakening is the precedent.
