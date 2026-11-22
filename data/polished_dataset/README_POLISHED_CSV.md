# Polished Transmission Error CSVs — Portable Evaluator Reference

This `track2-portable` branch **contains historical exported CSV files**, not
the raw measurement archive or the scripts needed to regenerate the datasets.
The source generation workflow converts raw measurements into direction-separated,
time-ordered curves in canonical research `main`.

The authoritative dataset lineage, signal definitions, equations, audited
normalization and use constraints remain in the
[research-main Transmission Error Dataset Family Reference](https://github.com/XiLab-Robotics/Physics-Informed-Neural-Networks/blob/main/doc/reference_summaries/08_Transmission_Error_Dataset_Family_Reference.md).
This external link is deliberate: `doc/reference_summaries/` is **not**
included in the portable branch. For packaged evaluator usage see the
[portable README](../../README.md).

## Historical Generator and Packaged Folder Structure

In the **separate research-main branch**, the original standalone generator is
[`data/generate_polished_dataset.py`](https://github.com/XiLab-Robotics/Physics-Informed-Neural-Networks/blob/main/data/generate_polished_dataset.py).
It historically uses `data/original_dataset` as input and
`data/polished_dataset` as output. The integrated generator is
[`scripts/datasets/generate_polished_transmission_error_dataset.py`](https://github.com/XiLab-Robotics/Physics-Informed-Neural-Networks/blob/main/scripts/datasets/generate_polished_transmission_error_dataset.py),
with a historical default output of `output/generated_polished_dataset/`.
Both are **absent from this branch**; do not execute those paths from a
portable checkout. Historical generator progress/overwrite behavior is not
an execution receipt for this branch.

Packaged data files here follow the direction/condition layout:

```text
data/polished_dataset/
  forward/
    25degree/
      1000rpm/
        1000.0rpm100.0Nm25.0deg.csv
  backward/
    25degree/
      1000rpm/
        1000.0rpm100.0Nm25.0deg.csv
```

## Historical Duplicate Conditions

During the original generation, source files were grouped by the nominal speed, torque, and temperature parsed
from the source filename. If multiple source files have the same conditions,
the Python exporter emits a `RuntimeWarning`, keeps the first sorted source
file, and skips later duplicates to avoid overwriting the same output path.

In the original dataset there are the following duplicated measurements that
have to be handled manually:

- ~~'200.0rpm0.0Nm25.0deg1.csv'~~
- ~~'200.0rpm100.0Nm25.0deg1.csv'~~
- ~~'800.0rpm200.0Nm25.0deg.csv'~~ --> '800.0rpm200.0Nm25.0deg_1.csv'
- ~~'1100.0rpm100.0Nm30.0deg_collegamento.csv'~~
- ~~'1600.0rpm100.0Nm30.0degCollegamiento.csv'~~
- ~~'1600.0rpm100.0Nm30.0degcollegamento2.csv'~~

## Filename Convention

Each exported file uses the nominal operating conditions from the source
filename:

```text
<speed>.0rpm<torque>.0Nm<temperature>.0deg.csv
```

Units:

```text
speed        rpm, motor side
torque       Nm
temperature  degC
```

Folder names omit unnecessary decimal places, for example `25degree` and
`1000rpm`. Filenames keep one decimal place, for example
`1000.0rpm100.0Nm25.0deg.csv`.

## File Content

Every exported CSV contains:

```text
theta,theta_dot,tau_load,T,theta_TE
```

Columns:

```text
theta      output-equivalent angle derived from the cumulative input encoder, deg
theta_dot  motor/input-side speed derived from consecutive position samples, rpm
tau_load   signed measured load/output-side Manner torque, Nm
T          measured tested-reducer oil temperature, degC
theta_TE   transmission error calculated from measured encoder positions, deg
```

`theta_TE` is calculated after the output-side zeroing correction:

```text
theta_TE = q_not_zeroed - theta
```

`theta` is not the unchanged absolute motor-encoder reading. The exporter
divides the common-zeroed cumulative input-side encoder position by the gear
ratio `81` and wraps the result to `[0, 360)`.

The output-side zeroing correction computes the first-three-sample
absolute/cumulative offset in radians, wraps it with
`atan2(sin(x), cos(x))`, applies the retained cluster correction, and adds the
result to the slow-shaft encoder angle.

Direction comes from the parent `forward/` or `backward/` folder. Filename
speed, torque, and temperature are nominal conditions; the CSV columns contain
sample-level measured or derived values.

## Safety and Provenance Boundary

The **historical generator**, not the packaged portable evaluator, was designed
to preserve existing output files unless `OVERWRITE_EXISTING_FILES = True`.
Its missing-input, invalid-path, empty-source and skipped-processing behavior
belongs to that generator workflow.

The portable script **reads the existing CSVs for offline inference** and can
write predicted curves, plots and summary CSVs to `--output-dir`. Use a fresh
output directory rather than overwriting tracked example results. Do not
reinterpret generated TE offsets as independently validated physical encoder
zeroing or approved machine compensation.

For the original source-side run commands and generator details, consult the
[research-main dataset-generator note](https://github.com/XiLab-Robotics/Physics-Informed-Neural-Networks/blob/main/doc/scripts/datasets/generate_polished_transmission_error_dataset.md).
This reference is external to `track2-portable` by design. No raw data
reprocessing or numerical parity test was performed during HYG-05.
