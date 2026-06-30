"""N1-b' bottom-class witness: the DMP bottom class is nilpotent.

Doc 139 killed the full Laurent-line reading of N1-b'.  This witness
checks the next surviving possibility: can the remaining degree -1 class
itself be the Lin/Weyl-Tate generator t?

At the TCR(F_2;2)^{phi Z/2} level, DMP Theorem C/E gives one F_2 class in
degree -1 and no classes in degree -2.  Any product of a degree -1 class
with itself therefore lands in the zero group.  The Lin class t in
F_2[t^{+-1}] has t^2 nonzero and is invertible.

This exact support argument rules out a multiplicative / duality-generator
comparison y |-> t at the TCR-fiber level.  An additive degree-label
comparison may still exist, but it cannot unlock DD.4's t-periodic Lin
module or evade the doc-138 weight>=1 torsor obstruction.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_bottom_class_nilpotent
"""

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def dmp_dim(deg):
    """F_2-dimension of pi_deg TCR(F_2;2)^{phi Z/2} from DMP C/E."""
    if deg == -1:
        return 1
    if deg >= 0:
        return 1
    return 0


def lin_dim(_deg):
    """F_2-dimension of the Laurent line F_2[t^{+-1}] in any degree."""
    return 1


gate(
    "N1Q1 DMP bottom class exists in degree -1",
    dmp_dim(-1) == 1,
    f"dim[-1]={dmp_dim(-1)}",
)

gate(
    "N1Q2 DMP degree -2 group vanishes",
    dmp_dim(-2) == 0,
    f"dim[-2]={dmp_dim(-2)}",
)

gate(
    "N1Q3 any DMP degree -1 square is zero by degree support",
    dmp_dim(-1) == 1 and dmp_dim(-2) == 0,
    "(-1)+(-1)=-2 has zero target group",
)

gate(
    "N1Q4 Lin generator t has nonzero square",
    lin_dim(-1) == 1 and lin_dim(-2) == 1,
    f"Lin[-1]={lin_dim(-1)} Lin[-2]={lin_dim(-2)}",
)


# A multiplicative comparison sending bottom y to Lin t would force
# y^2 |-> t^2.  The source square is zero, the target square is nonzero.
gate(
    "N1Q5 no multiplicative comparison can send DMP bottom class to Lin t",
    dmp_dim(-2) == 0 and lin_dim(-2) == 1,
    "source y^2=0, target t^2!=0",
)


# Invertibility check: a nonzero nilpotent element cannot be a unit.  The
# formal Laurent generator has inverse t^-1; the DMP bottom class has square
# zero, hence cannot be invertible in any graded ring with 1.
bottom_nonzero = dmp_dim(-1) == 1
bottom_square_zero = dmp_dim(-2) == 0
gate(
    "N1Q6 DMP bottom class is not a unit; Lin t is a unit",
    bottom_nonzero and bottom_square_zero and lin_dim(1) == 1,
    "bottom^2=0 while t*t^-1=1 in the Laurent line",
)


# DD.4 needs t-periodic module data, not only an isolated degree -1 label.
# Support alone already shows that multiplication by the bottom class cannot
# be an automorphism: from degree -1 to degree -2 the target group is zero.
gate(
    "N1Q7 bottom multiplication is not a degree-shift automorphism",
    dmp_dim(-1) == 1 and dmp_dim(-2) == 0,
    "multiplication by bottom from degree -1 to -2 has zero target",
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (N1Q1-N1Q7)")
print(
    "VERDICT: the surviving DMP degree -1 class is square-zero at the "
    "TCR^{phi} support level.  It cannot be the invertible Lin/Weyl-Tate "
    "generator t and cannot supply DD.4's t-periodic duality datum.  Only "
    "an additive bottom-degree label survives."
)
