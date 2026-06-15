# 131 - Cycle 2 pre-registration: the Weil-operator radius - Euler-assembled or RH-circular?

Status: PRE-REGISTRATION, 2026-06-15. Second post-reset cycle. This is
the design + fail-closed reading fixed BEFORE computation, per the
operating system. It is not a result. Refuted registrations are recorded
here, never relocated.

Direction: engage the properness frontier with a witness (the
proven-necessary step from doc 130). Doc 130 proved a decision-grade
second evaluation requires a properness / Poincare-duality truncation
producing a non-congruence, carrier-fixed odd slot. This cycle tests
whether the one banked realization of that truncation - the weight-2
Neron-Severi Hodge-index duality on the self-product surface (Connes-
Consani / Arakelov layer) - escapes doc 130 or collapses to it.

## 1. What is already banked (the starting point, lead-reran PASS)

```text
ns_hodge_index_duality  weight-2 NS pairing P_NS = canonical evaluation
                        of the duality D (D o D = id), NOT a metric; its
                        inertia FLIPS (0,1,1)->(1,0,1) iff a zero leaves
                        |alpha| = sqrt q. => A non-congruence pairing
                        whose inertia SEES the zeros = doc 130's E4'/E5'
                        REALIZED at weight 2.

kahler_forcing          The forcing Kahler => P_inf>=0 => RH FACTORS:
                        (E, cup product) free/geometric but INDEFINITE
                        alone; (C_W, Weil operator) the (p,q) datum;
                        Hodge-Riemann implication formal. Residue: C_W
                        carries the PHASE ((-1)^w) for free but its
                        RADIUS |alpha|=sqrt q is, over F_q, literally RH.
                        Arakelov Green forms are Sylvester-locked
                        (= doc 130 case C), named verbatim.

supporting: arakelov_signature, oriented_hodge_pairing,
            polarization_relation, archimedean_hodge_polarization (PASS).
```

So doc 130's escape is structurally realized at weight 2, and the ONLY
open factor is the carrier-fixedness of the eigenvalue (E5'): the radius
`|alpha| = sqrt q`.

## 2. The precise question

```text
Q131. Can the Weil-operator radius |alpha| = sqrt q (the weight-1
descent scale that makes the weight-2 NS Hodge index positive = c = D =
RH) be supplied over Z from the Euler/Satake assembly of the prime
factors (M4/M4r; the ku-face prime-power comb, doc 42's best supply
carrier) as a ZERO-FREE GEOMETRIC datum - or does every construction of
the radius over Z reduce to importing the zeros (|alpha|=sqrt q IS the
critical-line statement)?
```

This is doc 130's E5' at weight 2, and the last irreducible residue of
the kahler_forcing keystone. The phase factor of `C_W` is banked free;
the radius is the whole problem.

## 3. The gate

```text
- doc 130 E4'/E5': the odd slot is non-congruence (met: P_NS flips) and
  its eigenvalue is carrier-fixed BEFORE the acting map (the open test:
  the radius).
- doc 65 E1-E5: the second-evaluation normal form.
- doc 59 ZERO-IMPORT CIRCULARITY: the decisive guard. Any radius
  supplier must be audited for hidden zero-import. Supplying |alpha|=
  sqrt q from data that already encodes the critical line is circular.
- BB.1 FE-blindness kill-test: the supplier must do MORE than reproduce
  the functional equation.
- G-INT6 DOF ledger: the radius assembly must match more independent
  constraints than the free choices (scale, normalization, scheme) it
  introduces, or it is calibration.
- FREEZE PROTOCOL: zeros are computed and hashed BEFORE any import;
  used only for comparison, never to construct the radius.
- Carrier guard (doc 64): the radius supplier must die for Epstein/DH at
  effectivity, or it is carrier-blind.
```

## 4. The probes (mostly banked; one decisive extension)

```text
P131.1 (cheap, structural - run first). A doc-59 circularity audit of
  the radius. Enumerate every banked candidate radius-supplier - Euler/
  Satake prime product (M4), Arakelov/Green-form height, vdGS theta
  count, the ku-face comb - and decide for each whether it supplies
  |alpha|=sqrt q from zero-free geometric data or reduces to importing
  the critical-line bound. Fail-closed: any supplier that needs the
  zeros is REJECTED as doc 130 case S (self-supply) / doc 59 circular.

P131.2 (extension witness). Extend ns_hodge_index_duality to run the
  doc-130 trichotomy explicitly: confirm P_NS is non-congruence (not
  T^* F T of the FE form), then deform the radius INDEPENDENTLY of the
  planted zero ordinate and test whether the inertia flip survives a
  radius supplied by the Euler assembly rather than by |alpha|=sqrt q.
  Decisive: does the flip track an Euler-assembled radius (escape) or
  only the imported one (collapse)?

P131.3 (forcing check). Re-run kahler_forcing's factorization over the
  Z/self-product carrier (not F_q) and locate whether the radius residue
  is UNSOLVED (open, attackable) or provably CIRCULAR (every supplier
  imports the zeros).
```

## 5. Fail-closed readings (fixed now)

```text
R-ESCAPE  A zero-free Euler/geometric assembly of |alpha|=sqrt q exists
  and forces P_NS positivity without RH input. => First RH-grade forcing
  structure. ESCALATE: full-ledger scoring, P3 arrival test, freeze
  audit, independent re-derivation. (Low prior - this is RH-complete -
  but it is the only known route to a forcing structure.)

R-COLLAPSE  Every construction of the radius over Z provably imports the
  critical-line bound (doc 59 circular / doc 130 case S). => doc 130
  EXTENDS to the weight-2 proper object too: even Poincare-Serre /
  Hodge-Riemann duality cannot supply its own radius. Write the
  radius-circularity no-go (doc 132). The wall relocates to the EULER
  RADIUS ASSEMBLY itself = M4 = the forcing/de Bruijn-Newman frontier or
  genuinely new structure. This is the expected, full-value outcome.

R-PARTIAL  The computable shadow cannot decide circularity (the radius
  assembly is open, not provably circular). => Name the exact missing
  lemma (the M4 Euler descent of the radius) and either attack it or
  send the focused external question to Arakelov/Connes-Consani experts.
```

## 6. Honest prior (do not fool ourselves)

kahler_forcing already shows the forcing is a TAUTOLOGY over F_q (radius
= |alpha|=sqrt q = RH put in by hand as "Frobenius is a weight-1 Weil
number"). The program's banked verdicts point the same way: scale was
expelled from torsion (doc 31 FF.1); the coupled archimedean unit is
demanded six times and cannot be inserted (zero-slack theorem, doc 37);
M4 (the Euler radius descent) is the unsolved residue. So R-COLLAPSE is
the likely outcome, and the radius-circularity no-go (doc 132) is the
realistic deliverable. The point of the cycle is to decide CIRCULAR vs
merely UNSOLVED - the difference between "relocate the wall with a
theorem" and "a concrete open lemma to attack."

The cycle does NOT claim a path to proving RH. It claims a fail-closed
decision on whether the last banked forcing-structure candidate is
circular at its radius.

## 7. Guards and discipline

```text
- No zero import to construct the radius (doc 59 + freeze protocol).
- No unit insertion (zero-slack theorem, doc 37): the radius must be
  DERIVED from the Euler assembly, never hand-set.
- Epstein/DH must die at the radius supplier's effectivity (doc 64).
- G-INT6: ledger the constraints matched vs free choices for any
  proposed assembly.
- Every witness exit-gated, certified (ball arithmetic), lead-reran at
  landing.
- This is a no-go-or-witness cycle (doc 129): it ships the
  radius-circularity no-go OR an escape witness, nothing else.
```

## 8. Worker plan (on execution greenlight)

```text
W1  P131.1 circularity audit of all banked radius-suppliers (doc 59).
W2  P131.2 the ns_hodge_index_duality radius-deformation extension.
W3  P131.3 kahler_forcing factorization over Z + the M4 residue typing.
CRITIC  hunt hidden zero-import / unit-insertion across W1-W3; the
        freeze and G-INT6 audits.
```

Fresh-context workers, brief per the operating system; lead verifies
every landing before any doc 132 / escalation.

## 9. What this cycle would change

```text
ESCAPE   -> escalate to the first forcing-structure object (rare).
COLLAPSE -> doc 132 radius-circularity no-go; the doc-45 spec's clause E
            is then closed even against the proper object, and the only
            surviving frontier is the Euler radius assembly / forcing
            Lambda <= 0. The no-go map gains its sharpest entry.
PARTIAL  -> a single named open lemma (M4 Euler radius descent) and a
            focused external packet.
```
