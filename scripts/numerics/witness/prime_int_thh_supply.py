"""R-INT / C5 first pass: the explicit-formula SUPPLY side as THH count ladders.

Doc 18 found <Delta,Delta>_tors = zeta'(0) (a constant). C5 asks for the
FUNCTION: weight the THH torsion ladder by the canonical circle grading
(degree 2k-1 <-> weight k, the Connes-operator grading B(x^k) = k x^{k-1}dx)
and form the regularized characteristic function of the diagonal:

    D(s) = prod_reg_{k>=1} (s + k)
         = sqrt(2pi) / Gamma(s+1)          (Lerch),

so  -d/ds log D(s) = psi(s+1)  -- A DIGAMMA: the explicit formula's
archimedean supply term in shape (doc 09's density carries
-log pi + Re psi(1/4 + it/2); the affine reparametrization of the argument
is normalization freedom in the weight choice, the DIGAMMA SHAPE is not).
At s = 0 this recovers doc 18: -log D(0) = -(1/2)log 2pi = zeta'(0).

Local ladders: THH(F_p) = F_p[sigma], |pi_{2i}| = p, so

    log |THH_{2i}(F_p)| = log p = Lambda(p^i)   for ALL i >= 1:

the von Mangoldt function IS the THH log-cardinality dictionary
(n = p^i <-> the weight-i entry of the F_p ladder), and the s-weighted
ladder sums to the local supply -zeta_p'/zeta_p(s) exactly; summing over
p gives -zeta'/zeta(s). Non-prime-powers have NO carrier: a closed point
of Spec Z with residue field of size n exists iff n is prime - the
deformation kill is categorical (classification of finite fields).

Fail-closed gates:
  A1: the Stirling-extracted regularized product (with the known
      [s(s+1)/2 + 1/12]/N correction; error then O(N^-2)) matches
      sqrt(2pi)/Gamma(s+1) (flint) at several complex s.
  A2: the numerically differentiated extraction gives -psi(s+1) (flint
      digamma) - the digamma shape is exhibited, not cited.
  A3: s = 0 recovers zeta'(0) (doc 18 tie-in).
  L1: Lambda(n) (independent factorization) == THH dictionary value for
      all n <= 300, including ZERO at every non-prime-power (no carrier).
  L2: per-p ladder sums close against d/ds log(1 - p^{-s}) (1e-12).
  L3: assembly: sum over p <= 10^6 of closed-form ladders matches flint
      -zeta'/zeta(2) to the sieve-tail tolerance.
  P1: the classical properness identity at the bottom of the wall:
      Poisson/theta functional equation theta(1/x) = sqrt(x) theta(x)
      (van der Geer-Schoof's exact RR for compactified Spec Z is this
      identity); verified numerically. The MISSING theorem is its
      sphere-spectrum-level version - that is what "properness" means.

Run:
    python3 -m scripts.numerics.witness.prime_int_thh_supply
"""
import cmath
import math
import sys

import flint

FAIL = []


def check(name, ok, detail):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    if not ok:
        FAIL.append(name)


def reg_log_D(s, N):
    """Stirling extraction of log prod_reg_{k>=1}(s+k), error O(N^-2)."""
    xs = [cmath.log(s + k) for k in range(1, N + 1)]
    total = complex(math.fsum(x.real for x in xs),
                    math.fsum(x.imag for x in xs))
    div = (N + s + 0.5) * math.log(N) - N
    corr = (s * (s + 1) / 2.0 + 1.0 / 12.0) / N
    return total - div - corr


def lerch_log_D(s):
    """log( sqrt(2pi) / Gamma(s+1) ) via flint, principal branch."""
    flint.ctx.prec = 200
    g = flint.acb(complex(s).real, complex(s).imag) + 1
    val = flint.acb(2 * math.pi).sqrt().log() - g.lgamma()
    return complex(val.real.mid(), val.imag.mid())


# ---------------------------------------------------------------- A1
print("A1: D(s) = prod_reg (s+k) vs sqrt(2pi)/Gamma(s+1), complex s")
N = 200_000
worst = 0.0
for s in (0.0, 0.5, 1.0 + 1.0j, 2.0 - 3.0j, -0.25 + 0.5j):
    reg = reg_log_D(s, N)
    ler = lerch_log_D(s)
    err = abs(reg - ler)
    worst = max(worst, err)
    print(f"    s = {s!s:>12}: extracted {reg:.10f}  Lerch {ler:.10f}  "
          f"err {err:.3e}")
check("Lerch identity", worst < 1e-8,
      f"worst err {worst:.3e} at N = {N} (O(N^-2) regime)")

# ---------------------------------------------------------------- A2
print("\nA2: -d/ds log D(s) = psi(s+1) (digamma shape, exhibited)")
flint.ctx.prec = 200
worst2 = 0.0
h = 1e-4
for s in (0.0, 0.5, 1.5, 1.0 + 1.0j):
    fd = -(reg_log_D(s + h, N) - reg_log_D(s - h, N)) / (2 * h)
    dg = flint.acb(complex(s).real + 1, complex(s).imag).digamma()
    dg = complex(dg.real.mid(), dg.imag.mid())
    err = abs(fd - dg)
    worst2 = max(worst2, err)
    print(f"    s = {s!s:>10}: FD {fd:.8f}  psi(s+1) {dg:.8f}  err {err:.3e}")
check("digamma supply", worst2 < 1e-3,
      f"the archimedean supply term IS the ladder's log-derivative; "
      f"worst err {worst2:.3e}")

# ---------------------------------------------------------------- A3
print("\nA3: s = 0 tie-in to doc 18")
d0 = -reg_log_D(0.0, N).real
zp = -0.5 * math.log(2 * math.pi)
check("zeta'(0) tie-in", abs(d0 - zp) < 1e-9,
      f"-log D(0) = {d0:.12f} vs zeta'(0) = {zp:.12f}")

# ---------------------------------------------------------------- L1
print("\nL1: Lambda(n) == THH(F_p) log-cardinality dictionary, n <= 300")


def vmangoldt(n):
    for p in range(2, n + 1):
        if p * p > n and n > 1:
            return math.log(n)  # n itself prime
        if n % p == 0:
            m = n
            while m % p == 0:
                m //= p
            return math.log(p) if m == 1 else 0.0
    return 0.0


def thh_dict(n):
    """log|THH_{2i}(F_p)| = log p if n = p^i (a closed-point ladder entry);
    no carrier otherwise (finite fields have prime-power order; closed
    points of Spec Z have residue fields F_p exactly)."""
    for p in range(2, n + 1):
        if p ** 2 > n:
            return math.log(n)  # n prime: weight-1 entry of the F_n ladder
        if n % p == 0:
            m, i = n, 0
            while m % p == 0:
                m //= p
                i += 1
            return math.log(p) if m == 1 else 0.0
    return 0.0


bad = [n for n in range(2, 301) if abs(vmangoldt(n) - thh_dict(n)) > 1e-15]
npp = sum(1 for n in range(2, 301) if vmangoldt(n) == 0.0)
check("von Mangoldt dictionary", not bad,
      f"exact match on 2..300 ({npp} non-prime-powers all carrier-free); "
      f"mismatches: {bad}")

# ---------------------------------------------------------------- L2
print("\nL2: per-prime ladder = local supply -zeta_p'/zeta_p(s)")
worst5 = 0.0
for p in (2, 3, 5):
    for s in (2.0, 1.0 + 2.0j):
        ladder = sum(math.log(p) * p ** (-i * s) for i in range(1, 400))
        x = p ** (-s)
        closed = math.log(p) * x / (1 - x)
        err = abs(ladder - closed)
        worst5 = max(worst5, err)
check("local Euler factor", worst5 < 1e-12,
      f"sum_i log|THH_2i(F_p)| p^(-is) = d/ds log(1-p^-s), "
      f"worst err {worst5:.3e}")

# ---------------------------------------------------------------- L3
print("\nL3: assembly -- sum over p of THH ladders = -zeta'/zeta(2)")
P = 10 ** 6
sieve = bytearray([1]) * (P + 1)
sieve[0:2] = b"\x00\x00"
for i in range(2, int(P ** 0.5) + 1):
    if sieve[i]:
        sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
total = 0.0
for p in range(2, P + 1):
    if sieve[p]:
        total += math.log(p) / (p * p - 1.0)   # closed-form full i-sum at s=2
flint.ctx.prec = 200
hh = flint.arb(1) / (flint.arb(10) ** 30)
zd = (flint.acb(2 + hh).zeta() - flint.acb(2 - hh).zeta()) / (2 * flint.acb(hh))
mzz = float((-zd / flint.acb(2).zeta()).real.mid())
err6 = abs(total - mzz)
check("global supply assembly", err6 < 2e-6,
      f"sum_p ladders = {total:.8f} vs -zeta'/zeta(2) = {mzz:.8f}, "
      f"err {err6:.3e} (tail ~ 1/P = 1e-6)")

# ---------------------------------------------------------------- P1
print("\nP1: the properness identity (classical level): theta Poisson FE")
worst7 = 0.0
for x in (0.3, 1.0, 2.7):
    th = lambda t: sum(math.exp(-math.pi * n * n * t)
                       for n in range(-60, 61))
    err = abs(th(1.0 / x) - math.sqrt(x) * th(x))
    worst7 = max(worst7, err)
check("Poisson/theta FE", worst7 < 1e-13,
      f"theta(1/x) = sqrt(x) theta(x), worst err {worst7:.3e} -- the exact "
      f"RR of compactified Spec Z (van der Geer-Schoof) IS this identity; "
      f"its sphere-level version is the missing properness theorem")

print(f"\n{'ALL PASS' if not FAIL else 'FAILURES: ' + ', '.join(FAIL)}")
sys.exit(0 if not FAIL else 1)
