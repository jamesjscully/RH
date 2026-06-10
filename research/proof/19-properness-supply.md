# 19 - C5 first pass: properness decomposed; the supply side of the explicit formula is a THH count ladder

Status: C5 first pass executed 2026-06-09. Witness: prime_int_thh_supply.py
(ALL PASS, exit-code gated). Citation-grade inputs: Bokstedt's THH(Z),
THH(F_p) (doc 18 refs); van der Geer-Schoof arXiv:math/9802121 for the
classical proper section count.

## 1. What "properness" means for this search

Doc 18 relocated the wall to properness. Concretely, the FF proof uses
properness through four separable ingredients:

```text
PF (finiteness):  coherent cohomology of the proper surface is
                  finite-rank => Euler characteristics are honest
                  integers (no regularization);
PD (duality):     Serre duality => the pairing is symmetric and the
                  h^0(K - D) term exists;
PR (Riemann-Roch): chi(D) is computable from intersection numbers =>
                  section COUNTS are tied to the pairing;
PS (sections):    h^0(D) counts actual objects - the integers whose
                  "> -1 means >= 0" steps cross the zero-slack
                  thresholds (doc 16).
```

The derived square HZ ^ HZ is "affine over S": it has PF degree-wise
(every THH group is finite) but not in total (infinite tower), and it has
none of PD/PR/PS. C4' showed what survives without properness: the local
intersection theory (the diagonal's normal/cotangent data) - and that
alone already produced the sign and the archimedean constant.

## 2. The function-level upgrade: the diagonal's characteristic function

Weight the THH(Z) torsion ladder by the canonical circle grading (degree
2k-1 <-> weight k; the Connes operator B(x^k) = k x^{k-1} dx is where the
k in Z/k = pi_{2k-1} comes from) and form the regularized characteristic
function of the diagonal:

    D(s) = prod_reg_{k>=1} (s + k) = sqrt(2pi) / Gamma(s+1)     (Lerch)

    -d/ds log D(s) = psi(s+1)        (DIGAMMA)
    -log D(0)      = zeta'(0)        (doc 18's constant, recovered)

Witness: the Stirling-extracted product matches sqrt(2pi)/Gamma(s+1) at
complex s to 4e-10, and its numerical log-derivative matches flint's
digamma to 2e-6 - the shape is exhibited, not cited.

NORMALIZATION HONESTY: the weight choice (k vs k/2 vs 2k) is a modeling
decision; affine reparametrization of the Gamma argument is free. What is
normalization-INVARIANT: the log-derivative of the diagonal's regularized
characteristic function is A DIGAMMA. The explicit formula's archimedean
supply term (doc 09's density: -log pi + Re psi(1/4 + it/2)) is also a
digamma. The Gamma_R factor's analytic shape now has a count-level
carrier; the exact argument dictionary is deferred to the duality step
(where the 1/4 = self-dual normalization must come from).

## 3. The local ladders: von Mangoldt IS a THH log-cardinality

    log |THH_{2i}(F_p)| = log p = Lambda(p^i)   for every i >= 1.

The dictionary n = p^i <-> (weight-i entry of the F_p ladder) reproduces
the von Mangoldt function EXACTLY (verified n <= 300, all 220
non-prime-powers carrier-free), the s-weighted ladder sums to the local
supply -zeta_p'/zeta_p(s) exactly (1e-16), and the sum over p assembles
to -zeta'/zeta(2) (1e-6, sieve-tail limited).

THE DEFORMATION KILL IS CATEGORICAL: a closed point of Spec Z with
residue field of size n exists iff n is prime (classification of finite
fields); atoms at non-prime-powers, or atoms at p with weight != log p,
have NO carrier. DH cannot be built in this category - not because a
computation fails but because the object does not exist. This is P2 at
the level of INDIVIDUAL supply atoms, the strongest carrier kill so far.

## 4. Consequence: the supply side has a second description

The entire SUPPLY side of the explicit formula - the digamma supply plus
the Lambda(n) atoms, i.e. doc 09's density D_R(t) up to the pole terms -
is now reproduced as regularized cardinalities of THH over the sphere
with the canonical circle weight:

```text
archimedean supply  =  characteristic function of THH(Z)_tors   (sec 2)
prime atoms         =  log-cardinalities of THH(F_p) ladders    (sec 3)
pole terms          =  the rank parts (pi_0 = Z excess), where
                       Deninger's H^0/H^2 factors live - excluded
                       here exactly as there.
```

Against doc 10's realization spec inputs {free semigroup on log p,
KMS beta = 1/2, Lambda >= 0, digamma supply}: three of four now have a
count-level carrier (Lambda >= 0 is definitional cardinality positivity;
the log p spacings are the ladder weights; the digamma is sec 2). The
missing fourth - KMS beta = 1/2, the self-dual n^{-1/2} normalization -
is precisely a DUALITY datum, i.e. it must come from the properness
package (PD), not from the affine square. Consistent: the count grammar
already located self-duality as the critical-line selector (doc 17 C0').

## 5. Where the zeros are: properness = Poisson summation

What the supply description does NOT touch: the zeros. On the FF side
zeros enter through GLOBAL cohomology (PR/PS: Riemann-Roch on the proper
surface), never through the local supply. The classical model of the
missing package exists: van der Geer-Schoof (math/9802121) define
h^0(D) for compactified Spec Z as a THETA-regularized section count and
prove an EXACT Riemann-Roch h^0(D) - h^0(kappa - D) = deg D - (1/2)log|d|
whose entire proof is Poisson summation (witness P1 verifies the theta
functional equation, the identity itself). So:

```text
properness, in this program's coordinates, = Poisson summation:
  - classical level: theta FE / Tate's thesis (theorem; but the count
    h^0 is theta-REGULARIZED - non-integer, the same deficit as our
    zeta-regularized tower; the two regularizations are the two faces
    of the missing properness);
  - char-p THH level: Hesselholt's TP theorem REQUIRES smooth+proper -
    properness is the hypothesis, not the output;
  - S-level (what the program needs): a Poisson-summation / Serre-
    duality theorem for the derived square over the sphere, making the
    Euler pairing finite-rank and self-dual. Known relatives: the
    Braverman-Kazhdan/Ngo Poisson summation conjecture; CC's absolute
    Riemann-Roch program. OPEN.
```

The wall, one phrase sharper than doc 18: the program needs Poisson
summation as a theorem about ring spectra; everything else on the supply
side is already counts.

## 6. Fork scorecard and honest limits

- F1 value fork: the supply values are EF-equal BY CONSTRUCTION of the
  comparison (secs 2-3 verify the dictionary, they do not add zero-side
  information). What is genuinely new information: INTEGRALITY (each
  supply value is a cardinality), the FLOW (the circle action supplies
  the weight grading - gate G-INT's Phi), and the categorical
  deformation kill (sec 3). The zeros are untouched - no over-claim.
- P2: passes at atom granularity (strongest form to date).
- S-spec (doc 15): S1 partial (carrier = ring spectra; primes appear as
  closed points, not as input coefficients); S2 PASS (the doubling is
  the non-flatness of Z (x) Z over S); S3 degree-wise PASS / total
  regularized; S4 PASS (EF used only as comparison); S5 run (this doc).
- The pole terms and the KMS-1/2 normalization are NOT derived; both are
  expected from the duality package (sec 4-5). Fail-closed: if the
  S-level duality, once formulated, fails to produce the 1/4-shift
  digamma argument and the s(s-1) pole factors, the carrier is wrong.

## 7. Next

C5' (the properness front, fresh-context scale): formulate the duality/
Poisson question precisely - candidate vessel: the S^1-Tate construction
TP over the square (Hesselholt's vessel), with the vdGS theta-count as
the classical shadow to match; first diagnostic: compare the Frobenius
eigenvalue ladder of TP(F_p) (2 pi i / log p spacings) with the ladder
weights of sec 3 (the free-semigroup spacing input of doc 10).
C6 (Frobenius family): unchanged - ku ^ ku with psi^k graphs (doc 18).
