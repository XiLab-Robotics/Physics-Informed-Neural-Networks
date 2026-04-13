# Track 1 Overnight Gap-Closure Campaign Package

## Overview

This package prepares the next overnight `Track 1` batch after the canonical
paper-table replication milestone.

It is intentionally a single launch surface built from `4` logical campaign
blocks:

1. low-order `HGBM` ladder;
2. late-harmonic repair ladder;
3. `RandomForest` counterfactuals;
4. engineered-term recovery runs.

Operationally, the dedicated launcher runs the entire package through one
command. The four campaign blocks are organizational groups inside one
coordinated overnight batch.

## Included Runs

### Campaign A: Low-Order HGBM Ladder

1. `01_track1_hgbm_h01_deeper_low_order.yaml`
2. `02_track1_hgbm_h013_deeper_low_order.yaml`
3. `03_track1_hgbm_h01_ultradeep_guarded.yaml`
4. `04_track1_hgbm_h01_shallow_regularized.yaml`
5. `05_track1_hgbm_h0139_low_order_anchor.yaml`
6. `06_track1_hgbm_h014078_low_order_anchor.yaml`

### Campaign B: Late-Harmonic Repair Ladder

1. `07_track1_hgbm_h162_h240_repair.yaml`
2. `08_track1_hgbm_h081_h162_h240_repair.yaml`
3. `09_track1_hgbm_h156_h162_h240_repair.yaml`
4. `10_track1_hgbm_h039_h162_h240_bridge.yaml`
5. `11_track1_hgbm_h013_h162_h240_joint.yaml`
6. `12_track1_hgbm_h240_extreme_focus.yaml`

### Campaign C: Random-Forest Counterfactuals

1. `13_track1_rf_full_rcim_reference.yaml`
2. `14_track1_rf_h01_focus.yaml`
3. `15_track1_rf_h081_focus.yaml`
4. `16_track1_rf_h156_h162_h240_focus.yaml`

### Campaign D: Engineered-Term Recovery

1. `17_track1_hgbm_h01_engineered_recheck.yaml`
2. `18_track1_hgbm_h013_engineered_recheck.yaml`
3. `19_track1_hgbm_h162_h240_engineered_recheck.yaml`
4. `20_track1_rf_h01_h081_engineered_recheck.yaml`

## Scope Boundary

All runs stay inside the currently implemented harmonic-wise offline evaluator.

This package does not introduce new target parameterization code. Its role is
to push the current coefficient-based `Track 1` branch as far as possible
against:

- the paper Tables `3-6` gap surface;
- the shared offline `Target A` threshold.
