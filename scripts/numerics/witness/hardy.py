"""H^2(Omega_tau) Hardy-module engine (tracker A + B).

Inner product convention:
    <f,g>_tau = (1/2pi) int_{-inf}^{inf} f(tau+it) conj(g(tau+it)) dt.

With this convention the reproducing kernel of H^2({Re s > tau}) at w has
    ||k_w||^2 = 1/(2 (Re w - tau)),
so for a zero rho = beta + iT the barrier-oracle bound (tracker B) is
    dist(u, V_N(tau)) >= |u(rho)| / ||k_rho|| = |u(rho)| * sqrt(2(beta - tau)),
uniformly in N, because phi_tau(rho)=0 puts rho in every V_N(tau)^perp.

Half-plane module:  phi_tau(s) = ((s-1)/s^2) Z(s),  u(s) = (s-1)/s^2,
    V_N(tau) = span{ phi_tau(s) n^{-s} : 1 <= n <= N }.

Gram entry (real, since the Dirichlet coefficients are real):
    G[n,m] = (n m)^{-tau} * J(log(m/n)),   J(x) = (1/2pi) int |phi_tau(tau+it)|^2 e^{itx} dt.
Target:
    b[n]   = n^{-tau}    * B(log n),       B(x) = (1/2pi) int u(tau+it) conj(phi_tau(tau+it)) e^{itx} dt.
Norm (closed form, object-independent):
    ||u||^2 = (1/4) ((tau-1)^2/tau^3 + 1/tau).

Sampling uses flint acb (accurate); the linear algebra uses float64 for fast
condition-number scans.  certify_u_norm2 / certify_gram_entry use acb.integral
for rigorous enclosures (the Theorem-A tail error is the truncation remainder).
"""
from __future__ import annotations

import numpy as np
from flint import acb, arb, ctx

from .objects import TestObject, cpow


def u_norm2(tau: float) -> float:
    """||u||^2 in H^2(Omega_tau), closed form."""
    return 0.25 * ((tau - 1) ** 2 / tau ** 3 + 1 / tau)


def certify_u_norm2(tau, prec=200):
    """Rigorous enclosure of ||u||^2 = (1/2pi) int |u(tau+it)|^2 dt via the closed
    form; returned as an arb so the caller can compare against u_norm2()."""
    old = ctx.prec
    ctx.prec = prec
    t = arb(tau)
    val = ((t - 1) ** 2 / t ** 3 + 1 / t) / 4
    ctx.prec = old
    return val


def _phi_tau_value(obj: TestObject, s: acb) -> acb:
    return (s - 1) / (s * s) * obj.value(s)


def _u_value(s: acb) -> acb:
    return (s - 1) / (s * s)


class HardyModel:
    """Sampled H^2(Omega_tau) model for one test object at one tau."""

    def __init__(self, obj: TestObject, tau: float, T: float = 400.0,
                 dt: float = 0.04, prec: int = 64):
        self.obj, self.tau, self.T, self.dt = obj, tau, T, dt
        old = ctx.prec
        ctx.prec = prec
        ts = np.arange(0.0, T + dt, dt)
        phis = np.empty(ts.shape, dtype=np.complex128)
        us = np.empty(ts.shape, dtype=np.complex128)
        for k, t in enumerate(ts):
            s = acb(tau, float(t))
            ph = _phi_tau_value(obj, s)
            uu = _u_value(s)
            phis[k] = complex(float(ph.real), float(ph.imag))
            us[k] = complex(float(uu.real), float(uu.imag))
        ctx.prec = old
        self.ts = ts
        self.g = np.abs(phis) ** 2                 # |phi_tau|^2, even in t
        self.h = us * np.conj(phis)                # integrand for B; h(-t)=conj h(t)
        # trapezoid weights on [0,T]; integral over R folds via evenness
        self.w = np.full(ts.shape, dt)
        self.w[0] *= 0.5
        self.w[-1] *= 0.5

    def J(self, x: float) -> float:
        # (1/2pi) int_R |phi|^2 e^{itx} dt = (1/pi) int_0^inf |phi|^2 cos(tx) dt
        return float(np.sum(self.g * np.cos(self.ts * x) * self.w) / np.pi)

    def B(self, x: float) -> complex:
        # (1/2pi) int_R h(t) e^{itx} dt with h(-t)=conj h(t):
        #   = (1/pi) int_0^inf Re[h(t) e^{itx}] dt
        e = np.exp(1j * self.ts * x)
        return complex(np.sum(np.real(self.h * e) * self.w) / np.pi)

    def gram(self, N: int) -> np.ndarray:
        idx = np.arange(1, N + 1)
        G = np.empty((N, N))
        for a, n in enumerate(idx):
            for b, m in enumerate(idx):
                G[a, b] = (n * m) ** (-self.tau) * self.J(np.log(m / n))
        return G

    def target(self, N: int) -> np.ndarray:
        idx = np.arange(1, N + 1)
        return np.array([n ** (-self.tau) * self.B(np.log(n)).real for n in idx])

    def dist2(self, N: int):
        """dist(u,V_N(tau))^2 = ||u||^2 - b^T G^{-1} b, plus the Gram cond number."""
        G = self.gram(N)
        b = self.target(N)
        gi = np.linalg.solve(G, b)
        d2 = u_norm2(self.tau) - b @ gi
        return d2, np.linalg.cond(G)


# --- certified Gram entries (tracker N4) -----------------------------------
def certify_gram_entry(obj: TestObject, n: int, m: int, tau: float,
                       T: float = 60.0, prec: int = 80):
    """Rigorous enclosure of G[n,m] over the finite window |t|<=T, via
    acb.integral on the holomorphic form
        G[n,m] = (nm)^{-tau} (1/2pi) int phi(tau+it) n^{-(tau+it)}
                                          phi(tau-it) m^{-(tau-it)} dt.
    (|.|^2 is written as phi(s)phi(s-bar) using the real Dirichlet coeffs, so the
    integrand is holomorphic.)  The tail |t|>T is the Theorem-A error Err_{N,tau}
    and is NOT included here -- certifying it needs an explicit |zeta(tau+it)| bound."""
    old = ctx.prec
    ctx.prec = prec
    t0 = acb(tau)

    def integ(x, _order):
        sp = t0 + acb(0, 1) * x
        sm = t0 - acb(0, 1) * x
        fp = _phi_tau_value(obj, sp) * cpow(n, -sp)
        fm = _phi_tau_value(obj, sm) * cpow(m, -sm)
        return fp * fm

    val = acb.integral(integ, acb(-T), acb(T)) / (2 * acb.pi())
    ctx.prec = old
    return val  # acb enclosure (the certified window value)


# --- certified Gram tail bound (tracker N4) --------------------------------
def certify_gram_tail_bound(n: int, m: int, tau: float, T: float, prec: int = 120):
    """Rigorous upper bound on the Gram tail |Err_{n,m}| = |(nm)^{-tau} (1/2pi)
    int_{|t|>T} |phi_tau|^2 e^{it log(m/n)} dt|, VALID FOR tau > 1.

    For tau > 1, |zeta(tau+it)| <= zeta(tau) (Dirichlet series), so with
    |phi_tau(tau+it)|^2 = ((tau-1)^2+t^2)/(tau^2+t^2)^2 * |zeta(tau+it)|^2 and the
    elementary majorant (tau^2+t^2)^2 >= t^4:
        (1/2pi) int_{|t|>T} |phi_tau|^2 dt
          <= (zeta(tau)^2/pi) int_T^inf ((tau-1)^2+t^2)/t^4 dt
           = (zeta(tau)^2/pi) ( (tau-1)^2/(3 T^3) + 1/T ).
    Multiply by (nm)^{-tau} (|e^{itx}|=1).  Returned as an arb upper bound.

    For 1/2 < tau <= 1 this returns None: zeta is unbounded on the line there, so a
    rigorous tail needs a WINDOWED SECOND MOMENT  int_{|t|>T}|zeta(tau+it)|^2/t^2 dt
    near the 1-line -- the same analytic input the F5 height-localized criterion needs,
    and the genuinely open sub-task (see forward-theorem.md §F5).
    """
    if tau <= 1.0:
        return None
    old = ctx.prec
    ctx.prec = prec
    t = arb(tau)
    zeta_tau = arb(tau).zeta()
    tail_factor = (zeta_tau ** 2 / arb.pi()) * ((t - 1) ** 2 / (3 * arb(T) ** 3) + 1 / arb(T))
    bound = arb(n * m) ** (-t) * 2 * tail_factor
    ctx.prec = old
    return bound  # arb: certified upper bound on |Err_{n,m}|, tau>1


def certify_gram_entry_full(obj: TestObject, n: int, m: int, tau: float,
                            T: float = 60.0, prec: int = 80):
    """Fully certified G[n,m] enclosure for tau>1: the rigorous finite window
    (certify_gram_entry) widened by the rigorous tail bound.  Returns an acb whose
    ball contains the true G[n,m].  Returns None for tau<=1 (tail not yet certifiable)."""
    tail = certify_gram_tail_bound(n, m, tau, T, prec)
    if tail is None:
        return None
    window = certify_gram_entry(obj, n, m, tau, T=T, prec=prec)
    # widen the window enclosure by a real error ball of radius |tail| (Err is real)
    rad = float(tail.abs_upper())
    return window + acb(arb(0, rad))


# --- barrier oracle (tracker B) --------------------------------------------
def kernel_norm2(beta: float, tau: float) -> float:
    """||k_rho^{(tau)}||^2 = 1/(2(beta-tau)) for rho=beta+iT, beta>tau."""
    return 1.0 / (2.0 * (beta - tau))


def barrier_bound(obj: TestObject, rho: acb, tau: float, prec: int = 120):
    """N-uniform lower bound dist(u, V_N(tau)) >= |u(rho)| / ||k_rho||,
    valid for any tau in (1/2, beta) when Z(rho)=0 (so phi_tau(rho)=0).
    Returns (bound, |u(rho)|, ||k_rho||, |Z(rho)| residual)."""
    old = ctx.prec
    ctx.prec = prec
    rho = acb(rho)
    beta = float(rho.real)
    u_rho = _u_value(rho)
    abs_u = float(u_rho.abs_lower())
    z_resid = float(obj.value(rho).abs_upper())
    ctx.prec = old
    kn = np.sqrt(kernel_norm2(beta, tau))
    return abs_u / kn, abs_u, kn, z_resid
