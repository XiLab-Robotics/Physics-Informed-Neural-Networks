# Track 1 Extended Overnight Campaign Package

## Overview

This package prepares the larger and heavier `Track 1` overnight campaign
approved after the previous overnight batch showed that the current
harmonic-wise validation path is operationally cheap.

The package is intentionally launched through one command, but it is organized
into `6` logical blocks and `48` total runs:

1. wide low-order `HGBM` search;
2. heavy low-order `HGBM` runs;
3. late-harmonic repair expansion;
4. low-order plus late-harmonic bridge runs;
5. engineered-term recheck under heavy structure;
6. narrow `RF` controls.

## Included Run Files

### Block A

`01` to `12`

### Block B

`13` to `18`

### Block C

`19` to `26`

### Block D

`27` to `34`

### Block E

`35` to `40`

### Block F

`41` to `48`

## Scope Boundary

All runs stay inside the current repository-owned harmonic-wise offline
evaluator.

This package does not introduce a new target-parameterization implementation.
Its role is to push the current coefficient-based `Track 1` branch much harder
before escalating to a more structural pipeline change.
