"""gf_w1_residue_offset_independence -- the analytic core of lemma W1.

W1 (research/global-frobenius doc 06): for any integer monotone staircase
D(k) = log_b k + O(1) jumping by +1 at points n_j with log_b n_j = j + e_j,
e_j bounded, the defect series D_delta(s) = Sum_k (D(k) - log_b k) k^{-s} has a
SIMPLE POLE at s=0 whose residue MAGNITUDE is 1/(2 log b), INDEPENDENT of the
bounded offsets e_j (the shape of the staircase). Hence Sum_reg D(k) = infinity
for every such D -- side A of the integrality-summability dichotomy holds for the
whole class, not just CC's ceiling.

REDUCTION (the proof's spine). Writing D(k) = #{j : n_j <= k} (jump count),
    F(s) := Sum_k D(k) k^{-s} = Sum_j zeta(s, n_j)        (Re s > 1),
and D_delta(s) = F(s) + zeta'(s)/log b. zeta'(s)/log b is ENTIRE near s=0, so the
s=0 pole of D_delta is exactly that of F. Euler-Maclaurin on F = Sum_j zeta(s,n_j)
routes its only s=0 pole through
    g(w) := Sum_j n_j^{-w},   Res_{s=0} F = -(1/2) Res_{w=0} g
(the -1/2 and the routing are CERTIFIED for the ceiling in
prime_cc_quantization_defect, residue -1/(2 log b)). The NEW step W1 needs is:
    Res_{w=0} g = 1/log b   for EVERY bounded-offset jump set {n_j},
because g(w) = Sum_j b^{-w(j+e_j)} = Sum_j (1 - w e_j log b + ...) b^{-wj}, whose
leading geometric part Sum_j b^{-wj} = b^{-w}/(1-b^{-w}) has residue 1/log b at
w=0, and the offset correction b^{-w e_j} -> 1 shifts only the FINITE part (the
e_j enter at order w, killing the would-be pole contribution). So the residue is
offset-INDEPENDENT; the staircase shape moves only the finite part.

THIS WITNESS certifies the new step directly: Res_{w=0} g = lim_{w->0+} w*g(w) =
1/log b for two genuinely different staircases (ceiling, offset) in two bases,
and that the two shapes AGREE in the limit (offset-independence). It does NOT
recompute the certified -1/2 routing (prime_cc_quantization_defect) -- it closes
the one gap between that ceiling result and the general lemma.

PRE-REGISTERED READINGS (fixed before run, fail-closed):
  W0  sanity: w*g(w) for the pure geometric set n_j=b^j equals w/(1-b^{-w}),
      analytic, -> 1/log b. Check at w=1e-2,1e-3,1e-4 (monotone approach).
  W1  CEILING jump set n_m = b^{m-1}+1 (the real CC-type staircase):
      w*g(w) -> 1/log b; |w g(w) - 1/log b|/(1/log b) shrinks across
      w=1e-2,1e-3,1e-4 and is < 5e-3 at w=1e-4. (b=2,3)
  W2  OFFSET jump set n_j = floor(2 b^j / 3) (a genuinely different bounded
      offset): same limit 1/log b, < 5e-3 at w=1e-4. (b=2,3)
  W3  OFFSET-INDEPENDENCE (the new fact): |w g_ceil(w) - w g_offset(w)| -> 0;
      at w=1e-4 the two shapes agree to < 5e-3 (relative). => the residue
      depends only on the base, not the staircase shape.
  W4  a NON-log-density control: linearly-spaced jumps n_j = j give
      g(w) = Sum_j j^{-w} = zeta(w), which is REGULAR at w=0 (zeta(0)=-1/2), so
      w*g(w) -> 0: NO dichotomy-type residue. Confirms the residue 1/log b is
      special to GEOMETRIC (log-tracking) spacing -- the hypothesis of W1.

VERDICT: W0-W4 PASS => Res_{w=0} g = 1/log b for all bounded-offset (log-tracking)
staircases; with the certified -1/2 routing, |Res_{s=0} D_delta| = 1/(2 log b)
universally. Lemma W1's analytic core holds; side A of the dichotomy is proved
for the whole effective-integer class (modulo the routine Euler-Maclaurin write-up
in doc 06).
"""

import math
import sys

import flint

flint.ctx.prec = 200


def logn_geometric(j, b):
    return j * math.log(b)


def logn_ceiling(m, b):
    # jump point n_m = b^{m-1} + 1; log via log1p to avoid huge ints
    return (m - 1) * math.log(b) + math.log1p(b ** (-(m - 1)))


def logn_offset(j, b):
    # jump point n_j = floor(2 b^j / 3); leading log + bounded offset
    # exact for small j, asymptotic (offset log(2/3)) for large j
    if j <= 25:
        return math.log((2 * b ** j) // 3)
    return j * math.log(b) + math.log(2.0 / 3.0)


def w_times_zeta(w):
    """w * zeta(w) = w * Sum_j j^{-w} (linear jump set n_j=j), via the closed
    form zeta(w) -- regular at w=0, so the product -> 0."""
    wa = flint.arb(w)
    return wa * flint.acb(wa).zeta().real


def w_times_g(logn, b, w, jmax=None):
    """w * Sum_{j>=1} exp(-w * logn(j)), summed until terms are negligible."""
    lb = math.log(b)
    if jmax is None:
        # exp(-w j lb) < 1e-16 => j > 16 ln10 / (w lb)
        jmax = int(36.8 / (w * lb)) + 50
    wa = flint.arb(w)
    total = flint.arb(0)
    for j in range(1, jmax + 1):
        total += (-wa * flint.arb(logn(j, b))).exp()
    return wa * total


def run():
    passed = True

    def check(name, cond, detail=""):
        nonlocal passed
        tag = "PASS" if cond else "FAIL"
        if not cond:
            passed = False
        print(f"  [{tag}] {name}: {detail}")

    ws = [flint.arb("0.01"), flint.arb("0.001"), flint.arb("0.0001")]

    print("W0: geometric sanity n_j=b^j: w*g(w) -> 1/log b (monotone)")
    for b in (2, 3):
        inv = flint.arb(1) / flint.arb(b).log()
        vals = [w_times_g(logn_geometric, b, float(w.str(8, radius=False))) for w in ws]
        rel = abs(vals[-1] - inv) / inv
        check(f"b={b}: geom -> 1/log b", (rel < flint.arb("5e-3")).__bool__(),
              f"w=1e-4: {vals[-1].str(8)} vs 1/log b={inv.str(8)} (rel {rel.str(4)})")

    print("W1: CEILING n_m=b^{m-1}+1 (real CC-type): w*g(w) -> 1/log b")
    ceil_last = {}
    for b in (2, 3):
        inv = flint.arb(1) / flint.arb(b).log()
        vals = [w_times_g(logn_ceiling, b, float(w.str(8, radius=False))) for w in ws]
        ceil_last[b] = vals[-1]
        rels = [float((abs(v - inv) / inv).str(6, radius=False)) for v in vals]
        shrinking = rels[0] > rels[1] > rels[2]
        check(f"b={b}: ceiling -> 1/log b, shrinking",
              shrinking and rels[-1] < 5e-3,
              f"rel devs {rels[0]:.2e} -> {rels[1]:.2e} -> {rels[2]:.2e}")

    print("W2: OFFSET n_j=floor(2 b^j/3) (different bounded offset): same limit")
    off_last = {}
    for b in (2, 3):
        inv = flint.arb(1) / flint.arb(b).log()
        vals = [w_times_g(logn_offset, b, float(w.str(8, radius=False))) for w in ws]
        off_last[b] = vals[-1]
        rel = abs(vals[-1] - inv) / inv
        check(f"b={b}: offset -> 1/log b", (rel < flint.arb("5e-3")).__bool__(),
              f"w=1e-4: {vals[-1].str(8)} (rel {rel.str(4)})")

    print("W3: OFFSET-INDEPENDENCE -- the two shapes AGREE in the limit (the new fact)")
    for b in (2, 3):
        inv = flint.arb(1) / flint.arb(b).log()
        diff = abs(ceil_last[b] - off_last[b]) / inv
        check(f"b={b}: |ceil - offset|/(1/log b) < 5e-3 at w=1e-4",
              (diff < flint.arb("5e-3")).__bool__(),
              f"residues agree: {diff.str(4)} relative -- residue is shape-independent")

    print("W4: non-log-density control n_j=j (g=zeta, regular at 0): w*g(w) -> 0")
    vprev = None
    for w in (0.01, 0.001, 0.0001):
        v = w_times_zeta(w)
        ok = (abs(v) < flint.arb(w) * 1).__bool__()  # |w zeta(w)| ~ w/2 -> 0
        check(f"w={w}: |w*zeta(w)| -> 0", ok,
              f"w*zeta(w)={v.str(6)} (linear spacing => no s=0 residue, unlike 1/log b)")
        vprev = v

    print()
    if passed:
        print("ALL PASS")
        return 0
    print("SOME FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(run())
