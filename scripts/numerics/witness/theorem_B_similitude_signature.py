"""
Witness for Theorem B' (the structural form of the Geometric No-Go).

Claim: let F be a c-similitude of a non-degenerate Hermitian form H, i.e.
    F* H F = c H        (equivalently F.F^dagger = c.1,  F^dagger = c F^{-1})
with eigenvalues paired by the functional equation  alpha <-> c/conj(alpha).
Then:
  (A, FREE)  an F-invariant non-degenerate Hermitian form H EXISTS at every radius
             (the similitude / duality structure is satisfiable for any |alpha|);
  (B, = RH)  H can be chosen POSITIVE-DEFINITE  <=>  every |alpha| = sqrt(c)
             (all eigenvalues on the circle); off-line, H is forced indefinite (Krein),
             signature (k,k).

So Step A (similitude) does NOT determine the signature; positive-definiteness (Step B)
is exactly RH for the datum, and is independent of the structure that only sees Step A.

This is the single theorem behind the whole Geometric No-Go exhaustion table.

Run: python3 -m scripts.numerics.witness.theorem_B_similitude_signature
"""
import numpy as np


def invariant_form_in_eigenbasis(alphas, c):
    """
    Build the canonical F-invariant non-degenerate Hermitian form on C^n in the
    eigenbasis, for F = diag(alphas) with eigenvalues paired by alpha <-> c/conj(alpha).

    - A FIXED POINT  alpha = c/conj(alpha)  (i.e. |alpha|^2 = c):  H is definite on its
      eigenline -> diagonal entry +1 (signature (1,0)).
    - An OFF-LINE PAIR {alpha, beta=c/conj(alpha)} with alpha != beta:  the only invariant
      pairing couples the two eigenvectors (hyperbolic / Krein), H = [[0,1],[1,0]] block
      -> signature (1,1).

    Returns (H, signature=(pos, neg, zero)) ; H is Hermitian, non-degenerate.
    """
    n = len(alphas)
    H = np.zeros((n, n), dtype=complex)
    used = [False] * n
    tol = 1e-9
    for i in range(n):
        if used[i]:
            continue
        a = alphas[i]
        partner = c / np.conjugate(a)
        if abs(a - partner) < tol:
            # fixed point: |a|^2 = c, definite eigenline
            H[i, i] = 1.0
            used[i] = True
        else:
            # find j with alphas[j] ~ partner
            j = None
            for k in range(n):
                if k != i and not used[k] and abs(alphas[k] - partner) < tol:
                    j = k
                    break
            if j is None:
                # partner missing -> the datum is NOT self-dual; no invariant form.
                # (Should not happen for an FE-paired datum.)
                used[i] = True
                continue
            # hyperbolic pair -> Krein block, signature (1,1)
            H[i, j] = 1.0
            H[j, i] = 1.0
            used[i] = used[j] = True
    # signature
    eig = np.linalg.eigvalsh((H + H.conj().T) / 2)
    pos = int(np.sum(eig > tol))
    neg = int(np.sum(eig < -tol))
    zero = int(np.sum(np.abs(eig) <= tol))
    return H, (pos, neg, zero)


def check_invariance(alphas, c, H):
    """Verify F* H F = c H for F = diag(alphas). Returns the max residual."""
    F = np.diag(alphas)
    lhs = F.conj().T @ H @ F
    rhs = c * H
    return float(np.max(np.abs(lhs - rhs)))


def fe_paired(base_angles, c, radii):
    """
    Build an FE-paired eigenvalue multiset from base angles and per-pair radii.
    radius r contributes the pair {sqrt(c)*r*e^{i t}, (sqrt(c)/r)*e^{i t}} which satisfies
    alpha <-> c/conj(alpha): check c/conj(sqrt(c) r e^{it}) = sqrt(c)/r e^{it}. yes.
    r = 1 => on the circle (fixed point, |alpha|=sqrt(c)); r != 1 => off-line pair.
    """
    s = np.sqrt(c)
    al = []
    for t, r in zip(base_angles, radii):
        if abs(r - 1.0) < 1e-12:
            al.append(s * np.exp(1j * t))           # single on-circle eigenvalue (its own partner)
        else:
            al.append(s * r * np.exp(1j * t))        # off-line
            al.append((s / r) * np.exp(1j * t))      # its FE partner
    return np.array(al, dtype=complex)


def main():
    c = 7.0  # the similitude factor (= deg = q)
    print(f"Theorem B' witness:  c = deg = {c}\n")

    angles = [0.5, 1.3, 2.2, 2.9]

    # ON-LINE: all radii = 1  (every |alpha| = sqrt(c))  -> RH holds for the datum
    on = fe_paired(angles, c, radii=[1, 1, 1, 1])
    H_on, sig_on = invariant_form_in_eigenbasis(on, c)
    res_on = check_invariance(on, c, H_on)
    print("ON-LINE  (all |alpha| = sqrt c):")
    print(f"  |alpha| = {sorted(round(abs(a),6) for a in on)}")
    print(f"  invariant form exists, residual F* H F - cH = {res_on:.2e}  (Step A: FREE)")
    print(f"  signature (pos,neg,zero) = {sig_on}   -> POSITIVE-DEFINITE  (Step B holds)\n")

    # OFF-LINE: two pairs off the circle (r != 1) -> RH fails for the datum
    off = fe_paired(angles, c, radii=[1, 1.4, 1, 0.6])
    H_off, sig_off = invariant_form_in_eigenbasis(off, c)
    res_off = check_invariance(off, c, H_off)
    print("OFF-LINE  (two pairs off the circle):")
    print(f"  |alpha| = {sorted(round(abs(a),6) for a in off)}   (sqrt c = {np.sqrt(c):.6f})")
    print(f"  invariant form STILL exists, residual = {res_off:.2e}  (Step A: FREE off-line too)")
    print(f"  signature (pos,neg,zero) = {sig_off}   -> INDEFINITE / KREIN  (Step B fails)\n")

    # The theorem, asserted:
    assert res_on < 1e-9 and res_off < 1e-9, "invariant form must exist at every radius (Step A free)"
    assert sig_on[1] == 0 and sig_on[2] == 0, "on-line must be positive-definite (Step B holds)"
    assert sig_off[1] > 0 and sig_off[2] == 0, "off-line must be indefinite & non-degenerate (Krein)"
    # precise account: each on-line eigenvalue is a (1,0) block; each off-line pair is a (1,1) Krein block.
    n_offline_pairs = 2  # radii [1,1.4,1,0.6] -> two pairs (1.4, 0.6)
    assert sig_off[1] == n_offline_pairs, "neg index = number of off-line (Krein) pairs"
    print("CONCLUSION:")
    print("  Step A (similitude F* H F = cH) is satisfiable at EVERY radius -> it does NOT")
    print("  determine the signature.  Positive-definiteness (Step B) holds IFF every")
    print("  |alpha| = sqrt(c)  (RH for the datum).  Off-line is a consistent Krein form.")
    print("  => no structure seeing only Step A forces Step B.  [Theorem B', QED-by-witness]")


if __name__ == "__main__":
    main()
