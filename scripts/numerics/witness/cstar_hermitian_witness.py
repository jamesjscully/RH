"""cstar_hermitian_witness.py -- candidate 3 / NO-GO COMPLETION (2026-06-06).

THE QUESTION. Candidate 2 proved off-line F generates a CONSISTENT non-polarizable rigid
Tannakian category: rigid self-duality F.F-dagger=[deg] holds off-line too (Step A free, radius
not forced). Candidate 3's escape: demand a HERMITIAN self-duality -- a *-autonomous / dagger /
C*-tensor category with a conjugate-linear dualizing structure -- where the duality pairing is a
POSITIVE Hermitian form BY AXIOM. Doplicher-Roberts: a symmetric *C*-tensor* category with
conjugates reconstructs a COMPACT group. So "compactness from the duality" is a real theorem.

THE DECISIVE TEST (build it, do not assume it):
  Take an off-line semisimple F on V=C^d with |eig|=r (r != sqrt q).
  (A) Does F admit a *-structure / Hermitian self-duality (an anti-involution / Weil form,
      non-degenerate conjugate-linear pairing g with F-dagger = g-adjoint)? -- the *-autonomous /
      Hermitian level, conjugate-linear.
  (B) Is that g POSITIVE-DEFINITE (the C* / dagger / polarization axiom: Tr(u u^dagger)>0,
      Deligne Weil-form positivity), or only NON-DEGENERATE / INDEFINITE (Krein)?

  EXCEPTION_NEW_GEOMETRY  iff off-line admits NO non-degenerate Hermitian self-duality at all
                          (*-autonomy itself is INCONSISTENT off-line) -> positivity FORCED by
                          the duality -> the no-go is FALSE.
  NOGO_COMPLETE           iff off-line admits a non-degenerate Hermitian self-duality (a Krein /
                          indefinite *-structure) that is NOT positive-definite, i.e. the
                          *-structure is CONSISTENT off-line and positive-definiteness (C*) is a
                          STRICT EXTRA RESTRICTION -> positivity IMPORTED -> the no-go holds.

This is exactly Stehouwer-Steinebrunner (anti-involution = *-structure consistent WITHOUT
positivity; dagger/C* = the EXTRA positivity restriction to the positive-definite subclass) and
Deligne-Milne (Weil form non-deg = free; polarization = Tr(u u^phi)>0 = extra -> compact Galois).

Anchor: F_q. Falsify: DH.
"""
from __future__ import annotations
import numpy as np

np.set_printoptions(precision=4, suppress=True)


def frob_on_line(q, d, seed=0):
    """A semisimple F with all |eig| = sqrt(q): the on-line / pure Frobenius (RH holds)."""
    rng = np.random.default_rng(seed)
    thetas = rng.uniform(0, 2 * np.pi, d)
    eig = np.sqrt(q) * np.exp(1j * thetas)
    return _conjugate_into_real_basis(eig, rng), eig


def frob_off_line(q, d, ratio, seed=0):
    """A semisimple F that SATISFIES STEP A (the functional equation) but is OFF-LINE.

    CRITICAL (the fix that makes this an honest Frobenius datum): an honest Weil/Frobenius datum
    already carries the FE-pairing alpha <-> q/alpha (Step A, the perfect Poincare duality), which
    candidate 2 proved holds OFF-LINE too. So the eigenvalues MUST be closed under the FE
    involution alpha -> q/conj(alpha) for a Hermitian (conjugate-linear) self-duality U^* g U = g
    with U = F/sqrt(q) to exist. We therefore build eigenvalues in FE-PAIRS:
        pick alpha with |alpha| = sqrt(q)*ratio*rho (off-circle, rho!=1),
        its partner is beta = q / conj(alpha)  (so that |alpha|*|beta| = q, mu_alpha*conj(mu_beta)=1
        with mu = eig/sqrt q): a genuine NON-DEGENERATE invariant Hermitian pairing exists.
    This is the OFF-LINE datum of candidate 2: Step A holds, radius does not. d must be even."""
    assert d % 2 == 0, "FE-paired datum needs even d"
    rng = np.random.default_rng(seed)
    eig = []
    for _ in range(d // 2):
        theta = rng.uniform(0, 2 * np.pi)
        rho = ratio * rng.uniform(0.55, 1.7)  # off-circle modulus factor (rho != 1 -> off-line)
        alpha = np.sqrt(q) * rho * np.exp(1j * theta)
        beta = q / np.conj(alpha)  # FE partner: |alpha||beta| = q exactly
        eig.append(alpha)
        eig.append(beta)
    eig = np.array(eig)
    return _conjugate_into_real_basis(eig, rng), eig


def _conjugate_into_real_basis(eig, rng):
    """Build F = S diag(eig) S^{-1} with a generic invertible S (hide the eigenbasis)."""
    d = len(eig)
    S = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    return S @ np.diag(eig) @ np.linalg.inv(S)


# ---------------------------------------------------------------------------------------------
# (A) Hermitian self-duality / *-structure: a non-degenerate Hermitian form g (conjugate-linear
#     pairing) such that F is "g-unitary up to the radius", i.e. F^* g F = (radius^2) g where
#     F^* g := g-adjoint. Equivalently the normalized U = F/r preserves g: U^* g U = g.
#     A Hermitian self-duality for F means: EXISTS non-degenerate Hermitian g with g-adjoint(F)
#     = F up to scalar (the dualizing/conjugate-linear pairing). We test existence + signature.
# ---------------------------------------------------------------------------------------------

def hermitian_self_duality(F, r):
    """Find a non-degenerate Hermitian g with U^* g U = g where U = F / r (the normalized map).
    Returns (g, signature, is_definite). If g preserved by U is positive-definite -> C*/dagger
    (compact). If g is necessarily INDEFINITE -> Krein *-structure (consistent, non-positive).

    Construction: g = sum over the spectral/eigenbasis. For a semisimple U with eigenvalues mu_i
    (|mu_i| not all 1 when off-line), a U-invariant Hermitian form pairs eigenvector i with
    eigenvector j only when mu_i * conj(mu_j) = 1, i.e. mu_j = 1/conj(mu_i). The DIAGONAL pairing
    g(v_i, v_i) survives iff |mu_i| = 1. Off the circle, diagonal pairing is killed; the form must
    pair v_i with the eigenvector of reciprocal-conjugate eigenvalue -> a HYPERBOLIC (indefinite,
    signature-0) block. That block IS a non-degenerate Hermitian g -> *-structure EXISTS but is
    INDEFINITE. We construct it explicitly and read its inertia."""
    d = F.shape[0]
    U = F / r
    eigval, V = np.linalg.eig(U)  # columns of V are eigenvectors; U V = V diag(eigval)
    Vinv = np.linalg.inv(V)
    # In the eigenbasis, a U-invariant Hermitian form is a matrix H (in eigen-coords) with
    # H[i,j] nonzero only if eigval[i] * conj(eigval[j]) = 1. Build the MAXIMAL such non-degenerate H.
    n = d
    H = np.zeros((n, n), dtype=complex)
    used = [False] * n
    tol = 1e-6
    for i in range(n):
        if used[i]:
            continue
        mi = eigval[i]
        if abs(abs(mi) - 1.0) < tol:
            # |mu_i|=1: diagonal pairing allowed, real & nonzero. Sign = +1 by convention (could be -1).
            H[i, i] = 1.0
            used[i] = True
        else:
            # need partner j with eigval[j] = 1/conj(mi)  (so mi*conj(eigval[j])=1)
            target = 1.0 / np.conj(mi)
            j = None
            for k in range(n):
                if not used[k] and k != i and abs(eigval[k] - target) < 1e-3 * max(1, abs(target)):
                    j = k
                    break
            if j is None:
                # no reciprocal-conjugate partner present -> this eigendirection cannot be paired
                # -> the invariant Hermitian form is DEGENERATE on it. Record degeneracy.
                used[i] = True
                continue
            # hyperbolic 2x2 block: H[i,j]=1, H[j,i]=1 -> eigenvalues +1,-1 (signature 0, indefinite)
            H[i, j] = 1.0
            H[j, i] = 1.0
            used[i] = used[j] = True
    # transport H back to the standard basis: g = Vinv^* H Vinv  (so that U^* g U = g)
    g = Vinv.conj().T @ H @ Vinv
    g = 0.5 * (g + g.conj().T)  # Hermitize numerically
    # verify invariance U^* g U = g
    inv_err = np.linalg.norm(U.conj().T @ g @ U - g) / max(np.linalg.norm(g), 1e-30)
    # non-degeneracy and signature
    w = np.linalg.eigvalsh(g)
    rank = int(np.sum(np.abs(w) > 1e-6 * max(np.max(np.abs(w)), 1e-30)))
    n_pos = int(np.sum(w > 1e-6 * max(np.max(np.abs(w)), 1e-30)))
    n_neg = int(np.sum(w < -1e-6 * max(np.max(np.abs(w)), 1e-30)))
    nondegenerate = (rank == d)
    is_pos_def = (n_neg == 0 and n_pos == d)
    return {
        "g": g, "inv_err": float(inv_err), "rank": rank, "d": d,
        "n_pos": n_pos, "n_neg": n_neg, "nondegenerate": bool(nondegenerate),
        "positive_definite": bool(is_pos_def),
    }


def report(label, F, r, eig):
    res = hermitian_self_duality(F, r)
    print(f"\n=== {label} ===")
    print(f"  |eig| = {np.sort(np.abs(eig))}")
    print(f"  normalized |eig/r| = {np.sort(np.abs(eig / r))}")
    print(f"  invariance error U* g U - g : {res['inv_err']:.2e}")
    print(f"  Hermitian self-duality (*-structure) EXISTS & non-degenerate : {res['nondegenerate']}")
    print(f"  signature (n_pos, n_neg) of g : ({res['n_pos']}, {res['n_neg']})  rank {res['rank']}/{res['d']}")
    print(f"  POSITIVE-DEFINITE (C*/dagger/polarization) : {res['positive_definite']}")
    return res


if __name__ == "__main__":
    q, d = 7, 6
    print("CANDIDATE 3 -- C*/Hermitian-self-duality forces positivity? Anchor q =", q, " d =", d)

    F_on, eig_on = frob_on_line(q, d, seed=1)
    r_on = np.sqrt(q)
    on = report("ON-LINE  (|eig|=sqrt q, RH holds)", F_on, r_on, eig_on)

    # off-line: FE-paired (Step A holds) but off-circle. Normalize by sqrt(q) -- the FE radius --
    # because the FE involution alpha -> q/conj(alpha) is U -> (U^*)^{-1} exactly for U = F/sqrt(q).
    F_off, eig_off = frob_off_line(q, d, ratio=1.0, seed=2)
    off = report("OFF-LINE (FE-paired, off-circle, RH fails)", F_off, np.sqrt(q), eig_off)

    F_off2, eig_off2 = frob_off_line(q, d, ratio=1.3, seed=3)
    off2 = report("OFF-LINE (FE-paired, ratio 1.3, RH fails)", F_off2, np.sqrt(q), eig_off2)

    print("\n" + "=" * 80)
    print("VERDICT LOGIC:")
    print(f"  on-line   : *-structure exists={on['nondegenerate']}, positive-definite={on['positive_definite']}")
    print(f"  off-line  : *-structure exists={off['nondegenerate']}, positive-definite={off['positive_definite']}")
    print(f"  off-line2 : *-structure exists={off2['nondegenerate']}, positive-definite={off2['positive_definite']}")
    off_has_star = off["nondegenerate"] or off2["nondegenerate"]
    off_is_pos = off["positive_definite"] or off2["positive_definite"]
    if not off_has_star:
        print("\n  -> off-line admits NO non-degenerate Hermitian self-duality.")
        print("     *-autonomy itself is INCONSISTENT off-line -> positivity FORCED -> EXCEPTION_NEW_GEOMETRY")
    elif off_has_star and not off_is_pos:
        print("\n  -> off-line admits a NON-DEGENERATE INDEFINITE (Krein) Hermitian self-duality,")
        print("     consistent but NOT positive-definite. Positive-definiteness (C*/dagger/polarization)")
        print("     is a STRICT EXTRA RESTRICTION -> positivity IMPORTED -> NOGO_COMPLETE")
    else:
        print("\n  -> off-line *-structure is itself positive-definite?? recheck construction.")
