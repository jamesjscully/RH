using LinearAlgebra
using Printf
using ForwardDiff
using QuadGK

include("generated/active23_data.jl")

const DATA = ACTIVE23
const RTOL = 1e-7

one_side(u, center, hw) = begin
    rel = (u - center) / hw
    abs(rel) <= one(rel) ? cos(pi * (u - center) / (2hw))^2 : zero(rel)
end

raised_even(u, center, hw) = one_side(u, center, hw) + one_side(-u, center, hw)

function normalize_y(y)
    n = sqrt(sum(abs2, y))
    y ./ n
end

function coeffs(data, y)
    data.coeff_map * y
end

function qval(data, y, r)
    c = coeffs(data, y)
    u = data.edge - r
    s = zero(eltype(c))
    @inbounds for i in eachindex(c)
        s += c[i] * raised_even(u, data.centers[i], data.half_width)
    end
    s
end

function Kval(data, y, w)
    val, _ = quadgk(r -> qval(data, y, r) * qval(data, y, w - r),
                    0.0, w; rtol=RTOL)
    val
end

weight(data, w) = 2 * exp((2 * data.edge - w) / 2)

function weighted_current(data, y)
    val, _ = quadgk(w -> weight(data, w) * Kval(data, y, w),
                    data.w_min, data.w_max; rtol=RTOL)
    val
end

function beta(data, yraw)
    y = normalize_y(yraw)
    katom = Kval(data, y, data.w_atom)
    weighted_current(data, y) / (data.smooth_mass * katom)
end

before(data, yraw) = begin
    y = normalize_y(yraw)
    dot(y, data.S * y)
end

square_ray(data, yraw) = begin
    y = normalize_y(yraw)
    dot(y, data.square * y)
end

after(data, yraw) = begin
    y = normalize_y(yraw)
    dot(y, (data.S + data.G) * y)
end

function required_beta(data, yraw)
    y = normalize_y(yraw)
    katom = Kval(data, y, data.w_atom)
    data.atom_weight / data.smooth_mass +
        (max(zero(katom), -dot(y, data.S * y)) + dot(y, data.square * y)) /
        (data.smooth_mass * katom)
end

surplus(data, yraw) = beta(data, yraw) - required_beta(data, yraw)

ytheta(t) = [cos(t), sin(t)]

theta_of(y) = begin
    t = atan(y[2], y[1])
    t < 0 ? t + pi : t
end

function metrics_theta(t)
    y = ytheta(t)
    katom = Kval(DATA, y, DATA.w_atom)
    b = beta(DATA, y)
    req = required_beta(DATA, y)
    (
        theta = t,
        before = before(DATA, y),
        after = after(DATA, y),
        K_atom = katom,
        beta = b,
        required = req,
        surplus = b - req,
    )
end

function derivs_theta(t)
    (
        d_before = ForwardDiff.derivative(x -> before(DATA, ytheta(x)), t),
        d_after = ForwardDiff.derivative(x -> after(DATA, ytheta(x)), t),
        d_beta = ForwardDiff.derivative(x -> beta(DATA, ytheta(x)), t),
        d_required = ForwardDiff.derivative(x -> required_beta(DATA, ytheta(x)), t),
        d_surplus = ForwardDiff.derivative(x -> surplus(DATA, ytheta(x)), t),
    )
end

surplus_derivative(t) = ForwardDiff.derivative(x -> surplus(DATA, ytheta(x)), t)
surplus_second(t) = ForwardDiff.derivative(surplus_derivative, t)
S_theta(t) = before(DATA, ytheta(t))
Katom_theta(t) = Kval(DATA, ytheta(t), DATA.w_atom)

function wrap_theta(t)
    out = mod(t, pi)
    out < 0 ? out + pi : out
end

function refine_surplus_stationary(t0; steps = 8)
    t = t0
    for _ in 1:steps
        g = surplus_derivative(t)
        h = surplus_second(t)
        if !isfinite(g) || !isfinite(h) || abs(h) < 1e-10
            break
        end
        t = wrap_theta(t - g / h)
    end
    metrics_theta(t)
end

function bisect_root(f, a, b; steps = 60)
    fa = f(a)
    fb = f(b)
    if !isfinite(fa) || !isfinite(fb)
        return NaN
    end
    if abs(fa) < 1e-12
        return a
    end
    if abs(fb) < 1e-12
        return b
    end
    if fa * fb > 0
        return NaN
    end
    lo, hi = a, b
    flo, fhi = fa, fb
    for _ in 1:steps
        mid = (lo + hi) / 2
        fm = f(mid)
        if !isfinite(fm)
            return NaN
        end
        if abs(fm) < 1e-13
            return mid
        end
        if flo * fm <= 0
            hi = mid
            fhi = fm
        else
            lo = mid
            flo = fm
        end
    end
    (lo + hi) / 2
end

function unique_sorted(vals; tol = 1e-7)
    clean = sort([wrap_theta(v) for v in vals if isfinite(v)])
    out = Float64[]
    for v in clean
        if isempty(out) || abs(v - out[end]) > tol
            push!(out, v)
        end
    end
    if length(out) > 1 && abs((out[1] + pi) - out[end]) <= tol
        pop!(out)
    end
    out
end

function roots_on_circle(f; n = 720)
    ts = collect(range(0.0, pi; length = n + 1))
    vals = [f(t) for t in ts]
    roots = Float64[]
    for i in 1:n
        a, b = ts[i], ts[i + 1]
        fa, fb = vals[i], vals[i + 1]
        if !isfinite(fa) || !isfinite(fb)
            continue
        end
        if abs(fa) < 1e-10
            push!(roots, a)
        elseif fa * fb < 0
            r = bisect_root(f, a, b)
            if isfinite(r)
                push!(roots, r)
            end
        end
    end
    unique_sorted(roots)
end

function safe_surplus_derivative(t)
    if S_theta(t) < -1e-9 && Katom_theta(t) > 1e-10
        surplus_derivative(t)
    else
        NaN
    end
end

function kkt_candidates()
    s_roots = roots_on_circle(S_theta; n = 720)
    k_roots = roots_on_circle(Katom_theta; n = 720)
    d_roots = roots_on_circle(safe_surplus_derivative; n = 720)
    interior = [
        metrics_theta(t)
        for t in d_roots
        if S_theta(t) < -1e-9 && Katom_theta(t) > 1e-10
    ]
    s_boundary = [metrics_theta(t) for t in s_roots if Katom_theta(t) > 1e-10]
    k_boundary = [
        (
            theta = t,
            before = before(DATA, ytheta(t)),
            after = after(DATA, ytheta(t)),
            K_atom = Katom_theta(t),
        )
        for t in k_roots
        if before(DATA, ytheta(t)) < 1e-8
    ]
    (
        s_roots = s_roots,
        k_roots = k_roots,
        d_roots = d_roots,
        interior = interior,
        s_boundary = s_boundary,
        k_boundary = k_boundary,
    )
end

function scan_theta(n = 181)
    rows = [metrics_theta((i - 1) * pi / n) for i in 1:n]
    neg = filter(r -> r.before < -1e-9 && r.K_atom > 1e-12, rows)
    best = argmin([r.surplus for r in neg])
    refined = refine_surplus_stationary(neg[best].theta)
    active_t = theta_of(DATA.active_vec)
    active = metrics_theta(active_t)
    (
        rows = rows,
        negative_beta = neg,
        active = active,
        min_surplus = neg[best],
        refined_min_surplus = refined,
    )
end

function print_row(label, row)
    @printf("%-16s theta=%+.6f S=%+.6e after=%+.6e Katom=%+.6e beta=%+.6f req=%+.6f surplus=%+.6f\n",
            label, row.theta, row.before, row.after, row.K_atom, row.beta, row.required, row.surplus)
end

function print_derivs(label, t)
    d = derivs_theta(t)
    @printf("%-16s dS=%+.6e dAfter=%+.6e dBeta=%+.6e dReq=%+.6e dSurplus=%+.6e\n",
            label, d.d_before, d.d_after, d.d_beta, d.d_required, d.d_surplus)
end

function print_kkt_candidates(cands)
    println()
    println("[KKT candidate cases]")
    println("  S=0 roots:      ", join([@sprintf("%.6f", x) for x in cands.s_roots], ", "))
    println("  K_atom=0 roots: ", join([@sprintf("%.6f", x) for x in cands.k_roots], ", "))
    println("  dSurplus roots: ", join([@sprintf("%.6f", x) for x in cands.d_roots], ", "))
    if !isempty(cands.s_boundary)
        println("  Schur-boundary positive-atom candidates:")
        for row in cands.s_boundary
            print_row("    S boundary", row)
        end
    end
    if !isempty(cands.interior)
        println("  Interior stationary candidates:")
        for row in cands.interior
            print_row("    stationary", row)
            print_derivs("    derivative", row.theta)
        end
    end
    if !isempty(cands.k_boundary)
        println("  Atom-sector boundary candidates (beta singular; check after):")
        for row in cands.k_boundary
            @printf("    K boundary     theta=%+.6f S=%+.6e after=%+.6e Katom=%+.6e\n",
                    row.theta, row.before, row.after, row.K_atom)
        end
    end
end

function summary()
    println("="^78)
    println("Julia ForwardDiff + QuadGK active-23 reduced model")
    println("="^78)
    println("shell_dim=$(DATA.shell_dim), schur_eigs=$(DATA.schur_eigs)")
    active_t = theta_of(DATA.active_vec)
    scan = scan_theta()
    print_row("active", scan.active)
    print_derivs("active", active_t)
    print_row("grid min surplus", scan.min_surplus)
    print_derivs("grid min surplus", scan.min_surplus.theta)
    print_row("AD stationary", scan.refined_min_surplus)
    print_derivs("AD stationary", scan.refined_min_surplus.theta)
    cands = kkt_candidates()
    print_kkt_candidates(cands)
    println()
    println("Interpretation:")
    println("  active is the Schur-minimizing direction, not necessarily the beta-surplus minimizer.")
    println("  Here AD finds an interior stationary worst-surplus direction inside S<0.")
    println("  That suggests a finite lemma should prove positivity on the Schur-negative")
    println("  sector directly, not only at the active eigenvector or boundary.")
    (scan = scan, candidates = cands)
end

LAST_SCAN = summary()
LAST_CANDIDATES = LAST_SCAN.candidates
nothing
