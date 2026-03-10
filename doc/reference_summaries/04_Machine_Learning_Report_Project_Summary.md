# Machine Learning Report - Project Summary

## Source

- Reference PDF: `reference/Report Machine Learning.pdf`

## Document Objective

The report describes the practical work carried out on the test rig, the dataset construction process, the selection of significant TE frequencies, the import of models into TwinCAT, and the critical issues encountered during implementation.

## Main Contents

- Automated collection of the experimental dataset.
- Definition of the PLC-based experimental phases.
- Use of the `DataValid` variable to isolate the valid segment for TE computation.
- Analysis of the most relevant dimensionless frequencies.
- Import of the models into TwinCAT through dedicated function blocks.
- Practical reproduction and compensation tests.

## Reconstructed Experimental Workflow

- Set speed, torque, and temperature parameters.
- Monitor limits and safety conditions.
- Perform warm-up until the target temperature is reached.
- Execute homing and encoder zeroing.
- Run forward and backward tests.
- Record the data and segment the useful portion through `DataValid`.

## TwinCAT And Function Blocks

- `FB_Predict` is used to query the ML model.
- `ML_Transmission_Error` uses the model prediction to reconstruct and apply the compensation.
- Model import into TwinCAT requires attention to format, XML files, and runtime limitations.

## Important Technical Notes

- The experimental procedure is implemented as a state machine.
- Temperature can be treated as an initial constant value or as an updated signal, but the choice must be explicit.
- The frequencies used for compensation come from experimental analysis, not from arbitrary selection.
- PLC robustness requires NaN handling, cycle-time awareness, and simple runtime structures.

## Implications For This Repository

- The data pipeline must remain coherent with the real experiment, not only with static CSV files.
- Future configurations should be able to track:
  - operating conditions;
  - selected frequencies;
  - temperature usage strategy;
  - compensation mode.
- The project should maintain a clear separation among:
  - data collection;
  - harmonic analysis;
  - model training;
  - export and deployment.

## Derived Software Requirements

- Expose clearly the link between experimental inputs and model inputs.
- Keep the main pipeline steps reproducible.
- Shape the model output in a form directly usable for TE reconstruction and compensation.
