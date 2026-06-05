/-!
Abstract Hilbert-space placeholders used by the first witness-system skeleton.

The initial project avoids committing to a full analytic library. Concrete
inner-product and normed-space assumptions should be introduced only when a
specific theorem package needs them.
-/

namespace RH

structure AbstractSpace where
  Carrier : Type

end RH
