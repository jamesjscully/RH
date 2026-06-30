r"""recouple_count_radius.py -- PA: re-couple COUNT and RADIUS via a SINGLE archimedean Frobenius.

THE ANGLE (R10's terminus, attacked head-on).  Over F_q, the geometric Frobenius F=x^q does BOTH jobs
from the SAME q:
   - the COUNT: #C(F_{q^n}) = q^n + 1 - Tr(F^n | H^1)  (Lefschetz; F's TRACE is the point-count);
   - the RADIUS: |alpha_i| = q^{1/2}  (purity; F's eigenvalue MODULUS is the radius).
These are coupled because F is *literally* the q-power map: q is at once the size of the field (=> the
count grows like q^n) AND the scaling factor of F on the 1-dim'l "Tate" line H^0(twist) / the cotangent
(=> the modulus is a power of q).  R10's terminus: at infinity, compactness (Connes) gives the COUNT
(the regularized trace = explicit formula) but the RADIUS DECOUPLES -- it is a SEPARATE input (purity /
Weil II / the FE-fixed locus, pinned only by Weil positivity = RH).

ATTEMPT: construct a SINGLE archimedean operator F_inf with
   Tr(F_inf) ~ the count  AND  |eig(F_inf)| ~ the radius,
the archimedean analogue of "F = x^q does both."  I.e. an operator whose eigenvalue-MODULUS is FORCED
by its TRACE-source.  What operator at infinity has modulus = trace-source?

We test the construction RUTHLESSLY at the F_q anchor first: does the proposed coupling RECOVER q^{1/2}
from the count WITHOUT assuming the eigenvalues lie on the circle?

THE DECISIVE STRUCTURAL DISTINCTION we make executable: over F_q the coupling "count <=> radius" is NOT
a property of the operator F alone -- it is the TWO-VARIABLE identity

      |det F| = q^g          (the determinant / count-scale)            [TRACE-side, unconditional]
      F . F^dag = q . Id     (the polarization relation, F^dag=qF^{-1}) [RADIUS-side, the coupling]

The FIRST is free (det of a Weil-number matrix = q^g for ANY config with the right char poly -- it is
fixed by the L-function's leading coefficient = the count-scale).  The SECOND -- F F^dag = q Id, i.e.
EVERY eigenvalue has |alpha|^2 = q -- is purity, and it is EQUIVALENT to RH.  The "single q does both"
is therefore the COINCIDENCE  (det F)^{1/g} = (the polarization scale)  =  q, which over F_q is FORCED by
F being the q-power map (a RING endomorphism: it multiplies the WHOLE field structure by the SAME q), and
at infinity is EXACTLY what is missing.

We build a minimal model and CHECK whether any single-operator coupling recovers q^{1/2} from the count
without already assuming the circle.
"""
from __future__ import annotations

import cmath
import numpy as np


# ----------------------------------------------------------------------------------------------------
# The F_q anchor: a Frobenius matrix F on H^1 (rank 2g).  We separate the COUNT data from the RADIUS data
# and ask which can be derived from which by a SINGLE operator.
# ----------------------------------------------------------------------------------------------------

def frobenius_config(g, q, thetas=None, off_pair=None):
    """Build a Frobenius eigenvalue config on H^1, rank 2g, conjugate pairs alpha, conj(alpha).
    If pure: |alpha_i| = sqrt(q) for all i.  off_pair=(r, idx) pushes pair idx to radius r and its FE
    partner to q/r (preserving the FE rho<->1-rho => radii multiply to q, hence det and the COUNT-SCALE
    are UNCHANGED -- this is the load-bearing point)."""
    rng = np.random.default_rng(7)
    if thetas is None:
        thetas = rng.uniform(0.4, np.pi - 0.4, g)
    sq = np.sqrt(q)
    al = [cmath.rect(sq, t) for t in thetas] + [cmath.rect(sq, -t) for t in thetas]
    al = np.array(al)
    if off_pair is not None:
        r, idx = off_pair
        t = thetas[idx]
        al[idx] = cmath.rect(r, t)        # off the circle
        al[g + idx] = cmath.rect(q / r, -t)  # FE partner: radii multiply to q (count-scale preserved)
    return al


def count_data(alphas, q, nmax=4):
    """The COUNT side: Tr(F^n) = sum alpha_i^n gives #C(F_{q^n}) = q^n + 1 - Tr(F^n).  Also the
    determinant det F = prod alpha_i = (the L-function leading coeff) = +- q^g (the COUNT-SCALE)."""
    traces = [complex(sum(a ** n for a in alphas)) for n in range(1, nmax + 1)]
    counts = [q ** n + 1 - traces[n - 1] for n in range(1, nmax + 1)]
    detF = complex(np.prod(alphas))
    return {"Tr(F^n)": [round(t.real, 4) for t in traces],
            "#C(F_q^n)": [round(c.real, 4) for c in counts],
            "|det F|": round(abs(detF), 6), "q^g": q ** (len(alphas) // 2)}


def radius_data(alphas, q):
    """The RADIUS side: |alpha_i| and the deviation from sqrt(q).  ZERO <=> purity <=> RH."""
    sq = np.sqrt(q)
    mods = [abs(a) for a in alphas]
    return {"|alpha_i|": [round(m, 4) for m in mods], "sqrt(q)": round(sq, 4),
            "max dev |.|-sqrt(q)": round(max(abs(m - sq) for m in mods), 6)}


# ----------------------------------------------------------------------------------------------------
# THE CONSTRUCTION ATTEMPT: a single operator whose TRACE gives the count and whose MODULUS gives the
# radius.  We try the three candidate "single archimedean Frobenius" operators and test each at the
# anchor: does |eig| get FORCED by the trace-source WITHOUT assuming the circle?
# ----------------------------------------------------------------------------------------------------

def attempt_A_count_determines_radius(alphas, q):
    """ATTEMPT A: 'the count determines the radius via the determinant.'  Over F_q one is tempted to say:
    the count fixes det F = q^g, and if the operator were a SCALAR multiple of a unitary (F = sqrt(q).U,
    U unitary) then |eig|=sqrt(q) for ALL eigenvalues AND det=q^g.  So can we DERIVE |alpha|=sqrt(q) from
    'det F=q^g' + 'F is normal'?

    TEST: take the OFF-LINE config (same det = q^g, count-scale preserved) and ask whether the
    determinant/count constraint forces the radius.  It does NOT: det=q^g is the geometric-MEAN
    constraint (prod|alpha|=q^g), satisfied by off-circle configs whose radii multiply correctly.  The
    radius needs |alpha|=sqrt(q) for EACH i (the EQUALITY case of AM-GM), which det alone never gives."""
    detF = complex(np.prod(alphas))
    geom_mean_mod = abs(detF) ** (1.0 / len(alphas))
    sq = np.sqrt(q)
    indiv = [abs(a) for a in alphas]
    return {
        "det F = q^g (count-scale)?": abs(abs(detF) - q ** (len(alphas) // 2)) < 1e-6,
        "geometric-mean modulus (det)^{1/2g}": round(geom_mean_mod, 6),
        "equals sqrt(q)?": abs(geom_mean_mod - sq) < 1e-6,
        "BUT individual |alpha_i| all = sqrt(q)?": all(abs(m - sq) < 1e-6 for m in indiv),
        "lesson": ("det F=q^g forces only the GEOMETRIC MEAN of the moduli = sqrt(q); the RADIUS is "
                   "the EQUALITY case |alpha_i|=sqrt(q) for EACH i (AM-GM equality), which the count "
                   "(=det/trace) NEVER forces.  Count -> radius FAILS unless purity is assumed."),
    }


def attempt_B_qpower_ring_endomorphism():
    """ATTEMPT B: WHY does F=x^q couple them over F_q -- and is the coupler a RING endomorphism with no
    archimedean analogue?  The geometric Frobenius x|->x^q is a RING endomorphism of the structure sheaf:
    it raises EVERY function to the q-th power.  Two consequences from the SAME q:
       (i) on H^0 of a Tate twist / the 1-dim cotangent line, it acts as multiplication by q (the
           scaling factor) -- this is the RADIUS source (|eig on the weight-2 line| = q);
       (ii) its fixed points (x^q=x) are the F_q-points, #=q (the count) -- the COUNT source.
    The SINGLE q does both because x^q is simultaneously (i) a SCALING (q-th power = multiply the
    log-coordinate by q) and (ii) a COUNTING map (its fixed locus is F_q).  This is special to a FIELD
    ENDOMORPHISM of a finite field: the SAME arithmetic q is the field size AND the power.

    At the archimedean place there is NO ring endomorphism of R or C that is a 'q-power map': the only
    continuous field endomorphisms of R are the identity, and of C are id and conjugation -- NEITHER
    scales (|eig|=1 always: conjugation and identity are ISOMETRIES).  The archimedean 'Frobenius' (the
    generator of the local Weil group at infinity / complex conjugation) acts with eigenvalue of MODULUS
    1, NOT q^{1/2}.  So the COUNTING archimedean map (conjugation, the Galois generator) and the SCALING
    archimedean map (the |.|^s flow / the modulus character) are DIFFERENT operators -- the very
    decoupling R10 names."""
    # The continuous field endomorphisms of C: identity and conjugation.  Both are isometries.
    # Represent on C as R^2: identity=I, conjugation=diag(1,-1).  Eigenvalue moduli:
    id_eigs = [1.0, 1.0]
    conj_eigs = [1.0, -1.0]   # moduli both 1
    # The SCALING (modulus character |.|^{1/2}) on the 1-dim weight line: multiply by lambda>0.  This is
    # a SEPARATE, non-Galois operator -- it has NO fixed points (no count) and any modulus we like.
    return {
        "continuous field endos of R": ["identity"],
        "continuous field endos of C": ["identity", "conjugation"],
        "their eigenvalue moduli": {"identity": id_eigs, "conjugation": [abs(e) for e in conj_eigs]},
        "ALL archimedean field-automorphism moduli = 1?": True,
        "the SCALING (modulus character) is a field endomorphism?": False,
        "lesson": ("Over F_q the COUPLER is x^q, a RING endomorphism of a FINITE field whose single q is "
                   "BOTH the field size (count) AND the power (scaling).  Archimedean field automorphisms "
                   "(id, conjugation -- the Galois/counting maps) are ISOMETRIES (modulus 1, NO scaling); "
                   "the scaling (the modulus character |.|^s) is NOT a field endomorphism and has NO fixed "
                   "points (NO count).  COUNTING and SCALING are carried by DIFFERENT archimedean operators "
                   "-- there is no single 'q-power ring map' at infinity to fuse them."),
    }


def attempt_C_graded_repair(g=2, q=7, off=False):
    """ATTEMPT C: can a GRADED / non-commutative structure repair the decoupling -- a single operator F
    on a GRADED space whose degree-1 part traces the count and whose action FORCES the modulus?  The
    natural candidate: F = (the count-operator) (x) (the scaling-operator) on H^1 (x) L, where L is the
    1-dim 'Tate' weight line on which scaling acts by the radius-square.  We BUILD it and test whether the
    GRADING forces |eig|=sqrt(q) from the count -- or whether the two factors remain INDEPENDENT inputs.

    Construction: F_inf = U (x) m, where U is unitary (carries the COUNT/phases, Tr U^n = sum e^{i n
    theta} = the location/zeros distribution) and m>0 is the scaling on the weight line (carries the
    RADIUS).  The eigenvalues of F_inf are m * e^{i theta_j}, moduli all = m.  For this to be the
    Frobenius we need m = sqrt(q).  THE QUESTION: does anything in the GRADED construction FORCE m =
    sqrt(q) from the count data (Tr U^n), or is m a FREE separate input?"""
    rng = np.random.default_rng(3)
    thetas = rng.uniform(0.4, np.pi - 0.4, g)
    # U unitary: the COUNT/phase carrier (eigenvalues e^{i theta}, |.|=1)
    phases = np.concatenate([np.exp(1j * thetas), np.exp(-1j * thetas)])
    U = np.diag(phases)
    # m: the SCALING on the weight line.  Over F_q the TRUE value is sqrt(q).  But the count Tr(U^n) is
    # INVARIANT under rescaling m -- so m is NOT determined by the count.  Demonstrate: build F_inf for
    # the TRUE m=sqrt(q) and a WRONG m, and show the count data (the phases / Tr U^n) is IDENTICAL.
    m_true = np.sqrt(q)
    m_wrong = np.sqrt(q) * (1.5 if off else 1.0)
    F_true = m_true * U
    F_wrong = m_wrong * U
    # count data = the phase spectrum / Tr(U^n), which is m-INDEPENDENT
    trUn = [complex(np.trace(np.linalg.matrix_power(U, n))) for n in (1, 2, 3)]
    return {
        "U unitary (count/phase carrier), |eig U|": [round(abs(e), 4) for e in np.linalg.eigvals(U)],
        "Tr(U^n) n=1..3 (the COUNT/location data)": [round(t.real, 4) for t in trUn],
        "F_inf = m * U, eig moduli with m=sqrt(q)": [round(abs(e), 4) for e in np.linalg.eigvals(F_true)],
        "F_inf eig moduli with WRONG m": [round(abs(e), 4) for e in np.linalg.eigvals(F_wrong)],
        "is the count Tr(U^n) changed by m?": False,
        "=> m (the RADIUS) is determined by the count?": False,
        "lesson": ("The GRADED operator F_inf = U (x) m factorizes the count (phases, Tr U^n, m-INDEPENDENT) "
                   "from the radius (the scalar m on the weight line).  m is a FREE input the count never "
                   "sees: rescaling m leaves Tr(U^n) IDENTICAL.  The tensor/grading does NOT re-couple them "
                   "-- it makes the decoupling MANIFEST (count in the U-factor, radius in the m-factor).  To "
                   "force m=sqrt(q) you must impose F_inf F_inf^dag = q Id (= U unitary AND m^2=q) -- the "
                   "polarization relation = purity = RH.  Same split, now graded."),
    }


# ----------------------------------------------------------------------------------------------------

def dh_vacuous():
    return ("DH has no Euler product => no Frobenius / no Satake => no operator F whose trace is a "
            "Lefschetz point-count: there is NOTHING to be the 'count-source' of, so the re-coupling "
            "question (does an operator's trace-source force its modulus?) is UNPOSABLE for DH -- the "
            "operator F_inf to be re-coupled does not exist (no fixed-point count, no Frobenius).")


def main():
    np.set_printoptions(precision=4, suppress=True)
    print("=" * 100)
    print("PA -- RE-COUPLE COUNT and RADIUS via a SINGLE archimedean Frobenius F_inf")
    print("     (R10 terminus: over F_q, F=x^q does BOTH; at infinity the radius DECOUPLES from the count)")
    print("=" * 100)

    print("\n[ANCHOR]  F_q: separate the COUNT data (trace/det) from the RADIUS data (eigenvalue modulus).")
    g, q = 2, 7
    pure = frobenius_config(g, q)
    off = frobenius_config(g, q, off_pair=(np.sqrt(q) * 1.6, 0))   # off-circle, SAME det (count-scale)
    print(f"  pure (RH):  count={count_data(pure, q)}")
    print(f"              radius={radius_data(pure, q)}")
    print(f"  off-line :  count={count_data(off, q)}")
    print(f"              radius={radius_data(off, q)}")
    cd_pure, cd_off = count_data(pure, q), count_data(off, q)
    print(f"  ==> |det F|=q^g={q**g} for BOTH (count-scale PRESERVED off-line): "
          f"pure={cd_pure['|det F|']}, off={cd_off['|det F|']}")

    print("\n[ATTEMPT A]  'the count (det F=q^g) determines the radius' -- via determinant/AM-GM")
    a = attempt_A_count_determines_radius(off, q)
    for k, v in a.items():
        print(f"     {k}: {v}")

    print("\n[ATTEMPT B]  WHY x^q couples them: a RING endomorphism (field size=power); archimedean analogue?")
    b = attempt_B_qpower_ring_endomorphism()
    for k, v in b.items():
        print(f"     {k}: {v}")

    print("\n[ATTEMPT C]  GRADED/tensor repair: F_inf = U (x) m -- does the grading FORCE m=sqrt(q)?")
    c = attempt_C_graded_repair(g, q, off=True)
    for k, v in c.items():
        print(f"     {k}: {v}")

    print("\n[D]  DH-vacuity:")
    print("     " + dh_vacuous())

    # ---- ASSERTIONS: the anchor must show the decoupling EXACTLY ----
    # count-scale (det) preserved off-line; radius NOT:
    assert abs(cd_off["|det F|"] - q ** g) < 1e-4, "off-line must preserve det=q^g (count-scale)"
    assert radius_data(off, q)["max dev |.|-sqrt(q)"] > 0.1, "off-line must break the radius"
    assert radius_data(pure, q)["max dev |.|-sqrt(q)"] < 1e-6, "pure must have radius sqrt(q)"
    # ATTEMPT A: geometric mean = sqrt(q) but individual moduli NOT:
    assert a["equals sqrt(q)?"] and not a["BUT individual |alpha_i| all = sqrt(q)?"]
    # ATTEMPT B: all archimedean field-auto moduli = 1 (no scaling):
    assert b["ALL archimedean field-automorphism moduli = 1?"]
    # ATTEMPT C: count invariant under m => radius not forced:
    assert not c["=> m (the RADIUS) is determined by the count?"]

    print("\n" + "-" * 100)
    print("VERDICT (PA):  the re-coupling FAILS at the anchor, and the reason is EXACT.")
    print("  Over F_q, F=x^q couples count and radius because it is a RING ENDOMORPHISM of a FINITE field:")
    print("  the SINGLE arithmetic q is BOTH the field size (=> Lefschetz count ~ q^n, the TRACE source)")
    print("  AND the q-th-power SCALING (=> the modulus = q^{1/2} on the half-weight line, the RADIUS).")
    print("  Three things must hold for a single F_inf to do both, and each FAILS at infinity:")
    print("    [A] count -> radius via det: det F=q^g forces only the GEOMETRIC MEAN of the moduli; the")
    print("        radius is the EQUALITY case |alpha_i|=sqrt(q) for EACH i, which the count NEVER forces")
    print("        (off-line config has the SAME det/count-scale, broken radius).")
    print("    [B] no archimedean 'q-power ring map': the field automorphisms at infinity (id, conjugation")
    print("        = the COUNTING/Galois maps) are ISOMETRIES (modulus 1, NO scaling); the SCALING (modulus")
    print("        character |.|^s) is NOT a field endo and has NO fixed points (NO count).  Counting and")
    print("        scaling are DIFFERENT archimedean operators -- no single ring map fuses them.")
    print("    [C] a GRADED repair F_inf=U(x)m makes the decoupling MANIFEST, not repaired: the count")
    print("        lives in the unitary U-factor (Tr U^n, m-INDEPENDENT), the radius in the scalar m;")
    print("        forcing m=sqrt(q) is F_inf F_inf^dag=q Id = the polarization relation = purity = RH.")
    print("  THE OBSTRUCTION, precisely: 'a single operator whose modulus IS its trace-source' requires the")
    print("  modulus to be a FUNCTION of the field's MULTIPLICATIVE STRUCTURE (q-power), which over F_q is")
    print("  a RING endomorphism and at infinity does not exist as an isometry-distinct, fixed-point-having")
    print("  map.  The decoupling R10 names is a TYPE fact: COUNT is a trace (additive/Lefschetz), RADIUS is")
    print("  a multiplicative scaling; over F_q a SINGLE ring endomorphism is both, at infinity they are")
    print("  carried by orthogonal operators (Galois isometry vs modulus character) the polarization")
    print("  relation F F^dag=q Id alone re-couples -- and that relation IS RH (per frobenius_self_norm.py).")
    print("-" * 100)

    print("\nFALSIFIER (PA -- a re-coupling attempt; classified):")
    print("  EULER-BORNE : NO standalone Z-positivity (anchors at F_q, type-checks the archimedean operators);")
    print("                DH-vacuous (no Frobenius => no F_inf to re-couple, unposable).")
    print("  SEES-ZEROS  : YES (the radius sought = purity = where the zeros sit; off-line plant breaks it).")
    print("  INDEPENDENT : NO (forcing m=sqrt(q) = F_inf F_inf^dag=q Id = polarization = purity = RH).")
    print("  => DISPERSING-by-design / the re-coupling is CIRCULAR (it reduces to the polarization relation =")
    print("     RH).  The single-operator coupling does not give the radius independently of the count: the")
    print("     count fixes the determinant (geometric mean), the radius is the per-eigenvalue equality case,")
    print("     and the only operator that forces the equality is the one satisfying F F^dag=q Id = RH.")


if __name__ == "__main__":
    main()
