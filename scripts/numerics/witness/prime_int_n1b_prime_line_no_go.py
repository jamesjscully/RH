"""N1-b' witness: DMP support kills the full Laurent-line comparison.

Context:
  - EE.2 refuted the old Borel N1-b route and re-posed N1-b' on the
    geometric line y from the Quigley-Shah/DMP real-cyclotomic side.
  - Dotto-Moi-Patchkoria, Theorem C/E, compute
        TCR(F_2; 2)^{phi Z/2}
    as a wedge with F_2 in degrees 2n-1 and 2n for n >= 0.
    For k = F_2, both coker(id + Frobenius) and ker(id + Frobenius)
    are F_2.
  - Therefore the TCR fiber has a bottom class in degree -1, but no
    class in degree <= -2.

This is an exact support calculation, not a numerical approximation.  It
does not identify the bottom class y with the Weyl-Tate class t.  It only
rules out the stronger claim that N1-b' supplies a whole Laurent line
F_2[y^{+-1}] comparable to the Lin/Weyl-Tate line F_2[t^{+-1}].

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_prime_line_no_go
"""

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def f2_elements():
    return (0, 1)


def frob(x):
    return x * x % 2


def id_plus_frob(x):
    return (x + frob(x)) % 2


image = {id_plus_frob(x) for x in f2_elements()}
kernel = {x for x in f2_elements() if id_plus_frob(x) == 0}
coker_dim = 1 if image == {0} else 0
ker_dim = 1 if kernel == {0, 1} else 0

gate(
    "N1P1 DMP coefficients for F_2: coker(id+F)=F_2 and ker(id+F)=F_2",
    image == {0} and kernel == {0, 1} and coker_dim == 1 and ker_dim == 1,
    f"image={sorted(image)} kernel={sorted(kernel)}",
)


def dmp_tcr_phi_support(deg):
    """Dimension over F_2 from DMP Theorem C/E for k = F_2.

    The summands are Sigma^{2n-1} H F_2 and Sigma^{2n} H F_2 for n >= 0.
    Thus degree -1 and every degree >= 0 occur; degrees <= -2 do not.
    """
    if deg == -1:
        return 1
    if deg >= 0:
        return 1
    return 0


def laurent_line_support(_deg):
    """Dimension of F_2[t^{+-1}] or F_2[y^{+-1}] in any integer degree."""
    return 1


window = list(range(-6, 7))
dmp_support = {d: dmp_tcr_phi_support(d) for d in window}
line_support = {d: laurent_line_support(d) for d in window}

gate(
    "N1P2 DMP TCR support has bottom degree -1 and vanishes below",
    dmp_support[-1] == 1
    and all(dmp_support[d] == 0 for d in window if d <= -2)
    and all(dmp_support[d] == 1 for d in window if d >= -1),
    f"support={dmp_support}",
)

gate(
    "N1P3 Laurent line support is nonzero in every checked degree",
    all(v == 1 for v in line_support.values()),
    f"support={line_support}",
)

missing_negative_degrees = [
    d for d in window if line_support[d] == 1 and dmp_support[d] == 0
]
gate(
    "N1P4 no graded isomorphism from DMP TCR support to a Laurent line",
    missing_negative_degrees == [-6, -5, -4, -3, -2],
    f"missing={missing_negative_degrees}",
)


# The Lin/Weyl-Tate line F_2[t^{+-1}] needs a class in every degree.  One
# missing degree is enough to kill the full-line reading of N1-b'.
critical_degree = -2
gate(
    "N1P5 full Lin-line comparison fails already in degree -2",
    dmp_tcr_phi_support(critical_degree) == 0
    and laurent_line_support(critical_degree) == 1,
    f"TCR_phi[{critical_degree}]={dmp_tcr_phi_support(critical_degree)} "
    f"Lin[{critical_degree}]={laurent_line_support(critical_degree)}",
)


# Re-record the exact leading-coefficient obstruction from doc 138 in its
# smallest form: phi fixes z^1 coefficients of 1-units, so any coboundary has
# res_1 = 0, while c = (1+z)^-1 has res_1 = 1 over F_2.
def coeff_c(k):
    # (1+z)^-1 = 1 + z + z^2 + ... over F_2.
    return 1 if k >= 0 else 0


gate(
    "N1P6 doc-138 shear obstruction remains nonzero at leading coefficient",
    coeff_c(1) == 1,
    "res_1((1+z)^-1)=1; coboundaries have res_1=0",
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (N1P1-N1P6)")
print(
    "VERDICT: N1-b' cannot be a full Laurent-line comparison at the "
    "TCR^{phi} level.  DMP leaves only a bottom degree -1 class plus "
    "nonnegative degrees; the Lin/Weyl-Tate line has classes in all "
    "degrees.  Surviving work is a bottom-class comparison or a "
    "different carrier/external normalization, not an R1-unblocking line."
)
