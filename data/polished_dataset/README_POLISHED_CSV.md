# Polished Transmission Error CSV Export

The polished CSV export converts raw measurement files.

## Folder Structure

The input folder is definded by `INPUT_PATH`.
The output root is configured by `OUTPUT_PATH` in the exporter.
Both need to ne changed by the user.

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
from the source filename. If multiple source files have the same conditions, the
Python emits a `RuntimeWarning` and MATLAB emits a corresponding warning. Both
keep the first sorted source file and skip later duplicates to avoid overwriting
the same output path.

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
theta      input-side angle, wrapped to [0, 360) deg, scaled by transmission ratio
theta_dot  motor-side speed calculated from theta in rpm
tau_load   load torque in Nm
T          temperature in degC
theta_TE   transmission error in deg
```

`theta_TE` is calculated as follows:

```text
theta_TE = q_not_zeroed - theta
```

The output-side zeroing correction:
Compute the first-three-sample absolute/cumulative offset in radians, wrap with
`atan2(sin(x), cos(x))`, apply the cluster correction, then add the correction
to slow shaft encoder angle.
