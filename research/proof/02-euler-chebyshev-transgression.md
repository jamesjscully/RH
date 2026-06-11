# 02 - Euler-Chebyshev transgression lemma

Status: exact arithmetic identity proved. The missing part is the storage estimate for the
admissible geometric class of test kernels.

## 1. Why this is the first arithmetic lemma

The finite stress calculation produces a shift kernel `k(U)` and samples it at prime-power
logarithms:

```text
sum_{log n < B} 2 Lambda(n)n^{-1/2} k(log n).
```

The smooth PNT surrogate replaces this by

```text
int_a^B 2e^{U/2} k(U)dU.
```

The observed residual is not random noise. After setting

```text
phi(U) = 2e^{-U/2} k(U),
```

the exact discrete-minus-smooth residual is a Chebyshev transgression against

```text
F(U) = psi(e^U) - e^U,
psi(x) = sum_{n <= x} Lambda(n).
```

Here `psi` is Chebyshev's function, not the digamma function in `A_infty`.
No zero-side input is involved.

## 2. Lemma 2 - exact Euler-Chebyshev transgression

Let `a < B`. Let `phi` be `C^1` on `[a,B]`. Define the residual with the endpoint convention
`a < log n <= B`:

```text
R_{a,B}(phi)
  = sum_{a < log n <= B} Lambda(n) phi(log n)
    - int_a^B phi(U)e^U dU.
```

Let

```text
F(U) = psi(e^U) - e^U,
psi(e^U) = sum_{log n <= U} Lambda(n),
```

where `F` is taken right-continuous. Then

```text
R_{a,B}(phi)
  = phi(B)F(B) - phi(a)F(a)
    - int_a^B F(U) phi'(U)dU.
```

Equivalently, if `F_a(U)=F(U)-F(a)`, then the constant part cancels:

```text
R_{a,B}(phi)
  = phi(B)F_a(B) - int_a^B F_a(U)phi'(U)dU
```

Thus the normalized form is

```text
R_{a,B}(phi)
  = phi(B)F_a(B) - int_a^B F_a(U)phi'(U)dU.
```

## 3. Proof

In the Stieltjes sense,

```text
d psi(e^U) = sum_n Lambda(n) delta_{log n}.
```

Therefore

```text
R_{a,B}(phi)
  = int_{(a,B]} phi(U) d(psi(e^U) - e^U)
  = int_{(a,B]} phi(U) dF(U).
```

Since `phi` is continuously differentiable and `F` has bounded variation on finite intervals,
Stieltjes integration by parts gives

```text
int_{(a,B]} phi dF
  = phi(B)F(B) - phi(a)F(a) - int_a^B F(U)dphi(U).
```

Because `dphi(U)=phi'(U)dU`, this is the stated identity. qed

## 4. Weighted Prime-Toeplitz current form

For a geometric stress kernel `k`, define

```text
J_{a,B}(k)
  = sum_{a < log n <= B} 2 Lambda(n)n^{-1/2} k(log n)
    - int_a^B 2e^{U/2}k(U)dU.
```

With `phi(U)=2e^{-U/2}k(U)`, Lemma 2 gives

```text
J_{a,B}(k)
  = phi(B)F(B) - phi(a)F(a)
    - int_a^B F(U)phi'(U)dU.
```

This is the exact transgression functional:

```text
T_{a,B}(k)
  := phi(B)F(B) - phi(a)F(a) - int_a^B F phi',
  phi = 2e^{-U/2}k.
```

The numerical residual scripts are measuring this object for finite critical stresses.

## 5. What remains for the proof

The identity by itself is much weaker than the desired Schur inequality. Crude estimates such as

```text
|R_{a,B}(phi)| <= sup_{[a,B]} |F| * TV(phi)
```

are known to be too wasteful from the finite tests. The next lemma must use the fact that `phi` is
not arbitrary: it comes from a Sonin/Schur stress tensor. The target is a storage inequality of the
form

```text
T_{a,B}(k) + archimedean/Sonin drift >= -available shell margin,
```

or equivalently a Riccati-style estimate that permits negative prefix residuals but proves terminal
Schur positivity.
