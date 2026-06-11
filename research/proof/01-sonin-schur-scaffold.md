# 01 - Sonin support filtration and Schur scaffold

Status: structural scaffold. This is the first layer needed before attacking the storage lemma.

## 1. Convention fixed by the finite model

The numerical model in `scripts/numerics/witness/semilocal_2.py` uses compactly supported even
functions in the log variable `u`. If `h` is such a function, the positive-type Weil test is

```text
g = h * h#,
h#(u) = conjugate(h(-u)).
```

For even real `h`, this gives

```text
g(U) = <h, tau_U h>_{L2}
     = (1/2pi) int_R |hat h(t)|^2 cos(Ut) dt.
```

The pole terms are killed by the two functionals used in the code:

```text
ell_0(h) = hat h(0),
ell_1(h) = hat h(i/2).
```

Because `h` is even, `hat h(i/2) = hat h(-i/2)` in this real model. If we later leave the even
model, the correct pole-killing condition becomes `hat h(0)=hat h(i/2)=hat h(-i/2)=0`.

The finite nested model in `scripts/numerics/witness/prime_nested_cone.py` selects basis functions
whose individual support lies in `[-L/2,L/2]`. Then `g=h*h#` is supported in `[-L,L]`, so Euler atoms
with `log n >= L` do not act on the old subspace.

## 2. Continuum Sonin spaces

Fix `L > 0`. The archimedean form has logarithmic Fourier growth, so the honest starting point is
the form domain, not all compactly supported `L2`. Let

```text
D_L = { h in L2_even(R) :
          supp(h) subset [-L/2,L/2],
          int_R log(2+|t|)|hat h(t)|^2 dt < infinity }.
```

Equip `D_L` with the graph norm

```text
||h||_{D_L}^2 = ||h||_2^2 + int_R log(2+|t|)|hat h(t)|^2 dt.
```

This contains the smooth compactly supported even core and the raised-cosine finite bases used in
the witness scripts. Every `h in D_L` has bounded Fourier evaluations on the strip points needed
here, since

```text
|hat h(z)| <= ||h||_2 ( int_{-L/2}^{L/2} exp(-2 Im(z)u) du )^{1/2}.
```

Therefore `ell_0` and `ell_1` are continuous linear functionals on `D_L`. Define the pole-killed
Sonin window

```text
H_L = ker(ell_0) cap ker(ell_1) subset D_L.
```

For `L < R`, support inclusion gives an isometric map

```text
i_{L,R}: H_L -> H_R.
```

We henceforth identify `H_L` with its image in `H_R`.

## 3. Forms

Use the Fourier transform

```text
hat h(t) = int_R h(u)e^{itu}du.
```

For `h,k in H_R`, define the archimedean bilinear form on this form domain by

```text
A_infty(h,k)
  = -log(pi) <h,k>_{L2}
    + (1/2pi) int_R hat h(t) conjugate(hat k(t))
        Re psi(1/4 + it/2) dt.
```

For a shift `U >= 0`, define the Toeplitz atom

```text
B_U(h,k)
  = <h, tau_U k>_{L2}
  = (1/2pi) int_R hat h(t) conjugate(hat k(t)) e^{iUt} dt.
```

In the even real subspace this is the cosine form used in the scripts.

For a support edge `R`, define the truncated Euler form

```text
P_R(h,k) = sum_{log n < R} 2 Lambda(n)n^{-1/2} B_{log n}(h,k),
M_R = A_infty - P_R.
```

This is the arithmetic side of the Weil form after pole killing.

## 4. Lemma 1 - Sonin filtration and old-block invariance

**Lemma.** Let `0 < L < R`.

1. `H_L` is a closed form-domain subspace of `H_R`.
2. The inclusion `H_L -> H_R` is isometric for the `L2` metric and preserves the Fourier graph
   seminorm.
3. If `U >= L`, then `B_U(h,k)=0` for all `h,k in H_L`.
4. Consequently,

   ```text
   M_R|_{H_L x H_L} = M_L|_{H_L x H_L}.
   ```

**Proof.**

The spaces `D_L` are closed in the global logarithmic Fourier form domain: graph-norm convergence
implies `L2` convergence, and support in a fixed closed interval is preserved under `L2` limits. The
functionals `ell_0` and `ell_1` are continuous on `D_L`, so `H_L` is closed in `D_L`. Since support
inclusion carries `D_L` into `D_R` without changing the `L2` norm or Fourier graph seminorm, and the
same two functionals are killed, it carries `H_L` into `H_R`.

If `h,k in H_L`, then both are supported in `[-L/2,L/2]`. The correlation

```text
B_U(h,k) = int_R h(v) conjugate(k(v-U)) dv
```

can be nonzero only if the intervals `[-L/2,L/2]` and `[U-L/2,U+L/2]` intersect. For `U >= L` their
intersection has measure zero, hence the `L2` correlation is zero.

The only terms appearing in `P_R - P_L` have `L <= log n < R`, so they vanish on
`H_L x H_L`. The archimedean form is independent of the support edge. Therefore
`M_R|_{H_L x H_L}=M_L|_{H_L x H_L}`. qed

## 5. Schur-complement target

Let

```text
S_{L,R} = H_R orthogonal complement of H_L
```

with respect to the `L2` metric, so

```text
H_R = H_L direct_sum_{L2} S_{L,R}.
```

In this splitting write

```text
M_R =
  [ A  C  ]
  [ C* D  ].
```

By Lemma 1, `A` is the already-constructed old margin `M_L` on `H_L`; the new arithmetic data affect
only the shell and the old-shell coupling. If `A > 0`, positivity of the extension is equivalent to

```text
D - C* A^{-1} C >= 0.
```

Equivalently, when `D > 0`,

```text
|| A^{-1/2} C D^{-1/2} || <= 1.
```

This is the continuum form of the nested finite target tested by
`scripts/numerics/witness/prime_nested_cone.py`.

## 6. Next unresolved point

Lemma 1 does not prove positivity. It only gives the correct filtration and shows that the old block
is stable. The next proof step is to control the shell/coupling block by pairing the Schur defect
against admissible stress kernels and then using the Euler-Chebyshev transgression lemma.
