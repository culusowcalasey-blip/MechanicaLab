# Project 01 — Beam Failure Investigation

## Objective

Investigate how a simply supported beam responds to changing load, geometry, and material properties.

The first version will use classical beam-bending equations. Machine learning comes later, after the engineering model and dataset are understood.

## Learning sequence

1. Define the physical problem and assumptions.
2. Calculate bending stress from first principles.
3. Generate a controlled dataset.
4. Visualize stress and failure regions.
5. Check the simulation against hand calculations.
6. Train a simple ML surrogate.
7. Compare ML predictions with the engineering model.
8. Document limitations and failure cases.

## Initial model

For a rectangular cross-section:

- Maximum bending stress: sigma = M*c/I
- Rectangular second moment of area: I = b*h^3/12
- Outer-fiber distance: c = h/2

For a simply supported beam with a central point load:

- Maximum moment: M = P*L/4

The model is intentionally simple at first. We will add complexity only when the underlying mechanics are understood.

## Status

**Stage 0 — repository setup**

Next: implement and test the engineering calculation.
