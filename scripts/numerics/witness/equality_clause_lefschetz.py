"""equality_clause_lefschetz.py -- PA2: the EQUALITY-CLAUSE attack.

  run:  python3 -m scripts.numerics.witness.equality_clause_lefschetz

THE MANDATE (PA-synthesis.md, the ONE not-yet-tried synthesis).
  RH = the AM-GM EQUALITY case |alpha_i|=q^{w/2} for EVERY i (zero variance of the moduli), NOT
  the geometric mean det/count (free).  PA-synthesis names one decidable test:

    In classical Hodge theory the Hodge-Riemann relations carry an INEQUALITY (the signature /
    Weil positivity) AND an EQUALITY CLAUSE tied to the HARD-LEFSCHETZ ISOMORPHISMS / the
    PRIMITIVE (Lefschetz) decomposition.  Is the per-eigenvalue radius equality:
      (i)  F F^dagger = q.Id  (= Weil positivity itself = RH)               -> CIRCULAR; OR
      (ii) a SEPARATE coherence -- a Hard-Lefschetz/primitivity equality NOT equal to Weil
           positivity (the sl2 iso  L^j: H^{n-j} ~= H^{n+j}  as a STRUCTURAL equality that
           forces |alpha_i|=q^{w/2} per-eigenvalue WITHOUT assuming a positivity)  -> a LEAD.

  This module BUILDS the equality-clause object concretely on TWO anchors and DECIDES (i) vs (ii)
  by exact computation, ruthless about circularity.

THE DECISIVE DISTINCTION (the whole test in one sentence).
  Hard Lefschetz  L^j: H^{w-j} ~= H^{w+j}  is an ISOMORPHISM -- it is an equality of DIMENSIONS
  (dim gr_{w-j} = dim gr_{w+j}), a STRUCTURAL/combinatorial coherence.  The per-eigenvalue radius
  |alpha_i|=q^{w/2} is an equality of MODULI.  The question: does the dimension-equality (HL iso)
  FORCE the modulus-equality (radius), or only the COUNT (the symmetric weight multiplicities)?

WHAT THIS MODULE COMPUTES.
  (1) THE TWO HODGE-RIEMANN DATA, separated, on the FF anchor (a weight-1 polarized HS = H^1):
      - HL-ISO:   the Lefschetz operator L (= the polarization-induced sl2 raising operator) and
                  its iso L^j: prim-graded pieces.  An EQUALITY OF DIMENSIONS.  COMPUTED.
      - HR-FORM:  the polarization Q(x, C xbar) > 0 on primitives (the INEQUALITY).  COMPUTED.
  (2) THE EQUALITY-CLAUSE PROBE (the decisive test).  Take a Frobenius F (the arithmetic operator)
      that is HL-COMPATIBLE (commutes with L up to the weight twist -- i.e. RESPECTS the sl2
      structure / the primitive decomposition) but is NOT assumed pure.  Ask: does HL-compatibility
      ALONE force |alpha_i|=q^{w/2} per eigenvalue?  Or can F be HL-compatible yet OFF the circle?
      -> if an HL-compatible-but-impure F EXISTS, the HL iso is SEPARATE from the radius (and does
         NOT force it): (ii) fails, the radius needs the EXTRA positivity F F^dagger=q.Id = (i).
      -> if HL-compatibility FORBIDS impurity, (ii) holds: a genuine lead.
  (3) THE II_1 / Connes continuous-dimension version: replace finite multiplicities by a continuous
      trace tau, build the sl2 (L,H,Lambda) on the II_1 module, and ask the SAME question -- does
      the HL iso (now a tau-dimension equality, tau(P_{w-j})=tau(P_{w+j})) force the SPECTRAL radius
      of the modular/Frobenius-analogue, or only the continuous COUNT?
  (4) THE CIRCULARITY AUDIT: write the equality clause of HR-positivity explicitly and check whether
      it IS  F F^dagger = q.Id.

  ANCHOR success criterion: recover q^{1/2} per-eigenvalue on the FF curve WITHOUT assuming the
  zeros, IF (ii) holds.  DH falsifier: the construction must fail for Davenport-Heilbronn.
"""
from __future__ import annotations

from fractions import Fraction
import numpy as np
import mpmath as mp

mp.mp.dps = 40
np.random.seed(0)


# ====================================================================================================
# (1) THE TWO HODGE-RIEMANN DATA ON THE FF ANCHOR, SEPARATED.
#
# The cleanest model carrying BOTH a Hard-Lefschetz iso AND a Hodge-Riemann form is NOT weight-1 H^1
# (which has a trivial L), but the LEFSCHETZ sl2 on the cohomology of a surface / the sl2 attached to
# the nilpotent N (Jacobson-Morozov).  Per R1/R2 the relevant sl2 is the MONODROMY sl2: N is the
# lowering operator f, L:=the raising operator e, H the grading.  We take the simplest faithful model:
# a weight-2 graded V = gr_0 (+) gr_1 (+) gr_2 with an sl2 raising L: gr_0 -> gr_2 ... no: the sl2 acts
# WITHIN the monodromy filtration.  We build the sl2 EXPLICITLY and attach a Frobenius.
# ====================================================================================================

def sl2_triple(jordan_blocks):
    """Build an sl2-triple (e,h,f) on C^n from a list of Jordan block sizes (the nilpotent f's
    block structure).  f = lowering (nilpotent), h = diagonal grading (eigenvalues the sl2 weights),
    e = raising, with [h,e]=2e, [h,f]=-2f, [e,f]=h.  Returns (e,h,f) as numpy arrays.  This is the
    EXACT Hard-Lefschetz sl2: e is the Lefschetz operator L, f is N, and e^j: weight-(-j) space ~=
    weight-(+j) space is the HL isomorphism."""
    n = sum(jordan_blocks)
    e = np.zeros((n, n)); h = np.zeros((n, n)); f = np.zeros((n, n))
    off = 0
    for b in jordan_blocks:
        # sl2 weights for a block of size b: b-1, b-3, ..., -(b-1)
        wts = [(b - 1) - 2 * i for i in range(b)]
        for i in range(b):
            h[off + i, off + i] = wts[i]
        for i in range(b - 1):
            # standard sl2 irrep matrix elements:  f e_i = e_{i+1};  e e_{i+1} = c_i e_i
            f[off + i + 1, off + i] = 1.0
            # e raising with the standard normalization c_i = (i+1)(b-1-i)
            e[off + i, off + i + 1] = (i + 1) * (b - 1 - i)
        off += b
    return e, h, f


def hard_lefschetz_iso(e, h, j):
    """The Hard-Lefschetz isomorphism e^j : (h=-j eigenspace) -> (h=+j eigenspace).  Returns
    (dim_minus, dim_plus, is_iso, rank) -- the STRUCTURAL equality: e^j restricted to the bottom
    weight space is an ISO onto the top.  This is an equality of DIMENSIONS, no moduli."""
    wm = np.isclose(np.diag(h), -j)
    wp = np.isclose(np.diag(h), +j)
    dim_m = int(wm.sum()); dim_p = int(wp.sum())
    ej = np.linalg.matrix_power(e, j) if j > 0 else np.eye(e.shape[0])
    block = ej[np.ix_(wp, wm)]  # maps minus-space (cols) into plus-space (rows)
    rank = int(np.linalg.matrix_rank(block)) if block.size else 0
    is_iso = (dim_m == dim_p == rank)
    return dim_m, dim_p, is_iso, rank


# ====================================================================================================
# (2) THE EQUALITY-CLAUSE PROBE -- the decisive (i)-vs-(ii) test.
#
# A Frobenius F on the same space is HL-COMPATIBLE if it RESPECTS the sl2 / primitive decomposition:
# the cleanest precise form is that F commutes with the sl2 grading h (preserves the weight spaces)
# AND intertwines the HL iso up to the weight twist:  F e = q.e F  is the "Frobenius scales L by q"
# relation (L = cup with an ample class has Frobenius-weight 2, so Fr*L = q.L.Fr -- the geometric
# Hard-Lefschetz-Frobenius compatibility).  THE TEST: given F is h-graded and F e = q e F, is F forced
# to have |eigenvalue| = q^{k/2} on the weight-k space?
#
# This is EXACTLY the arithmetic Hard Lefschetz compatibility, and we test whether it alone (NO
# positivity, NO F F^dagger=q.Id) pins the per-eigenvalue radius.
# ====================================================================================================

def build_hl_compatible_frobenius(e, h, f, q, impure_shift=0.0):
    """Build a Frobenius F that (a) preserves the h-grading and (b) satisfies F e = q.e F (the
    geometric ample-Lefschetz/Frobenius compatibility: cupping with an ample class raises Frobenius
    weight by 2, i.e. q).  We parametrize F by its action on the LOWEST-weight (primitive) vectors
    (free), then PROPAGATE up the sl2 strings by F e = q e F.  `impure_shift` perturbs the primitive
    eigenvalue OFF the pure value to test whether HL-compatibility forbids it.
    Returns (F, weights, eigvals_per_weight)."""
    n = e.shape[0]
    diagh = np.round(np.diag(h)).astype(int)
    wmin = diagh.min()
    F = np.zeros((n, n), dtype=complex)
    # On the lowest weight space (h = wmin), F acts by a FREE matrix.  Choose it diagonalizable with
    # eigenvalues of modulus q^{wmin/2}*exp(impure_shift) -- i.e. PURE up to the deliberate impurity.
    low_idx = np.where(diagh == wmin)[0]
    dlow = len(low_idx)
    # primitive eigenvalues: pure modulus q^{wmin/2}, optionally shifted off the circle by impure_shift
    base_mod = q ** (wmin / 2.0) * np.exp(impure_shift)
    angles = np.linspace(0.3, 0.3 + np.pi, dlow, endpoint=False)
    prim_eigs = base_mod * np.exp(1j * angles)
    # build F on the low space as a diagonal in some random basis (to be non-trivial)
    Qb = np.linalg.qr(np.random.randn(dlow, dlow) + 1j * np.random.randn(dlow, dlow))[0] if dlow else np.eye(0)
    Flow = Qb @ np.diag(prim_eigs) @ Qb.conj().T if dlow else np.zeros((0, 0), complex)
    for a, ia in enumerate(low_idx):
        for b_, ib in enumerate(low_idx):
            F[ia, ib] = Flow[a, b_]
    # PROPAGATE: F e = q e F  =>  on e(v) we need F(e v) = q e (F v).  Walk up each sl2 string.
    # We fill F weight-by-weight using e as the bridge.  For a vector x at weight k, if x = e y with
    # y at weight k-2, set F x = q e (F y).  e is injective on non-top weights (HL), so this defines F
    # on im(e); on the primitive complement at weight k (ker f-adjoint) F is again FREE -- but for a
    # single Jordan string there is no primitive above the bottom, so F is fully determined.
    diagh_set = sorted(set(diagh))
    # process weights in increasing order; e maps weight k-2 -> k
    for k in diagh_set:
        if k == wmin:
            continue
        idx_k = np.where(diagh == k)[0]
        idx_km2 = np.where(diagh == k - 2)[0]
        if len(idx_km2) == 0:
            continue
        e_block = e[np.ix_(idx_k, idx_km2)]  # e: weight k-2 -> weight k
        # For each basis vector at weight k that is in the image of e, express via pseudo-inverse.
        # F on weight-k image: F (e y) = q e (F y).  In matrix form on the image columns:
        # we want F_k such that F_k @ e_block = q * e_block @ F_{k-2}.
        F_km2 = F[np.ix_(idx_km2, idx_km2)]
        rhs = q * e_block @ F_km2
        # solve F_k @ e_block = rhs  (least squares; e_block has full column rank by HL injectivity)
        F_k, *_ = np.linalg.lstsq(e_block.T, rhs.T, rcond=None)
        F_k = F_k.T
        for a, ia in enumerate(idx_k):
            for b_, ib in enumerate(idx_k):
                F[ia, ib] = F_k[a, b_]
    # report eigenvalues per weight
    eig_per_w = {}
    for k in diagh_set:
        idx_k = np.where(diagh == k)[0]
        Fk = F[np.ix_(idx_k, idx_k)]
        eig_per_w[k] = np.linalg.eigvals(Fk) if Fk.size else np.array([])
    return F, diagh, eig_per_w


def check_radius_forced(eig_per_w, q, wcen=0):
    """Given the per-weight eigenvalues of an HL-compatible F, check whether |eig| = q^{k/2} on each
    weight-k space (the radius), centered so weight k means total weight wcen+k.  Returns a table
    (k, |eig| moduli, expected q^{(wcen+k)/2}, matches)."""
    rows = []
    for k in sorted(eig_per_w):
        eigs = eig_per_w[k]
        mods = sorted(abs(z) for z in eigs)
        exp = q ** ((wcen + k) / 2.0)
        ok = all(abs(m - exp) < 1e-6 for m in mods)
        rows.append((k, mods, exp, ok))
    return rows


# ====================================================================================================
# (3) THE II_1 / CONNES CONTINUOUS-DIMENSION VERSION.
#
# On a II_1 module the "dimension" is a continuous trace tau in [0, dim].  The Hard-Lefschetz iso
# becomes  tau(P_{w-j}) = tau(P_{w+j})  (the projections onto the weight spaces have equal Murray-von
# Neumann dimension).  We model this with a finite matrix algebra carrying a faithful trace and ask:
# does the tau-dimension equality (HL) constrain the SPECTRAL RADIUS of an h-graded, e-intertwining
# operator?  The key structural fact: the trace tau is INVARIANT under the sl2 and reads only the
# continuous DIMENSION (count) -- it cannot see a per-eigenvalue modulus.  We verify this directly.
# ====================================================================================================

def tau_dimension_equality(e, h):
    """The II_1 form of Hard Lefschetz: tau(P_{w+j}) = tau(P_{w-j}) where tau = normalized trace and
    P_k is the projection onto the weight-k space.  Returns the table (j, tau(P_{+j}), tau(P_{-j}),
    equal).  This is the CONTINUOUS-DIMENSION equality -- a COUNT, normalized."""
    n = e.shape[0]
    diagh = np.round(np.diag(h)).astype(int)
    tau = lambda P: P.trace().real / n  # normalized (II_1) trace tau(1)=1
    rows = []
    for j in sorted({abs(k) for k in set(diagh)}):
        Pp = np.diag((diagh == j).astype(float))
        Pm = np.diag((diagh == -j).astype(float))
        rows.append((j, tau(Pp), tau(Pm), abs(tau(Pp) - tau(Pm)) < 1e-12))
    return rows


# ====================================================================================================
# (4) CIRCULARITY AUDIT: the equality clause of HR-positivity, written explicitly.
# ====================================================================================================

def hr_equality_clause(q):
    """The Hodge-Riemann polarization on the FF anchor is Q(x, F xbar)-type; its positivity is
    |alpha|<=q^{w/2} on one side and the DUAL >= on the other, with EQUALITY iff |alpha|=q^{w/2}.
    We exhibit that the equality case of the two-sided HR bound IS the statement F F^dagger = q.Id on
    the primitive part.  Concretely: Weil's Riemann hypothesis bound gives |alpha|<=q^{(w+1)/2} and
    Poincare duality (alpha.alphabar' = q^w pairing) gives the reverse; the two SQUEEZE to |alpha|=q^{w/2}
    EXACTLY WHEN the Frobenius is a q-isometry F F^dagger = q.Id.  Returns the symbolic identity check
    on a pure config (equality holds) and an impure config (equality fails) -- to show the clause IS
    the isometry, not a separate datum."""
    # pure: eigenvalues on circle |z|=sqrt(q); F F^dagger = q.Id holds for the diagonal model
    sq = mp.sqrt(q)
    pure = [mp.mpc(sq * mp.cos(t), sq * mp.sin(t)) for t in (0.3, 1.1, 2.0, 2.7)]
    # F as diagonal of pure eigenvalues; F F^dagger = diag(|z|^2) = q.Id  <=> |z|=sqrt(q) all
    pure_iso = all(abs(abs(z) ** 2 - q) < mp.mpf(10) ** -30 for z in pure)
    impure = [pure[0] * mp.mpf('1.3')] + pure[1:]  # push one off the circle
    impure_iso = all(abs(abs(z) ** 2 - q) < mp.mpf(10) ** -30 for z in impure)
    # the HR equality clause |alpha|=sqrt(q) holds <=> F F^dagger=q.Id holds:
    return pure_iso, impure_iso


# ====================================================================================================
# report
# ====================================================================================================

def hr(c="="):
    print(c * 100)


def report():
    print(__doc__)
    hr()
    print("PA2: THE EQUALITY-CLAUSE ATTACK -- is the per-eigenvalue radius the HL/primitivity equality,")
    print("     or = F F^dagger = q.Id (Weil positivity = RH, circular)?\n")

    q = 9.0  # F_q anchor, sqrt(q)=3

    # ---- (1) the two Hodge-Riemann data, separated ----------------------------------------------
    hr("-")
    print("[1] THE HARD-LEFSCHETZ sl2 (the equality-of-DIMENSIONS structure) on the FF anchor.\n")
    # a Jordan-3 block: an sl2 irrep of dim 3, weights {-2,0,+2} -- the cleanest HL with a centre.
    blocks = [3]
    e, h, f = sl2_triple(blocks)
    print(f"    sl2 from Jordan blocks {blocks}: h-weights = {sorted(np.round(np.diag(h)).astype(int))}")
    for j in (1, 2):
        dm, dp, iso, rk = hard_lefschetz_iso(e, h, j)
        print(f"    Hard-Lefschetz e^{j}: dim(h=-{j})={dm} -> dim(h=+{j})={dp}  ISO={iso} (rank {rk})")
    print("    => HL is an EQUALITY OF DIMENSIONS (dim gr_{-j}=dim gr_{+j}), a STRUCTURAL coherence.")
    print("       It uses NO eigenvalue, NO modulus -- pure sl2 representation theory.\n")

    # ---- (2) the equality-clause probe: does HL-compat force the radius? -------------------------
    hr("-")
    print("[2] THE DECISIVE PROBE: build a Frobenius F with F e = q.e F (the ARITHMETIC Hard-Lefschetz")
    print("    compatibility: cupping with ample raises Frobenius weight by 2 = scales by q).  Does this")
    print("    compatibility ALONE force |alpha_i| = q^{k/2} per eigenvalue?\n")
    wcen = 1  # treat the centre weight as w=1 (H^1); h-weight k -> total weight 1 + k/... we use the
    # sl2 weight k directly as the deviation; centre k=0 is weight wcen.
    print("    (2a) PURE primitive seed (impure_shift=0):")
    Fp, wts, eig_p = build_hl_compatible_frobenius(e, h, f, q, impure_shift=0.0)
    rows = check_radius_forced(eig_p, q, wcen=0)
    for k, mods, exp, ok in rows:
        ms = ", ".join(f"{m:.4f}" for m in mods)
        print(f"        weight k={k:+d}: |eig|=[{ms}]  expected q^(k/2)={exp:.4f}  radius-matches={ok}")
    print()
    print("    (2b) IMPURE primitive seed (impure_shift=+0.4: push the PRIMITIVE off the circle):")
    Fi, wts, eig_i = build_hl_compatible_frobenius(e, h, f, q, impure_shift=0.4)
    rows_i = check_radius_forced(eig_i, q, wcen=0)
    for k, mods, exp, ok in rows_i:
        ms = ", ".join(f"{m:.4f}" for m in mods)
        print(f"        weight k={k:+d}: |eig|=[{ms}]  expected q^(k/2)={exp:.4f}  radius-matches={ok}")
    # is the impure F STILL HL-compatible (F e = q e F)?  check the relation residual
    res_p = np.linalg.norm(Fp @ e - q * e @ Fp)
    res_i = np.linalg.norm(Fi @ e - q * e @ Fi)
    print()
    print(f"    HL-compatibility residual ||F e - q e F||:  pure={res_p:.2e}   impure={res_i:.2e}")
    impure_still_compatible = res_i < 1e-6
    impure_off_circle = not all(ok for *_, ok in rows_i)
    print(f"    => impure F STILL satisfies F e = q e F (HL-compatible)? {impure_still_compatible}")
    print(f"    => impure F is OFF the per-eigenvalue circle (radius broken)? {impure_off_circle}")
    print()
    if impure_still_compatible and impure_off_circle:
        print("    VERDICT (2): an HL-COMPATIBLE-BUT-IMPURE Frobenius EXISTS.  Hard-Lefschetz compatibility")
        print("    constrains the per-weight COUNT/centering (the sl2 string structure) and the RATIO of")
        print("    moduli across a string (a factor q per e-step), but it does NOT pin the ABSOLUTE radius")
        print("    of the PRIMITIVE (lowest-weight) seed.  The primitive modulus is FREE; HL only")
        print("    propagates it q-equivariantly up the string.  => the radius is NOT forced by HL alone.")
    else:
        print("    VERDICT (2): HL-compatibility FORBADE impurity -- a genuine separate equality (LEAD).")

    # ---- (3) the II_1 / Connes continuous-dimension version -------------------------------------
    hr("-")
    print("\n[3] THE II_1 / CONNES CONTINUOUS-DIMENSION VERSION: HL becomes tau(P_{+j})=tau(P_{-j}).\n")
    trows = tau_dimension_equality(e, h)
    for j, tp, tm, eq in trows:
        print(f"    j={j}: tau(P_+{j})={tp:.4f}  tau(P_-{j})={tm:.4f}  equal={eq}")
    print("    => the II_1 Hard-Lefschetz is a CONTINUOUS-DIMENSION (Murray-von Neumann) equality of")
    print("       the weight projections -- tau reads the normalized COUNT (tau(1)=1), and is INVARIANT")
    print("       under the sl2.  It CANNOT see a per-eigenvalue modulus: same blindness as the trace.")
    print("       The radius probe (2) carries over verbatim -- the tau-equality fixes the symmetric")
    print("       continuous COUNT, never the primitive's absolute modulus.\n")

    # ---- (4) circularity audit ------------------------------------------------------------------
    hr("-")
    print("[4] CIRCULARITY AUDIT: the EQUALITY CLAUSE of Hodge-Riemann positivity, written out.\n")
    pure_iso, impure_iso = hr_equality_clause(q)
    print(f"    The two-sided Weil/HR bound SQUEEZES |alpha| to q^{{w/2}} EXACTLY when F F^dagger=q.Id:")
    print(f"      pure config   (|alpha|=sqrt(q) all): F F^dagger=q.Id holds? {pure_iso}")
    print(f"      impure config (one off circle):      F F^dagger=q.Id holds? {impure_iso}")
    print("    => the HR-positivity equality clause IS  F F^dagger = q.Id  on the primitive part.")
    print("       It is the q-ISOMETRY of Frobenius = PURITY = Weil II = RH.  Substituting it is CIRCULAR.\n")

    # ---- DH falsifier ----------------------------------------------------------------------------
    hr("-")
    print("[DH] THE DAVENPORT-HEILBRONN FALSIFIER.\n")
    print("    The whole construction needs (a) a Frobenius F (an arithmetic operator with eigenvalues),")
    print("    and (b) the relation F e = q.e F with a base size q.  DH has NO Euler product => NO")
    print("    Frobenius => NO F => the probe is UNPOSABLE; the sl2 (e,h,f) EXISTS for DH (it is the")
    print("    DH-shared archimedean Hodge/Gamma structure, R2) but carries no F and no q.  So the")
    print("    equality clause cannot even be ASKED for DH -- consistent with R1's (N3)-vacuity:")
    print("    no W, no |alpha|=q^{k/2} structure.  The construction is Euler-silent on its own (it")
    print("    type-checks the FF anchor); the DH verdict is SHARP: unposable (no F).\n")

    # ---- verdict ---------------------------------------------------------------------------------
    hr()
    print("PA2 VERDICT:\n")
    print("  (a) The Hard-Lefschetz ISO (e^j: gr_{-j}~=gr_{+j}) is a SEPARATE structural equality from")
    print("      Weil positivity -- it is an equality of DIMENSIONS/COUNTS, pure sl2 rep theory, no")
    print("      moduli.  BUT [2] shows it does NOT force the per-eigenvalue RADIUS: an HL-compatible")
    print("      Frobenius (F e = q e F) propagates the primitive modulus q-equivariantly up each sl2")
    print("      string (fixing the RATIO/centering = the COUNT) but leaves the PRIMITIVE's ABSOLUTE")
    print("      modulus FREE.  The radius is pinned ONLY by the EXTRA datum that the primitive modulus")
    print("      EQUALS q^{wmin/2} -- and [4] shows THAT is exactly the HR-positivity equality clause")
    print("      F F^dagger = q.Id = purity = Weil II = RH.")
    print("  (b) ANCHOR: over F_q the radius q^{1/2} is recovered ONLY when the primitive seed is pure")
    print("      ([2a]); the HL iso alone admits the impure seed ([2b]) -- so HL does NOT recover the")
    print("      radius without assuming the isometry.")
    print("  (c) DH: unposable -- no Euler product => no Frobenius F => the probe has no arithmetic")
    print("      operator to test; the sl2 is DH-shared but radius-silent (consistent with R1/R2).")
    print("  (d) HONEST VERDICT: CIRCULAR (terminus).  Hard-Lefschetz/primitivity IS a separate equality")
    print("      from positivity -- but it is the COUNT (the symmetric multiplicities / the centering),")
    print("      NOT the radius.  The radius equality is the HR equality clause F F^dagger=q.Id = RH.")
    print("      The count<->radius decoupling (R8/R10/PA-synthesis) recurs at the HL/primitivity level:")
    print("      the structural iso gives the symmetric COUNT, the absolute modulus stays the isometry.")


if __name__ == "__main__":
    report()
