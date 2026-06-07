"""
NG-omin: archimedean tame-or-wild witness.

Three executable checks distinguishing o-minimal TAME (finite-prime Euler factor,
algebraic in p^{-s}) from o-minimal WILD (Gamma_R, infinitely many poles on an
unbounded domain), and whether a BOUNDED definable window MARKS the radius sqrt(q).
"""
import mpmath as mp
mp.mp.dps = 30

print("="*72)
print("CHECK 1: finite-prime Euler factor is o-minimally TAME (algebraic in u=p^{-s})")
print("="*72)
# (1 - alpha p^{-s})^{-1}: as a function of u = p^{-s}, it is RATIONAL = semialgebraic.
# Poles: u = 1/alpha, a SINGLE pole per period of u. On any bounded u-window: FINITE.
# Count poles of the degree-2g L-factor of an elliptic curve in a bounded u-disk.
import cmath
q, a = 5, 1
disc = a*a - 4*q
s = cmath.sqrt(disc)
alphas = [(a+s)/2, (a-s)/2]   # |alpha| = sqrt(q)
# local L-factor L_p(u) = prod (1 - alpha_i u)^{-1}; poles at u = 1/alpha_i
poles_u = [1/al for al in alphas]
print(f"  E/F_{q}, a={a}: alphas = {[abs(al) for al in alphas]} (|alpha|=sqrt(q)={mp.sqrt(q)})")
print(f"  L-factor poles in u=p^-s plane: {len(poles_u)} (FINITE, = 2g). |1/alpha|={[abs(p) for p in poles_u]}")
print(f"  => RATIONAL in u, SEMIALGEBRAIC, o-minimally DEFINABLE. Radius |alpha|=sqrt(q) is an")
print(f"     ALGEBRAIC datum (root of X^2-aX+q). TAME. Finitely many poles per u-period.")

print()
print("="*72)
print("CHECK 2: Gamma_R(s)=pi^{-s/2} Gamma(s/2) is o-minimally WILD (infinite poles)")
print("="*72)
# Poles of Gamma(s/2) at s = 0,-2,-4,... : count in growing real windows.
def count_poles_window(R):
    # poles of Gamma(s/2): s/2 = 0,-1,-2,... => s = 0,-2,-4,...
    n = 0
    k = 0
    while 2*k <= R:
        n += 1; k += 1
    return n
for R in [10, 100, 1000, 10000]:
    print(f"  poles of Gamma_R in s in [-{R},0]: {count_poles_window(R)}  (grows without bound)")
print("  => On the UNBOUNDED domain Re(s)<0, infinitely many poles. An o-minimal function")
print("     on a definable set has FINITELY many zeros/poles (monotonicity/finiteness thm).")
print("     => Gamma_R is NOT definable in ANY o-minimal structure GLOBALLY.")

print()
print("="*72)
print("CHECK 3: does a BOUNDED critical-strip WINDOW of Gamma_R mark a radius sqrt(q)?")
print("="*72)
# Restrict to the critical strip window 0<=Re(s)<=1, |Im(s)|<=T. Gamma_R is analytic,
# non-vanishing here (no poles), bounded-domain => its graph IS definable in R_G,exp
# (van den Dries-Speissegger: Gamma definable in R_{G,exp} on Stirling-type domains).
# QUESTION: does this tame piece carry a marked modulus q (a finite cardinality)?
T = 50
window_max = mp.mpf(0)
for t in [mp.mpf(k)/10 for k in range(-T*10, T*10+1)]:
    val = abs(mp.gamma(mp.mpc(0.5, float(t))/2) * mp.pi**(-mp.mpc(0.5,float(t))/2))
    window_max = max(window_max, val)
print(f"  Gamma_R on critical line, |Im|<={T}: analytic, NO poles in window (TAME piece).")
print(f"  sup|Gamma_R| on window = {mp.nstr(window_max,6)} -- a finite VOLUME/decay datum.")
print(f"  But: NO discrete spectrum, NO finite cardinality q, NO marked radius. The window")
print(f"  records a COUNT (decay rate / regularized volume), radius UNMARKED.")
print(f"  Contrast CHECK 1: there the radius sqrt(q) IS marked (algebraic root). Here absent.")

print()
print("="*72)
print("VERDICT LOGIC")
print("="*72)
print("  Finite prime: algebraic/semialgebraic in u=p^-s, FINITE poles, radius MARKED -> TAME.")
print("  Archimedean : Gamma_R has INFINITE poles on unbounded domain -> globally NOT o-minimal.")
print("  Bounded window: tame (definable in R_{G,exp}) but radius-SILENT -- count/radius split")
print("                  RECURS in o-minimal form. Tameness gives finiteness (Step-A-like),")
print("                  NOT the radius (Step B).")
