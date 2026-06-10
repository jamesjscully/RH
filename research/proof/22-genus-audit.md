# 22 - Q-SCHEME first gate executed: the genus clash is invariant-level; the sign is reading-relative; the O_K control is live

Status: 2026-06-10. Witness: prime_int_genus_audit.py (ALL PASS,
exit-code gated, pre-registered readings A1-A5 in the docstring).
Decides tension T-b of doc 21 and discharges the first Q-SCHEME gate.
Inputs on citation: CC arXiv:2205.01391/2306.00456 (transcribed by
fleet worker K, verifier-confirmed); Lindenstrauss-Madsen Trans. AMS
352 (2000) (THH_{2n-1}(O_K) = D^{-1}/n O_K; located this session,
statement confirmed against the published abstract + downstream
literature; line-level check = open debt).

## 1. Verdicts

A1 (CC internal): chi(O) = +1 <=> g_CC = 0 <=> deg_2 K = -2 = 2g - 2.
CC's two probes agree with each other, exactly, in integers. Their RR
is a real curve-level theorem with a self-consistent genus.

A2 (units): no point-unit log q (integer q >= 2) makes the THH
cotangent degree (1/2)log 2pi an integer (exact: 2pi = q^{2m} is
impossible; numerics: min gap 0.16 over q <= 10^4). The THH "genus"
never had an integer home in any standard unit.

A3 (THE DECISION): no unit u > 0 reconciles the probes - g_THH(u) =
1 + (1/4)log 2pi / u > 1 always, g_CC = 0 unit-free. The clash is
INVARIANT-LEVEL: CC's chi computes cohomology-with-duality over their
base; doc 18's diagonal computes the cotangent of the unit map over S.
Different objects, both correct. (Doc 21 reading (a)/(b), now decided;
reading (c) "unit error" is EXCLUDED.)

A4 (the sign): in the OPERATOR reading (eigenvalues ck, scale free -
Deninger's convention is c = 1/(2pi)), <Delta,Delta>(c) = zeta'(0) +
(1/2)log c FLIPS SIGN at c = 2pi (flint vs closed form to 2e-16). In
the COUNT reading - the program's native G-INT grammar - ladder entries
are cardinalities, dimensionless, scale canonically 1, and the negative
sign stands. CONSEQUENCE: doc 18's sign claim is interpretation-
relative; it is a theorem of the count reading only. The genus NUMBER
1.459 (which spent both the unit and the reading) is demoted to
calibration per G-INT6; doc 18 annotated in place.

A5 (the ring-bearing control, G-INT6): Lindenstrauss-Madsen gives
|THH_{2n-1}(O_K)| = n^d |d_K| (spot-checked exactly for Z[i]), hence

    <Delta,Delta>_{O_K} = d zeta'(0) + (1/2) log|d_K|.

Values: Q -0.919, Q(i) -1.145, Q(sqrt5) -1.033, Q(sqrt-23) -0.270,
Q(zeta5) -1.262 - every field distinct from zeta'(0), and the
discriminant enters with exponent 1/2: exactly the |d_K|^{s/2} of
xi_K's functional equation. The dictionary, fed a different ring,
returns that ring's own completed-zeta datum - a fitted dictionary
would not. (Also structurally: the multiplicity d of the digamma
ladder = r_1 + 2 r_2 = the total Gamma_R-multiplicity of xi_K by
duplication.) The G-INT6 control is LIVE and passes its design test.

## 2. What this changes

- T-b is closed as a tension and reopened as a TARGET: the wall is now
  measured. The identification the FF index needs - one square on which
  CC's duality-grade chi and the THH cotangent pairing are THE SAME
  invariant - is the properness step, with the concrete calibration
  pair (deg K_CC, deg Omega_THH) = (-2 log 2, +(1/2) log 2pi). Any
  proposed duality-over-S must explain BOTH numbers or show which one
  its objects cannot see.
- The program's hard currency is restated by G-INT6: exact integer
  identities (Bokstedt tower, lcm ladder, Lambda dictionary, LM orders)
  pass; dimensionful readings (genus, "the constant is zeta'(0)") are
  calibration. The count reading is canonical for signs; the operator
  reading is convention until a theorem (the C5''-infty scheme
  selector) fixes it.
- The O_K family is now a standing test bench: any future construction
  claiming to "produce zeta's data" must be run on O_K and produce
  xi_K's (different different, different discriminant) - failure =
  fitting.

## 3. Open continuations

- Workers M (THR reflection-Tate fold, gate C5''-infty first checkpoint)
  and N (the CC square posed in their tolerant-module formalism) are in
  flight; their results land in research/work/M,N-*.md.
- LM line-level verification debt (the D^{-1}/n O_K statement is cited
  from the abstract + downstream literature, not re-derived).
- C6'/C6''/C6''' as ranked in doc 21 sec 5.
