import Lake
open Lake DSL

package «rh» where
  version := v!"0.1.0"
  keywords := #["mathematics", "riemann-hypothesis", "formalization"]

lean_lib RH where
  roots := #[`RH]
