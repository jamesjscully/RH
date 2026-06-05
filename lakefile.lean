import Lake
open Lake DSL

package «rh» where
  version := v!"0.1.0"
  keywords := #["mathematics", "riemann-hypothesis", "formalization"]

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "v4.30.0"

@[default_target]
lean_lib RH where
  roots := #[`RH]
