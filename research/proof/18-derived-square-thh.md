# 18 - C4' executed: the derived square has sign, and the sign is the archimedean constant (R-INT, second pass)

Status: C4' (doc 17 section 6) executed 2026-06-09. Witness:
prime_int_derived_square.py (ALL PASS, exit-code gated). Inputs taken on
citation: Bokstedt's THH(Z) and THH(F_p) (refs in section 7). Result: the
Euler pairing on the derived square Z (x)^L_S Z is sign-bearing on the
diagonal, the curve vanishing breaks, and the value is zeta'(0) - the
archimedean constant produced from pure torsion counts. The integrality
gate fails only through the infinite tower; the wall relocates to
PROPERNESS over the sphere.

## 1. Setup

The pairing is the Tor-form (Serre intersection form), the same one that
vanishes identically on the curve (doc 17 section 6):

    <M, N>_R = sum_i (-1)^i log |pi_i (M ^_R N)|,    R = HZ ^ HZ.

The marquee class is the diagonal Delta = HZ (R-module via
multiplication). By definition of topological Hochschild homology,

    Delta ^_R Delta = HZ ^_{HZ^HZ} HZ = THH(Z).

So the derived self-intersection of the diagonal in the arithmetic square
IS THH(Z) - no construction needed; the object the program was trying to
build by hand has a standard name.

## 2. Input (citation-grade): Bokstedt's theorem

    THH(Z) ~ HZ v V_{k>=1} Sigma^{2k-1} HZ/k :
    pi_0 = Z,  pi_{2k-1} = Z/k (k >= 1),  even positive degrees vanish.

    THH(F_p) = F_p[sigma], |sigma| = 2:  pi_{2i} = F_p for all i >= 0.

All positive-degree homotopy of THH(Z) is FINITE - integer cardinalities,
exactly what gate G-INT demanded. pi_0 = Z is the excess part (Delta cap
Delta = Delta, a curve, not points); by HKR the higher Tor of the diagonal
on C x C is Omega^i_C, and the intersection NUMBER Delta^2 = 2 - 2g is
carried by the cotangent data. Here the positive-degree torsion of THH(Z)
is precisely the cotangent data of Z over S.

## 3. The computation

All torsion sits in ODD degrees, so every finite group contributes with a
MINUS sign:

    <Delta, Delta>_tors = - sum_{k>=1} log k
                        = zeta'(0)              (zeta-regularization)
                        = -(1/2) log 2pi
                        = -0.918938533205...    NEGATIVE.

Equivalently: the regularized order of THH(Z)_torsion is
prod_reg k = sqrt(2pi), and e^{<Delta,Delta>} = (2pi)^{-1/2}.

Witness checks (fail-closed): T1 the curve control is exactly 0 on a
(p,a,b) grid; T2 the regularization is exhibited numerically (Stirling
constant to 3.7e-14, not cited); T3 independent zeta'(0) by flint central
difference (1.1e-16); T4 the Abel constant sum_reg 1 = -1/2 for the local
case. Local control:

    <Delta, Delta>_{F_p-square} = log p * (1 - 1/2) = (1/2) log p > 0.

## 4. Readings (pre-registered, now taken)

(i) SIGN EXISTS. This is the first sign-bearing, torsion-sourced pairing
on an arithmetic square in the program - the thing doc 16/17 proved cannot
exist on the curve (|Ext^1| = |Hom|) and the Arakelov audit found missing
at the archimedean place. The non-flatness of Z (x) Z over the SPHERE is
where the sign lives.

(ii) THE VALUE IS THE ARCHIMEDEAN CONSTANT. zeta'(0) = -(1/2) log 2pi is
the constant of the completed zeta function (e^{zeta'(0)} = regularized
det of the archimedean factor).

[SCALE NOTE 2026-06-10, from the fleet audit (J-doc + doc 21)]: this
value is regularization-SCHEME-independent (a positive-real half-ladder
has no conjugate-pairing ambiguity; both arg conventions agree) but
SCALE-dependent: rescaling the eigenvalues by c shifts log det by
zeta_H(0, s+1) log c = -(s + 1/2) log c, i.e. the constant is the
UNIT-SCALE value and shifts by -(1/2) log c. The scale-invariant content
is the digamma log-derivative shape plus the anomalous dimension
-(s + 1/2). The claim "the torsion produces zeta'(0)" therefore carries
one unit choice; what it produces invariantly is the Gamma-factor SHAPE. The program's recurring finding was "the
archimedean place is identical for zeta and its fakes, and that is where
positivity dies." Here the archimedean constant is PRODUCED - from
integer torsion cardinalities - rather than inserted. The carrier is the
ring structure: DH and Epstein have no ring, hence no THH, hence no
square at all (P2 carrier filter passes; necessary, not sufficient).

(iii) GENUS > 1. On C x C the diagonal computes Delta^2 = 2 - 2g =
-deg Omega^1_C. Reading 2 - 2g_Z = zeta'(0) gives

    g_Z = 1 + (1/4) log 2pi = 1.459469...  > 1:

"Spec Z is a hyperbolic curve over S." The fact that Castelnuovo/Weil
positivity arguments NEED g >= 1 (the g = 0 case has no Jacobian to
bound) makes the sign of this number load-bearing, not decorative.

## 5. The honest scorecard (gates and forks)

- G-INT5 (no-scale): PASS. The second dimension is homotopy (the sphere's
  higher torsion), not a residue field at infinity. Not covered by the F1
  survey's scale-criterion kill.
- Carrier filter (P2/S4' necessary condition): PASS. No ring => no THH.
- G-INT1 (integer-valued): DEGREE-WISE PASS, TOTAL FAIL. Every pi_i is a
  finite group; the non-integer (transcendental, even) enters ONLY through
  the infinite tower's regularization. FF has finitely many Ext groups
  because the surface is PROPER (coherent duality truncates). The derived
  square is "affine" over S; nothing truncates the tower.
- F1 value fork: NOT YET TOUCHING ZEROS. The object sees the archimedean
  Euler factor, not the zeros. On the FF side the zeros enter through the
  GLOBAL Euler characteristic (H^0, H^1 of line bundles on the proper
  surface, i.e. Riemann-Roch), not through the local intersection form.

CONSEQUENCE - the wall relocates with new precision: not "no integer
pairing exists" (one does, degree by degree, with sign) but

    no PROPERNESS: the program now needs the compactified derived square
    and a finiteness/duality theorem over S that makes the Euler pairing
    finite-rank per class - the S-arithmetic Riemann-Roch. The zeros sit
    behind exactly that wall.

This is the third independent arrival at the archimedean place, but the
first with a constructive residue: the place's CONSTANT came out of the
torsion, unprompted.

## 6. Open continuations (ranked)

C5 (properness): what is the Tate/TP-style compactification of the
square? Hesselholt's theorem (section 7) is the proof of concept: for
smooth PROPER F_q-schemes, TP's regularized determinants compute the
Hasse-Weil zeta - properness is the hypothesis there too. Question: is
there a TP-analogue over the square HZ^HZ whose pairing is finite-rank,
and does its diagonal class reproduce the full Gamma_R factor (digamma
term of the explicit formula, not just the constant)?

C6 (Frobenius family): the FF proof needs the graphs of Frobenius powers
as a second family of classes; Spec Z over S has none (ring maps HZ -> HZ
are trivial). The chromatic world DOES have them: Adams operations psi^k
are ring maps, the only known candidate for the missing two-parameter
family of correspondences. POSING CONSTRAINT (audited 2026-06-09): for
PERIODIC KU the pairing does not apply - Stonek (arXiv:1801.00156) proves
THH(KU) ~ KU v Sigma KU_Q: inverting Bott RATIONALIZES the diagonal's
cotangent data (divisible, no cardinalities). The same trade as the q->1
groupoid leak: buy the flow/symmetry, lose the integers. The correct
target is CONNECTIVE ku: Adams operations still act, and THH(ku) has
honest finite torsion (Ausoni's computation). C6 = the Euler pairing on
the ku ^ ku square with the psi^k graphs as the second class family.

Background: T1 interval certification (unchanged).

## 7. Literature position (audited 2026-06-09)

- Bokstedt, "The topological Hochschild homology of Z and Z/p"
  (unpublished, standard citation; statement confirmed in multiple
  published sources, e.g. arXiv:1711.10226, arXiv:2505.02218).
- Hesselholt, "Topological Hochschild homology and the Hasse-Weil zeta
  function" (arXiv:1602.01980): for X smooth proper over F_q, regularized
  determinants over TP realize zeta(X, s) - Deninger's program made
  unconditional in char p. Our section 5 wall statement is the
  arithmetic-square face of his properness hypothesis.
- "Topological Hochschild homology and zeta values" (arXiv:2011.11549,
  Duke 2024): THH filtrations + Weil-etale compute special values
  zeta*(X, n). The THH <-> zeta-values bridge is established machinery.
- The specific observation prod_reg |THH_{2k-1}(Z)| = sqrt(2pi) =
  e^{-zeta'(0)} with the genus/diagonal reading: likely folklore-adjacent
  in the S-arithmetic community (Rognes school); not located in print as
  such. The gate-system framing (sign on the square, carrier fork,
  properness relocation) is this program's.

The program's position after C4': the missing object has been narrowed
from "an integer-valued sign-bearing pairing on a square" (doc 16) to
"a properness theorem for the derived square over S" - a named, posed
problem in an active field, with the local case already a theorem.
