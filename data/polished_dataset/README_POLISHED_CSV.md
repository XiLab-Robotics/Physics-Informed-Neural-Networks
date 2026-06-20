# Polished Transmission Error CSV Export

The polished CSV export converts raw measurement files from
`data/original_dataset/` into direction-separated, time-ordered CSV files.

The canonical dataset lineage, signal definitions, equations, audit results,
and usage constraints are documented in the
[Transmission Error Dataset Family Reference](../../doc/reference_summaries/08_Transmission_Error_Dataset_Family_Reference.md).

## Folder Structure

The standalone generator is stored one level above this dataset:

```text
data/generate_polished_dataset.py
```

Its defaults are:

```text
input  = data/original_dataset
output = data/polished_dataset
```

The complete repository-integrated copy is:

```text
scripts/datasets/generate_polished_transmission_error_dataset.py
```

Its output defaults to `output/generated_polished_dataset/`. Both scripts show
verbose startup information and a `tqdm` progress bar while processing source
conditions.

The script exports all selected source files into direction and
operating-condition folders:

```text
csv/
  forward/
    25degree/
      1000rpm/
        1000.0rpm100.0Nm25.0deg.csv
  backward/
    25degree/
      1000rpm/
        1000.0rpm100.0Nm25.0deg.csv
```

## Duplicate Conditions

Source files are grouped by the nominal speed, torque, and temperature parsed
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

## Safety

Existing destination files are not replaced unless
`OVERWRITE_EXISTING_FILES = True`. Missing inputs, invalid paths, empty source
inventories, and processing skips cause the run to fail visibly.

See
`doc/scripts/datasets/generate_polished_transmission_error_dataset.md` for the
standalone and repository commands and the exact verified differences.
