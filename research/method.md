# The bridge-building loop — our theory-building process (2026-06-06)

A loose process for building new theory in an identified direction. Not rigid — enough to keep us
honest and moving. The governing principle: **definition-first, reverse-engineered from the
conclusion; move *all* the hardness into one constructive question; never "try to prove RH."**

## The six steps (loop, not line)

1. **MECHANISM.** In every case where the bridge already works, state the *object-free* reason it
   works — strip the mechanism off the instances. (Output: an abstract structural statement.)
2. **AXIOMS.** Reverse-engineer axioms on an abstract object so that **`axioms ⟹ goal` is FORMAL**
   (a one-line lemma). If it isn't formal, the *gap in the implication names the missing axiom* —
   that failure is the most useful output, not a setback.
3. **OBSTRUCTION.** Name, as a precise *object* (not a feeling), what blocks importing the mechanism
   here. (Output: a thing you can point at.)
4. **REPAIR + UNIVERSAL PROPERTY.** The minimal new structure that annihilates the obstruction —
   stated as *what the object represents* (a functor / universal property), not as a hand
   construction. (Output: a spec the object must satisfy, and the one positivity/construction left.)
5. **MODEL + FALSIFY.** A candidate realization, tested on the *simplest nontrivial case* and against
   the kill-tests (`falsify.py`: Euler-borne / sees-zeros / independent). (Output: pass, or a located
   failure.)
6. **LOOP.** A failure *measures* the next missing axiom/structure — add it, return to step 2. The
   definition is wrong the first several times *by design*; each pass is bisection on the space of
   definitions.

## The discipline that makes it reliable
At every moment you are doing exactly one of: **(a) sharpening axioms so the conclusion is more
formal**, or **(b) measuring a specific failure that names the next axiom**. You are never flailing at
the theorem; you are converging on the definition. The falsifier stays in the loop on every guess so
no RH-silent / circular candidate is ever mistaken for progress.

## Where the hardness is allowed to live
After step 2, *all* difficulty should sit in step 4–5 (construct a model / verify one positivity) —
the conclusion from the axioms must be trivial. If you find yourself doing hard analysis to get from
the axioms to the goal, you have the wrong axioms (return to step 2). The art is choosing *where* to
put the one hard thing so a definition can dissolve it.
