/-!
Placeholder module for complex-analytic foundations.

This file intentionally starts small. As the project matures it should collect
basic half-plane, disk, and complex-function definitions that are not already
available from upstream libraries.
-/

namespace RH

structure ComplexPoint where
  re : Float
  im : Float
deriving Repr

end RH
