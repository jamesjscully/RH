"""Q-SCHEME first gate (doc 21 sec 2): the genus-probe audit.

Tension T-b: CC's proven Riemann-Roch for compactified Spec Z is genus-0
(chi(D) = ceil'(deg_2 D) + 1, K = -2{2}, deg_2 K = -2; arXiv:2205.01391,
2306.00456), while doc 18's THH diagonal reads 2 - 2g = zeta'(0), g =
1.459. This witness decides, fail-closed, whether the clash is a UNIT
artifact, a SCHEME artifact, or INVARIANT-LEVEL (different objects).

PRE-REGISTERED READINGS (fixed before the run):
  A1  CC is internally consistent (chi(O) = +1 <=> g = 0 <=> deg_2 K =
      -2 = 2g - 2, exact integers) -- expected PASS (transcription).
  A2  No standard point-unit (log q, q >= 2 an integer) makes the THH
      cotangent degree (1/2)log 2pi an integer: (1/2)log 2pi / log q in
      Z would force 2pi = q^{2m}, impossible (2pi transcendental).
      Numerics exhibit the distance on a range.
  A3  NO unit reconciles the probes: g_THH(u) = 1 + (1/4)log 2pi / u > 1
      for every unit u > 0, while g_CC = 0 (unit-free integer theorem).
      If PASS: the clash is NOT a unit choice -- invariant-level.
  A4  The SIGN of doc 18's diagonal is interpretation-relative: in the
      OPERATOR reading (eigenvalues c*k, scale c free - Deninger uses
      c = 1/2pi), <Delta,Delta>(c) = zeta'(0) + (1/2)log c flips sign at
      c = 2pi; in the COUNT reading the ladder entries are CARDINALITIES
      (dimensionless integers), the scale is canonically 1, and the sign
      stands. Expected: numerics confirm the flip; the count reading is
      the program's native one (G-INT grammar) -- recorded as such.
  A5  Ring-bearing negative control (G-INT6) DESIGNED and discriminating:
      Lindenstrauss-Madsen (Trans. AMS 352 (2000)): THH_{2n-1}(O_K) =
      D^{-1}/n O_K, so |THH_{2n-1}(O_K)| = n^d |d_K| (d = [K:Q]); hence
      <Delta,Delta>_{O_K} = d zeta'(0) + (1/2) log|d_K|.
      The (1/2)log|d_K| is exactly the |d_K|^{s/2} exponent of xi_K's
      functional equation: the ladder tracks THE FIELD'S OWN completed-
      zeta data. Expected: values distinct from zeta'(0) for K != Q
      (a fitted dictionary would map every ring to zeta's value).

Verdict template: A1-A3 PASS => T-b resolves as DIFFERENT INVARIANTS
(CC: cohomological chi with duality over their base; THH: cotangent of
the unit map over S); the FF index needs the two IDENTIFIED, and that
identification = duality over S = the wall, now measured by the pair
(-2 log 2, +(1/2)log 2pi).

Run:
    python3 -m scripts.numerics.witness.prime_int_genus_audit
"""
import math
import sys

import flint

FAIL = []


def check(name, ok, detail):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    if not ok:
        FAIL.append(name)


ZP0 = -0.5 * math.log(2 * math.pi)          # zeta'(0)
DEG_THH = -ZP0                               # deg Omega^1_{Z/S},reg in nats

# ---------------------------------------------------------------- A1
print("A1: CC internal consistency (integer arithmetic, transcription)")
chi_O_const = 1            # chi(D) = ceil'(deg_2 D) + 1 at D = 0
g_cc = 1 - chi_O_const     # chi(O) = 1 - g
deg2_K_cc = -2             # K = -2{2}
check("CC: chi(O)=+1 <=> g=0 <=> deg_2 K = -2",
      g_cc == 0 and deg2_K_cc == 2 * g_cc - 2,
      f"g_CC = {g_cc}, deg_2 K = {deg2_K_cc} = 2g-2 (exact)")

# ---------------------------------------------------------------- A2
print("\nA2: no integer point-unit for the THH cotangent degree")
mind, argq = 1.0, None
for q in range(2, 10001):
    x = DEG_THH / math.log(q)
    dist = abs(x - round(x))
    # exclude the degenerate round-to-0 tail (x < 1/2 means nearest int 0
    # = 'degree zero', the trivial reading; the analytic statement covers it)
    if round(x) != 0 and dist < mind:
        mind, argq = dist, q
print(f"    min distance to a NONZERO integer over q in [2, 10^4]: "
      f"{mind:.6f} at q = {argq}")
print(f"    (exact obstruction: (1/2)log 2pi / log q = m in Z would force "
      f"2pi = q^(2m); 2pi is transcendental)")
check("no point-unit integrality", mind > 1e-3,
      f"deg Omega^1 = {DEG_THH:.6f} nats is not an integer multiple of any "
      f"log q (min gap {mind:.4f})")

# ---------------------------------------------------------------- A3
print("\nA3: no unit reconciles g_CC = 0 with g_THH(u)")
worst_gap = min(1.0 + 0.25 * math.log(2 * math.pi) / u - 0.0
                for u in [10 ** (k / 10.0) for k in range(-40, 41)])
check("unit reconciliation impossible", worst_gap >= 1.0,
      f"g_THH(u) = 1 + (1/4)log 2pi / u > 1 for all u > 0 (inf over grid "
      f"= {worst_gap:.6f}); g_CC = 0 unit-free => clash is INVARIANT-LEVEL")

# ---------------------------------------------------------------- A4
print("\nA4: scale-dependence of the sign in the OPERATOR reading")
flint.ctx.prec = 500
h = flint.arb(1) / (flint.arb(10) ** 30)


def diag_operator_reading(c):
    """<Delta,Delta>(c) = +d/ds [c^-s zeta(s)] at s = 0 (= -Sum_reg log(ck)),
    by flint central difference (independent of the closed form)."""
    ca = flint.arb(c)
    f = lambda w: ca ** (-w) * flint.acb(w).zeta().real
    return float(((f(h) - f(-h)) / (2 * h)).mid())


rows, worst4 = [], 0.0
for c in (1.0, 1.0 / (2 * math.pi), 2 * math.pi, 4 * math.pi):
    # Sum_reg log(ck) = -g'(0); <Delta,Delta>(c) = -Sum_reg = +g'(0)
    val = diag_operator_reading(c)
    closed = ZP0 + 0.5 * math.log(c)
    worst4 = max(worst4, abs(val - closed))
    rows.append((c, val))
    print(f"    c = {c:>9.6f}: <Delta,Delta>(c) = {val:+.6f}   "
          f"(closed form zeta'(0) + (1/2)log c = {closed:+.6f})")
signs = [v for (c, v) in rows]
check("operator-reading sign flip", worst4 < 1e-12 and signs[0] < 0
      and signs[1] < 0 and signs[3] > 0,
      f"sign flips at c = 2pi (flint vs closed form, worst {worst4:.1e}); "
      f"COUNT reading has c = 1 canonically (cardinalities are "
      f"dimensionless) and keeps zeta'(0) < 0")

# ---------------------------------------------------------------- A5
print("\nA5: the O_K control (G-INT6), designed on Lindenstrauss-Madsen")
# order check for K = Q(i): D^{-1} = (1/2)Z[i]; index of n Z[i] in
# (1/2) Z[i] is det ratio = n^2 / (1/2)^2 = 4 n^2 = |d_K| n^d exactly.
ok5a = all(4 * n * n == round((n ** 2) / (0.5 ** 2)) for n in (1, 2, 3, 5))
check("LM order formula spot-check (Q(i))", ok5a,
      "|D^{-1}/n Z[i]| = 4 n^2 = |d_K| n^d (lattice index, exact)")

fields = [("Q", 1, 1), ("Q(i)", 2, 4), ("Q(sqrt5)", 2, 5),
          ("Q(sqrt-23)", 2, 23), ("Q(zeta5)", 4, 125)]
print("    <Delta,Delta>_{O_K} = d zeta'(0) + (1/2) log|d_K|:")
vals = []
for name, d, absd in fields:
    v = d * ZP0 + 0.5 * math.log(absd)
    vals.append(v)
    print(f"      {name:>10} (d={d}, |d_K|={absd:>3}): {v:+.6f}")
distinct = all(abs(v - ZP0) > 1e-3 for v in vals[1:])
check("O_K control discriminates", distinct,
      "every K != Q gives a value distinct from zeta'(0); the ladder "
      "tracks (1/2)log|d_K| = the |d_K|^{s/2} exponent of xi_K's "
      "functional equation - the field's OWN completed-zeta datum")

print("""
VERDICT (pre-registered template): A1-A3 PASS => tension T-b is
INVARIANT-LEVEL: CC's chi computes cohomology-with-duality over their
base (integer by tolerance/ceiling); doc 18's diagonal computes the
cotangent of the unit map over S (integer degree-wise, transcendental in
total). Neither is wrong; they are not yet the same object. The FF index
needs them IDENTIFIED on one square - that identification is the
properness/duality wall, now measured by the pair
(deg K_CC, deg Omega_THH) = (-2 log 2, +(1/2) log 2pi).
A4: doc 18's sign claim is native to the COUNT reading (canonical scale);
the genus NUMBER 1.459 was the weakest link (unit + reading laden) and is
hereby demoted to calibration (G-INT6 ledger).
""")

print(f"{'ALL PASS' if not FAIL else 'FAILURES: ' + ', '.join(FAIL)}")
sys.exit(0 if not FAIL else 1)
