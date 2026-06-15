"""zero_in_form_pairing.py -- AGENDA NEXT #1 (CONSTRUCT, load-bearing). THE CORRECTED TARGET.

THE WHOLE SELF-PAIRING FAMILY IS CLOSED (DONE #0/top). Every route tried -- symmetric T^T A T
(hecke_correspondence), real theta-twist T^T A Theta T (theta_twisted_pairing), complex/Hermitian
T^T (A+iAJ) T (complex_structure_pairing) -- has the shape

        (plant)^T (fixed DH-shared form) (plant)

and is INERTIA-LOCKED by Sylvester's law of inertia (identical for symmetric AND Hermitian forms): a
REAL plant T with det T != 0 gives a *-congruence, so inertia(T^T F T) = inertia(F) = the inertia of
the FIXED form F (built from the DH-shared archimedean A), independent of T's spectrum => RH-SILENT.

THE CORRECTED CONSTRUCTION TARGET (agenda NEXT #1, verbatim): the zeros -- the plant's eigenvalue
LOCATIONS -- must enter the intersection FORM ITSELF, not as the congruence factor T. The escape named:
a form B(T) that DEPENDS on the plant T's spectrum. The agenda names TWO concrete candidates:

    (1) the NON-SELF-ADJOINT PART     Omega(T) := T - T^T        (antisymmetric, = 0 iff T symmetric)
    (2) the SELF-COMMUTATOR / Poisson  C(T)    := [T, T^T] = T T^T - T^T T   (symmetric, traceless,
                                                                              = 0 iff T normal)

Neither is a congruence (plant)^T(fixed form)(plant): both are built FROM T's OWN entries, so Sylvester
does NOT apply and their inertia can, a priori, track T's spectrum. The decisive question (agenda):
"is there a zeta-intrinsic form whose inertia = sign(Im rho)-type data (the off-line Weil pair (beta,
1-beta) splits a +/- only when beta != 1/2)? Does its inertia flip on/off-line?"

WHAT MAKES THIS THE RIGHT PLACE TO LOOK (the structural reason, stated before the numerics).
  - The FE involution is theta (s|->1-s), realized on the chiral basis as the reflection Theta
    (theta_twisted_pairing). The completed-zeta symmetry says the genuine Weil operator is
    theta-self-adjoint: T^Theta := Theta T^T Theta should equal T (on-line / RH content). So
        Omega_theta(T) := T - Theta T^T Theta
    is the FE-DEFECT of T. For an on-line (beta=1/2) plant the FE pair (beta,1-beta) is degenerate
    (a point IS its own FE image) and the defect is small/structured; an off-line plant injects an
    asymmetric (beta,1-beta) pair, beta != 1-beta, which is exactly the data Omega_theta is built to
    expose. THIS is "the zeros enter the form": the form Omega_theta(T) measures how far T is from
    FE-self-adjoint, and an off-line zero is precisely an FE-asymmetry.
  - The self-commutator C(T) is the NORMALITY defect: a self-adjoint (real-spectrum) operator is
    normal. RH says the zero-spectrum is real; an off-line zero makes the corresponding operator
    NON-normal. So sig(C(T)) / ||C(T)|| is a candidate normality-defect detector.

WHAT THIS MODULE COMPUTES (executable) and the DECISIVE falsifier:

  (Z1) Build the chiral A, Theta, T (reusing theta_twisted_pairing primitives). Certify Theta is a
       genuine reflection and A FE-invariant (the load-bearing exact facts).

  (Z2) The NON-CONGRUENCE forms. For the FE-forced Weil pair planted at beta:
         Omega(T)        = T - T^T                  (raw non-self-adjoint part, antisymmetric)
         Omega_theta(T)  = T - Theta T^T Theta      (FE-defect: T minus its FE-adjoint)
         C(T)            = T T^T - T^T T             (self-commutator, symmetric)
       Report for each: (a) its inertia (symmetric part), (b) its norm, (c) whether it is a congruence
       of a fixed form (it is NOT -- verified structurally), and crucially whether these DEPEND on the
       plant's spectrum (||.|| changes with beta) AND whether the INERTIA flips on/off-line.

  (Z3) THE DECISIVE FALSIFIER (sees-zeros). Plant the FE-forced Weil pair (beta, 1-beta) and ask
       whether ANY of {inertia(sym Omega_theta), inertia(C), the antisym-spectrum of Omega} FLIPS
       on-line (beta=1/2) vs off-line (beta=0.6). Plus the three falsify.py axes.

THE HONEST PRIOR (do not fool ourselves). The likely obstruction, named in advance:
  - The plant adds a SYMMETRIC perturbation dT to T (plant_in_operator builds a SYMMETRIC overlap
    kernel: the (i,j) entry depends on |ci-cj +- u|, symmetric in i<->j). If dT is symmetric AND the
    base T_z is (nearly) symmetric on the chiral basis, then Omega(T) = T - T^T is NEAR ZERO and
    carries no plant data -- the non-self-adjoint part is an artifact of basis non-orthogonality, not
    of the zeros. We MEASURE ||Omega|| and ||C|| and their beta-dependence to see whether the plant
    actually enters the antisymmetric/normality channel at all. If the forms are plant-INDEPENDENT or
    do not flip, that NAMES the obstruction: the FE-forced (beta,1-beta) symmetric plant cannot inject
    a sign(Im rho) asymmetry into a REAL form (the off-line-ness is a COMPLEX datum -- gamma, the
    height -- and the real Weil pair (beta,1-beta) is symmetric under conjugation, so a REAL form sees
    only |rho|-type / beta-symmetric data). That would CLOSE the corrected target too and sharpen the
    wall to: the sign(Im rho) datum is intrinsically complex and cannot live in a real form's inertia.

Tags: [THM] (Omega, C are NOT congruences; antisymmetric spectrum is +-i.lambda; FE-adjoint defect;
the FE pair (beta,1-beta) is beta-symmetric), [computed] (the forms, their norms, beta-dependence, the
on/off-line flip test, the three axes), [CONJ] (whether a real T-built form's inertia tracks sign Im rho).

Run:  python3 -m scripts.numerics.witness.zero_in_form_pairing
"""
from __future__ import annotations

import numpy as np

from .theta_twisted_pairing import (
    chiral_centers, theta_matrix, archimedean_gram, correspondence_operator,
    plant_FE_pair, signature, sym,
)


def antisym(Mx):
    return (Mx - Mx.T) / 2


def antisym_spectrum(Mx, tol=1e-9):
    """For a REAL antisymmetric matrix K = -K^T, eigenvalues are +-i.lambda_k (lambda_k>=0). Return the
    sorted nonnegative lambda_k (the singular-value-like spectrum) and the count of nonzero pairs."""
    K = antisym(Mx)
    # eigenvalues of a real antisymmetric matrix are purely imaginary; take |Im|.
    ev = np.linalg.eigvals(K)
    lam = np.sort(np.abs(ev.imag))[::-1]
    nz = int(np.sum(lam > tol))
    return lam, nz


def fe_adjoint(T, Theta):
    """The FE-adjoint of T: T^{theta} = Theta T^T Theta (the adjoint w.r.t. the FE reflection). On-line /
    RH content is T^{theta} = T (FE-self-adjointness). Omega_theta = T - T^{theta} is the FE-defect."""
    return Theta @ T.T @ Theta


def causal_operator(centers, width, M=60, plant=None):
    """THE STEELMAN of the corrected target: a genuinely NON-self-adjoint, NON-normal zeta-intrinsic
    operator -- the ONE-DIRECTIONAL (causal) prime shift = the genuine Frobenius/transfer operator
        (T f)(u) = sum Lambda(n)/sqrt(n) f(u - log n)   (FORWARD shift only, not the two-sided symmetric
    kernel of correspondence_operator, which is exactly symmetric => all T-built forms vanish). With the
    forward shift, T_ij = overlap of g_i(center ci) with g_j shifted to center cj+log n, which is NOT
    symmetric in i<->j, so ||T-T^T|| > 0 and [T,T^T] != 0 (T genuinely non-normal). plant=(beta,gamma)
    adds the off-line resonance term."""
    from .explicit_formula import von_mangoldt
    cn = [float(von_mangoldt(n)) for n in range(1, M + 1)]
    k = len(centers)
    Tm = np.zeros((k, k))
    for i, ci in enumerate(centers):
        for j, cj in enumerate(centers):
            s = 0.0
            for n in range(2, M + 1):
                if cn[n - 1] == 0.0:
                    continue
                u = np.log(n)
                s += cn[n - 1] * np.exp(-(ci - (cj + u)) ** 2 / (4 * width ** 2)) / n
            Tm[i, j] = s
    if plant is not None:
        beta, gamma = plant
        for i, ci in enumerate(centers):
            for j, cj in enumerate(centers):
                s = 0.0
                for n in range(2, M):
                    u = np.log(n)
                    s += np.cos(gamma * u) * np.exp((beta - 0.5) * u) * \
                        np.exp(-(ci - (cj + u)) ** 2 / (4 * width ** 2)) / n
                Tm[i, j] += s
    return Tm


def causal_FE_pair(centers, width, beta, gamma=14.0):
    """Plant the FE-forced Weil pair (beta, 1-beta) additively into the CAUSAL (non-symmetric) operator."""
    base = causal_operator(centers, width)
    T = base.copy()
    for b in (beta, 1 - beta):
        T = T + (causal_operator(centers, width, plant=(b, gamma)) - base)
    return T


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

    # (Z1) certify the FE structure
    theta_nontrivial = float(np.linalg.norm(Theta - Id))
    fe_inv_defect = float(np.linalg.norm(Theta @ A @ Theta - A))

    # how (anti)symmetric is the BASE T_z on the chiral basis? (the honest-prior measurement)
    base_antisym = float(np.linalg.norm(antisym(T_z)))
    base_sym = float(np.linalg.norm(sym(T_z)))
    # FE-defect of the base operator
    base_fe_defect = float(np.linalg.norm(T_z - fe_adjoint(T_z, Theta)))

    # ---- axis 1: Euler-borne ----
    op_diff = float(np.max(np.abs(T_z - T_d)))
    euler_borne = op_diff > 1e-6

    # ---- (Z2)/(Z3) the NON-CONGRUENCE forms, planted on/off-line ----
    T_on = plant_FE_pair(T_z, centers, width, beta=0.5)
    T_off = plant_FE_pair(T_z, centers, width, beta=0.6)

    def forms(T):
        Omega = antisym(T)                       # raw non-self-adjoint part T-T^T (over 2)
        Omega_theta = T - fe_adjoint(T, Theta)   # FE-defect: T - Theta T^T Theta
        C = T @ T.T - T.T @ T                    # self-commutator [T,T^T] (symmetric, traceless)
        lam_O, nz_O = antisym_spectrum(2 * Omega)            # antisym spectrum of T-T^T
        lam_Ot, nz_Ot = antisym_spectrum(antisym(Omega_theta))  # antisym part of the FE-defect
        return {
            "||Omega = T-T^T||": float(np.linalg.norm(2 * Omega)),
            "antisym-spectrum nonzero count (T-T^T)": nz_O,
            "max |lambda| (T-T^T)": float(lam_O[0]) if len(lam_O) else 0.0,
            "||Omega_theta = T-Theta T^T Theta|| (FE-defect)": float(np.linalg.norm(Omega_theta)),
            "sig(sym Omega_theta)": signature(sym(Omega_theta)),
            "||sym Omega_theta||": float(np.linalg.norm(sym(Omega_theta))),
            "||C = [T,T^T]|| (normality defect)": float(np.linalg.norm(C)),
            "sig(C)": signature(C),       # C is symmetric => genuine inertia
            "trace(C) (should be ~0)": float(np.trace(C)),
        }

    f_on = forms(T_on)
    f_off = forms(T_off)

    # the candidate RH content: do the T-BUILT FORMS' inertiae flip on/off-line?
    sig_Otheta_on = f_on["sig(sym Omega_theta)"]
    sig_Otheta_off = f_off["sig(sym Omega_theta)"]
    Otheta_flips = sig_Otheta_on != sig_Otheta_off

    sig_C_on = f_on["sig(C)"]
    sig_C_off = f_off["sig(C)"]
    C_flips = sig_C_on != sig_C_off

    # also the antisym spectrum count of T-T^T (a non-inertia spectral datum)
    O_count_on = f_on["antisym-spectrum nonzero count (T-T^T)"]
    O_count_off = f_off["antisym-spectrum nonzero count (T-T^T)"]
    O_count_flips = O_count_on != O_count_off

    # ---- THE STEELMAN: the genuinely NON-symmetric, NON-normal CAUSAL operator ----
    # correspondence_operator's two-sided kernel is EXACTLY symmetric => all forms vanish (0,0,n). The
    # honest steelman uses the one-directional Frobenius/transfer operator (||T-T^T||>0, ||[T,T^T]||>0).
    Tc_on = causal_FE_pair(centers, width, beta=0.5)
    Tc_off = causal_FE_pair(centers, width, beta=0.6)
    fc_on = forms(Tc_on)
    fc_off = forms(Tc_off)
    causal_nonsym = float(np.linalg.norm(antisym(Tc_on)))
    causal_C = float(np.linalg.norm(Tc_on @ Tc_on.T - Tc_on.T @ Tc_on))
    causal_C_flips = fc_on["sig(C)"] != fc_off["sig(C)"]
    causal_Ot_flips = fc_on["sig(sym Omega_theta)"] != fc_off["sig(sym Omega_theta)"]

    sees_zeros = (Otheta_flips or C_flips or O_count_flips
                  or causal_C_flips or causal_Ot_flips)

    # ---- axis 3: independent ----
    # All forms are assembled from (T, Theta) = the explicit-formula prime side and the FE. Even if a
    # flip appeared, its positivity would still be the Weil/explicit-formula content unless a genuinely
    # new (non-Weil) positivity were proved. Set False unless a flip + a non-circular proof appears.
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
        "basis_dim (chiral)": k,
        "arch_metric_DH_shared (max|A_z-A_dh|)": arch_shared,
        "--- (Z1) FE structure certified ---": "",
        "||Theta - Id|| (theta nontrivial)": theta_nontrivial,
        "||Theta A Theta - A|| (A FE-invariant)": fe_inv_defect,
        "--- honest prior: is the BASE T even non-symmetric / FE-asymmetric? ---": "",
        "||antisym(T_z)|| (raw non-self-adjoint part)": base_antisym,
        "||sym(T_z)|| (for scale)": base_sym,
        "||T_z - Theta T_z^T Theta|| (base FE-defect)": base_fe_defect,
        "--- axis 1: Euler-borne ---": "",
        "axis1_euler_borne": euler_borne,
        "operator_diff_z_DH": op_diff,
        "--- (Z2)/(Z3) NON-CONGRUENCE forms on-line (beta=1/2) ---": "",
        **{f"  ON  {kk}": vv for kk, vv in f_on.items()},
        "--- (Z2)/(Z3) NON-CONGRUENCE forms off-line (beta=0.6, FE pair) ---": "",
        **{f"  OFF {kk}": vv for kk, vv in f_off.items()},
        "--- STEELMAN: the genuinely NON-normal CAUSAL Frobenius operator ---": "",
        "||antisym(T_causal)|| (genuinely non-self-adjoint)": causal_nonsym,
        "||C(T_causal)|| (genuinely non-normal)": causal_C,
        "causal sig(C) on/off": (fc_on["sig(C)"], fc_off["sig(C)"]),
        "causal sig(sym Omega_theta) on/off": (fc_on["sig(sym Omega_theta)"],
                                               fc_off["sig(sym Omega_theta)"]),
        "causal sig(C) flips": causal_C_flips,
        "causal sig(sym Omega_theta) flips": causal_Ot_flips,
        "--- DECISIVE: do the T-BUILT FORMS' inertiae FLIP on/off-line? ---": "",
        "sig(sym Omega_theta) flips (FE-defect inertia, two-sided T)": Otheta_flips,
        "sig(C) flips (normality-defect inertia, two-sided T)": C_flips,
        "antisym-count(T-T^T) flips (two-sided T)": O_count_flips,
        "--- axes 2,3 ---": "",
        "axis2_sees_zeros (any T-built-form inertia flips)": sees_zeros,
        "axis3_independent": independent,
        "VERDICT": verdict,
    }


def summary():
    np.set_printoptions(precision=4, suppress=True)
    print("zero_in_form_pairing.py -- the CORRECTED target: zeros enter the FORM, not the congruence\n")
    print("The whole self-pairing family (plant)^T(fixed form)(plant) is Sylvester-locked (DONE #0).")
    print("Corrected target (NEXT #1): a form B(T) built FROM T's OWN entries -- the non-self-adjoint")
    print("part Omega=T-T^T, the FE-defect Omega_theta=T-Theta T^T Theta, the self-commutator C=[T,T^T]")
    print("-- NOT a congruence of any fixed form, so Sylvester does not apply. Decisive: does any of")
    print("their inertiae FLIP on-line (beta=1/2) vs off-line (beta=0.6, FE-forced Weil pair)?\n")

    results = {}
    for label, base in [("chiral [l2,l3,l5,l7]", [np.log(2), np.log(3), np.log(5), np.log(7)]),
                        ("chiral [l2,l3,l5]", [np.log(2), np.log(3), np.log(5)]),
                        ("chiral [l2,l3,l5,l7,l11]",
                         [np.log(2), np.log(3), np.log(5), np.log(7), np.log(11)])]:
        v = run(base)
        results[label] = v
        print(f"=== {label} (dim {v['basis_dim (chiral)']}) ===")
        for kk, vv in v.items():
            if kk in ("basis_dim (chiral)",):
                continue
            if kk.startswith("---"):
                print(f"  {kk}")
            else:
                print(f"    {kk:52s}: {vv}")
        print()

    print("[interpretation -- the decisive measurement]")
    v = results["chiral [l2,l3,l5,l7]"]
    print(f"  base T non-self-adjoint part ||antisym(T_z)||={v['||antisym(T_z)|| (raw non-self-adjoint part)']:.3e}, "
          f"base FE-defect={v['||T_z - Theta T_z^T Theta|| (base FE-defect)']:.3e} (||sym(T_z)||="
          f"{v['||sym(T_z)|| (for scale)']:.3f}).")
    print(f"  FE-defect inertia flips? {v['sig(sym Omega_theta) flips (FE-defect inertia, two-sided T)']}; "
          f"normality-defect inertia flips? {v['sig(C) flips (normality-defect inertia, two-sided T)']}; "
          f"antisym-count flips? {v['antisym-count(T-T^T) flips (two-sided T)']}.")
    print(f"  VERDICT: {v['VERDICT']}")


if __name__ == "__main__":
    summary()
