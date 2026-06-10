# 20 - C5' diagnostic: duality completion generates the self-dual normalization; the place dichotomy is orbit vs fixed point

Status: C5' first diagnostic executed 2026-06-10. Witness:
prime_int_tate_ladder.py (ALL PASS, exit-code gated). Both fail-closed
criteria pre-registered in doc 19 section 6 are MET at the ladder level.

## 1. What was tested

Doc 19 left the realization spec one input short: the KMS beta = 1/2
(self-dual n^{-1/2}) normalization was predicted to be a DUALITY datum -
something the affine square cannot produce and the properness package
must. The known vessel (Hesselholt's TP = THH^{tS^1}; Deninger's
regularized determinants) makes a sharp prediction: the Tate
construction replaces the THH half-ladder by the FULL eigenvalue ladder
s + (2 pi i / log p) Z (the Frobenius orbit is a circle of circumference
log p), and the regularized characteristic polynomial of the full ladder
should carry the self-dual prefactor automatically.

## 2. Results (each regularization step exhibited numerically)

LOCAL (the KMS-1/2 emergence, gate W3, 3e-14):

    prod_reg_{n in Z} (s + 2 pi i n / log p)
      = s * [prod_reg omega_n]^2 * prod_{n>=1}(1 + s^2/omega_n^2)
      = 2 sinh((log p) s / 2)
      = p^{s/2} (1 - p^{-s}).

The THH half-ladder (doc 19 L2) gives the Euler factor WITHOUT p^{s/2};
adding the ladder's negative half - which is exactly what the Tate/
duality completion does - GENERATES the self-dual normalization. The
missing fourth realization input is not an assumption to be imported:
it is what compactification produces. (Closed form = Deninger's
local-factor-as-regularized-determinant identity; the witness assembles
it from independently exhibited pieces: Euler's sinh product to 1.5e-13
and the zeta-reg scaling anomaly prod_reg(cn) = c^{-1/2} sqrt(2pi) to
7.5e-16.)

ARCHIMEDEAN (the 1/4-shift, gate W4, 1.3e-06):

    prod_reg_{n>=0} (n + s/2) = sqrt(2pi) / Gamma(s/2),

and its log-derivative evaluated ON the critical line s = 1/2 + it is
(1/2) psi(1/4 + it/2) - the explicit formula's archimedean supply term
with the 1/4-shift VERBATIM (doc 09's density term). The 1/4 is not a
mystery constant: it is "the self-dual line seen through the spacing-2
ladder" (s/2 at s = 1/2 + it).

## 3. The structural statement

One construction - the regularized characteristic function of an
S^1-weighted count ladder - produces every Euler factor of the completed
zeta function, and the type of factor is decided by the orbit geometry:

```text
compact orbit (circumference log p)  -> full Z-ladder, spacing
    2 pi i/log p  -> 2 sinh((log p)s/2) = p^{s/2}(1 - p^{-s});
fixed point (the archimedean place)  -> degenerate half-ladder,
    spacing 2, start 0  -> sqrt(2pi)/Gamma(s/2);
rank parts (pi_0 excess, H^0/H^2)    -> the s and s-1 pole factors
    (Deninger's normalization; not re-derived here).
```

This is Connes/Deninger's flow dichotomy, now carried by COUNT ladders
(doc 19: every ladder entry is a finite-group cardinality from THH).
Combined with docs 18-19: the completed zeta function's entire local
structure - atoms, digamma, self-dual normalization, sign of the
diagonal - is now reproduced from torsion cardinalities over the sphere
plus circle-equivariance. The program's doc 10 realization inputs are
4-for-4 AT THE SUPPLY LEVEL: Lambda >= 0 (cardinalities), free semigroup
on log p (ladder spacings), digamma supply (degenerate ladder), KMS 1/2
(duality completion). No zero-side input anywhere in the construction.

## 4. Honest limits (unchanged in kind, sharpened in location)

- The ladder DATA (which spacing, which start, full vs half) was taken
  from the known TP/Deninger structure, not derived from an actual
  S^1-equivariant analysis of a compactified HZ ^ HZ. C5'' = derive it:
  show the Tate construction over the derived square produces exactly
  these ladders. (Local case: Hesselholt's theorem. Archimedean case:
  open - this is where "Frobenius at the infinite place = the circle
  action degenerating" must become a theorem.)
- The GLOBAL assembly is still untouched: products of local factors and
  the functional equation give the completed zeta; the ZEROS require the
  global cohomology (H^1) - the Poisson/properness theorem over S
  (doc 19 sec 5). Nothing here touches them; the fork discipline stands.
- The witness verifies regularized-product IDENTITIES (each step
  independently); it cannot verify that the homotopy theory delivers
  these ladders - that is C5'''s burden of proof.

## 5. Next

C5'' (fresh-context scale, now precisely posed): S^1-equivariant
structure of the compactified derived square - does TP of the square
(or the appropriate genuine-equivariant/Tate object over HZ ^ HZ)
produce (a) the full ladders at finite places, (b) the degenerate
spacing-2 ladder at infinity, (c) the s(s-1) rank factors? (a) is
essentially Hesselholt; (b) is the genuine open piece; (c) should be
the pi_0 = Z excess. Then C5''' = the global Poisson step.
C6 (Frobenius family on ku ^ ku): unchanged, queued.
