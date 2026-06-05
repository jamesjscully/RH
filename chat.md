# RH Witness-System Strategy

Source: https://chatgpt.com/share/6a1def2c-fe64-83ea-b621-80ddbf6f9a7e

## User 1

# Strategy for a Representation-Theoretic Witness-System Program Toward the Riemann Hypothesis

## 1. Why the program must be organized around witness systems

The Riemann hypothesis (RH) has many exact reformulations. That fact alone is not strategically useful. An exact reformulation becomes a serious proof vehicle only if it supports all of the following simultaneously.

1. It must identify a **critical statement** that is exactly equivalent to RH.
2. It must admit a **finite-dimensional hierarchy** whose truncations can be analyzed explicitly.
3. Finite progress must already imply a genuine theorem, such as a zero-free half-plane or a positivity statement.
4. A hypothetical zero off the critical line must force a **visible defect in the same finite coordinates**. Otherwise the route is only forward.
5. The passage from finite statements to the critical limit must be mathematically controlled.

The classical function-space formulations around Nyman, Beurling, and Báez-Duarte come much closer to this than most RH-equivalent criteria because they already have the right basic shape: a target vector, a structured family of witnesses, and a closure statement that is exactly RH. But even there, one immediately sees the real difficulty. The space of possible witness families is larger than any one route, and the strategic question is not just how to optimize within one family. The real question is:

> **Which witness systems have enough structure to make critical closure both forward-effective and reverse-detecting?**

That question is more primary than any single route. A route should be regarded as a **derived notion**: a route is a path through a parameterized witness system, or through a chain of transported witness systems, along which the forward frontier approaches the critical boundary and the reverse obstruction remains visible.

This changes the mathematical program in two ways.

First, the proof search cannot be organized only around direct approximation theorems. It must also include a **representation theory of witness systems**: transports, normal forms, dominance relations, universality theorems, and rigidity theorems.

Second, the space of witness systems should not be treated as a linear space of bases. It is not. Its elements are theorem-bearing analytic objects with nonlinear properties such as exactness, off-critical continuation, dual visibility, margin preservation, and limit stability. The correct analogue of a basis is therefore a **basis of constructors** or a finite presentation language for witness systems.

The document below describes a mathematical strategy built on that perspective.

---

## 2. Concrete mathematical patterns that force the abstraction

The abstractions below are not speculative. They are forced by patterns already visible in the literature.

### 2.1. The Nyman–Beurling–Báez-Duarte closure principle

Let
\[
\rho(x)=x-\lfloor x\rfloor,\qquad \chi=\chi_{(0,1)},
\qquad \rho_a(x)=\rho\!\left(\frac{1}{ax}\right).
\]
The Nyman–Beurling criterion expresses RH as a closure statement in \(L^2(0,\infty)\). Báez-Duarte strengthened this by proving that one may restrict from the continuous family \(a\ge 1\) to the discrete family \(a\in\mathbb N\):
\[
\mathrm{RH}
\iff
\chi \in \overline{\operatorname{span}\{\rho_a:a\in\mathbb N\}}^{\,L^2(0,\infty)}.
\]
This is the prototypical witness-system statement: there is a target, a nested discrete family, and an exact critical closure theorem [BD02].

Báez-Duarte then proved a much broader kernel-based version. For a suitable kernel \(f\), define its co-Poisson or Müntz transform
\[
P_f(x)=\sum_{n\ge 1}f(nx)-\frac1x\int_0^\infty f(t)\,dt.
\]
The general strong criterion shows that for a broad class of kernels \(f\), RH is equivalent to the closure of \(f\) by dilates of \(P_f\), with a necessity theorem under general regularity and a sufficiency theorem under compact support and a Mellin-transform nonvanishing condition in the critical strip [BD05]. This is the first serious indication that the correct object is not one basis but a **kernel-generated family of witness systems**.

Darses and Hillion then extended this picture in a probabilistic direction by randomizing the dilation parameters. Their work gives new criteria that overlap significantly with the general strong Báez-Duarte picture and, crucially, extends the sufficiency direction to certain non-compactly supported kernels [DH21]. This is strategically important because it shows that the witness-system moduli space is naturally larger than deterministic integer dilations.

### 2.2. Hardy-space transport and the semigroup pattern

Noor transported the Báez-Duarte criterion into Hardy space. In his formulation, one considers
\[
h_k(z)=\frac{1}{1-z}\log\!\left(\frac{1+z+\cdots+z^{k-1}}{k}\right),\qquad k\ge 2,
\]
and the span
\[
\mathcal N=\operatorname{span}\{h_k:k\ge 2\}\subset H^2.
\]
RH is equivalent to
\[
1\in \overline{\mathcal N}^{\,H^2}.
\]
The same work also shows that \(\mathcal N\) is dense in the compact-open topology unconditionally [Noor19]. This is a decisive warning sign: **compact-open density is not the same as \(H^2\)-density**. It is an exact example of how a route can prove the wrong topology and therefore make no progress on RH.

The Hardy model also reveals a semigroup that was invisible in the raw \(L^2\) formulation:
\[
(W_n f)(z)=(1+z+\cdots+z^{n-1})f(z^n),\qquad n\ge 1.
\]
These operators satisfy identities such as
\[
W_n h_k = h_{nk}-h_n.
\]
Manzur, Noor, and Santos studied this semigroup directly and showed that several questions about cyclicity, invariant subspaces, and spectra for \(W_n\) are equivalent to RH or yield generalizations of the Báez-Duarte criterion [MNS23]. The correct conclusion is not merely that the Hardy formulation is convenient. It is that witness systems should be expected to carry an internal **semigroup-orbit structure**.

### 2.3. The module/range viewpoint on Hardy half-planes

A second major pattern is the multiplication-operator or module avatar. Wei and Wu study multiplication by an analytic function \(\phi\) on Hardy spaces \(H^2(\Omega_\tau)\), where
\[
\Omega_\tau=\{s\in\mathbb C:\Re(s)>\tau\}.
\]
They show that if \(\phi\) satisfies three natural conditions —
1. polynomial growth in \(\Omega_\tau\),
2. analyticity across the boundary \(\Re(s)=\tau\),
3. decay slower than every exponential along the real half-line —
then
\[
\phi(s)\neq 0 \text{ on } \Omega_\tau
\iff
\overline{\operatorname{Ran}(M_\phi)}^{\,H^2(\Omega_\tau)} = H^2(\Omega_\tau),
\]
and more precisely,
\[
\overline{\operatorname{Ran}(M_\phi)}
=
\{F\in H^2(\Omega_\tau): F/\phi \text{ is analytic in } \Omega_\tau\}.
\]
For the special choice
\[
\phi(s)=\frac{s-1}{s^2}\zeta(s),
\]
this becomes a Hardy-space zero-free-region criterion for the zeta function [WW22].

This is not just another equivalent reformulation. It shows that the right structural object is often not merely a span, but a **range of a multiplication operator** inside a Hardy module. It also forces additional geometry into the picture: boundary analyticity, growth conditions, and the closure of a module range.

Wei and Wu also prove a useful weak version of the Nyman–Beurling–Báez-Duarte criterion: zero-freeness of \(\zeta\) in \(\Omega_\tau\) is equivalent to the existence of Dirichlet polynomials \(D_N\) such that
\[
\zeta(s)D_N(s)\to 1 \quad (\Re(s)>1)
\]
and
\[
\left\|\frac{s-1}{s^2}\zeta(s)D_N(s)\right\|_{H^2(\Omega_\tau)}
\]
remains bounded [WW22]. This shows that boundedness in the correct Hardy norm is itself a meaningful finite witness property. It also exposes an explicit arithmetic feature: if the coefficients \(a_N(n)\) of \(D_N(s)=\sum_{n\le N} a_N(n)n^{-s}\) are uniformly bounded and \(\zeta(s)D_N(s)\to 1\) on \(\Re(s)>1\), then \(a_N(n)\to \mu(n)\) pointwise [WW22]. This is an early appearance of **arithmetic locking**.

### 2.4. Off-critical deformations and zero-free half-planes

A closure criterion at one critical space is still not enough. A viable route needs nearby spaces in which finite progress already implies honest zero-free regions.

Ghosh, Kremnizer, Noor, and Santos developed a broad framework in which spaces of analytic functions yield zero-free half-planes for \(\zeta\) once certain closure properties hold [GKNS24]. This shows that one should not think only in terms of the single critical topology. One should think in terms of a **family of ambient spaces** \(\mathcal H_\theta\) with a distinguished critical parameter.

Gallardo-Gutiérrez and Seco sharpen this in weighted Dirichlet and related sequence spaces. They show that if appropriate approximation problems hold in weighted Dirichlet spaces \(D_\alpha\) with \(\alpha\in(-3,-2)\), then
\[
\Re(s) > -\frac{\alpha+1}{2}
\]
is zero-free for \(\zeta\), and more generally similar statements hold in the spaces \(X_\alpha^p\) / \(\ell_\alpha^p\) [GGS25]. They also emphasize why Hilbert-space models matter: orthogonal projection, finite-dimensional optimization, and explicit algorithms become available [GGS25].

The same paper records a striking arithmetic constraint. If one approximates \(1/(1-z)\) by finite linear combinations of the classical functions \(R_k\), the coefficients \(c_{k,n}\) must satisfy
\[
c_{k,n}\to -\frac{\mu(k)}{k}
\]
for each fixed \(k\), and when the \(c_{k,n}\) are chosen from orthogonal projections onto the natural finite spans, RH is equivalent to this specific limit profile [GGS25]. This is precisely the kind of rigidity that a serious witness system should expose and remember.

### 2.5. Dual spaces, orthogonality, and biorthogonal structure

A forward closure scheme is not sufficient. One needs a dual space in which failure of closure becomes a theorem.

Calderaro, Manzur, Noor, and Santos analyze the orthogonal complement
\[
\mathcal N^\perp\subset H^2
\]
of the Hardy family \((h_k)_{k\ge 2}\). Using unbounded Toeplitz operators and de Branges–Rovnyak spaces, they show that the size and dimension of \(\mathcal N^\perp\) reveal information about zeros of \(\zeta\). They also prove that \((h_k)\) possesses a complete biorthogonal sequence in \(H^2\) [CMNS24].

This is strategically decisive. It shows that a witness family should not be judged only by the forward span \(W_N\). It should also be judged by whether it supports an **explicit dual extremal theory**: orthogonal complement, annihilator, Toeplitz kernel, de Branges–Rovnyak model, biorthogonal sequence, or similar.

Related reverse information appears in the Nyman–Beurling–Báez-Duarte distance
\[
d_N^2
=
\inf_{A_N}
\frac{1}{2\pi}\int_{-\infty}^{\infty}
\left|1-\zeta A_N\!\left(\frac12+it\right)\right|^2
\frac{dt}{\frac14+t^2},
\]
where the infimum is over Dirichlet polynomials \(A_N(s)\) of length \(N\). RH is equivalent to \(d_N\to 0\). Burnol proved a nontrivial lower bound in this approximation problem [Burnol01]. Bettin, Conrey, and Farmer showed, under RH together with a condition on
\[
\sum_\rho \frac{1}{|\zeta'(\rho)|^2},
\]
that the optimal constant matches Burnol’s lower bound [BCF12]. Maier and Rassias studied \(d_N\) under the assumption that \(\zeta\) has four nontrivial zeros off the critical line, obtaining an explicit criterion for RH-failure in terms of the behavior of \(d_N\) [MR17].

The lesson is that **reverse-detecting closure is possible in principle**. The same finite quantity can carry forward approximation information and converse obstruction information.

### 2.6. Bohr lift, multiplicative grading, and infinite-polydisk structure

The semigroup picture carries still more structure after the Bohr transform. Dan and Guo show that the periodic dilation completeness problem can be reformulated as a cyclicity problem in the Hardy space over the infinite-dimensional polydisk \(H^2_\infty\) via the Bohr transform [DG20]. This is directly relevant because multiplicative witness systems are naturally graded by prime exponents.

The strategic lesson is that multiplicative witness systems should often be represented in a **prime-graded model**. If
\[
n=\prod_j p_j^{\alpha_j(n)},
\]
then a Dirichlet series
\[
\sum_{n\ge 1} a_n n^{-s}
\]
lifts to a formal analytic function on the infinite polydisk
\[
\sum_{n\ge 1} a_n z_1^{\alpha_1(n)}z_2^{\alpha_2(n)}\cdots.
\]
This lift often reveals module structure, cyclicity, and semigroup invariants that are difficult to see in the one-variable half-plane picture. It also exposes arithmetic locking more naturally because prime factorization becomes visible directly in the multigrading.

### 2.7. Kernel and Sonine normal forms

The co-Poisson / Müntz transform already suggests that witness systems should be studied at the level of kernels, not just basis functions. Burnol’s work links the zeros of \(\zeta\), co-Poisson formulas, and de Branges Sonine spaces, and proves complete/minimal-system results for zeta zeros inside these spaces [Burnol04]. This strongly suggests that a broad class of witness systems should admit a **kernel normal form** and, when possible, a **Sonine/de Branges avatar**.

This matters strategically because de Branges-type spaces provide more than aesthetic structure. They often come with canonical reproducing kernels, ordered subspace structures, self-adjoint extensions, and explicit spectral models. Those are precisely the tools one wants for reverse detection and rigidity.

### 2.8. Bridges between de Branges–Rovnyak and Dirichlet spaces

The dual side in Noor’s Hardy-space work already uses de Branges–Rovnyak and local Dirichlet spaces [Noor19]. Dellepiane, Peloso, and Tabacco then prove a precise classification of when a de Branges–Rovnyak space \(H(b)\) is also a harmonically weighted Dirichlet space \(D_\mu\) for finitely supported \(\mu\) [DPT25]. This is strategically important because it shows that an abstract operator-range space can collapse to a concrete integral/norm space in exactly describable situations.

The lesson is that one should actively search for witness systems that admit **avatar collapses**: cases in which the abstract dual/module picture and the concrete weighted-Dirichlet picture become literally the same space.

### 2.9. Explicit-formula positivity and deformation laboratories

The explicit formula provides a universal positivity backend. Bombieri’s study of Weil’s quadratic functional stresses the key fact:
\[
\text{Weil’s quadratic functional is positive semidefinite}
\iff \mathrm{RH}.
\]
He also develops finite-support extremal problems for this quadratic functional [Bombieri00]. Lagarias shows that generalized Li coefficients are values of Weil’s quadratic functional [Lagarias04]. Suzuki introduces screw-function analogues of Weil and Li positivity and proves several RH-equivalent conditions together with unconditional partial results [Suzuki22].

The de Bruijn–Newman deformation provides a complementary one-parameter laboratory. Rodgers and Tao proved \(\Lambda\ge 0\), establishing Newman’s conjecture [RT18]. More recently, a rigorous interval-arithmetic computation proved that the classical de Bruijn–Newman kernel is not PF\(_5\) by exhibiting a certified negative \(5\times 5\) Toeplitz minor [Mich26]. That is exactly the sort of finite-dimensional obstruction theorem this program should treat as first-class.

Finally, local zero geometry provides a way to normalize reverse sensitivity. Conrey’s survey highlights Speiser’s theorem and related derivative criteria [Conrey03]. Radziwiłł proves that positive proportions of small gaps between zeros of \(\zeta\) are equivalent to positive proportions of zeros of \(\zeta'\) lying very close to the critical line [Rad13]. This shows that reverse detection should not be measured only against raw height \(T\); it should be measured on the **local zero-spacing scale**.

---

## 3. The primitive object: a multi-avatar witness system

A single “witness family” is not enough structure. A strong mathematical object should be visible in several mathematically distinct but transport-compatible ways. The correct primitive object is therefore a **multi-avatar witness system**.

### 3.1. Presented witness system

A presented witness system is a tuple
\[
\mathfrak W=
(\Theta,\theta_c,\mathcal H,v,G,\rho,\kappa,\mu,I_\bullet,\phi,\mathcal D,\mathcal Q,\mathcal A,\mathcal K,\Pi),
\]
whose components are as follows.

- \(\Theta\) is a parameter space, partially ordered so that \(\theta\downarrow\theta_c\) means approach to the critical topology.
- \(\theta_c\in\Theta\) is the critical parameter.
- \(\mathcal H=\{\mathcal H_\theta\}_{\theta\in\Theta}\) is a family of ambient spaces, usually analytic function spaces or Mellin-transform models.
- \(v=\{v_\theta\}_{\theta\in\Theta}\) is the target family.
- \(G\) is a finitely presented semigroup or operator monoid.
- \(\rho_\theta:G\to \operatorname{End}(\mathcal H_\theta)\) is an action of \(G\) on each ambient space.
- \(\kappa_\theta\in\mathcal H_\theta\) is a seed vector or kernel.
- \(\mu_\theta\) is an optional bounded multiplier or intertwiner.
- \(I_N\subset G\) is a nested truncation scheme.
- \(\phi_\theta\) is an optional multiplier defining a module/range avatar.
- \(\mathcal D_\theta\) is a dual apparatus.
- \(\mathcal Q_{N,\theta}\) is a finite-compression / positivity apparatus.
- \(\mathcal A_\theta\) is an arithmetic profile.
- \(\mathcal K_\theta\) is an optional kernel normal-form / co-Poisson / Sonine apparatus.
- \(\Pi\) is a certificate schema for finite reductions and quantitative inequalities.

The associated \(N\)-th witness space is
\[
W_N(\theta)
=
\operatorname{span}\{\mu_\theta\,\rho_\theta(g)\kappa_\theta : g\in I_N\}.
\]

The associated approximation functional is
\[
E_{\mathfrak W}(N,\theta)
=
\inf_{w\in W_N(\theta)}\|v_\theta-w\|_{\mathcal H_\theta}.
\]

At this level, \(\mathfrak W\) is only **data**. None of the strategically important properties — exactness, converse theorems, limit stability, or anything else — are built in. They must be supplied by theorems.

### 3.2. The six compulsory avatars

A witness system is not strong until it carries six compulsory avatars.

#### 3.2.1. Closure avatar

This is the primary closure/approximation picture:
\[
(\mathcal H_\theta, v_\theta, W_N(\theta), E_{\mathfrak W}(N,\theta)).
\]
It must support a critical theorem
\[
\mathrm{RH}
\iff
v_{\theta_c}\in \overline{\bigcup_N W_N(\theta_c)}^{\,\mathcal H_{\theta_c}},
\]
and off-critical theorems linking \(E_{\mathfrak W}(N,\theta)\) to zero-free regions or positivity statements.

#### 3.2.2. Module avatar

This is the multiplication-operator picture. It consists of a Hardy or module space, a multiplier \(\phi_\theta\), and the range closure
\[
\overline{\operatorname{Ran}(M_{\phi_\theta})}.
\]
In the Hardy half-plane setting, the prototype is
\[
\phi_\tau(s)=\frac{s-1}{s^2}\zeta(s),
\]
with
\[
\zeta(s)\neq 0 \text{ on } \Omega_\tau
\iff
\overline{\operatorname{Ran}(M_{\phi_\tau})}=H^2(\Omega_\tau),
\]
under the explicit boundary, growth, and decay hypotheses from [WW22].

This avatar is compulsory because it exposes **range geometry**, **boundary/growth constraints**, and explicit orthogonal-complement descriptions.

#### 3.2.3. Semigroup avatar

This is the orbit/cyclicity picture. It records the semigroup \(G\), its action \(\rho_\theta\), the seed \(\kappa_\theta\), and the truncations \(I_N\). The classical Hardy prototype is the weighted composition semigroup
\[
(W_n f)(z)=(1+z+\cdots+z^{n-1})f(z^n).
\]
This avatar is compulsory because it reveals invariant-subspace structure, cyclicity, and multiplicative symmetries. It is also the natural location for Bohr-lift / infinite-polydisk representations.

#### 3.2.4. Dual avatar

This is the obstruction/extremal picture. It consists of dual objects such as
- orthogonal complements,
- annihilators,
- Toeplitz kernels,
- de Branges–Rovnyak spaces,
- local Dirichlet spaces,
- reproducing-kernel extremizers,
- complete biorthogonal systems.

This avatar is compulsory because a forward span is not enough. The system must provide a mechanism by which a hypothetical zero off the line becomes a **dual witness**.

#### 3.2.5. Finite-compression avatar

This is the finite hierarchy of compressions:
- Gram matrices,
- Hankel or Toeplitz minors,
- compressed integral operators,
- finite sections of positivity forms,
- explicit quadratic forms in the finite coefficients.

This avatar is compulsory because all serious progress will eventually have to pass through finite-dimensional linear algebra with explicit error control. The de Bruijn–Newman PF\(_5\) theorem is a model example [Mich26]. In the Hardy-module setting, the quantities \(\|\phi D_N\|_{H^2(\Omega_\tau)}^2\) acquire explicit quadratic-form descriptions in terms of arithmetic sums [WW22].

#### 3.2.6. Arithmetic avatar

This is the asymptotic coefficient geometry of the canonical finite extremizers. A witness system does not merely produce arbitrary coefficients. It often predicts a distinguished limiting profile, such as
\[
a_N(n)\to \mu(n)
\quad\text{or}\quad
c_{k,n}\to -\frac{\mu(k)}{k}.
\]
This avatar is compulsory because it measures whether the finite witnesses are correctly “locked” to the arithmetic of \(\zeta\). A family with no arithmetic locking may still approximate well numerically, but it is structurally suspicious.

### 3.3. Preferred normal-form avatar: kernel / co-Poisson / Sonine

When available, a witness system should also carry a preferred normal-form avatar built from a kernel \(f\), its co-Poisson/Müntz transform \(P_f\), its Mellin transform, and possibly a Sonine or de Branges realization. This avatar is not made compulsory only because some witness systems may require work before it can be extracted. But mathematically it is highly desirable, because it is the most likely source of canonical normal forms and universality theorems [BD05], [Burnol04].

### 3.4. Internal transport theorems between avatars

A multi-avatar witness system is not just a bag of equivalent pictures. The strategy requires explicit theorems relating the avatars. Typical internal transports are:

- closure avatar \(\leftrightarrow\) module avatar via Mellin/Fourier/Hardy transforms;
- closure avatar \(\leftrightarrow\) semigroup avatar via orbit generation and cyclicity;
- closure avatar \(\leftrightarrow\) dual avatar via orthogonality and Hahn–Banach / Hilbert-space duality;
- dual avatar \(\leftrightarrow\) de Branges–Rovnyak / Dirichlet avatar via operator theory [Noor19], [DPT25];
- closure avatar \(\leftrightarrow\) finite-compression avatar via Gram or Toeplitz reductions;
- semigroup avatar \(\leftrightarrow\) Bohr-lift avatar via prime-graded coordinate representations [DG20];
- kernel avatar \(\leftrightarrow\) closure avatar via co-Poisson/Müntz transforms [BD05].

A witness system is mathematically weak if it exists in only one avatar. Strength comes from the transport network.

---

## 4. The theorem obligations that make a witness system strong

The central notions are theorem-level predicates on presented witness systems.

### 4.1. Exact critical theorem

A witness system has an **exact core** if there is a theorem of the form
\[
\mathrm{RH}
\iff
v_{\theta_c}\in
\overline{\bigcup_N W_N(\theta_c)}^{\,\mathcal H_{\theta_c}}.
\]
This blocks the “wrong topology” failure mode. The topology and ambient space at the critical parameter must be declared explicitly and must be the one appearing in the exact equivalence.

### 4.2. Off-critical frontier theorem

A witness system is **forward-effective** if for \(\theta>\theta_c\) there is a theorem converting finite approximation or finite positivity into an actual zero-free region. This can take several forms.

- Approximation form:
  \[
  E_{\mathfrak W}(N,\theta)\le \varepsilon
  \Longrightarrow
  \zeta(s)\neq 0 \text{ in } \Re(s)>\tau(\theta,\varepsilon).
  \]

- Module form:
  \[
  \overline{\operatorname{Ran}(M_{\phi_\theta})}=H^2(\Omega_{\tau(\theta)})
  \Longrightarrow
  \zeta(s)\neq 0 \text{ in } \Omega_{\tau(\theta)}.
  \]

- Positivity form:
  \[
  \mathcal Q_{N,\theta}\succeq mI
  \Longrightarrow
  \text{zero-free / positivity consequence}.
  \]

The point is not the exact syntax. The point is that finite progress at \((N,\theta)\) must imply a genuine theorem.

### 4.3. Reverse obstruction theorem

A witness system is **reverse-detecting** if a hypothetical zero off the critical line produces a quantitative defect in the same coordinates. There must be a theorem of the form:

> If \(\zeta(\beta+iT)=0\) with \(\beta>1/2\), then for a specified region of \((N,\theta)\) there is either
> (a) a lower bound on \(E_{\mathfrak W}(N,\theta)\), or
> (b) a nonzero element of the dual space \(\mathcal D_\theta\), or
> (c) a negative or degenerate direction for \(\mathcal Q_{N,\theta}\).

This blocks the “forward bridge with no converse” failure mode.

### 4.4. Biorthogonal or extremal dual theorem

A witness system is **dually explicit** if its dual space is not merely existential. There should be a concrete extremal theory: a complete biorthogonal sequence, a reproducing-kernel characterization, an explicit Toeplitz-kernel model, or an equivalent explicit dual basis.

This matters because lower bounds and converse results are almost never obtained from an undefined annihilator. They come from extremizers.

### 4.5. Finite-compression theorem

A witness system is **finitely compressible** if every relevant infinite-dimensional statement reduces to a finite-dimensional object plus explicit remainder bounds. Formally, one needs theorems of the form

\[
E_{\mathfrak W}(N,\theta)^2
=
\text{finite optimization over } \mathbb C^{m(N)}
\;+\;
\text{explicit tail error},
\]
or
\[
\mathcal Q_{N,\theta}
=
\text{explicit matrix/operator compression}
\;+\;
\text{controlled remainder}.
\]

This is where Gram matrices, Toeplitz minors, Hankel forms, and compressed positivity operators become first-class.

### 4.6. Arithmetic-locking theorem

A witness system is **arithmetically locked** if the canonical finite extremizers converge to a distinguished arithmetic profile. This can be stated in several equivalent ways:
- coefficient convergence to \(\mu(n)\),
- projection coefficients converging to \(-\mu(k)/k\),
- asymptotic recovery of a canonical Dirichlet or Euler product profile,
- prime-graded coefficient stabilization under the Bohr lift.

This theorem prevents the witness family from being too unconstrained.

### 4.7. Height-normalized reverse theorem

A witness system is **height-stable** if its reverse defect survives the height limit after normalization by the local microscopic scale. The natural scale near height \(T\) is the average zero spacing
\[
\Delta_T \sim \frac{2\pi}{\log T}.
\]
If a hypothetical zero lies at
\[
\beta+iT,\qquad \beta=\frac12+\eta,
\]
the relevant normalized horizontal displacement is
\[
\delta=\frac{\eta}{\Delta_T}
=
\frac{\eta\log T}{2\pi}.
\]
The reverse theorem should therefore control a renormalized defect
\[
\widetilde G_{\mathfrak W}(\delta;N,\theta,T),
\]
not just a raw-height defect \(G_{\mathfrak W}(\eta,T;N,\theta)\).

This blocks height leakage. Without such a theorem, a converse may become invisible at large height.

### 4.8. Margin theorem

A witness system is **margin preserving** if every positivity or approximation theorem carries a certified margin that dominates the entire analytic and numerical loss budget. This can be stated schematically as
\[
\lambda_{\min}(\mathcal Q_{N,\theta}) > L_{\mathfrak W}(N,\theta,T),
\]
or
\[
\widetilde G_{\mathfrak W}(\delta;N,\theta,T) > L_{\mathfrak W}(N,\theta,T),
\]
where \(L_{\mathfrak W}\) is the accumulated loss from truncation, transport, tail bounds, norm comparison, and finite compression.

This blocks “positivity without margin”.

### 4.9. Limit-stability theorem

A witness system is **limit stable** if the asymptotic directions
\[
N\to\infty,\qquad \theta\downarrow\theta_c,\qquad T\to\infty
\]
can be coupled along an admissible path with sufficient uniformity. One needs a theorem schema of the following type:

- there exists an admissible path \((N_m,\theta_m)\) with \(N_m\to\infty\), \(\theta_m\downarrow\theta_c\),
- the forward frontier approaches the critical line,
- the reverse modulus remains larger than the loss,
- the relevant limits commute or are controlled along this path.

Without this, finite theorems may accumulate forever without ever reaching the critical statement.

### 4.10. Unconditional core and shadow-model separation

A witness system belongs to the **proof spine** only if all its core avatars and transport theorems are unconditional. Conditional structures are allowed, but only as **shadow models**.

For example, Suzuki’s Hilbert space derived from the Weil distribution is explicitly constructed under RH and then shown to be isomorphic to a de Branges space [Suzuki23]. That makes it a valuable diagnostic normal form, but not part of the unconditional implication chain.

This blocks circularity.

### 4.11. Strong admissibility

A witness system is **strongly admissible** if it satisfies:

1. exact critical theorem,
2. off-critical frontier theorem,
3. reverse obstruction theorem,
4. explicit dual/extremal theorem,
5. finite-compression theorem,
6. arithmetic-locking theorem,
7. height-normalized reverse theorem,
8. margin theorem,
9. limit-stability theorem,
10. unconditional core / shadow separation.

This is the real meaning of “a witness family with sufficient structure”.

---

## 5. Quantitative invariants

To compare witness systems and to determine whether a local route is actually converging, one should attach the following invariants.

### 5.1. Approximation distance

\[
E_{\mathfrak W}(N,\theta)
=
\inf_{w\in W_N(\theta)}\|v_\theta-w\|_{\mathcal H_\theta}.
\]

### 5.2. Forward frontier

\[
F_{\mathfrak W}(N,\theta)
=
\inf\bigl\{\sigma>1/2:\text{ the finite theorem at }(N,\theta)\text{ proves }\zeta(s)\neq 0\text{ for }\Re(s)>\sigma\bigr\}.
\]
A route is forward-effective only if \(F_{\mathfrak W}(N_m,\theta_m)\downarrow 1/2\).

### 5.3. Positivity margin

\[
M_{\mathfrak W}(N,\theta)
=
\lambda_{\min}(\mathcal Q_{N,\theta}),
\]
or more generally the smallest positive spectral margin in the relevant finite-compression object.

### 5.4. Conditioning profile

\[
\kappa_{\mathfrak W}(N,\theta)
=
\text{condition number / frame bound ratio / stability constant of the finite hierarchy}.
\]
This controls the geometry of the witness space. Pathological growth in \(\kappa_{\mathfrak W}\) is a sign that the family may be strategically unusable even if it is exact.

### 5.5. Arithmetic-locking defect

Let \(c_{N,\theta}\) be the canonical finite coefficients (for example, orthogonal projection coefficients, extremal coefficients, or minimal-norm coefficients), and let \(a^\infty_\theta\) be the predicted arithmetic profile. Define
\[
A_{\mathfrak W}(N,\theta)
=
\|c_{N,\theta}-a^\infty_\theta\|_{\mathfrak a},
\]
for a natural coefficient norm \(\|\cdot\|_{\mathfrak a}\). A route is arithmetically faithful only if \(A_{\mathfrak W}(N,\theta)\to 0\) in the regime dictated by the theory.

### 5.6. Reverse modulus

\[
G_{\mathfrak W}(\eta,T;N,\theta)
=
\text{minimum defect forced at }(N,\theta)\text{ by a zero at } \frac12+\eta+iT.
\]
This may be measured as a lower bound on \(E_{\mathfrak W}(N,\theta)\), as a dual norm, or as a negative/degenerate direction in \(\mathcal Q_{N,\theta}\).

### 5.7. Height-normalized reverse modulus

\[
\widetilde G_{\mathfrak W}(\delta;N,\theta,T),
\qquad
\delta=\frac{\eta\log T}{2\pi}.
\]
This is the correct converse invariant for large-height analysis.

### 5.8. Derivative-zero / gap sensitivity

\[
J_{\mathfrak W}(N,\theta;T)
=
\text{sensitivity of the witness system at }(N,\theta)\text{ to local geometry of }\zeta'(s)\text{ or zero gaps near }T.
\]
This is a diagnostic invariant rather than an endpoint invariant, but it matters because Radziwiłł’s equivalence between small zero gaps and zeros of \(\zeta'\) near the line shows that local geometry is a natural converse sensor [Rad13].

### 5.9. Total loss

\[
L_{\mathfrak W}(N,\theta,T)
=
L_{\mathrm{tail}}
+
L_{\mathrm{transport}}
+
L_{\mathrm{compression}}
+
L_{\mathrm{positivity}}
+
L_{\mathrm{height}}
\]
is the cumulative certified slack in the finite theorem package. All forward and converse theorems must be compared against this quantity.

### 5.10. Signal-to-slack ratio

\[
\Sigma_{\mathfrak W}(\delta;N,\theta,T)
=
\frac{\widetilde G_{\mathfrak W}(\delta;N,\theta,T)}{L_{\mathfrak W}(N,\theta,T)}
\]
or, more conservatively,
\[
\Sigma^\flat_{\mathfrak W}(\delta;N,\theta,T)
=
\widetilde G_{\mathfrak W}(\delta;N,\theta,T)-L_{\mathfrak W}(N,\theta,T).
\]
A local route is only mathematically meaningful if the signal-to-slack quantity stays positive in the relevant regime.

---

## 6. The space of witness systems and its representation theory

### 6.1. Why a literal basis is the wrong abstraction

The set of strongly admissible witness systems is not a vector space. One cannot expect a basis in the linear-algebra sense. The correct replacement is a **presentation language** for witness systems and a **dominance preorder** on the resulting objects.

A witness system should therefore be regarded as a finitely generated analytic object built from a small list of constructors. The representation theory of witness systems asks whether every strongly admissible system is generated, up to controlled transport, from a small number of principal seeds.

### 6.2. Constructor basis

The natural constructors are:

1. **Kernel seed.** Choose a kernel \(f\), a transform \(P_f\), and a target.
2. **Semigroup orbit.** Form the orbit of a seed under a semigroup action.
3. **Module/range realization.** Convert a closure statement into the range closure of a multiplication operator.
4. **Multiplier twist.** Multiply by bounded intertwiners to move between models.
5. **Parameter deformation.** Move inside a family \(\mathcal H_\theta\).
6. **Bohr lift / prime grading.** Lift multiplicative structure to a multivariable cyclicity problem.
7. **Dualization.** Form annihilator, orthogonal complement, Toeplitz kernel, reproducing-kernel model, or biorthogonal system.
8. **Finite compression.** Pass to Gram, Hankel, Toeplitz, or operator truncations.
9. **Positivity synthesis.** Couple the system to the explicit-formula / Weil positivity backend.
10. **Normal-form reduction.** When possible, transport to a kernel/Sonine or de Branges-type avatar.

This is the right analogue of a basis.

### 6.3. Dominance preorder

Write
\[
\mathfrak W \preceq \mathfrak W'
\]
if there is a transport from \(\mathfrak W\) to \(\mathfrak W'\) under which:
- exactness is preserved,
- off-critical frontiers degrade by at most controlled factors,
- reverse moduli degrade by at most controlled factors,
- conditioning remains comparably bounded,
- arithmetic-locking data are transported coherently,
- finite-compression margins remain within a controlled loss budget.

This preorder is the mathematical language for “one witness system is no stronger than another”. It is what should replace informal claims that one route is “more general”.

### 6.4. Principal classes

A **principal class** is a class of strongly admissible witness systems that is closed under the natural constructors and minimal, up to \(\preceq\), among systems exhibiting a given structural pattern.

At present, the most credible principal classes are:

- semigroup-generated Hardy / module systems,
- weighted Hardy / weighted Dirichlet deformation systems,
- co-Poisson / Müntz / Sonine kernel systems,
- explicit-formula positivity and de Bruijn–Newman finite hierarchy systems.

The purpose of the representation theory is not to prove in advance which one will solve RH. It is to reduce the space of possibilities to principal classes that actually deserve arithmetic effort.

### 6.5. Universality program

The universality program asks whether every strongly admissible witness system is dominated by a principal class. In ideal form:

> **Universality conjecture.** Every strongly admissible witness system is dominated, after finitely many constructors and bounded transports, by a semigroup/module/kernel system arising from a small list of principal seeds.

A full theorem of this form may be too ambitious, but partial universality theorems would already be strategically transformative.

### 6.6. Rigidity program

The rigidity program is the dual of universality. It tries to prove that whole syntactic subclasses can never be strongly admissible. The prototype is Bober’s complete classification of a Vasyunin-related family of step functions arising from the Nyman–Beurling approach [Bober07]. This shows that low-complexity witness subclasses can sometimes be classified exactly.

Rigidity results of the following type are especially valuable:

- bounded-complexity step families fail norm fidelity,
- certain kernel classes cannot achieve reverse detection,
- certain weight regimes cause conditioning blow-up,
- certain finite-compression hierarchies lose all positivity margin near the critical parameter.

### 6.7. Normal-form program

The normal-form program asks for exact or approximate reductions of strong witness systems to more structured avatars:
- module to weighted Dirichlet,
- semigroup to Bohr-lift cyclicity,
- closure to co-Poisson / Müntz,
- dual spaces to de Branges–Rovnyak or Sonine spaces.

This is where the Dellepiane–Peloso–Tabacco classification of \(H(b)=D_\mu\) cases becomes relevant [DPT25], and where Burnol’s Sonine perspective becomes relevant [Burnol04].

---

## 7. Principal witness-system classes and what they are supposed to do

### 7.1. Semigroup/module Hardy class

This class begins with the Hardy-space avatar of the Báez-Duarte criterion [Noor19], its semigroup \(W_n\) [MNS23], and the multiplication-operator / range formulation of zero-free regions [WW22].

Its role is to provide:
- exact critical closure in a classical Hilbert space,
- a natural semigroup orbit structure,
- a module/range formulation,
- explicit Hardy norms and dual spaces,
- direct access to \(H^2\)-, \(H^p\)-, Toeplitz-, and de Branges–Rovnyak techniques.

This class should be treated as the main source of **operator-theoretic normal forms**.

### 7.2. Weighted Hardy and weighted Dirichlet deformation class

This class consists of deformations around the critical space that produce actual zero-free half-planes [GKNS24], [GGS25]. It provides the natural off-critical parameter \(\theta\), the finite optimization problems that are solvable by orthogonal projection in Hilbert settings, and the arithmetic profile \(-\mu(k)/k\) on the coefficient side [GGS25].

Its role is to provide:
- the off-critical frontier,
- parameter monotonicity,
- explicit optimization geometry,
- arithmetic locking,
- candidate limit paths \(\theta\downarrow\theta_c\).

This class should be treated as the main source of **forward effectivity**.

### 7.3. Co-Poisson / Müntz / Sonine kernel class

This class begins with kernel seeds \(f\), their co-Poisson transforms \(P_f\), and the general strong criterion [BD05], together with Burnol’s Sonine/de Branges realization [Burnol04] and Darses–Hillion’s probabilistic non-compact extensions [DH21].

Its role is to provide:
- kernel normal forms,
- Mellin-transform control,
- regularization mechanisms,
- de Branges and Sonine spectral structure,
- a large but still structured moduli space of witness systems.

This class should be treated as the main source of **representation theory and normal forms**.

### 7.4. Explicit-formula / Toeplitz / de Bruijn–Newman class

This class is not the main forward route, but it is indispensable as a positivity and obstruction laboratory. It includes:
- Weil’s quadratic functional [Bombieri00],
- Li/Weil connections [Lagarias04],
- screw-function positivity analogues [Suzuki22],
- de Bruijn–Newman finite Toeplitz hierarchies [RT18], [Mich26].

Its role is to provide:
- common positivity objects,
- finite hierarchy templates,
- sharp obstruction theorems,
- translation between zero data and finite PSD/Toeplitz data.

This class should be treated as the main source of **finite-dimensional positivity and obstruction methodology**.

---

## 8. The mathematical proof architecture

The program should proceed in two interacting phases: a **representation phase** on the space of witness systems and a **convergence phase** inside the principal classes that survive representation-theoretic pruning.

### 8.1. Phase I: representation and pruning

The first phase proves theorems about witness systems as such.

1. **Internal avatar equivalences.** Prove exact transports between closure, module, semigroup, dual, finite-compression, and arithmetic avatars in the canonical classes.
2. **Constructor theorems.** Prove which constructors preserve strong admissibility.
3. **Dominance theorems.** Prove that certain classes dominate others.
4. **Rigidity theorems.** Eliminate whole families that can never be strongly admissible.
5. **Normal-form theorems.** Identify classes where abstract avatars collapse to concrete integral or kernel models.

The output of Phase I is not RH. The output is a drastically smaller search space and a collection of principal classes worthy of detailed analysis.

### 8.2. Phase II: convergence inside a principal class

Inside a principal class, the proof spine has to exhibit the following structure.

#### Step 1: exact critical theorem

Fix a strongly admissible witness system \(\mathfrak W\) and prove
\[
\mathrm{RH}
\iff
v_{\theta_c}\in
\overline{\bigcup_N W_N(\theta_c)}^{\,\mathcal H_{\theta_c}}.
\]

#### Step 2: off-critical frontier theorem

For \(\theta>\theta_c\), prove finite theorems converting approximation or positivity into explicit zero-free regions. Define the forward frontier \(F_{\mathfrak W}(N,\theta)\).

#### Step 3: finite-compression theorem with margins

Reduce all relevant quantities at \((N,\theta)\) to explicit finite optimization or finite PSD/Toeplitz data plus explicit losses. Define \(M_{\mathfrak W}(N,\theta)\), \(\kappa_{\mathfrak W}(N,\theta)\), and \(L_{\mathfrak W}(N,\theta,T)\).

#### Step 4: converse theorem and dual lower bounds

Show that any off-line zero at \(1/2+\eta+iT\) forces a visible defect:
\[
\widetilde G_{\mathfrak W}(\delta;N,\theta,T) > 0,
\qquad
\delta = \frac{\eta\log T}{2\pi},
\]
either in the approximation distance, the dual space, or the positivity hierarchy.

#### Step 5: arithmetic locking

Show that the canonical finite extremizers converge to the predicted arithmetic profile. This is where the Möbius asymptotics or related prime-sum profiles enter as theorem outputs rather than heuristics.

#### Step 6: positivity synthesis

Transport the finite hierarchy into the explicit-formula / positivity backend and prove that the forward theorem, reverse theorem, and positivity theorem are mutually consistent only in the RH-compatible regime.

#### Step 7: path theorem and critical limit

Construct an admissible path \((N_m,\theta_m)\) with \(N_m\to\infty\), \(\theta_m\downarrow\theta_c\) such that
\[
F_{\mathfrak W}(N_m,\theta_m)\downarrow \frac12
\]
and, for every fixed renormalized defect \(\delta>0\),
\[
\inf_{T\ge T_0(m)}
\Bigl(
\widetilde G_{\mathfrak W}(\delta;N_m,\theta_m,T)
-
L_{\mathfrak W}(N_m,\theta_m,T)
\Bigr)>0
\]
for all sufficiently large \(m\).

This is the point where the whole route either succeeds or fails for intrinsic reasons.

### 8.3. The precise contradiction mechanism

Suppose, toward contradiction, that RH fails. Then there is a zero
\[
\beta+iT
\quad\text{with}\quad
\beta>\frac12.
\]
Fix \(\delta=\frac{(\beta-1/2)\log T}{2\pi}>0\). By the reverse theorem, this forces a defect
\[
\widetilde G_{\mathfrak W}(\delta;N_m,\theta_m,T).
\]
By the path theorem, for all sufficiently large \(m\), this defect exceeds the total loss budget. But the forward theorem and positivity synthesis imply that the corresponding finite hierarchy at \((N_m,\theta_m)\) is already too close to the RH-consistent regime for such a defect to exist. This contradiction forces RH.

This is the mathematical shape of a successful witness-system proof program. The route succeeds only when the same finite coordinates carry both the forward convergence and the converse obstruction.

---

## 9. Failure modes and their translation into theorem obligations

The earlier failure modes remain valid, but they must now be expressed directly in witness-system language.

### 9.1. Proving the wrong topology

A closure statement in the wrong topology is mathematically irrelevant to RH even if it is true and elegant. The Hardy-space example makes this explicit: compact-open density is unconditional, but \(H^2\)-density is the RH-equivalent statement [Noor19].

**Witness-system translation.** Every presented witness system must declare:
- the exact critical ambient space \(\mathcal H_{\theta_c}\),
- the exact closure topology,
- the transport theorems identifying equivalent critical avatars.

No theorem package may enter the proof spine unless its target topology matches the exact core.

### 9.2. Forward bridges with no converse

A forward approximation theorem with no converse can generate endless progress of the wrong kind. The existence of Burnol lower bounds, BCF-type optimal constants, and CMNS orthogonality theory shows that converse structure is available and must be demanded [Burnol01], [BCF12], [CMNS24].

**Witness-system translation.** A principal witness system must carry an explicit reverse theorem, not merely a dual space in principle.

### 9.3. Conditionality and circularity

Conditional structures are useful, but they cannot appear in the proof spine. Suzuki’s Weil-distribution Hilbert space is a good example: it is informative, but it is constructed under RH [Suzuki23].

**Witness-system translation.** Every theorem and every avatar must be tagged as:
- unconditional,
- conditional on RH or an RH-equivalent statement,
- conditional on auxiliary arithmetic hypotheses,
- diagnostic only.

Only unconditional avatars and unconditional transports may appear in the main implication chain.

### 9.4. Height leakage

A converse theorem that deteriorates as \(T\to\infty\) is useless against a potential high zero. Radziwiłł’s work shows that the relevant geometry near height \(T\) is microscopic and tied to local zero spacing and zeros of \(\zeta'\) [Rad13].

**Witness-system translation.** Reverse detectability must be formulated in terms of a renormalized defect \(\widetilde G_{\mathfrak W}\) at local scale \(2\pi/\log T\), and the system should ideally expose derivative-zero sensitivity \(J_{\mathfrak W}\) as a diagnostic invariant.

### 9.5. Pathological witness-space geometry

An exact family can still be useless if its finite sections are too ill-conditioned or if the ambient spaces become too singular near the critical parameter. The weighted-space literature already shows that weights may be too fast or too slow to give a nontrivial half-plane [GKNS24], [GGS25].

**Witness-system translation.** Conditioning \(\kappa_{\mathfrak W}(N,\theta)\), frame bounds, growth constants, and weight geometry must be tracked as theorem outputs. A witness system with uncontrollable geometric degeneration near \(\theta_c\) is not strongly admissible.

### 9.6. Noncommuting limits

There are at least three asymptotic directions:
\[
N\to\infty,\qquad \theta\downarrow\theta_c,\qquad T\to\infty.
\]
If the proof requires these limits in an order that cannot be justified, it will stall at the end.

**Witness-system translation.** Limit stability is not an epilogue. It is one of the defining theorem obligations. Admissible paths must be specified early.

### 9.7. Positivity without margin

Finite PSD evidence means nothing if the smallest positive margin is of the same order as the truncation or transport error. Bombieri’s finite-support extremal viewpoint and the PF\(_5\) de Bruijn–Newman theorem both reinforce the point that finite positivity must be accompanied by explicit margins [Bombieri00], [Mich26].

**Witness-system translation.** Every finite positivity theorem must carry a strict inequality against the full loss budget.

### 9.8. Untracked assumptions

Dependence on \(\zeta'(\rho)\), simplicity of zeros, or moment bounds can silently enter through residue calculations, dual descriptions, or asymptotic formulas. The BCF theorem shows explicitly that assumptions involving \(\sum |\zeta'(\rho)|^{-2}\) matter [BCF12].

**Witness-system translation.** Every theorem package must expose an **assumption ledger**. If a package depends on auxiliary hypotheses, those hypotheses are part of the statement and cannot be hidden inside a transport or asymptotic shortcut.

### 9.9. Neglecting obstruction theorems

A theorem program that only accumulates forward theorems will waste effort. Bober’s classification of Vasyunin-related step-function families and the PF\(_5\) Toeplitz obstruction show that classification and obstruction theorems can cut away entire regions of the search space [Bober07], [Mich26].

**Witness-system translation.** Every principal class must have an obstruction agenda:
- rigidity theorems for syntactic subclasses,
- lower bounds for the approximation functional,
- negativity/degeneracy theorems for finite hierarchies,
- impossibility theorems for whole transport templates.

---

## 10. What counts as mathematical progress

The program should treat the following theorem types as co-equal forms of progress.

### 10.1. Representation theorems

- a new exact transport between avatars,
- a new dominance theorem,
- a new normal-form reduction,
- a new universality theorem for a class of witness systems.

### 10.2. Rigidity and obstruction theorems

- a classification theorem ruling out an entire class,
- a lower bound theorem for \(E_{\mathfrak W}(N,\theta)\),
- a theorem that a certain finite hierarchy must develop a negative or degenerate direction,
- a theorem showing that a certain weight regime or multiplier class cannot be strongly admissible.

### 10.3. Forward frontier theorems

- a new zero-free half-plane from an off-critical parameter,
- a stronger frontier \(F_{\mathfrak W}(N,\theta)\),
- a more stable finite hierarchy with better conditioning.

### 10.4. Dual/extremal theorems

- an explicit description of a dual space,
- a biorthogonal sequence,
- a reproducing-kernel extremal principle,
- a direct theorem connecting off-line zeros to finite defects.

### 10.5. Arithmetic theorems

- stabilization of canonical finite coefficients,
- identification of a Möbius or prime-sum locking profile,
- compatibility theorems between arithmetic locking and positivity or duality.

A theorem package is truly strategic only when it strengthens at least one of these categories without weakening the others.

---

## 11. The initial theorem agenda

The mathematically right first agenda is not “push one route harder”. It is to stabilize the six-avatar theory in the principal classes.

### 11.1. Semigroup/module package

For the Hardy class:
- formalize the exact \(H^2\)-closure criterion,
- formalize the weighted composition semigroup and its cyclicity/invariant-subspace consequences,
- formalize the multiplication-operator/range criterion in \(H^2(\Omega_\tau)\),
- prove the transport theorems between span, orbit, and range.

This package turns the classical Hardy picture into a genuine multi-avatar witness system.

### 11.2. Dual/extremal package

For the same class:
- describe the dual obstruction space explicitly,
- transport it into de Branges–Rovnyak / Toeplitz or local Dirichlet language,
- prove existence and completeness of a biorthogonal sequence or another explicit dual extremizer family,
- express off-line zeros as dual defects.

This is what converts forward closure into reverse-detecting closure.

### 11.3. Weighted deformation package

For the weighted Hardy/Dirichlet class:
- identify the correct parameter space \(\Theta\),
- prove zero-free half-plane theorems across \(\Theta\),
- determine the region of parameter space in which the weights are mathematically viable,
- record the arithmetic-locking profile,
- quantify conditioning and limit behavior as \(\theta\downarrow\theta_c\).

This package supplies the off-critical frontier.

### 11.4. Kernel normal-form package

For the co-Poisson/Müntz class:
- identify the admissible kernel conditions,
- prove transports from the kernel avatar to the closure avatar,
- determine which kernels admit non-compact support while preserving sufficiency,
- search for Sonine/de Branges normal forms.

This package is the best candidate for representation-theoretic simplification.

### 11.5. Finite hierarchy and positivity package

Across all principal classes:
- define the canonical finite-compression objects,
- prove exact reduction formulas plus tail bounds,
- couple the hierarchy to the explicit-formula / Weil backend,
- prove spectral-margin theorems,
- develop obstruction theorems in the style of PF\(_5\) [Mich26].

This package is where constructive mathematics and finite linear algebra enter the proof spine.

### 11.6. Local-geometry diagnostic package

Across all principal classes:
- define derivative-zero sensitivity \(J_{\mathfrak W}\),
- relate it to local gap geometry,
- test whether candidate witness systems actually see the microscopic critical-line structure indicated by Radziwiłł’s equivalence [Rad13].

This package prevents hidden height leakage.

---

## 12. The strategic endpoint

The program does not seek an arbitrary RH-equivalent theorem. It seeks the following specific object:

> A strongly admissible witness system \(\mathfrak W\), belonging to a principal class under the dominance preorder, together with an admissible path \((N_m,\theta_m)\) such that
> (i) the forward frontier tends to the critical line,
> (ii) the reverse modulus remains larger than the full loss budget after height normalization, and
> (iii) all core avatars and transports are unconditional.

That is the exact point at which a witness-system route becomes a genuine proof route.

The abstraction is not ornamental. It is the only mathematically honest way to avoid two opposite failures:
- spending years optimizing a witness family that has no reverse force, and
- drowning in an unstructured ocean of formally possible witness families.

The whole strategy therefore rests on the following principle:

> **Do not optimize witness families in isolation. First classify the space of witness systems, identify the principal classes, and insist that the same finite coordinates carry exact closure, off-critical progress, dual obstructions, arithmetic locking, finite margins, and a stable critical limit.**

That is the maximum amount of relevant mathematical structure currently available.

---

## References

**[BD02]** Luis Báez-Duarte, *A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis* (2002/2003).
arXiv: https://arxiv.org/abs/math/0205003
EuDML: https://eudml.org/doc/252348

**[BD05]** Luis Báez-Duarte, *A general strong Nyman–Beurling criterion for the Riemann hypothesis* (2005).
arXiv: https://arxiv.org/abs/math/0505453
DOI page: https://doi.org/10.2298/PIM0578117B

**[DH21]** Sébastien Darses and Erwan Hillion, *On probabilistic generalizations of the Nyman–Beurling criterion for the zeta function* (2021).
arXiv: https://arxiv.org/abs/1805.06733
PDF: https://cml.centre-mersenne.org/item/10.5802/cml.71.pdf

**[Noor19]** S. Waleed Noor, *A Hardy space analysis of the Báez-Duarte criterion for the RH* (2019).
arXiv: https://arxiv.org/abs/1809.09577

**[CMNS24]** Francisco Calderaro, Juan Manzur, Waleed Noor, Charles Santos, *Orthogonality questions in the Hardy space related to \(\zeta\)-zeros* (2024 version).
arXiv: https://arxiv.org/abs/2203.05030

**[MNS23]** Juan Manzur, Waleed Noor, Charles F. Santos, *A weighted composition semigroup related to three open problems* (2022/2023).
arXiv: https://arxiv.org/abs/2111.05398

**[WW22]** Fei Wei and Dongsheng Wu, *A characterization of the zero-free region of the Riemann zeta function and its applications* (2022).
PDF: https://bimsa.net/doc/publication/1424.pdf

**[GKNS24]** Aditya Ghosh, Kobi Kremnizer, Waleed Noor, Charles F. Santos, *Zero-free half-planes of the \(\zeta\)-function via spaces of analytic functions* (2024).
arXiv PDF: https://arxiv.org/pdf/2206.00434

**[GGS25]** Eva A. Gallardo-Gutiérrez and Daniel Seco, *Zero-Free Regions of the Riemann Zeta Function and Approximation in Weighted Dirichlet Spaces* (2025).
Springer page: https://link.springer.com/article/10.1007/s11785-025-01661-2
arXiv: https://arxiv.org/abs/2206.02654

**[DG20]** Hui Dan and Kunyu Guo, *The Periodic Dilation Completeness Problem: Cyclic vectors in the Hardy space over the infinite-dimensional polydisk* (2020/2021).
arXiv: https://arxiv.org/abs/1908.03113

**[Burnol01]** Jean-François Burnol, *A lower bound in an approximation problem involving the zeros of the Riemann zeta function* (2001/2002).
arXiv: https://arxiv.org/abs/math/0103058

**[Burnol04]** Jean-François Burnol, *Two complete and minimal systems associated with the zeros of the Riemann zeta function* (2004).
arXiv: https://arxiv.org/abs/math/0203120
EuDML: https://eudml.org/doc/249278

**[BCF12]** Sandro Bettin, J. Brian Conrey, David W. Farmer, *An optimal choice of Dirichlet polynomials for the Nyman–Beurling criterion* (2012/2013).
arXiv: https://arxiv.org/abs/1211.5191

**[MR17]** Helmut Maier and Michael Th. Rassias, *A criterion related to the Riemann Hypothesis* (2017/2018).
arXiv: https://arxiv.org/abs/1705.09918

**[DPT25]** Eugenio Dellepiane, Marco M. Peloso, Anita Tabacco, *On the equality of de Branges–Rovnyak and Dirichlet spaces* (2025).
arXiv: https://arxiv.org/abs/2505.16572

**[Bombieri00]** Enrico Bombieri, *Remarks on Weil’s quadratic functional in the theory of prime numbers* (2000).
EuDML: https://eudml.org/doc/252338

**[Lagarias04]** Jeffrey C. Lagarias, *Li Coefficients for Automorphic L-Functions* (2004/2007).
arXiv: https://arxiv.org/abs/math/0404394
Numdam PDF: https://www.numdam.org/item/10.5802/aif.2311.pdf

**[Suzuki22]** Masatoshi Suzuki, *Aspects of the screw function corresponding to the Riemann zeta-function* (2022/2023).
arXiv: https://arxiv.org/abs/2206.03682

**[Suzuki23]** Masatoshi Suzuki, *On the Hilbert space derived from the Weil distribution* (2023).
arXiv: https://arxiv.org/abs/2301.00421

**[RT18]** Brad Rodgers and Terence Tao, *The de Bruijn–Newman constant is non-negative* (2018/2020).
arXiv: https://arxiv.org/abs/1801.05914

**[Mich26]** *On the Pólya Frequency Order of the de Bruijn–Newman Kernel. Certified Failure at Order Five and the Toeplitz Threshold Phenomenon* (2026).
arXiv: https://arxiv.org/abs/2602.20313

**[Rad13]** Maksym Radziwiłł, *Gaps between zeros of \(\zeta(s)\) and the distribution of zeros of \(\zeta'(s)\)* (2013).
arXiv: https://arxiv.org/abs/1301.3232

**[Conrey03]** J. Brian Conrey, *The Riemann Hypothesis* (2003).
PDF: https://empslocal.ex.ac.uk/people/staff/mrwatkin/zeta/conreyRH.pdf

**[Bober07]** Jonathan Bober, *Factorial ratios, hypergeometric series, and a family of step functions* (2007).
arXiv: https://arxiv.org/abs/0709.1977

I want you to carefully review this strategy.

## Assistant 2

I’m checking the cited results and newer references against the primary literature while assessing whether the witness-system abstraction genuinely constrains a proof route or mostly repackages known difficulties. Then I’ll separate what is theorem-backed and strategically meaningful from what is useful language but currently overstated, under-specified, or mis-targeted.

## Assistant 3

The literature map is largely real, especially for the Hardy/module/weighted-space/kernel components. The real pressure point is whether your strong-admissibility axioms define a plausible, realizable subclass with genuine reverse-detecting force, rather than a meta-framework that bundles all the hard requirements together.

## Assistant 4

The sharpest corrections so far are concrete: your strongest support is the exact closure/transport/range/off-critical machinery, but there is still no theorem-level same-coordinate reverse obstruction, and the δ=ηlogT/(2π) normalization only matches microscopic η≍1/logT, not fixed η>0.

## Assistant 5

Overall judgment: this is a serious research architecture, not just a pile of equivalences with a new label. Its strongest move is the insistence that an RH-equivalent statement is only strategically meaningful if it comes with finite truncations, off-critical theorems, converse visibility, and controlled passage to the critical limit. The literature you assemble really does support the claim that the Nyman–Báez-Duarte line has already ramified into several interoperable pictures: Hardy-space closure and semigroup cyclicity, multiplication-range criteria on half-planes, weighted deformations yielding honest zero-free regions, dual/biorthogonal structures, kernel/co-Poisson/Sonine normal forms, and Bohr-lift multiplicative models.
arXiv
+7
arXiv
+7
arXiv
+7

The document is also right about the topology issue. That point is not philosophical. Noor really does show that RH is equivalent to 1∈
span
	​

{h
k
	​

}
H
2
, while the same family is unconditionally dense in the compact-open topology. So a route can genuinely prove the wrong density theorem and make no progress on RH. Your insistence that the critical topology be declared explicitly is exactly the correct response to that literature. Likewise, your decision to treat finite obstructions as first-class results is justified: Burnol gives nontrivial lower bounds in the Nyman distance problem, Bettin–Conrey–Farmer identify a conditional optimal constant, Maier–Rassias analyze the same distance under specific off-line-zero hypotheses, and Michałowski’s 2026 arXiv preprint gives a rigorously interval-certified negative 5×5 Toeplitz minor proving PF
5
	​

 failure for the classical de Bruijn–Newman kernel, while leaving PF
4
	​

 open.
arXiv
+5
arXiv
+5
arXiv
+5

So the core idea is good: stop optimizing isolated witness families and instead ask which systems carry enough structure that forward approximation and reverse obstruction live in the same coordinates. That is the right question. It is much sharper than “find another reformulation of RH.”

That said, as a proof strategy, the program still overreaches in a few important places.

First, the primitive object is over-specified in the wrong directions. Requiring G to be finitely presented is too strong if taken literally: the canonical multiplicative semigroup behind integer dilations is N
×
, which is not finitely generated. And a single seed κ
θ
	​

 is too restrictive for several natural module/range constructions, which are better viewed as finitely generated submodules than as single semigroup orbits. I would replace this by an effectively presented countable semigroup with a canonical finite truncation family, and I would allow finitely many seeds from the outset.

Second, the framework is still too approximation-centric. Your own “principal classes” show this. The explicit-formula / Weil / de Bruijn–Newman side is not naturally a target-vector closure problem with an optional positivity apparatus; it is fundamentally a cone-membership / positivity / finite-minor system. Forcing everything into

v
θ
c
	​

	​

∈
N
⋃
	​

W
N
	​

(θ
c
	​

)
	​


keeps approximation primary even where the mathematics wants positivity primary. I would broaden the primitive notion from “target vector plus witness spans” to “target constraint plus finitely compressible witness data,” where the target may be a closed subspace, a closed range, or a positivity cone.

Third, the six compulsory avatars are too rigid. Exact core, dual obstruction, finite compression, and quantitative loss control are genuinely structural. But semigroup, module, arithmetic-locking, Bohr lift, and Sonine/de Branges avatars are better treated as enhancement layers, not compulsory features of every viable class. As written, the compulsory list starts to define admissibility by the examples currently on the table.

Fourth, your notion of strong admissibility is closer to “a route that has already solved the hard part” than to a usable research class. Exact core, off-critical frontier, explicit duals, finite compression, reverse detection, height normalization, margin domination, and limit stability are not peer-level obligations. The last four are essentially the unsolved center of the problem. If Phase I studies the space of strongly admissible systems, there may be almost no unconditional examples to study. I would replace the binary adjective by a filtration: exact systems, forward-effective systems, dual-explicit systems, finitely compressible systems, reverse-detecting systems, and height-stable systems. Then a representation theory of lower levels is not vacuous.

Fifth, your dominance preorder and universality conjecture need a much harder quantitative core. What you are really after is not representation theory in the classical irreducible/module sense; it is a functorial normal-form theory of cyclic subspaces, modules, kernels, and positivity systems. Qualitative transport is easy. Quantitative transport is everything. A Mellin or Hardy transform can preserve exact closure and still destroy the only things that matter for a proof: margin, conditioning, or reverse signal. So a morphism must come with inequalities of the form

E
′
≲E+ε,G
′
≳G−ε,M
′
≳M−ε,κ
′
≲Φ(κ).

Without that, “dominance” is too soft to support universality. I would not state the global universality conjecture yet. At present it reads as a philosophical bet, not a mathematically grounded conjecture.

The real technical bottleneck is exactly the one you identify: reverse obstruction in the same finite coordinates. Here the document is strongest conceptually and weakest theoremically. But there is one place where you can say something more concrete than the current text does. In the Wei–Wu module model, the closed range is characterized by divisibility F/ϕ analytic, and for

ϕ(s)=
s
2
s−1
	​

ζ(s),

a zero ρ of ζ gives an annihilator by evaluation (and, for multiplicity m, by jets up to order m−1). Thus every finite witness of the form ϕD
N
	​

 vanishes at ρ, so for the target v(s)=
s
2
s−1
	​

,

∥v−w∥≥
∥k
ρ
	​

∥
∣v(ρ)∣
	​


with k
ρ
	​

 the reproducing kernel. That is already a same-coordinate reverse theorem in embryo, not just rhetoric. It follows directly from their range description and kernel formula. But it is also too weak: in the half-plane normalization of Wei–Wu, ∥k
ρ
	​

∥
−2
 is proportional to ℜρ−τ, while v(ρ)∼∣ρ∣
−1
, so the naive lower bound decays badly with height. This is a concrete model of your height leakage problem.
BIMSA
+1

That also explains why I do not think your normalized defect

δ=
2π
ηlogT
	​


is the whole story for truncation-based systems. It is the right scale for local zero geometry, especially in light of Radziwiłł’s equivalence between small gaps of zeros of ζ and zeros of ζ
′
 close to the line. But finite witness hierarchies have their own resolution scale, usually tied to N or to the deformation parameter. In Nyman/Báez-Duarte type problems, off-line-zero effects typically show up through N
ρ−1/2
-type terms. So a realistic reverse modulus probably depends on both local zero geometry near height T and a truncation-resolution variable such as (β−
2
1
	​

)logN. Your path theorem should therefore be explicitly three-parameter from the start, or else include a resolution function R
W
	​

(N,θ) telling you which heights are even visible at level N.
arXiv
+1

I am also not convinced by your Step 6, positivity synthesis, as presently written. Bombieri’s Weil functional, Lagarias’s Li-coefficient interpretation, Suzuki’s screw-function analogues, Rodgers–Tao’s de Bruijn–Newman theorem, and the PF
5
	​

 obstruction preprint all justify keeping positivity in the program. And your unconditional/core vs conditional/shadow separation is exactly right; Suzuki’s 2023 Weil-distribution Hilbert space is explicitly RH-conditional and belongs in the shadow layer, not the proof spine. But unless you exhibit an actual intertwiner from finite witness coordinates to a concrete test-function class for the Weil/Sonine/de Branges side, positivity remains an adjacent laboratory, not yet an integrated backend. I would only elevate positivity synthesis to the spine after a Sonine/de Branges collapse or some comparably rigid normal form has been proved.
arXiv
+5
EuDML
+5
EuDML
+5

That, in turn, is why I think the kernel / Sonine / de Branges line may deserve even more prominence than you currently give it. Báez-Duarte’s kernel generalization gives a genuinely broader closure framework, with necessity in a large class and sufficiency under compact support plus Mellin nonvanishing; Darses–Hillion extend that picture to probabilistic/non-compact settings with extra coefficient control; Burnol links co-Poisson ideas to Sonine spaces and complete/minimal systems from zeta zeros; and Dellepiane–Peloso–Tabacco show that some de Branges–Rovnyak spaces literally collapse to weighted Dirichlet spaces in a classified finite-atomic setting. If any part of your program has a plausible chance to make “representation theory of witness systems” non-metaphorical, it is probably this one.
arXiv
+4
arXiv
+4
arXiv
+4

So if I were tightening the document, I would make three concrete changes. I would demote universality from conjecture to long-range question. I would split avatars into core and enhancement layers. And I would frontload one hard, concrete theorem problem: in the Wei–Wu / CMNS Hardy-module setting, quantify the defect forced by a zero ρ not just on the infinite closed range but on the canonical finite Dirichlet subspaces, using reproducing kernels, jet annihilators, biorthogonals, and finite Gram sections. CMNS already provide the orthogonality and biorthogonal infrastructure. That is the place where your abstract reverse program can most plausibly become an actual estimate.
arXiv
+2
BIMSA
+2

The second concrete task should be to treat conditioning blow-up near the critical parameter as a primary obstruction theorem, not as bookkeeping. GKNS and Gallardo-Gutiérrez–Seco show that off-critical analytic spaces really do yield bona fide zero-free half-planes, and the latter explicitly emphasize the constructive advantage of Hilbert projections and the coefficient limit −μ(k)/k. But the same body of work also shows that nontrivial zero-free half-planes can require extreme weights. A route that reaches ℜs=
2
1
	​

 has to prove that the forward frontier improves faster than the geometry degenerates. That may well be the main obstruction, not a secondary estimate.
arXiv
+2
arXiv
+2

So my bottom line is this. As a research manifesto, this is strong. It is better organized than most RH programs because it separates exactness, off-critical effectivity, converse visibility, finite compression, arithmetic locking, and conditional shadow models. As a proof strategy, it is not yet narrow enough. The hard part has been relocated into strong admissibility, reverse modulus, and positivity synthesis. The decisive next step is not more abstraction. It is one sharp quantitative reverse theorem in a class with explicit duals and finitely compressible coordinates. Once that exists, the representation theory will start to deserve its name.

## User 6

Excellent work. I want you to take on the responsibility of transforming this project from a great research manifesto to a robust proof strategy. Redraft the strategy to address your concerns

## Assistant 7

I’m redrafting it into a narrower, theorem-driven proof spine: weaken the overfitted primitive object, separate core from enhancement structure, replace binary admissibility with a graded ladder, and center everything on one concrete same-coordinate reverse theorem in the Hardy/module setting.

## Assistant 8

The broader universality and positivity ambitions are being demoted to a secondary normal-form program. The main route now starts from one class with exact core and explicit dual, and builds height control plus truncation resolution into the reverse theorem and path problem from the outset.

## Assistant 9

Below is a redraft that narrows the manifesto into a proof strategy. The main changes are structural. The primitive object is broadened from a closure-only witness family to a quantitative witness-constraint system. “Strong admissibility” is replaced by a graded hierarchy so the program is not vacuous at the unconditional level. The global universality language is demoted. The proof spine is concentrated in the Hardy-module / weighted-deformation class. And the entire program is forced to hinge on one decisive missing theorem: a scale-stable reverse theorem in the same finite coordinates as the forward approximation.

Revised strategy for a quantitative witness-constraint program toward the Riemann hypothesis
1. Organizing principle

A proof route toward RH should not be organized around a single approximation criterion in isolation. It should be organized around a quantitative witness-constraint system whose finite truncations already carry the information that a proof would need. An RH-equivalent reformulation is strategically relevant only if it supplies five things at once: an exact critical theorem, an off-critical forward frontier, an explicit finite compression, a reverse defect visible in the same coordinates, and a coupled limit path that reaches the critical line without losing the signal.

The decisive correction is this: the program should not try to classify all possible “witness systems” first and only later ask how to prove RH in one of them. It should instead isolate a base class where the missing theorems are concrete, finite, and operator-theoretic, and only then ask which other systems admit quantitative transports into that base class.

2. Primitive object: a quantitative witness-constraint system

The right primitive object is not just a target vector plus a span. It is a tuple

W=(Θ,θ
c
	​

,{H
θ
	​

},{C
θ
	​

},{V
N
	​

(θ)},{D
θ
	​

},{Q
N,θ
	​

},{L
N,θ
	​

},T),

with the following meaning.

Θ is a parameter space with critical parameter θ
c
	​

. The spaces H
θ
	​

 are ambient Hilbert or Banach spaces, but the proof spine should preferentially live in Hilbert spaces because finite compression, orthogonal projection, and dual extremals are then explicit. The object C
θ
	​

 is the constraint to be satisfied at parameter θ. It may be a target vector v
θ
	​

, a range condition such as u
θ
	​

∈
Ran(M
ϕ
θ
	​

	​

)
	​

, or a positivity condition such as membership in a PSD cone. The finite witness spaces V
N
	​

(θ) are generated from an effectively presented countable monoid and finitely many seeds, not from a literally finitely presented semigroup and a single seed. Concretely, one should allow

V
N
	​

(θ)=span{μ
θ,j
	​

ρ
θ
	​

(g)κ
θ,j
	​

:g∈I
N
	​

, 1≤j≤r},

with I
N
	​

 finite and nested, and r<∞ fixed. This is the correct level of generality for the actual examples.

The point of replacing a target vector by a target constraint is that not all serious RH structures are closure problems of the same type. Noor’s H
2
-closure formulation is genuinely of target-vector type, but Wei–Wu’s criterion is a module/range statement, and the explicit-formula / de Bruijn–Newman side is fundamentally a positivity / finite-minor system rather than a span-closure problem. Noor proves that RH is equivalent to 1∈
span{h
k
	​

:k≥2}
	​

H
2
, while the same family is unconditionally dense only in the compact-open topology; that is exactly the warning that the topology and the constraint type must be part of the primitive data. Wei–Wu prove that for suitable ϕ,

Ran(M
ϕ
	​

)={F∈H
2
(Ω
τ
	​

):F/ϕ analytic in Ω
τ
∘
	​

},

and for ϕ(s)=
s
2
s−1
	​

ζ(s), zero-freeness in ℜs>τ is equivalent to the corresponding range being all of H
2
(Ω
τ
	​

).
arXiv
+2
BIMSA
+2

3. Core structure versus enhancement structure

The original manifesto made too many avatars compulsory. That overfits the current examples. The corrected version separates core structure from enhancement structure.

A system belongs to the core proof program only if it has the following layers.

An E-system has an exact critical theorem. An F-system adds an off-critical frontier theorem turning finite information into an actual zero-free region or positivity consequence. A C-system adds finite compression, conditioning control, and an explicit loss budget. A D-system adds an explicit dual/extremal model—biorthogonals, Toeplitz kernels, reproducing kernels, or equivalent. An R-system adds a reverse theorem in the same finite coordinates. An S-system adds a scale-stable coupled path theorem that lets N→∞ and θ↓θ
c
	​

 without losing reverse visibility. A P-system additionally couples to an external positivity backend.

This graded hierarchy matters because almost no currently available systems are fully “strong” in the sense of already containing everything one would need for a proof. But several important systems already sit high in the hierarchy. Noor gives an exact critical H
2
 model with a semigroup action. Wei–Wu give a module/range avatar and a bounded-Dirichlet-polynomial criterion. Calderaro–Manzur–Noor–Santos give an explicit orthogonality picture and a complete biorthogonal sequence. Ghosh–Kremnizer–Noor–Santos and Gallardo-Gutiérrez–Seco give off-critical spaces that produce genuine zero-free half-planes, and Gallardo-Gutiérrez–Seco also emphasize the constructive value of Hilbert-space truncations and record the coefficient rigidity c
k,n
	​

→−μ(k)/k.
arXiv
+5
arXiv
+5
BIMSA
+5

The enhancement structure—semigroup orbit, module avatar, arithmetic locking, Bohr lift, kernel/co-Poisson/Sonine normal forms, explicit-formula positivity—is highly valuable, but not every base class needs all of it before entering the proof spine.

4. Quantitative morphisms and dominance

Representation theory only becomes mathematically serious here if “transport” means quantitative transport. A mere formal equivalence between two avatars is not enough. A morphism Φ:W→W
′
 should come with inequalities of the shape

E
Φ(N,θ)
′
	​

≤AE
N,θ
	​

+ε
N,θ
	​

,G
Φ(N,θ)
′
	​

≥BG
N,θ
	​

−ε
N,θ
	​

,
M
Φ(N,θ)
′
	​

≥BM
N,θ
	​

−ε
N,θ
	​

,κ
Φ(N,θ)
′
	​

≤Ψ(κ
N,θ
	​

),

where E is the forward error, G the reverse modulus, M the positivity margin, and κ the conditioning profile. Only then does it make sense to write W⪯
q
	​

W
′
.

This changes the representation-theoretic agenda. The program should not state a global universality conjecture at present. That claim is too strong and too qualitative. What it should state are relative normal-form problems: within a concrete graded class, can every system be transported into a Hardy-module or kernel normal form while preserving margins, reverse signal, and conditioning up to controlled loss? That is a mathematically tractable question. A global universality principle is not.

5. Two scales of reverse visibility

The reverse theory must be formulated on two scales, not one. If ρ=β+iT is a hypothetical zero with β>1/2, then the local spectral scale at height T is

δ
T
	​

=
2π
(β−
2
1
	​

)logT
	​

.

That is the correct normalization for local zero geometry. But finite witness systems also have a separate resolution scale, determined by the truncation and the deformation. Write it as

ν
N,θ
	​

=(β−σ(θ))R
θ
	​

(N),

where σ(θ) is the off-critical frontier delivered by the forward theorem and R
θ
	​

(N) is the effective resolution of the finite hierarchy at level (N,θ).

The crucial correction to the original manifesto is this: a reverse theorem depending only on δ
T
	​

 is not enough. A finite hierarchy can miss a zero for purely resolution-theoretic reasons even if the height-normalized geometry is favorable. The right reverse modulus is therefore

G
W
	​

(δ
T
	​

,ν
N,θ
	​

;N,θ,T),

not a function of height alone. The path theorem must force the approach to the critical line to be slower than the gain in finite resolution, schematically through a condition of the form

R
θ
m
	​

	​

(N
m
	​

)(θ
m
	​

−θ
c
	​

)→∞

along the admissible path. That condition is non-negotiable. Without it, the route can accumulate forward theorems forever and still fail to see a critical-line defect in finite coordinates.

6. The base class that should carry the proof spine

The proof spine should start in the Hardy-module / weighted-deformation class. It is the only currently available class that already contains, in one connected package, an exact critical Hilbert-space statement, a module/range avatar, a semigroup picture, explicit dual machinery, and off-critical deformations with genuine zero-free consequences. Noor’s Hardy-space model gives the exact critical theorem, the semigroup W
n
	​

, and the warning about compact-open density. Wei–Wu give the module/range statement on half-plane Hardy spaces and a weaker Nyman–Beurling–Báez-Duarte criterion phrased in terms of Dirichlet polynomials D
N
	​

 with bounded ∥ϕD
N
	​

∥
H
2
(Ω
τ
	​

)
	​

. Calderaro–Manzur–Noor–Santos analyze the orthogonal complement via unbounded Toeplitz and de Branges–Rovnyak methods and prove that (h
k
	​

) has a complete biorthogonal sequence. GKNS and Gallardo-Gutiérrez–Seco provide the off-critical deformations that turn approximation statements into actual zero-free half-planes, and Gallardo-Gutiérrez–Seco emphasize that in Hilbert models the finite truncations become constructive through orthogonal projection and finite-dimensional optimization.
arXiv
+5
arXiv
+5
BIMSA
+5

The concrete base system should therefore be built from two transported avatars of the same structure.

The critical avatar is Noor’s disk Hardy-space model:

N
N
c
	​

=span{h
k
	​

:2≤k≤N}⊂H
2
(D),target 1.

The off-critical avatar is Wei–Wu’s half-plane module model:

ϕ
τ
	​

(s)=
s
2
s−1
	​

ζ(s),u(s)=
s
2
s−1
	​

,
V
N
	​

(τ)={ϕ
τ
	​

(s)D
N
	​

(s):D
N
	​

(s)=
n≤N
∑
	​

a
n
	​

n
−s
}⊂H
2
(Ω
τ
	​

),
2
1
	​

<τ≤1.

The disk and half-plane models are to be connected by an explicit Cayley/Mellin transport with quantified norm comparison, not just qualitative equivalence. The weighted Dirichlet / weighted Hardy spaces then provide the deformation family that produces the forward frontier. The base strategy is to prove everything first in the half-plane module coordinates, where zeros become annihilators naturally, and then transport back to the exact critical H
2
(D) statement.
arXiv
+3
BIMSA
+3
BIMSA
+3

7. The central theorem package

The entire program should now be stated as the problem of proving three specific theorem packages in this base class.

Theorem A: finite compression with explicit losses. For each τ>1/2 and N, one needs an explicit finite quadratic-form representation of

∥u−P
V
N
	​

(τ)
	​

u∥
H
2
(Ω
τ
	​

)
2
	​

,

together with certified tail bounds and conditioning estimates. The point is not merely that such a norm is finite. It is that the extremal problem should reduce to a finite Gram matrix G
N,τ
	​

 and target vector b
N,τ
	​

 with

dist(u,V
N
	​

(τ))
2
=∥u∥
2
−b
N,τ
∗
	​

G
N,τ
−1
	​

b
N,τ
	​

+Err
N,τ
	​

,

and with Err
N,τ
	​

 and κ(G
N,τ
	​

) explicitly controlled. Wei–Wu already note, at the critical Hardy half-plane, that ∥ϕD
N
	​

∥
2
 becomes an explicit positive-definite quadratic form in the Dirichlet coefficients, and Gallardo-Gutiérrez–Seco make the same constructive point in the weighted Dirichlet setting. That observation must be upgraded from a convenient feature into a theorem package with a full loss ledger.
BIMSA
+2
BIMSA
+2

Theorem B: finite reverse visibility in the same coordinates. This is the real bottleneck. If ρ=β+iT is a zero of ζ with β>τ, then every element of V
N
	​

(τ) vanishes at ρ. So evaluation and, when relevant, jet functionals at ρ annihilate the finite witness space. In reproducing-kernel language this gives immediate orthogonal defect functionals. But the raw evaluation defect is not enough; by itself it is too weak and too height-sensitive. The correct theorem must construct localized dual packets

ψ
N,τ,ρ
	​

∈V
N
	​

(τ)
⊥
,

built from evaluation kernels, jets, and the CMNS biorthogonal machinery, such that

dist(u,V
N
	​

(τ))≥G(δ
T
	​

,ν
N,τ
	​

)−L
N,τ,T
	​


with G explicit and genuinely positive whenever the off-line zero is visible at the finite resolution scale. The decisive point is that the same N and the same finite coordinates appearing in the forward extremal problem must also carry this reverse obstruction. CMNS provide the right dual infrastructure for attempting exactly this construction.
arXiv
+2
arXiv
+2

Theorem C: a coupled path theorem. Let τ
m
	​

↓1/2 and N
m
	​

→∞. One needs a theorem showing that these can be coupled so that the forward frontier approaches the critical line while the finite hierarchy still resolves off-line zeros at that frontier scale. Schematically, the path must satisfy

R
τ
m
	​

	​

(N
m
	​

)(τ
m
	​

−
2
1
	​

)→∞,L
N
m
	​

,τ
m
	​

,T
	​

→0,κ(N
m
	​

,τ
m
	​

) remains controlled enough,

and at the same time the forward theorem must force

dist(u,V
N
m
	​

	​

(τ
m
	​

))→0.

If RH failed, Theorem B would then force a positive lower bound along the same path for sufficiently large m, giving the contradiction. This is the correct endgame. It replaces the earlier abstract “limit-stability” language by one concrete coupled-resolution requirement.

8. What becomes secondary, and why

The kernel / co-Poisson / Sonine line remains important, but it should be treated as a normal-form track, not as the initial proof spine. Báez-Duarte’s general strong criterion shows that kernel-generated systems are genuinely broader than the original discrete criterion, with necessity in a very broad class and sufficiency under compact support plus a Mellin-transform nonvanishing hypothesis. Darses–Hillion show that a probabilistic enlargement of the Nyman–Beurling picture overlaps significantly with the general strong Báez-Duarte setting and can accommodate non-compact behavior under extra coefficient control. That makes the kernel class the most plausible source of future normal forms, but it does not yet provide the quantitative reverse machinery needed for the main spine.
arXiv
+2
arXiv
+2

The Bohr-lift / prime-graded and de Branges–Rovnyak / Dirichlet-collapse tracks are also secondary at this stage. Dan–Guo show that the periodic dilation completeness problem can be transported to cyclicity in the Hardy space over the infinite polydisk, which is exactly the kind of prime-graded normal form one would want for multiplicative witness systems. Dellepiane–Peloso–Tabacco show that, for finite atomic measures, one can precisely characterize when a de Branges–Rovnyak space is also a harmonically weighted Dirichlet space. Both are structurally important, but neither should enter the proof spine until there is a margin-preserving transport from the base Hardy-module coordinates.
arXiv
+1

The explicit-formula / Weil / de Bruijn–Newman line should be retained as a positivity and obstruction laboratory, not yet as a core backend. Bombieri’s memoir makes precise that Weil’s quadratic functional is positive semidefinite exactly under RH; Lagarias relates Li-type coefficients to values of that functional; Rodgers–Tao establish Λ≥0 for the de Bruijn–Newman constant; and Michałowski’s 2026 arXiv preprint gives a rigorously certified negative 5×5 Toeplitz minor for the classical de Bruijn–Newman kernel, while leaving PF
4
	​

 open. This is exactly the right laboratory for finite positivity and obstruction methods. But positivity only joins the main proof spine after there is an explicit intertwiner from the finite Hardy-module coordinates to the relevant explicit-formula test-function coordinates with certified margin control.
arXiv
+3
EuDML
+3
arXiv
+3

9. Immediate theorem agenda

The immediate agenda is therefore much narrower than the original manifesto, and much harder in a productive way.

Build the exact transport between Noor’s H
2
(D) finite spans and Wei–Wu’s H
2
(Ω
τ
	​

) finite Dirichlet module spaces, with explicit operator norms and losses.

Derive the finite extremal package for V
N
	​

(τ): Gram matrices, target vectors, error terms, and condition numbers.

Construct the first reverse packets from evaluation kernels and jets at zeros of ζ, then strengthen them using the CMNS biorthogonal system until the lower bound depends on both height scale and truncation scale.

Determine the resolution function R
τ
	​

(N) for the finite Dirichlet hierarchy and couple it to the off-critical frontier coming from the weighted Hardy/Dirichlet deformations of GKNS and Gallardo-Gutiérrez–Seco.

Only after that, revisit kernel normal forms, Bohr lifts, and positivity synthesis, asking whether they preserve the already-proved finite margins and reverse moduli.

10. Strategic endpoint

A genuine proof route now has a sharply stated endpoint. One must exhibit a base system in the Hardy-module / weighted-deformation class together with a path (N
m
	​

,τ
m
	​

) such that:

τ
m
	​

↓
2
1
	​

,dist(u,V
N
m
	​

	​

(τ
m
	​

))→0,

while simultaneously

R
τ
m
	​

	​

(N
m
	​

)(τ
m
	​

−
2
1
	​

)→∞,G(δ
T
	​

,ν
N
m
	​

,τ
m
	​

	​

)−L
N
m
	​

,τ
m
	​

,T
	​

>0

for every fixed off-line zero ρ that would exist if RH failed.

That is the exact point at which the program becomes a proof strategy rather than a manifesto. It is narrower because it does not pretend to solve the representation theory of all witness systems in advance. It is stronger because it makes one theorem package decisive: a scale-stable reverse theorem in finite Hardy-module coordinates. If that theorem cannot be proved, the strategy fails for intrinsic reasons. If it can be proved, the rest of the architecture has a real spine rather than a collection of compatible metaphors.
