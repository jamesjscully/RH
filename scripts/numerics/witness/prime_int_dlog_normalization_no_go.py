"""R1 dlog-normalization witness: invariant form detects, does not pin.

The surviving R1 construction-grade escape after docs 138-140 is an
external phi-invariant normalization, with dlog(1+z) named as the candidate.

This witness checks the exact F_2[[z]] differential calculation.  Let

    phi(z) = z/(1+z),        c = (1+z)^-1,
    omega = dlog(c) = dz/(1+z).

Then omega is phi-invariant.  But if c were a shear coboundary
c = b / phi(b), then

    dlog(c) = dlog(b) + phi^* dlog(b)

would lie in the trace image alpha |-> alpha + phi^* alpha on 1-forms.
For any alpha = A(z) dz, the constant term of alpha + phi^* alpha is zero
because phi(0)=0 and dphi(0)=1, while omega has constant term one.  Hence
the dlog form cannot trivialize the cocycle; it records the same obstruction.

Run:
    python3 -m scripts.numerics.witness.prime_int_dlog_normalization_no_go
"""

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def add(a, b, n):
    return [(a[i] if i < len(a) else 0) ^ (b[i] if i < len(b) else 0) for i in range(n)]


def mul(a, b, n):
    out = [0] * n
    for i, ai in enumerate(a[:n]):
        if not ai:
            continue
        for j, bj in enumerate(b[: n - i]):
            if bj:
                out[i + j] ^= 1
    return out


def pow_series(a, k, n):
    out = [1] + [0] * (n - 1)
    base = a[:n]
    while k:
        if k & 1:
            out = mul(out, base, n)
        k >>= 1
        if k:
            base = mul(base, base, n)
    return out


def compose(a, f, n):
    out = [0] * n
    power = [1] + [0] * (n - 1)
    for coeff in a[:n]:
        if coeff:
            out = add(out, power, n)
        power = mul(power, f, n)
    return out


def inv_one_plus_z(n):
    # (1+z)^-1 = 1 + z + z^2 + ... over F_2.
    return [1] * n


def phi_series(n):
    # z/(1+z) = z + z^2 + z^3 + ...
    return [0] + [1] * (n - 1)


def dphi_series(n):
    # d/dz z/(1+z) = (1+z)^-2 = 1 + z^2 + z^4 + ...
    inv = inv_one_plus_z(n)
    return mul(inv, inv, n)


def phi_pullback_one_form(a, n):
    # phi^*(A(z) dz) = A(phi(z)) * phi'(z) dz.
    return mul(compose(a, phi_series(n), n), dphi_series(n), n)


def trace_one_form(a, n):
    return add(a, phi_pullback_one_form(a, n), n)


def omega(n):
    # dlog((1+z)^-1) = dz/(1+z).
    return inv_one_plus_z(n)


for n in (4, 6, 8, 10, 12):
    phi = phi_series(n)
    phi2 = compose(phi, phi, n)
    z = [0, 1] + [0] * (n - 2)
    gate(
        f"DLG1 phi is an involution at truncation {n}",
        phi2 == z,
        f"phi2={phi2}",
    )

for n in (4, 6, 8, 10, 12):
    om = omega(n)
    phi_om = phi_pullback_one_form(om, n)
    gate(
        f"DLG2 omega=dlog((1+z)^-1) is phi-invariant at truncation {n}",
        phi_om == om,
        f"omega={om} phi*omega={phi_om}",
    )

for n in (4, 6, 8, 10, 12):
    om = omega(n)
    gate(
        f"DLG3 omega has nonzero constant term at truncation {n}",
        om[0] == 1,
        f"omega_0={om[0]}",
    )

for n in (4, 6, 8, 10, 12):
    all_trace_constants_zero = True
    for mask in range(1 << n):
        a = [(mask >> i) & 1 for i in range(n)]
        if trace_one_form(a, n)[0] != 0:
            all_trace_constants_zero = False
            break
    gate(
        f"DLG4 every differential trace alpha+phi*alpha has zero constant at truncation {n}",
        all_trace_constants_zero,
        "constant trace term is a_0+a_0=0",
    )

for n in (4, 6, 8, 10, 12):
    om_tuple = tuple(omega(n))
    trace_image = set()
    for mask in range(1 << n):
        a = [(mask >> i) & 1 for i in range(n)]
        trace_image.add(tuple(trace_one_form(a, n)))
    gate(
        f"DLG5 omega is not in trace image at truncation {n}",
        om_tuple not in trace_image,
        f"|trace_image|={len(trace_image)}",
    )


# The unit-level obstruction from doc 138 and the differential obstruction
# have the same leading bit: res_1(c)=1 and const(dlog c)=1.
gate(
    "DLG6 dlog preserves the leading obstruction bit",
    inv_one_plus_z(3)[1] == 1 and omega(3)[0] == 1,
    "res_1(c)=1, const(dlog c)=1",
)

if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (DLG1-DLG6)")
print(
    "VERDICT: dlog(1+z) is phi-invariant, but it is not a normalization "
    "that trivializes the DDG7b cocycle.  The invariant differential is "
    "outside the trace image and carries the same leading obstruction bit."
)
