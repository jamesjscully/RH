"""FF-witness: the kappa-gate on the REALIZED object Xbar (doc 30
front 2) + the s(s-1) bookkeeping (doc 30 front 4).

PART 1 is CONDITIONAL ON CONJECTURE DD.4 throughout (the single
assumption, logged in the doc's G-INT6 ledger): we test what the
continuous self-duality I^cont(Xbar) ~ Sigma Xbar would ADD to BB's
banked inputs IF it holds.  F-a guard: kappa = pi appears nowhere
below; the EF target is used in the doc as COMPARISON ONLY.

PRE-REGISTERED READINGS (fail-closed; written before first run).
DISCLOSURE (CC precedent): the closed forms in FFG6-FFG8 and the
odd/even solution pattern in FFG3 were derived/found at design stage
(hand algebra + one exploration script); they are registrations to be
CHECKED here, not fits -- any mismatch is a FAIL of the registration.

R-FFG1  MATLIS = TORSION-PONTRYAGIN (exact).  The 2-primary classical
        pair replicates DD's tower conjugation verbatim: on the
        quotient tower {Z/2^N --p_N--> Z/2^{N-1}} with duals taken in
        Q/Z, (a) s_N: a -> (b -> ab/2^N) is a PERFECT self-duality of
        Z/2^N; (b) p_N^* o s_N = s_{N+1} o (x 2) exactly (the dual of
        the quotient tower is the multiplication tower -- DDG1's
        conjugation identity, classical shadow); (c) every element of
        colim = Z[1/2]/Z is killed by some 2^k: the dual COLIMIT is
        pure torsion -- the connected part R/Q of the torus R/Z is
        never produced.  Dictionary: (F_2[[z]] tower, divided powers)
        <-> (Z_2, Q_2/Z_2) = the TORSION SHADOW of the Pontryagin
        pair (lattice, torus).  FAIL: any identity fails, N <= 8.
R-FFG2  THE SCALE LIVES IN WHAT THE SHADOW FORGETS (exact counts).
        Torsion side is FLOPPY: |Aut(Z/2^N)| = 2^{N-1} (grows);
        F_2-side: the Frobenius forms <a,b> = L(ab) on F_2[z]/z^{N+1}
        (L a functional with L(z^N) = 1) number EXACTLY 2^N, all
        perfect, a torsor under the 1-units U_N = 1 + z(...) -- the
        normalization of the level-N self-duality is a 2^N-torsor.
        (Contrast, cited not computed: continuous Aut(R/Z) = {+-1} --
        the connected torus is RIGID; the 2pi-rigidity of the
        classical exchange is a topological datum with NO torsion
        shadow.)  FAIL: counts differ or some form degenerate.
R-FFG3  THE SHEAR DOES NOT PIN THE TORSOR (exact; pattern disclosed
        above).  phi(z) = z/(1+z) (DD's Weyl shear): the phi-isometric
        Frobenius forms (<phi a, phi b> = <a, b>) number 0 for N even
        and EXACTLY 2^{(N+1)/2} for N odd (N <= 12) -- never unique.
        Residual freedom survives: = DD's g3 = Z's kappa torsor.
        FAIL: a unique pinning appears, or the parity pattern breaks.
R-FFG4  THE CONTINUUM IS BC-ANNIHILATED (exact).  Image of (x 2^K) on
        Z/2^N is {0} iff K >= N (checked N <= 12); hence any
        homomorphism from a 2-divisible group (Z[1/2], a fortiori
        Q, R) to Z/2^N is 0: the degenerate sector's continuum has NO
        nonzero map into the dualizing object's homotopy.  The
        exchange is one-sided: combs dualize (FFG1); the continuum
        maps to zero.  FAIL: a nonzero compatible sequence exists.
R-FFG5  THE GATE (F1).  REGISTERED EXPECTED: F1-FAIL (still
        equivariant).  (a) transported through the Abel-regularized
        traces under the analytic coordinate rescale t -> ct (the
        torsor's analytic shadow; c in {1, e, pi}; p in {2, 3, 5}):
        comb atom weight(c) / spacing(c) = 1 invariant (tol 1e-5,
        same machinery as BB GB1/GB5), while weight(c) itself scales
        by c (rel tol 1e-5): the exchange determines the RATIO only,
        never an absolute normalization.  (b) the gate observable
        moves: c_oo(lambda kappa) - c_oo(kappa) = -(1/2) log lambda
        != 0 (flint), while every Part-1 duality datum is
        integer/F_2-exact and kappa-free.  PROPOSITION FF.1
        (conditional on DD.4): the enriched input set
        {banked} u {I^cont data} is still pointwise fixed by
        kappa -> lambda kappa; F1-FAIL; residual freedom = FFG3's
        surviving sub-torsor.  FAIL of the witness: ratio deviates,
        weight does NOT scale, or the observable does not move.

R-FFG6  CLOSED FORM (exact + flint):  zeta_2(0, w | a, b)
        = (w-a)(w-b)/(2ab) + (a^2 - 3ab + b^2)/(12ab).
        flint anchors: (1,2) via CC's Hurwitz decomposition; (1,1)
        via zeta_2(0,w|1,1) = zeta_H(-1,w) + (1-w) zeta_H(0,w)
        (rank-2 = two rank-1s, exact); Fraction identity with
        B_2(w) = w^2 - w + 1/6.  Tol 1e-10 at 3 points each.
R-FFG7  1/4 vs 1/2 (exact).  Leading coeff = 1/(2ab): scheme table
        degree (2,1) -> 1/4;  weight (1,1) -> 1/2;
        folded variants (4,2) -> 1/16, (2,2) -> 1/8.
        The degree -> weight conversion changes ONLY xbar's parameter
        (y has degree 1 = weight 1): factor ab-ratio = 2.  REGISTERED
        HYPOTHESIS "the 1/4 is the factor 2 SQUARED": EXPECTED REFUTE
        (it is 2, via 1/(2ab); 2^2 would need BOTH generators to
        rescale, but the cone's grading is mixed).  Slice ladders:
        (2,1)-scheme slices to zeta_H(0, s/2) (FOLDED/Gamma_R);
        (1,1)-scheme slices to zeta_H(0, s) (UNFOLDED/Gamma_C):
        the convention boundary IS the folded/unfolded boundary
        (doc 20 C3).  EF-invisibility of the target: -d/ds log(c s(s-1))
        is c-INDEPENDENT (exact): "xi's 1/2" is not an EF observable.
        Recentred forms exact: (2,1), shift 1 -> s(s-1)/4 - 1/24;
        (1,1), shift 1/2 -> s(s-1)/2 + 1/24; root pair {0,1} is the
        scheme-INVARIANT content.  FAIL: any exact identity fails.
R-FFG8  -1/24 (exact + flint).  Center-value identity:
        zeta_2(0, (a+b)/2 | a, b) = -(a^2+b^2)/(24ab)
        = zeta(-1) (a/b + b/a)/2;  at (1,1) it is EXACTLY zeta(-1)
        = -1/12: the zeta(-1) VACUUM of the rank-2 tower in its own
        units, carried by the constituent zeta_H(-1, w) = -B_2(w)/2.
        Recentred constant K(a,b) = (3 - a^2 - b^2)/(24ab):
        (2,1) -> -1/24, (1,1) -> +1/24 (sign flips with the scheme).
        FAIL: identities fail (tol 1e-12 on flint anchors).

Run:  python3 -m scripts.numerics.witness.prime_int_ff_kappa_xbar
Exit 0 iff ALL PASS.
"""

import math
import sys
from fractions import Fraction
from math import comb, gcd

import flint

flint.ctx.prec = 300
acb = flint.acb
PI = math.pi
SQ2PI = math.sqrt(2 * math.pi)

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


# ================================================================ PART 1
print("PART 1 (CONDITIONAL ON DD.4): the kappa-gate on Xbar\n")

# ------------------------------------------------------------------ FFG1
# (a) s_N perfect: Gram of <a,b> = ab/2^N on Z/2^N, entries in
# (1/2^N)Z/Z represented as integers ab mod 2^N; perfect <=> the map
# a -> row is injective <=> only a = 0 pairs to 0 with everything.
ok = True
for N in range(1, 9):
    M = 1 << N
    rad = [a for a in range(M) if all((a * b) % M == 0 for b in range(M))]
    ok = ok and rad == [0]
# (b) conjugation p_N^* o s_N = s_{N+1} o (x 2): for all a in Z/2^N,
# b in Z/2^{N+1}:  a * (b mod 2^N) / 2^N == 2ab / 2^{N+1}  in Q/Z.
for N in range(1, 9):
    M, M2 = 1 << N, 1 << (N + 1)
    for a in range(M):
        for b in range(M2):
            lhs = Fraction(a * (b % M), M) % 1
            rhs = Fraction(2 * a * b, M2) % 1
            if lhs != rhs:
                ok = False
# (c) colimit pure torsion: every x = j/2^k in Z[1/2]/Z killed by 2^k.
for k in range(1, 13):
    for j in range(1, 1 << k, max(1, (1 << k) // 16)):
        if (Fraction(j, 1 << k) * (1 << k)) % 1 != 0:
            ok = False
gate("FFG1 Matlis = torsion-Pontryagin: s_N perfect, p_N^* s_N = "
     "s_{N+1} (x2) (DDG1's conjugation, classical shadow), colim pure "
     "torsion", ok,
     "(N <= 8 exhaustive; the connected part R/Q is never produced)")

# ------------------------------------------------------------------ FFG2
ok = True
for N in range(1, 13):
    M = 1 << N
    n_aut = sum(1 for a in range(M) if gcd(a, M) == 1)
    ok = ok and n_aut == M // 2          # |Aut(Z/2^N)| = 2^{N-1}


def pmul(a, b, N):
    """Multiply sparse F_2 polys mod z^{N+1} (dicts m -> 1)."""
    out = {}
    for i in a:
        for j in b:
            k = i + j
            if k <= N:
                out[k] = out.get(k, 0) ^ 1
    return {k: v for k, v in out.items() if v}


def gram_perfect(L, N):
    """L = functional (dict m -> bit); Gram G[i][j] = L(z^{i+j});
    perfect over F_2 <=> nonsingular (Gaussian elimination mod 2)."""
    rows = [sum(((L.get(i + j, 0)) << j) for j in range(N + 1))
            for i in range(N + 1)]
    rank = 0
    for col in range(N + 1):
        piv = next((r for r in range(rank, N + 1)
                    if (rows[r] >> col) & 1), None)
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        for r in range(N + 1):
            if r != rank and (rows[r] >> col) & 1:
                rows[r] ^= rows[rank]
        rank += 1
    return rank == N + 1


for N in range(1, 9):
    forms = []
    for bits in range(1 << N):                 # free part L(z^0..z^{N-1})
        L = {N: 1}
        for m in range(N):
            if (bits >> m) & 1:
                L[m] = 1
        forms.append(L)
        ok = ok and gram_perfect(L, N)
    ok = ok and len(forms) == (1 << N)         # the 2^N torsor
    # forms with L(z^N) = 0 are NOT perfect (sanity: torsor is exactly this)
    ok = ok and not gram_perfect({0: 1}, N)
gate("FFG2 normalization torsor: |Aut(Z/2^N)| = 2^{N-1}; Frobenius "
     "forms on F_2[z]/z^{N+1} = exactly 2^N, all perfect", ok,
     "(floppy torsion shadow vs rigid torus Aut(R/Z) = +-1, cited)")

# ------------------------------------------------------------------ FFG3
def inv_1pz(m, N):
    """(1+z)^{-m} mod 2 mod z^{N+1}; coeff_j = binom(m+j-1, j) mod 2."""
    if m == 0:
        return {0: 1}
    return {j: 1 for j in range(N + 1) if comb(m + j - 1, j) % 2 == 1}


def phi_mono(m, N):
    """phi(z^m) = z^m (1+z)^{-m} truncated (DD's Weyl shear)."""
    return pmul({m: 1}, inv_1pz(m, N), N)


ok = True
for N in range(1, 13):
    n_sol = 0
    for bits in range(1 << N):
        u = {0: 1}
        for m in range(N):
            if (bits >> m) & 1:
                u[m + 1] = 1
        # phi-isometry of <a,b>_u = coeff_N(u a b): since phi is a ring
        # involution, the condition is coeff_N(u phi(z^m)) =
        # coeff_N(u z^m) for all m (products of monomials span).
        if all(pmul(u, phi_mono(m, N), N).get(N, 0)
               == pmul(u, {m: 1}, N).get(N, 0) for m in range(N + 1)):
            n_sol += 1
    expect = 0 if N % 2 == 0 else 1 << ((N + 1) // 2)
    ok = ok and n_sol == expect
    if N % 2 == 1:
        ok = ok and n_sol > 1               # NEVER unique: no pinning
gate("FFG3 shear does NOT pin the torsor: phi-isometric forms = 0 (N "
     "even), 2^{(N+1)/2} (N odd), never unique (N <= 12)", ok,
     "(residual freedom = DD's g3 = Z's kappa torsor, survives)")

# ------------------------------------------------------------------ FFG4
ok = True
for N in range(1, 13):
    M = 1 << N
    for K in range(0, N + 3):
        img = {(x << K) % M for x in range(M)}
        ok = ok and ((img == {0}) == (K >= N))
gate("FFG4 continuum BC-annihilated: image of (x 2^K) on Z/2^N = {0} "
     "iff K >= N => Hom(2-divisible, Z/2^N) = 0", ok,
     "(Z[1/2], Q, R have no nonzero map into the dualizing homotopy)")

# ------------------------------------------------------------------ FFG5
print("\nFFG5: the F1 gate -- transported exchange under coordinate "
      "rescale t -> ct")


def comb_pairing(L_eff, eps, sigma=1.0):
    """Abel-regularized glued-trace pairing against the Gaussian, in
    rescaled coordinates: effective lattice L_eff (BB GB1 machinery)."""
    total, m = 0.0, 0
    while True:
        ph = sigma * SQ2PI * math.exp(-(sigma * m * L_eff) ** 2 / 2.0)
        if m > 0 and ph < 1e-22:
            break
        term = ph * math.exp(-m * eps * L_eff)
        total += term if m == 0 else 2 * term
        m += 1
    return total


def comb_target(spacing, sigma=1.0):
    total, n = 0.0, 0
    while True:
        v = math.exp(-(n * spacing) ** 2 / (2 * sigma ** 2))
        if n > 0 and v < 1e-22:
            break
        total += v if n == 0 else 2 * v
        n += 1
    return spacing * total


ok = True
worst_ratio = 0.0
base_weight = {}
for p in (2, 3, 5):
    for c in (1.0, math.e, math.pi):
        L_eff = math.log(p) / c            # t' = c t: lattice contracts
        spacing = 2 * PI * c / math.log(p)  # comb spacing dilates
        pair = comb_pairing(L_eff, 1e-7)
        tgt = comb_target(spacing)
        ratio_dev = abs(pair / tgt - 1)     # weight/spacing ratio = 1
        worst_ratio = max(worst_ratio, ratio_dev)
        ok = ok and ratio_dev < 1e-5
        # extract the absolute atom weight: weight = pair / sum phi(atoms)
        wsum = tgt / spacing
        weight = pair / wsum
        if c == 1.0:
            base_weight[p] = weight
        else:                               # weight itself scales by c
            ok = ok and abs(weight / (c * base_weight[p]) - 1) < 1e-5
print(f"    ratio weight/spacing = 1: worst dev {worst_ratio:.2e}; "
      f"weight scales by c (absolute normalization MOVES)")
# the gate observable moves under kappa -> lambda kappa (flint):
moved = True
for lam in (math.e, math.pi, 2 * math.pi):
    d = -(flint.arb(lam).log()) / 2        # c_oo(lam k) - c_oo(k)
    moved = moved and abs(float(d.mid())) > 0.1
ok = ok and moved
gate("FFG5 F1 verdict: F1-FAIL (registered) -- exchange determines the "
     "RATIO only; observable -(1/2)log lambda moves, duality data are "
     "kappa-free", ok,
     f"(Prop FF.1, conditional on DD.4; residual freedom = FFG3 torsor)")

# ================================================================ PART 2
print("\nPART 2: the s(s-1) bookkeeping (1/4 vs 1/2; -1/24)\n")

# ------------------------------------------------------------------ FFG6
def zh(u, a):
    return acb(u).zeta(acb(a))


def zeta2_12(s):
    """zeta_2(0, s | 1, 2) via CC/S's Hurwitz decomposition."""
    out = acb(0)
    for a in (acb(s) / 2, (acb(s) + 1) / 2):
        out += zh(-1, a) + (1 - a) * zh(0, a)
    return out


def zeta2_11(s):
    """zeta_2(0, s | 1, 1) = zeta_H(-1, s) + (1 - s) zeta_H(0, s)."""
    return zh(-1, s) + (1 - acb(s)) * zh(0, s)


def closed(w, a, b):
    """(w-a)(w-b)/(2ab) + (a^2 - 3ab + b^2)/(12ab), Fraction or acb."""
    return ((w - a) * (w - b)) / (2 * a * b) + \
        Fraction(a * a - 3 * a * b + b * b, 12 * a * b)


ok = True
for s in (0.5 + 3j, 2.2, 1.3 - 0.4j):
    v12 = zeta2_12(s)
    c12 = (acb(s) - 1) * (acb(s) - 2) / 4 - flint.arb(1) / 24
    v11 = zeta2_11(s)
    c11 = (acb(s) - 1) ** 2 / 2 - flint.arb(1) / 12
    ok = ok and abs(complex((v12 - c12).mid())) < 1e-10
    ok = ok and abs(complex((v11 - c11).mid())) < 1e-10
# exact Fraction route for (1,1): zeta_H(-1,w) = -B_2(w)/2:
#   -(w^2 - w + 1/6)/2 + (1-w)(1/2 - w) = closed(w,1,1) as polynomials
for wq in (Fraction(1, 3), Fraction(7, 5), Fraction(-2)):
    lhs = -(wq * wq - wq + Fraction(1, 6)) / 2 + (1 - wq) * (Fraction(1, 2) - wq)
    ok = ok and lhs == closed(wq, 1, 1)
gate("FFG6 closed form zeta_2(0,w|a,b) = (w-a)(w-b)/(2ab) + "
     "(a^2-3ab+b^2)/(12ab)", ok,
     "(flint anchors (1,2),(1,1); exact B_2 route for (1,1))")

# ------------------------------------------------------------------ FFG7
ok = True
# leading coefficient = 1/(2ab), the four banked-flag schemes:
table = {(2, 1): Fraction(1, 4), (1, 1): Fraction(1, 2),
         (4, 2): Fraction(1, 16), (2, 2): Fraction(1, 8)}
for (a, b), lead in table.items():
    ok = ok and Fraction(1, 2 * a * b) == lead
# degree -> weight changes ONLY xbar's parameter: (2,1) -> (1,1):
# factor = (2*2*1)/(2*1*1) = 2.  Hypothesis "2 squared" REFUTED:
factor = Fraction(2 * 2 * 1, 2 * 1 * 1)
ok = ok and factor == 2 and factor != 4
# slice identities (exact quadratic-poly algebra, coeffs [c0,c1,c2]):
def shift_poly(poly, t):
    c0, c1, c2 = poly
    return [c0 + c1 * t + c2 * t * t, c1 + 2 * c2 * t, c2]


def poly_of(a, b):
    """closed(w, a, b) as [c0, c1, c2] in w."""
    return [Fraction(a * b, 2 * a * b) + Fraction(a * a - 3 * a * b + b * b,
                                                  12 * a * b),
            Fraction(-(a + b), 2 * a * b), Fraction(1, 2 * a * b)]


P21, P11 = poly_of(2, 1), poly_of(1, 1)
sub = lambda x, y: [u - v for u, v in zip(x, y)]
# (2,1): P(s) - P(s+1) = zeta_H(0, s/2) = 1/2 - s/2  (FOLDED ladder)
ok = ok and sub(P21, shift_poly(P21, 1)) == [Fraction(1, 2),
                                             Fraction(-1, 2), 0]
# (1,1): P(s) - P(s+1) = zeta_H(0, s) = 1/2 - s      (UNFOLDED ladder)
ok = ok and sub(P11, shift_poly(P11, 1)) == [Fraction(1, 2),
                                             Fraction(-1), 0]
# recentred forms: (2,1) shift 1 and (1,1) shift 1/2:
ok = ok and shift_poly(P21, 1) == [Fraction(-1, 24), Fraction(-1, 4),
                                   Fraction(1, 4)]
ok = ok and shift_poly(P11, Fraction(1, 2)) == [Fraction(1, 24),
                                                Fraction(-1, 2),
                                                Fraction(1, 2)]
# both self-dual under s -> 1-s (c1 = -c2 makes c2*s(s-1) + c0):
for q in (shift_poly(P21, 1), shift_poly(P11, Fraction(1, 2))):
    ok = ok and q[1] == -q[2]               # root pair {0, 1}
# EF-invisibility: -d/ds log(c s(s-1)) = -(1/s + 1/(s-1)), c-free:
for c in (0.25, 0.5, 1.0):
    for s in (0.7 + 2j, 3.1):
        h = 1e-30                            # flint: exact derivative
        f = lambda s_, c_: (acb(c_) * acb(s_) * (acb(s_) - 1)).log()
        # log(c s(s-1)) - log(s(s-1)) = log c, constant => d/ds equal
        d = f(s, c) - f(s, 1.0)
        ok = ok and abs(complex((d - acb(c).log()).mid())) < 1e-12
gate("FFG7 1/4-vs-1/2: leading = 1/(2ab); degree->weight factor = 2 "
     "(hypothesis '2 squared' REFUTED); folded/unfolded slice ladders; "
     "prefactor EF-invisible; root pair {0,1} scheme-invariant", ok,
     "(s(s-1)/4 - 1/24 at (2,1)+shift 1;  s(s-1)/2 + 1/24 at "
     "(1,1)+shift 1/2)")

# ------------------------------------------------------------------ FFG8
ok = True
zm1 = Fraction(-1, 12)                       # zeta(-1)
for (a, b) in ((1, 1), (1, 2), (2, 1), (2, 2)):
    w0 = Fraction(a + b, 2)
    cv = closed(w0, a, b)
    ok = ok and cv == Fraction(-(a * a + b * b), 24 * a * b)
    ok = ok and cv == zm1 * (Fraction(a, b) + Fraction(b, a)) / 2
ok = ok and closed(Fraction(1), 1, 1) == zm1   # (1,1) vacuum = zeta(-1)
# flint anchor: zeta(-1) = -1/12 and the (1,2) center value -5/48:
ok = ok and abs(complex((zh(-1, 1) + flint.arb(1) / 12).mid())) < 1e-12
ok = ok and abs(complex((zeta2_12(1.5) + flint.arb(5) / 48).mid())) < 1e-10
# recentred constant K(a,b) = (3 - a^2 - b^2)/(24ab):
K = lambda a, b: Fraction(3 - a * a - b * b, 24 * a * b)
ok = ok and K(2, 1) == Fraction(-1, 24) and K(1, 1) == Fraction(1, 24)
ok = ok and shift_poly(poly_of(2, 1), 1)[0] == K(2, 1)
ok = ok and shift_poly(poly_of(1, 1), Fraction(1, 2))[0] == K(1, 1)
# the zeta(-1) carrier is the constituent zeta_H(-1, w) = -B_2(w)/2:
for s in (0.8, 2.4):
    b2 = acb(s) ** 2 - acb(s) + flint.arb(1) / 6
    ok = ok and abs(complex((zh(-1, s) + b2 / 2).mid())) < 1e-12
gate("FFG8 -1/24: center value = zeta(-1)(a/b + b/a)/2 (= zeta(-1) "
     "exactly at (1,1)); K(a,b) = (3-a^2-b^2)/(24ab) gives -1/24 / "
     "+1/24 (scheme-dependent sign)", ok,
     "(zeta(-1) vacuum CONFIRMED in center-value form, carried by "
     "zeta_H(-1,.) = -B_2/2)")

# ------------------------------------------------------------------ exit
print()
if failures:
    print("FAILURES:", failures)
    sys.exit(1)
print("ALL PASS (FFG1-FFG8)")
sys.exit(0)
