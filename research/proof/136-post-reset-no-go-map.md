# 136 - The post-reset no-go map: the analytic frontier is closed

Status: consolidation / synthesis, 2026-06-16. This is not a new attack;
it folds the five post-reset no-go cycles (docs 130, 132, 133, 134, 135)
into one structural map and records the program's banked product: every
banked analytic route to RH factors through a single missing arithmetic
object. It is the second branch of STRATEGY sec 4's win-win, executed.

## 1. The one missing object

```text
End(S^2/Z) with a positive Rosati involution F^dag = (deg) F^{-1}.

  The self-product correspondence algebra on the compactified arithmetic
  line, whose self-norm <F,F> = deg(F) is the sum over zeros (a norm iff
  RH). Present over F_q (F = Frobenius; <F,F> = 2gq unconditionally; its
  positivity is the Riemann hypothesis for the curve). ABSENT over Z: the
  square is affine over the sphere, ring maps HZ -> HZ are trivial, the
  Ext tower is untruncated (doc 18), so there is no correspondence on
  S^2/Z and the only self-norm is the RH-conditional sum over zeros.

  = the Connes-Consani C x C / scaling-site Jacobian = the F_1 / Connes /
  Deninger object (STRATEGY sec 1, sec 7). Building it is the program's
  sole remaining target.
```

## 2. The map: four faces, one object

The five cycles attacked the missing object from four directions. Each
closed with the same structure (sec 3).

```text
face                doc      free / DH-shared half          RH-content half
------------------- -------- ------------------------------ ------------------
second evaluation   130      congruence / transport         unforced odd slot
                             (Sylvester-locked, RH-silent)   (needs properness)
radius / MODULUS    132,133  determinant edge p^{k-1} / FE   even split |a|=|b|
                             (Euler-free, RH-independent)    (= RH-for-f)
reality / PHASE     134      FE relation F F^dag = c.Id      positivity theta F
                             (holds for DH, RH-silent)       theta = F* (= RH)
phase certificate   135      arch(g) = Gamma_R phase         prime(g) signed;
                             (Euler-free, DH-shared)         positivity = the
                                                             doc-13 r = RH
```

## 3. The structural invariant (why every face collapses the same way)

```text
INVARIANT 136.1. In every face, a banked candidate splits into

    [FREE half]  the functional-equation / edge / modulus / relation /
                 archimedean datum -- Euler-free or RH-independent, and
                 SHARED VERBATIM with the RH-false Davenport-Heilbronn
                 function (it has a FE, no Euler product); hence RH-silent;
    +
    [RH half]    the split / phase / positivity / reality / second-evaluation
                 datum -- which is RH-equivalent (or needs properness).

Every banked construction supplies the FREE half; NONE supplies the RH
half. The two are separated by exactly the missing object's positive Rosati
involution F^dag = (deg) F^{-1}: over F_q the Frobenius correspondence joins
them (the edge's square root, the phase, the reality, the odd slot are all
forced by Frobenius acting with weights, Weil II); over Z that joiner is
absent, so the RH half floats free and is reachable only by importing RH.
```

This is why the DH kill-test (STRATEGY sec 5) is decisive throughout: the
free half holds for DH, so any certificate built from it is RH-silent; the
RH half detects DH's off-line zeros only by supplying their location, which
is RH-strength.

## 4. The exhaustion (what was swept, with mechanism)

```text
LOCAL, per-prime (doc 132). Every per-prime radius supplier is (S)
  self-supplied = RH, (C) Sylvester-locked / FE-shared = RH-silent, or (E)
  absent carrier. The Euler edge is free; the even split is the acting
  map's own modulus. Witnesses cw_radius_assembly, cc_radius_deformation_
  probe (flip_tracks=IMPORTED_ONLY), ns_hodge_index_duality, kahler_forcing.

GLOBAL suppliers (doc 133). Rankin-Selberg at the edge presupposes
  Ramanujan (absolute convergence past the edge = the purity bound); CC
  curve-level integer RR + Pontryagin-Serre duality is FE-blind at the
  radius (archimedean Kahler form DH-shared, arakelov_signature
  max|A_zeta-A_DH|=0); both banked flows (CC scaling site, dBN) reproduce
  only the DH-shared FE/Haar self-dual axis and carry no discrete arithmetic
  gap q. The local even split is automorphy-firewalled (Deligne), not a
  sub-target. Witnesses rs_pole_radius_probe, scaling_site_radius,
  schmid_sl2_orbit_radius, dbn_flow_functional, probe_pa_local_split_escape.

OPERATOR / reality (doc 134). Hilbert-Polya positivity by axiom imports RH
  (off-line admits a consistent Krein-indefinite self-duality;
  cstar_hermitian_witness NOGO_COMPLETE); forcing it pins to the single
  relation F^dag = (deg) F^{-1} on End(S^2/Z), absent over Z. The only
  unconditional positivity (sym^2 modulus) controls the wrong half.
  Witnesses positivity_reality, frobenius_self_norm, operator_domination.

PHASE certificate (doc 135). The argument-principle / winding positivity
  for arg m reduces term-by-term to the Weil explicit formula
  int w g = arch(g) - prime(g), manifest-positive only via the doc-13 zero
  cross-correlation = uniform tau < 1 = RH; it holds for the genuine DH
  function (RH-silent) or detects it at RH-strength. Witnesses
  probe_pa_argm_to_tau, probe_pb_dh_phase_killtest, probe_pc_weaker_phase_
  escape, phase_winding, off_diagonal, explicit_formula.
```

Every banked analytic carrier -- local and global, modulus and phase -- is
killed and the mechanism named. No banked supplier, of any kind, fixes the
RH half without RH.

## 5. Relation to STRATEGY: the win-win negative, executed

```text
STRATEGY sec 4 (the win-win): "Either a structured family's limit
obstruction is a provable forcing structure (a real step toward RH), or
every analytic family converges to a dispersing equivalence -- strong
evidence that all analytic obstructions factor through the missing F_1
object. The negative result is itself worth proving."

The post-reset cycles are that NEGATIVE BRANCH, proven (at the program's
standard rigor) for the banked analytic corpus: every banked analytic
obstruction -- count, modulus, phase, operator -- factors through the one
missing object End(S^2/Z). The forcing structure does not live in the
analytic data; it lives in (or requires) the unbuilt arithmetic
correspondence. This is the doc-13 tracking equivalence (RH <=> uniform
tau < 1 = zero cross-correlation) seen from every analytic side at once.
```

## 6. Honest scope and limits

```text
- RELOCATION, not absolute impossibility. Each cycle closes the BANKED /
  level-2 candidates for its face and relocates the wall to the missing
  object (doc 135 sec 6). None is an unconditional impossibility theorem;
  a genuinely new mechanism outside STRATEGY sec 1's five templates is
  unconstructed, NOT excluded (doc 133's downgrade, kept honest).
- RIGOR. The witnesses are mpmath / python-flint FLOAT illustrations
  (structural, functional-equation / argument-principle / explicit-formula
  level, not threshold-sensitive). Promoting any kill to a citable external
  theorem needs ball-arithmetic certification (the banked interval ladder).
- SCOPE OF THE DH KILL-TEST. It certifies RH-silence of the free half and
  RH-strength of the RH half; it does not by itself prove the missing object
  cannot exist (it cannot -- the object exists over F_q).
```

## 7. The single remaining target + standing kill-ledger

```text
TARGET: build End(S^2/Z) with a positive Rosati involution F^dag =
(deg) F^{-1} (the CC C x C / scaling-site Jacobian). Geometric / arithmetic,
not an inequality on the line. A famous, decades-open construction (F_1 /
Connes / Deninger); a long arc, to be scoped as such, not as a quick cycle.

STANDING KILL-LEDGER (any future analytic proposal trips one of these):
  KILL-RAD.1/2/3      (doc 132)  self-supplied split / Sylvester-FE / absent.
  KILL-RAD133.1-4     (doc 133)  weaker-band radius-silent / FE-blind global /
                                 false-flow-analogy.
  KILL-REAL.1/2/3     (doc 134)  positivity-by-axiom / modulus-for-phase /
                                 missing-algebra evasion.
  KILL-PHASE.1/2/3/4  (doc 135)  holds-for-DH / zero-correlation-in-disguise /
                                 modulus-for-phase / partial-count.
DO NOT re-attack the analytic faces; each is closed. Engage the construction
frontier ONLY with a runnable witness or a stated theorem -- never a schema
(doc 129).
```

## 8. Witness ledger (the computational base of this map)

```text
cw_radius_assembly              edge Euler-free / split not supplied
cc_radius_deformation_probe     NS flip edge-blind, tracks imported split
ns_hodge_index_duality          weight-2 NS pairing, flips with the zeros
kahler_forcing                  forcing factors; radius = the residue
arakelov_signature              max|A_zeta - A_DH| = 0 (CC arm DH-shared)
rs_pole_radius_probe            RS pole at edge presupposes Ramanujan
scaling_site_radius             marked arithmetic q absent; gapless
schmid_sl2_orbit_radius         SL(2)-orbit gives parity, not the radius
dbn_flow_functional             no reality-monotone Euler flow functional
probe_pa_local_split_escape     eps-band radius-silent (automorphy firewall)
cstar_hermitian_witness         positivity-by-axiom imports RH (NOGO_COMPLETE)
positivity_reality              reality = phase; sym^2 modulus = wrong half
frobenius_self_norm             the wall = the missing Rosati F^dag=(deg)F^-1
operator_domination             Sylvester locks all *-congruences (26 confs)
probe_pa_argm_to_tau            int w g = arch - prime; positivity = doc-13 r
probe_pb_dh_phase_killtest      genuine DH: on-line w>=0 verbatim (RH-silent)
probe_pc_weaker_phase_escape    no weaker Euler-borne phase positivity
phase_winding                   w = w_arch - w_zeros; w_arch DH-shared
off_diagonal                    Weil Gram PSD on zeros, indefinite off-line
explicit_formula                zeta prime side = von Mangoldt to 2.5e-60
```

All lead-reran exit 0 across cycles 1-5. This map is the program's banked
analytic product; the next chapter is the construction of End(S^2/Z).
