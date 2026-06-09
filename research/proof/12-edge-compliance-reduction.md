# 12 - The edge-compliance reduction (exact per-edge storage structure)

Status: derived exactly. Conditional on nothing for the rank-exact form; the one-mode
form uses 11(c)'s rank-one collapse with its computable sigma_2 correction. This is
the realization skeleton of doc 10, obtained by derivation rather than construction.

## 1. The old block is frozen within an edge

Along the chronological chain of one edge L -> R, every cell update has

```text
E_A^{(j)} = 0    EXACTLY
```

(Lemma 1.3: all atoms and all smooth mass of the edge have U >= L, hence vanish on
H_L x H_L). Therefore A_j = A for the whole chain, X_j = A^{-1} C_j, and the Schur
complement is EXPLICITLY quadratic in the accumulated coupling:

```text
S_j = D_j - C_j^* A^{-1} C_j,
D_j = D_0 + sum_{k<=j} E_D^{(k)},    C_j = C_0 + sum_{k<=j} E_C^{(k)}.
```

No stepwise Riccati recursion is needed within an edge; the within-edge "Riccati
square" of the witnesses is identified below as the compliance term.

## 2. The compliance form

By 11(c), each E_C^{(k)} factors (to sigma_2 ~ 1e-4 relative, exactly at rank <= 2)
through the leading terminal edge-jet functional, represented by a FIXED vector
u in the old coordinates:

```text
E_C^{(k)} ~ u . (t^{(k)})^*,
t^{(k)}_m = int_{I_k} rho_m(w(U)) d mu_0(U)  -  m_k rho_m(w(U_k)),
rho_m(w) = (q_u * r_{y_m})(w)   (the edge-convolution profile, doc 11 exact),
```

i.e. the cell's smooth-minus-atom sampling of the edge-convolution profile -
precisely the beta-surplus integrand of docs 07-08, now derived as the general
coupling datum. Let

```text
alpha = u^* A^{-1} u   > 0      (the EDGE COMPLIANCE: all old-space memory),
b     = C_0^* A^{-1} u          (shell vector),
v_j   = sum_{k<=j} t^{(k)}      (accumulated arithmetic transgression).
```

Then, exactly (modulo the stated rank correction),

```text
S_j = S_0 + sum_{k<=j} E_D^{(k)} - (v_j b^* + b v_j^*) - alpha v_j v_j^*.
```

## 3. What this says

```text
1. The ENTIRE influence of the old space on an edge chain is TWO objects:
   the scalar alpha and the vector b. The growing window, the cumulative Euler
   history, the eigmin(A) decay - all of it enters one edge only through alpha
   (and b). This is the one-mode realization state, derived.
2. The arithmetic enters only through (i) the transgression numbers v_N (the
   doc-02 Chebyshev transgression of the edge-convolution profiles - the
   beta-surplus data) and (ii) the shell-bulk sum of E_D.
3. The within-edge storage theorem is a ds-dimensional (ds ~ 2) quadratic
   matrix inequality:
       terminal positivity  <=>
       alpha v_N v_N^* + (v_N b^* + b v_N^*)  <=  S_0 + sum E_D.
4. The witnesses' "Riccati square cost" = alpha |v|^2 - the compliance term.
   It does not vanish; it is now interpretable: the old space charges the
   arithmetic transgression at rate alpha for crossing the edge.
5. The cross-edge induction is a recursion in (alpha, b, S) driven by exact
   transgression data: the full theorem = uniform control of this scalar
   recursion along the filtration. The exponential decay of eigmin(A) appears
   here as growth of alpha (compliance blow-up) - the knife-edge in its final
   coordinate: prove that v_N shrinks (equidistribution of atoms against the
   convolution profile) at the rate alpha grows.
```

## 4. Theorem-shaped residue

```text
Edge-compliance storage theorem (the target, restated exactly):
For every edge of the filtration, with alpha, b, S_0, E_D, v as above,

    alpha v v^* + v b^* + b v^*  <=  S_0 + sum E_D .

Arithmetic side: v is a Chebyshev-transgression vector of one-sided
edge-convolution profiles (doc 02 identity applies verbatim).
Geometric side: alpha, b, S_0, E_D from the archimedean form and history.
```

This replaces both the per-cell lemmas (refuted in 09) and the abstract storage
LMI (vacuous as bare existence): it is the exact, minimal, per-edge statement the
realization must produce uniformly. The fail-closed witnesses to build next:
compute (alpha, b, v_N, S_0 + sum E_D) along the ladder; verify the inequality
margin reproduces eigmin(H); track alpha growth vs |v_N| decay; run DH (its v
should violate). If alpha |v_N|^2 fails to shrink relative to margins at larger R,
the one-mode form is insufficient and the rank-2 exact form takes over.
