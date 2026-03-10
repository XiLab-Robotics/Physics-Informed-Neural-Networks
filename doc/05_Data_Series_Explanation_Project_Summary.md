# Data Series Explanation - Project Summary

## Source

- Reference PDF: `reference/SpiegazioneSerieDati.pdf`

## Document Objective

This document explains how the test-rig data series are built and which operational steps determine the validity of the samples used to compute Transmission Error.

## Measurement System Structure

- Absolute Renishaw encoders on the high-speed and low-speed sides.
- Bosch position-controlled servomotor on the input side.
- Bosch torque-controlled servomotor on the output side.
- Manner torquemeter.
- Temperature sensors.
- Tested reducer and secondary reducer.

## Meaning Of The Data

- Raw absolute encoder values are available.
- Cumulative multi-turn values computed after common zeroing are available.
- TE computation uses only a specific valid sample window identified by `DataValid`.

## Test Operational Procedure

1. Warm-up until the target temperature is reached.
2. Homing to the absolute zero position of the reducer.
3. Unloading of the low-speed side.
4. Common software zeroing of the two encoders.
5. Run the input-side motor at the target speed.
6. Ramp the torque on the low-speed side up to the target value.
7. Start data acquisition in steady operating conditions.
8. Activate `DataValid` only in the angular interval used for TE computation.

## Key Messages

- The common zeroing does not necessarily coincide with the absolute zero of each encoder.
- The `DataValid` window is essential to avoid using samples that are inconsistent with the TE definition.
- The same procedure is repeated for both motion directions.

## Implications For This Repository

- Data loaders must preserve or reconstruct the meaning of `DataValid`.
- Angular features must be interpreted with the distinction between raw, zeroed, and cumulative signals.
- Future preprocessing must avoid mixing valid segments with transient segments.

## Pipeline Requirements

- Always track which position representation is being used.
- Keep the ability to filter the valid window.
- Make the difference between absolute zero, software zeroing, and cumulative position explicit in code.
