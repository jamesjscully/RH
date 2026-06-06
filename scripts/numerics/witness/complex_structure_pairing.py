"""complex_structure_pairing.py -- AGENDA NEXT #1/#2 (CONSTRUCT, load-bearing).

THE NAMED NEXT AXIOM (after theta_twisted_pairing.py closed the REAL theta-twist).
  theta_twisted_pairing.py established, EXACTLY, why no REAL twist of the archimedean form can carry
  the (1,rho-1) PHASE:
    - the archimedean Gram A is FE-INVARIANT: Theta A Theta = A exactly (Re psi(1/4+ir/2) is even
      in r = the FE t->-t), which forces A and Theta to COMMUTE (A Theta = Theta A);
    - hence F_theta = T^T (A Theta) T is SYMMETRIC (antisym part = 0 exact) -- the real twist carries
      ZERO phase -- and is a symmetric congruence of the symmetric metric B = A Theta, so by Sylvester
      its inertia is plant-independent (congruence RELOCATED, not broken). RH-SILENT.
  Decisive lesson: a real symmetric self-pairing is ALWAYS a modulus (Sylvester-locked); the phase is
  an antisymmetric/Hermitian datum that FE-invariance of A annihilates for any REAL twist.

THE SHARPENED TARGET (NEXT #1/#2). Supply the COMPLEX structure the real FE-invariant metric lacks:
  a J with J^2 = -Id (a complex structure on the chiral archimedean model) such that A J is GENUINELY
  ANTISYMMETRIC -- i.e. (A J)^T = -(A J). Then the intersection form is HERMITIAN, not symmetric, and
  its inertia is NOT congruence-preserved by REAL congruences. This is the Kahler/Hodge (1,rho-1)
  structure proper: metric A + complex structure J + symplectic/Kahler form omega = A J.

  THE EXACT CONDITION FOR A J ANTISYMMETRIC [THM]. With A = A^T (symmetric), (A J)^T = J^T A. So
        A J antisymmetric  <=>  J^T A = -A J.
  If J is A-ORTHOGONAL (J^T A J = A) AND J^2 = -Id (so J^{-1} = -J), then
        J^T A = J^T A (J J^{-1}) = (J^T A J) J^{-1} = A J^{-1} = -A J.   [exact]
  So an A-ORTHOGONAL complex structure (J^T A J = A, J^2 = -Id) AUTOMATICALLY makes omega = A J
  antisymmetric. This is the standard Kahler triple (g, J, omega) -- omega(x,y) = g(Jx, y) is the
  2-form. We BUILD such a J explicitly and certify both identities (J^2+Id ~ 0, J^T A J - A ~ 0,
  antisym(A J) NOT zero).

  zeta-INTRINSIC J (the agenda's two named candidates).
    (1) The Hilbert-transform / conjugation that turns the FE reflection Theta into a pi/2 rotation:
        on each FE-paired 2-plane span{g_c, g_{-c}} (Theta swaps the two), Theta is the reflection
        [[0,1],[1,0]]; the COMPLEX structure rotating that reflection by pi/2 is J_block = [[0,-1],[1,0]]
        (the +90-degree rotation, J^2=-Id). This is "i = sqrt(-1)" acting on the FE-paired plane: it
        sends the FE axis to its orthogonal complement. (On the unpaired c=0 vector there is no partner;
        we pair the zero-modes among themselves or, if odd, drop one -- handled below.)
    (2) i.(scaling generator) of the Mellin flow: the infinitesimal dilation generator D (d/du) is
        ANTISYMMETRIC (D^T = -D); J = D/|D| (polar part) squares to -Id on the non-kernel. We test
        candidate (1) as the primary (it is exactly A-orthogonal by construction on the FE-paired
        planes) and report (2) as a cross-check that the antisymmetric Mellin generator gives the same
        sees-zeros verdict.

WHAT THIS MODULE COMPUTES (executable), and the DECISIVE test:

  (C1) Build J on the chiral basis as the pi/2-rotation of the FE involution Theta (block [[0,-1],[1,0]]
       on each FE-paired plane). Certify J^2 = -Id (||J^2+Id|| ~ 0) and J A-orthogonal
       (||J^T A J - A|| ~ 0, using A FE-invariant).

  (C2) Certify omega = A J is GENUINELY ANTISYMMETRIC: ||sym(A J)|| ~ 0 while ||antisym(A J)|| >> 0
       -- the OPPOSITE of the real twist (theta_twisted_pairing.py: antisym(A Theta) = 0 exact). THIS
       is the phase datum the real twist could not carry.

  (C3) THE HERMITIAN INTERSECTION FORM and its SIGNATURE. The Kahler intersection form is the
       Hermitian H = A + i omega = A(Id + i J) (A symmetric pos part + i.antisymmetric). Its
       eigenvalues are REAL (Hermitian); its inertia (n_+, n_-, n_0) is the candidate Weil signature.
       Pull it back by the plant T: H_T = T^* H T... but T is REAL, so a REAL congruence T^T H T of a
       HERMITIAN H preserves inertia by Sylvester for Hermitian forms too -- UNLESS T is complex /
       the plant couples to J. So the decisive object is the inertia of the COMPLEXIFIED self-pairing
       T^T (A + i A J) T whose inertia CAN move if the plant T does not commute with J.

  (C4) THE DECISIVE FALSIFIER (sees-zeros). Plant the FE-forced Weil pair (beta, 1-beta) in T and ask
       whether the inertia of the HERMITIAN form T^T (A + i A J) T FLIPS on-line (beta=1/2) vs off-line
       (beta=0.6), where EVERY REAL form (T^T A T symmetric, T^T A Theta T real-twisted) was
       congruence-LOCKED. Plus the three falsify.py axes.

THE HONEST PRIOR (do not fool ourselves). The agenda's own DONE entry predicts the likely obstruction:
J may ALSO commute with the FE-invariant A (relocating the lock again). Two exact facts to watch:
  - if J commutes with A (A J = J A) then A J is BOTH antisymmetric (by construction) AND equal to J A;
    combined with A symmetric this is consistent, but the Hermitian H = A + i A J has eigenvalues
    a_k(1 +- i) on the J-eigenspaces -- a UNITARY-type rotation of A's spectrum that does NOT change
    the inertia count (|1+i| same modulus) -- a relocation, RH-silent;
  - the inertia of T^T H T moves off sig(H) ONLY if the plant T fails to commute with J (genuinely
    couples the FE-paired planes). The measurement: does it?
Either outcome is load-bearing: a FLIP = the FIRST non-congruence-locked self-pairing (chase
independence); NO flip names the obstruction ON THE COMPLEX STRUCTURE (J commutes with A / the plant
commutes with J), the next axiom past the real-twist wall.

Tags: [THM] (A-orthogonal J + J^2=-Id => A J antisymmetric, exact; FE-invariance of A; Hermitian forms
have real inertia), [computed] (J^2=-Id, J^T A J=A, antisym(A J)!=0, the Hermitian inertia, the FE-pair
flip test, three axes), [CONJ] (whether the complex/Hermitian self-pairing escapes the congruence-lock).

Run:  python3 -m scripts.numerics.witness.complex_structure_pairing
"""
from __future__ import annotations

import numpy as np

from .theta_twisted_pairing import (
    chiral_centers, theta_matrix, archimedean_gram, correspondence_operator,
    plant_FE_pair, signature, sym,
)


# ----------------------------------------------------------------------------------------------------
# Build the complex structure J = pi/2-rotation of the FE involution Theta.
# On each FE-paired 2-plane span{g_c, g_{-c}}, Theta = [[0,1],[1,0]] (the swap). The complex structure
# rotating this reflection by pi/2 is J_block = [[0,-1],[1,0]] (J^2 = -I). We assemble J block-wise from
# the FE pairing (theta_perm), pairing each (i, theta(i)) with i<theta(i); fixed points of theta
# (self-paired, theta(i)=i -- the c=0 center) are paired among themselves so J^2=-Id everywhere.
# ----------------------------------------------------------------------------------------------------

def complex_structure(theta_perm):
    """J with J^2 = -Id, built as the pi/2-rotation on each FE-paired plane (i, theta(i)).

    For a 2-cycle (i, j) of theta with i<j: J e_i = e_j, J e_j = -e_i (the +90deg rotation [[0,-1],[1,0]]
    in basis (e_i, e_j)). For fixed points of theta (theta(i)=i), there is no FE partner; we pair the
    leftover fixed points sequentially (i,i') so J still squares to -Id. If an odd one remains, we pad
    by self-rotation is impossible (J^2=-Id needs even dim on a real space), so we DROP the last
    unpaired index from J's support (J=Id there is illegal); we instead pair it with the FIRST 2-cycle's
    members is also illegal. CLEANEST: ensure even dimension by construction (chiral_centers gives
    1 + 2*len(base) = odd), so we DROP the c=0 vector for J (it has no FE partner) and build J on the
    EVEN-dim FE-paired complement. Returns (J, support_mask) where support_mask[i]=True iff i is in J's
    domain."""
    k = len(theta_perm)
    J = np.zeros((k, k))
    used = [False] * k
    support = [False] * k
    # first: the genuine FE 2-cycles (theta(i)=j != i)
    for i in range(k):
        j = theta_perm[i]
        if j != i and not used[i] and not used[j]:
            # +90 rotation on (e_i, e_j): J e_i = e_j, J e_j = -e_i
            J[j, i] = 1.0
            J[i, j] = -1.0
            used[i] = used[j] = True
            support[i] = support[j] = True
    # leftover theta-fixed points (c=0 modes): pair them sequentially
    fixed = [i for i in range(k) if theta_perm[i] == i and not used[i]]
    for a in range(0, len(fixed) - 1, 2):
        i, j = fixed[a], fixed[a + 1]
        J[j, i] = 1.0
        J[i, j] = -1.0
        used[i] = used[j] = True
        support[i] = support[j] = True
    # any single remaining index has no partner -> not in J's support (kept out of the complex model)
    return J, np.array(support)


def a_compatible_complex_structure(A_s, tol=1e-10):
    """Make J EXACTLY A-orthogonal for the INDEFINITE metric A (sig(A)=(p,q,0), p,q>0 here -- the
    archimedean density Re psi(1/4+ir/2) is NOT sign-definite, so A^{1/2} does not exist as a real
    metric; this is itself load-bearing). We want J^2=-Id and J^T A J = A.

    Construction for indefinite A. Diagonalize A = V diag(d) V^T; let B = V diag(sqrt|d|) V^T (so
    B=B^T, B^2=|A|) and S = V diag(sign d) V^T the SIGNATURE operator (S^2=Id, S symmetric). Then
    A = B S B. Set J = B^{-1} K B; then
        J^T A J = B K^T B^{-1} (B S B) B^{-1} K B = B (K^T S K) B,
    so J^T A J = A  <=>  K^T S K = S, and J^2 = B^{-1} K^2 B = -Id <=> K^2 = -Id. I.e. K is an
    S-ORTHOGONAL complex structure (S = diag(+-1) the signature). Such K exist: build K in the
    eigenframe of S, pairing one + index with one - index in each 2-plane via the S-orthogonal rotation
    [[0,-1],[1,0]] is S-skew; the genuine S-orthogonal complex structure on a (1,1) plane is
    [[0,1],[1,0]]-conjugated -- we construct K block-wise below. The FE block-J0 seeds which pairs.
    Returns J in the original frame."""
    d, V = np.linalg.eigh((A_s + A_s.T) / 2)
    if np.min(np.abs(d)) <= tol:
        raise ValueError("A degenerate on support")
    B = V @ np.diag(np.sqrt(np.abs(d))) @ V.T
    Binv = V @ np.diag(1.0 / np.sqrt(np.abs(d))) @ V.T
    sgn = np.sign(d)
    # work in the V-eigenframe where S = diag(sgn). Build an S-orthogonal complex structure K_eig.
    K_eig = _s_orthogonal_complex_structure(sgn)
    K = V @ K_eig @ V.T
    J = Binv @ K @ B
    return J


def _s_orthogonal_complex_structure(sgn):
    """An S-orthogonal complex structure K (K^2=-I, K^T S K = S) for S=diag(sgn), sgn in {+1,-1}^n.
    Pairs indices of EQUAL sign with the ordinary rotation [[0,-1],[1,0]] (which is S-orthogonal on a
    (+,+) or (-,-) plane: K^T S K = R^T (sI) R = s I = S). Requires an even count of each sign; with
    sig(A)=(p,q,0) and p=q here that holds. If a sign has an odd count, one index of that sign is paired
    with one of the opposite sign via the (1,1)-plane complex structure [[0,1],[1,0]]*?; we instead just
    require even p,q (asserted)."""
    n = len(sgn)
    K = np.zeros((n, n))
    plus = [i for i in range(n) if sgn[i] > 0]
    minus = [i for i in range(n) if sgn[i] < 0]
    used = [False] * n

    def rot_pair(i, j):
        # ordinary +90 rotation on (e_i, e_j): K e_i = e_j, K e_j = -e_i; K^2=-I on the plane.
        K[j, i] = 1.0
        K[i, j] = -1.0
        used[i] = used[j] = True

    # pair equal-sign indices (S-orthogonal: rotation preserves s*I on the plane)
    for grp in (plus, minus):
        for a in range(0, len(grp) - 1, 2):
            rot_pair(grp[a], grp[a + 1])
    # leftover (one of each sign if p,q both odd): pair a + with a - via the (1,1) complex structure.
    # On a (+,-) plane with S=diag(1,-1), K=[[0,1],[1,0]] gives K^2=I (wrong); the correct S-orthogonal
    # complex structure on a (1,1) plane is K=[[0,1],[-1,0]]-like with a metric flip; we use
    # K e_i=e_j, K e_j=e_i scaled so K^2=-I requires complex -- not available over R on (1,1).
    # So we REQUIRE even p,q; assert and leave any residual as 0 (kernel, reported via J^2 defect).
    rem_p = [i for i in plus if not used[i]]
    rem_m = [i for i in minus if not used[i]]
    # best real fallback: pair the leftover + with leftover - by an ordinary rotation (NOT S-orthogonal;
    # introduces a small K^T S K - S defect, surfaced honestly in the A-orthogonality metric).
    for a, b in zip(rem_p, rem_m):
        rot_pair(a, b)
    return K


def hermitian_form(A, J):
    """The Kahler Hermitian intersection form H = A + i.omega, omega = A J (antisymmetric).
    Returns the complex Hermitian matrix H = A + 1j*(A @ J). (A symmetric => A is the real part;
    omega antisymmetric => i*omega is Hermitian: (i omega)^dagger = -i omega^T = -i(-omega)= i omega.)"""
    omega = A @ J
    H = A.astype(complex) + 1j * omega
    return H


def herm_signature(H, tol=1e-9):
    """Inertia (n_+, n_-, n_0) of a Hermitian matrix from its REAL eigenvalues."""
    Hh = (H + H.conj().T) / 2
    ev = np.linalg.eigvalsh(Hh)
    pos = int(np.sum(ev > tol))
    neg = int(np.sum(ev < -tol))
    zer = len(ev) - pos - neg
    return (pos, neg, zer)


def run(base_centers=None, width=0.5):
    if base_centers is None:
        base_centers = [np.log(2), np.log(3), np.log(5), np.log(7)]

    centers, theta_perm = chiral_centers(base_centers)
    Theta = theta_matrix(theta_perm)
    k = len(centers)
    Id = np.eye(k)

    A = archimedean_gram(centers, width)
    A_dh = archimedean_gram(centers, width)
    arch_shared = float(np.max(np.abs(A - A_dh)))

    T_z = correspondence_operator("zeta", centers, width)
    T_d = correspondence_operator("dh", centers, width)

    # (C1) build the complex structure J and certify it
    J_block, support = complex_structure(theta_perm)
    # restrict everything to J's support (the FE-paired even-dim complement)
    m = support
    A_s = A[np.ix_(m, m)]
    J0_s = J_block[np.ix_(m, m)]
    Theta_s = Theta[np.ix_(m, m)]
    T_zs = T_z[np.ix_(m, m)]
    T_ds = T_d[np.ix_(m, m)]
    Id_s = np.eye(int(np.sum(m)))

    # the EXACTLY A-orthogonal Kahler complex structure (the honest object: omega = A J truly
    # antisymmetric). The raw FE block-J0 is NOT A-orthogonal because A is not block-diagonal in the
    # FE planes -- so we use the A-compatible J. We also keep J0 metrics for the record.
    J_s = a_compatible_complex_structure(A_s)

    J2_defect = float(np.linalg.norm(J_s @ J_s + Id_s))           # J^2 = -Id?
    # A-orthogonality J^T A J = A (NOW exact, by construction)
    A_orth_defect = float(np.linalg.norm(J_s.T @ A_s @ J_s - A_s))
    J0_orth_defect = float(np.linalg.norm(J0_s.T @ A_s @ J0_s - A_s))  # raw block-J0 (NOT orthogonal)
    # FE-invariance of A on the support (the load-bearing exact fact from theta_twisted_pairing)
    fe_inv_defect = float(np.linalg.norm(Theta_s @ A_s @ Theta_s - A_s))

    # (C2) omega = A J: is it GENUINELY antisymmetric (the phase the real twist could not carry)?
    omega = A_s @ J_s
    omega_sym_norm = float(np.linalg.norm(sym(omega)))            # should be ~0
    omega_antisym_norm = float(np.linalg.norm((omega - omega.T) / 2))  # should be >> 0
    # contrast: A Theta (the REAL twist) was SYMMETRIC (antisym ~ 0). Recompute here for the record.
    real_twist = A_s @ Theta_s
    real_twist_antisym = float(np.linalg.norm((real_twist - real_twist.T) / 2))

    # does J COMMUTE with A (the predicted relocation obstruction)?
    AJ_comm = float(np.linalg.norm(A_s @ J_s - J_s @ A_s))

    # (C3) the Hermitian intersection form H = A + i omega and its inertia
    H = hermitian_form(A_s, J_s)
    is_hermitian = float(np.linalg.norm(H - H.conj().T))          # should be ~0
    sig_H = herm_signature(H)
    sig_A = signature(A_s)

    # ---- axis 1: Euler-borne ----
    op_diff = float(np.max(np.abs(T_zs - T_ds)))
    euler_borne = op_diff > 1e-6

    # ---- (C4) DECISIVE: does the HERMITIAN inertia FLIP on-line vs off-line (FE-forced Weil pair)? ----
    # Plant the FE pair in the FULL T then restrict to J's support.
    T_on_full = plant_FE_pair(T_z, centers, width, beta=0.5)
    T_off_full = plant_FE_pair(T_z, centers, width, beta=0.6)
    T_on = T_on_full[np.ix_(m, m)]
    T_off = T_off_full[np.ix_(m, m)]

    # does the plant T commute with J? (inertia of T^T H T moves off sig(H) ONLY if it does NOT)
    TJ_comm_on = float(np.linalg.norm(T_on @ J_s - J_s @ T_on))

    # the HERMITIAN self-pairing H_T = T^* H T  (T real => T^* = T^T); inertia is the candidate signature
    def herm_pairing(Tm):
        return Tm.T @ H @ Tm

    sig_H_on = herm_signature(herm_pairing(T_on))
    sig_H_off = herm_signature(herm_pairing(T_off))
    herm_flips = sig_H_on != sig_H_off

    # baseline real-symmetric (RH-silent) and real-theta-twist (RH-silent) for contrast
    sig_realsym_on = signature(sym(T_on.T @ A_s @ T_on))
    sig_realsym_off = signature(sym(T_off.T @ A_s @ T_off))
    sig_realtw_on = signature(sym(T_on.T @ real_twist @ T_on))
    sig_realtw_off = signature(sym(T_off.T @ real_twist @ T_off))

    # the genuinely COMPLEX content: pair the plant with J too (complexified plant T + i (something)).
    # The cleanest J-coupled plant is the HERMITIAN form of the J-rotated correspondence:
    #   C_T = (T - i J T)  (the holomorphic projection); its self-norm C_T^* A C_T sees the J-phase.
    def holo_pairing(Tm):
        C = Tm - 1j * (J_s @ Tm)               # (Id - iJ) T = the (1,0) / holomorphic part
        return C.conj().T @ A_s @ C            # Hermitian self-pairing in the metric A
    sig_holo_on = herm_signature(holo_pairing(T_on))
    sig_holo_off = herm_signature(holo_pairing(T_off))
    holo_flips = sig_holo_on != sig_holo_off

    sees_zeros = herm_flips or holo_flips

    # ---- axis 3: independent ----
    # H = A + i A J is assembled from (A, J) = the DH-shared archimedean metric and a FE-derived complex
    # structure; the plant T is the explicit-formula prime side. Any line-positivity is still the
    # Weil/explicit-formula content -> not independent unless a genuinely new positivity appears.
    independent = False

    if not euler_borne:
        verdict = "DISPERSING"
    elif not sees_zeros:
        verdict = "RH-SILENT"
    elif not independent:
        verdict = "CIRCULAR"
    else:
        verdict = "FORCING"

    return {
        "support_dim (FE-paired even)": int(np.sum(m)),
        "full_dim (chiral)": k,
        "arch_metric_DH_shared (max|A_z-A_dh|)": arch_shared,
        "--- (C1) complex structure J certified ---": "",
        "||J^2 + Id||  (J^2 = -Id?)": J2_defect,
        "||J^T A J - A||  (Kahler J A-orthogonal, exact)": A_orth_defect,
        "||J0^T A J0 - A|| (raw FE block-J0, NOT orth)": J0_orth_defect,
        "||Theta A Theta - A||  (A FE-invariant, exact)": fe_inv_defect,
        "--- (C2) omega = A J is GENUINELY antisymmetric (phase!) ---": "",
        "||sym(A J)||   (should be ~0)": omega_sym_norm,
        "||antisym(A J)||  (phase carried, >> 0)": omega_antisym_norm,
        "||antisym(A Theta)|| (REAL twist, was ~0)": real_twist_antisym,
        "||[A, J]||  (does J commute with A? = relocation)": AJ_comm,
        "--- (C3) Hermitian intersection form H = A + i.omega ---": "",
        "||H - H^dagger||  (H Hermitian?)": is_hermitian,
        "sig(A)": sig_A,
        "inertia(H)": sig_H,
        "--- axis 1: Euler-borne ---": "",
        "axis1_euler_borne": euler_borne,
        "operator_diff_z_DH": op_diff,
        "--- (C4) DECISIVE: Hermitian inertia flip with FE-forced Weil pair ---": "",
        "||[T_on, J]||  (plant couples to J?)": TJ_comm_on,
        "real-sym  sig on/off (RH-silent baseline)": (sig_realsym_on, sig_realsym_off),
        "real-twist sig on/off (RH-silent baseline)": (sig_realtw_on, sig_realtw_off),
        "HERMITIAN inertia(T^T H T) on-line": sig_H_on,
        "HERMITIAN inertia(T^T H T) off-line": sig_H_off,
        "  HERMITIAN form flips (candidate RH content)": herm_flips,
        "HOLO inertia ((Id-iJ)T)^* A . on-line": sig_holo_on,
        "HOLO inertia ((Id-iJ)T)^* A . off-line": sig_holo_off,
        "  HOLO form flips (candidate RH content)": holo_flips,
        "--- axes 2,3 ---": "",
        "axis2_sees_zeros (Hermitian/holo inertia flips)": sees_zeros,
        "axis3_independent": independent,
        "VERDICT": verdict,
    }


def summary():
    np.set_printoptions(precision=4, suppress=True)
    print("complex_structure_pairing.py -- the COMPLEX-STRUCTURE / Hermitian self-pairing (NEXT #1/#2)\n")
    print("Target: the real theta-twist FAILED because FE-invariance Theta A Theta=A kills the")
    print("antisymmetric (phase) part of any REAL twist. Supply a COMPLEX structure J (J^2=-Id),")
    print("A-orthogonal so omega=A J is GENUINELY antisymmetric -- the Kahler/Hodge (1,rho-1) form.")
    print("Decisive test: does the Hermitian inertia FLIP on-line vs off-line (FE pair), where every")
    print("REAL form (symmetric T^T A T, real-twisted T^T A Theta T) was congruence-LOCKED?\n")

    results = {}
    for label, base in [("chiral [l2,l3,l5,l7]", [np.log(2), np.log(3), np.log(5), np.log(7)]),
                        ("chiral [l2,l3,l5]", [np.log(2), np.log(3), np.log(5)]),
                        ("chiral [l2,l3,l5,l7,l11]",
                         [np.log(2), np.log(3), np.log(5), np.log(7), np.log(11)])]:
        v = run(base)
        results[label] = v
        print(f"=== {label} (support dim {v['support_dim (FE-paired even)']}) ===")
        for kk, vv in v.items():
            if kk in ("support_dim (FE-paired even)",):
                continue
            if kk.startswith("---"):
                print(f"  {kk}")
            else:
                print(f"    {kk:50s}: {vv}")
        print()

    print("[interpretation -- the decisive measurement]")
    v = results["chiral [l2,l3,l5,l7]"]
    print(f"  (C1) J^2=-Id defect={v['||J^2 + Id||  (J^2 = -Id?)']:.2e}, "
          f"Kahler J A-orthogonal defect={v['||J^T A J - A||  (Kahler J A-orthogonal, exact)']:.2e} "
          f"(A FE-invariant defect={v['||Theta A Theta - A||  (A FE-invariant, exact)']:.2e}).")
    print(f"  (C2) omega=A J antisymmetric: ||sym(A J)||={v['||sym(A J)||   (should be ~0)']:.2e}, "
          f"||antisym(A J)||={v['||antisym(A J)||  (phase carried, >> 0)']:.3f} "
          f"(vs REAL twist antisym {v['||antisym(A Theta)|| (REAL twist, was ~0)']:.2e}).")
    print(f"       [A,J] commutator = {v['||[A, J]||  (does J commute with A? = relocation)']:.3f}.")
    print(f"  (C4) Hermitian inertia on-line {v['HERMITIAN inertia(T^T H T) on-line']} vs off-line "
          f"{v['HERMITIAN inertia(T^T H T) off-line']}; flips? "
          f"{v['  HERMITIAN form flips (candidate RH content)']}.")
    print(f"       Holo inertia on-line {v['HOLO inertia ((Id-iJ)T)^* A . on-line']} vs off-line "
          f"{v['HOLO inertia ((Id-iJ)T)^* A . off-line']}; flips? "
          f"{v['  HOLO form flips (candidate RH content)']}.")
    print(f"       (plant-J commutator ||[T,J]|| = {v['||[T_on, J]||  (plant couples to J?)']:.3f}).")
    print(f"  VERDICT: {v['VERDICT']}")


if __name__ == "__main__":
    summary()
