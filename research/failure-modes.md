# Failure Modes

## Wrong Topology

A witness family may be dense in a topology that does not imply the RH-equivalent critical statement.

Mitigation:

Every theorem must state the norm and topology.

## Height Leakage

Evaluation defects at zeros may decay too quickly as \(T\to\infty\).

Mitigation:

Track height dependence in raw and projected reverse packets.

## Conditioning Blow-Up

Finite Gram matrices may become ill-conditioned as \(\tau\downarrow1/2\).

Mitigation:

Make condition numbers part of Theorem A.

## Noncommuting Limits

The limits \(N\to\infty\), \(\tau\downarrow1/2\), and \(T\to\infty\) may not commute.

Mitigation:

All path theorems must explicitly couple \(N,\tau,T\).

## Reverse Signal Outside Forward Coordinates

An obstruction may exist in the infinite space but not in the finite coordinates used by forward approximation.

Mitigation:

Theorem B requires same-coordinate reverse visibility.

## Transport Loss

Transforms between disk, half-plane, weighted, kernel, or positivity avatars may destroy margins.

Mitigation:

Every transport must include forward, reverse, conditioning, and loss inequalities.

## Positivity Without Intertwiner

Explicit-formula positivity may remain adjacent to the strategy without connecting to finite witness coordinates.

Mitigation:

Keep positivity secondary until a certified finite-coordinate intertwiner exists.

## Over-Abstraction

The program may spend effort classifying witness systems before proving anything in the base class.

Mitigation:

Prioritize Theorem A/B/C in the Hardy-module base class.
