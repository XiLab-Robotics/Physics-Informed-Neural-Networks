# RCIM Paper Reference Benchmark

## Scope

This benchmark is the canonical repository-owned comparison surface for
RCIM paper-reference model replication. It has been reset around three
explicit surfaces:

- `paper original`: values reconstructed from the original paper tables;
- `paper retuned`: recovered-original RCIM models retuned through
  `run_rcim_original_reference_training.ps1`;
- `Track 1`: repository-owned exact-paper model-bank results, reset to
  empty pending cells until the next Track 1 pass repopulates them.

Forward Track 1 cells must compare against the better value between
`paper original` and `paper retuned`. Backward Track 1 cells must
compare against `paper retuned`, because the paper does not provide
backward original tables.

## Current Archive Status

- retuned family-direction archives promoted: `22`
- archive root: `models/paper_reference/rcim_retuned/`
- accepted export contract: `20` ONNX files, `20` PKL files, `0` export errors
- detailed closeout report:
  `doc/reports/analysis/rcim_retuned_reference_closeout/[2026-05-13]/rcim_retuned_reference_closeout_report.md`

## Forward Tables

### Forward Table 2 - Amplitude MAE

#### Paper Original

Paper-side repository-owned reconstruction:

<!-- markdownlint-disable MD013 -->
| Model | `0` | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | 0.002600 | 5.60e-05 | 1.60e-04 | 1.50e-04 | 7.90e-05 | 2.60e-04 | 9.10e-05 | 4.40e-04 | 6.90e-04 | 2.90e-04 |
| `MLP` | 0.009500 | 0.006500 | 0.006500 | 0.005600 | 0.006900 | 0.007100 | 0.007400 | 0.006800 | 0.008100 | 0.005500 |
| `RF` | 0.003000 | 2.40e-05 | 2.00e-05 | 2.90e-05 | 2.60e-05 | 3.80e-05 | 1.10e-05 | 5.70e-05 | 6.80e-05 | 2.90e-05 |
| `DT` | 0.003400 | 2.90e-05 | 2.20e-05 | 4.00e-05 | 3.20e-05 | 5.90e-05 | 1.30e-05 | 6.30e-05 | 6.20e-05 | 5.10e-05 |
| `ET` | 0.003500 | 3.10e-05 | 2.40e-05 | 3.80e-05 | 3.20e-05 | 5.90e-05 | 1.80e-05 | 5.70e-05 | 8.80e-05 | 7.20e-05 |
| `ERT` | 0.003100 | 2.70e-05 | 2.30e-05 | 2.90e-05 | 2.30e-05 | 3.80e-05 | 1.20e-05 | 1.70e-05 | 2.30e-05 | 2.40e-05 |
| `GBM` | 0.003100 | 2.70e-05 | 2.10e-05 | 2.80e-05 | 2.70e-05 | 3.90e-05 | 1.20e-05 | 6.10e-05 | 7.10e-05 | 3.00e-05 |
| `HGBM` | 0.002400 | 2.70e-05 | 1.50e-05 | 2.10e-05 | 2.60e-05 | 2.70e-05 | 1.20e-05 | 1.00e-04 | 1.70e-04 | 3.50e-05 |
| `XGBM` | 0.002500 | 5.50e-05 | 8.10e-05 | 1.10e-04 | 6.60e-05 | 1.10e-04 | 4.60e-05 | 2.30e-04 | 2.60e-04 | 1.40e-04 |
| `LGBM` | 0.002500 | 2.70e-05 | 1.80e-05 | 2.40e-05 | 2.70e-05 | 3.00e-05 | 1.20e-05 | 9.00e-05 | 1.60e-04 | 3.20e-05 |
<!-- markdownlint-enable MD013 -->

#### Paper Retuned

<!-- markdownlint-disable MD013 -->
| Model | `0` | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | 0.002912 | 4.66302e-05 | 6.04508e-05 | 7.55757e-05 | 7.10815e-05 | 0.000121731 | 5.12823e-05 | 0.000696237 | 0.000698217 | 0.00024679 |
| `MLP` | 0.014562 | 0.007778 | 0.0111 | 0.007793 | 0.009778 | 0.011258 | 0.011897 | 0.008305 | 0.00701 | 0.015629 |
| `RF` | 0.00351 | 3.10238e-05 | 2.31505e-05 | 3.6618e-05 | 2.97441e-05 | 5.5576e-05 | 1.52476e-05 | 8.91596e-05 | 6.69908e-05 | 4.50935e-05 |
| `DT` | 0.00351 | 3.10238e-05 | 2.31505e-05 | 3.6618e-05 | 2.97753e-05 | 5.5576e-05 | 1.52993e-05 | 8.91254e-05 | 6.69908e-05 | 4.50935e-05 |
| `ET` | 0.003923 | 3.39405e-05 | 2.73594e-05 | 3.96039e-05 | 2.81046e-05 | 6.39258e-05 | 1.5678e-05 | 6.23185e-05 | 6.8023e-05 | 4.45344e-05 |
| `ERT` | 0.003923 | 3.39405e-05 | 2.73594e-05 | 3.96039e-05 | 2.81046e-05 | 6.39258e-05 | 1.5678e-05 | 6.23185e-05 | 6.8023e-05 | 4.45344e-05 |
| `GBM` | 0.002618 | 2.63076e-05 | 1.86476e-05 | 2.34801e-05 | 2.56511e-05 | 2.36904e-05 | 1.22957e-05 | 0.000107198 | 0.000119594 | 3.49172e-05 |
| `HGBM` | 0.002618 | 2.63076e-05 | 1.86476e-05 | 2.34801e-05 | 2.56511e-05 | 2.36904e-05 | 1.22957e-05 | 0.000107198 | 0.000119594 | 3.49172e-05 |
| `XGBM` | 0.014562 | 0.007778 | 0.0111 | 0.007793 | 0.009778 | 0.011258 | 0.011897 | 0.008305 | 0.00701 | 0.015629 |
| `LGBM` | 0.002575 | 2.62664e-05 | 1.87327e-05 | 2.33772e-05 | 2.5798e-05 | 2.51835e-05 | 1.20466e-05 | 0.000107466 | 0.000118095 | 3.52105e-05 |
| `ELM` | 0.008394 | 2.88142e-05 | 7.87396e-05 | 0.000112282 | 4.01642e-05 | 0.000296962 | 2.83329e-05 | 0.000856622 | 0.001067 | 0.000369496 |
<!-- markdownlint-enable MD013 -->

#### Track 1

<!-- markdownlint-disable MD013 -->
| Model | `0` | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `SVM` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `MLP` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `RF` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `DT` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `ET` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `ERT` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `GBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `HGBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `XGBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `LGBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `ELM` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
<!-- markdownlint-enable MD013 -->

### Forward Table 3 - Amplitude RMSE

#### Paper Original

Paper-side repository-owned reconstruction:

<!-- markdownlint-disable MD013 -->
| Model | `0` | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | 0.003300 | 7.40e-05 | 1.80e-04 | 1.80e-04 | 9.50e-05 | 3.30e-04 | 1.00e-04 | 8.80e-04 | 0.002200 | 4.70e-04 |
| `MLP` | 0.0140 | 0.0120 | 0.0120 | 0.0100 | 0.0140 | 0.0130 | 0.0150 | 0.0130 | 0.0160 | 0.0100 |
| `RF` | 0.004100 | 3.50e-05 | 3.00e-05 | 3.80e-05 | 3.70e-05 | 5.60e-05 | 1.50e-05 | 1.70e-04 | 2.20e-04 | 5.40e-05 |
| `DT` | 0.004900 | 4.00e-05 | 3.30e-05 | 5.30e-05 | 4.50e-05 | 8.20e-05 | 1.80e-05 | 2.00e-04 | 1.70e-04 | 1.10e-04 |
| `ET` | 0.004500 | 4.20e-05 | 3.50e-05 | 5.10e-05 | 4.30e-05 | 8.50e-05 | 2.70e-05 | 1.90e-04 | 3.80e-04 | 1.80e-04 |
| `ERT` | 0.004000 | 3.70e-05 | 3.40e-05 | 4.00e-05 | 3.60e-05 | 5.70e-05 | 1.60e-05 | 1.30e-04 | 1.60e-04 | 4.20e-05 |
| `GBM` | 0.004000 | 3.60e-05 | 3.10e-05 | 3.90e-05 | 3.90e-05 | 5.50e-05 | 1.60e-05 | 1.70e-04 | 2.20e-04 | 4.70e-05 |
| `HGBM` | 0.003400 | 3.60e-05 | 2.50e-05 | 3.20e-05 | 3.80e-05 | 4.50e-05 | 1.60e-05 | 2.50e-04 | 5.00e-04 | 7.40e-05 |
| `XGBM` | 0.003500 | 7.10e-05 | 1.00e-04 | 1.30e-04 | 8.70e-05 | 1.50e-04 | 6.00e-05 | 5.40e-04 | 7.50e-04 | 2.10e-04 |
| `LGBM` | 0.003500 | 3.70e-05 | 2.60e-05 | 3.30e-05 | 3.80e-05 | 4.60e-05 | 1.60e-05 | 2.20e-04 | 4.70e-04 | 6.20e-05 |
<!-- markdownlint-enable MD013 -->

#### Paper Retuned

<!-- markdownlint-disable MD013 -->
| Model | `0` | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | 0.004123 | 6.08873e-05 | 7.62318e-05 | 9.55895e-05 | 8.97431e-05 | 0.000165775 | 6.03122e-05 | 0.001528 | 0.002377 | 0.000612235 |
| `MLP` | 0.023068 | 0.013469 | 0.02176 | 0.015826 | 0.018224 | 0.021632 | 0.020561 | 0.015097 | 0.014136 | 0.025682 |
| `RF` | 0.004879 | 4.30608e-05 | 3.33725e-05 | 5.05612e-05 | 4.50903e-05 | 7.97431e-05 | 2.37782e-05 | 0.000298279 | 0.000196766 | 7.18479e-05 |
| `DT` | 0.004879 | 4.30523e-05 | 3.33725e-05 | 5.05612e-05 | 4.50974e-05 | 7.97431e-05 | 2.38369e-05 | 0.000298278 | 0.000196766 | 7.18479e-05 |
| `ET` | 0.005512 | 4.98162e-05 | 4.46899e-05 | 5.37782e-05 | 4.20959e-05 | 8.92871e-05 | 2.55713e-05 | 0.000190094 | 0.000186599 | 6.97557e-05 |
| `ERT` | 0.005512 | 4.98162e-05 | 4.46899e-05 | 5.37782e-05 | 4.20959e-05 | 8.92871e-05 | 2.55713e-05 | 0.000190094 | 0.000186599 | 6.97557e-05 |
| `GBM` | 0.003898 | 3.66942e-05 | 2.64492e-05 | 3.2727e-05 | 3.5704e-05 | 3.51107e-05 | 1.92161e-05 | 0.000264253 | 0.000275736 | 7.01425e-05 |
| `HGBM` | 0.003898 | 3.66942e-05 | 2.64492e-05 | 3.2727e-05 | 3.5704e-05 | 3.51107e-05 | 1.92161e-05 | 0.000264253 | 0.000275736 | 7.01425e-05 |
| `XGBM` | 0.023068 | 0.013469 | 0.02176 | 0.015826 | 0.018224 | 0.021632 | 0.020561 | 0.015097 | 0.014136 | 0.025682 |
| `LGBM` | 0.00379 | 3.66354e-05 | 2.67199e-05 | 3.21329e-05 | 3.57956e-05 | 3.707e-05 | 1.89939e-05 | 0.000267423 | 0.000266197 | 7.02233e-05 |
| `ELM` | 0.010659 | 3.82909e-05 | 9.6453e-05 | 0.000153107 | 6.26075e-05 | 0.0003916 | 3.88056e-05 | 0.00157 | 0.002357 | 0.000636913 |
<!-- markdownlint-enable MD013 -->

#### Track 1

<!-- markdownlint-disable MD013 -->
| Model | `0` | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `SVM` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `MLP` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `RF` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `DT` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `ET` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `ERT` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `GBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `HGBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `XGBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `LGBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `ELM` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
<!-- markdownlint-enable MD013 -->

### Forward Table 4 - Phase MAE

#### Paper Original

Paper-side repository-owned reconstruction:

<!-- markdownlint-disable MD013 -->
| Model | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | 0.002200 | 0.0330 | 0.0270 | 0.0610 | 0.1900 | 0.1300 | 1.200 | 0.4900 | 0.4900 |
| `MLP` | 0.007200 | 0.0650 | 0.0620 | 0.0800 | 0.1600 | 0.1500 | 1.900 | 0.7800 | 0.7000 |
| `RF` | 0.002000 | 0.0240 | 0.0280 | 0.0370 | 0.0740 | 0.0530 | 0.5100 | 0.2300 | 0.2500 |
| `DT` | 0.002100 | 0.0300 | 0.0360 | 0.0430 | 0.0900 | 0.0660 | 0.5200 | 0.2000 | 0.2300 |
| `ET` | 0.002400 | 0.0310 | 0.0350 | 0.0510 | 0.0940 | 0.0870 | 0.7100 | 0.2800 | 0.2600 |
| `ERT` | 0.002200 | 0.0270 | 0.0280 | 0.0400 | 0.0760 | 0.0560 | 0.5300 | 0.2000 | 0.2300 |
| `GBM` | 0.002000 | 0.0240 | 0.0300 | 0.0360 | 0.0740 | 0.0530 | 0.5400 | 0.2500 | 0.2900 |
| `HGBM` | 0.001900 | 0.0200 | 0.0210 | 0.0400 | 0.0910 | 0.0570 | 0.7400 | 0.3500 | 0.3600 |
| `XGBM` | 0.001900 | 0.0240 | 0.0320 | 0.0610 | 0.1400 | 0.0910 | 0.9600 | 0.5400 | 0.3900 |
| `LGBM` | 0.001800 | 0.0210 | 0.0210 | 0.0400 | 0.0950 | 0.0550 | 0.7400 | 0.3500 | 0.3400 |
<!-- markdownlint-enable MD013 -->

#### Paper Retuned

<!-- markdownlint-disable MD013 -->
| Model | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | 0.002861 | 0.039126 | 0.038193 | 0.095298 | 0.19446 | 0.167816 | 1.545304 | 0.854949 | 0.747385 |
| `MLP` | 0.020549 | 0.068079 | 0.081528 | 0.07124 | 0.145159 | 0.141555 | 1.653017 | 0.90848 | 0.781412 |
| `RF` | 0.002236 | 0.02734 | 0.032261 | 0.045518 | 0.075769 | 0.06362 | 0.490024 | 0.24597 | 0.287325 |
| `DT` | 0.002239 | 0.02734 | 0.032261 | 0.045456 | 0.07449 | 0.06362 | 0.490408 | 0.245312 | 0.287325 |
| `ET` | 0.002979 | 0.032667 | 0.032921 | 0.046145 | 0.105701 | 0.077808 | 0.474651 | 0.284212 | 0.297142 |
| `ERT` | 0.002979 | 0.032667 | 0.032921 | 0.046145 | 0.105701 | 0.077808 | 0.474651 | 0.284212 | 0.297142 |
| `GBM` | 0.001955 | 0.025438 | 0.020247 | 0.037234 | 0.071251 | 0.048207 | 0.605127 | 0.337684 | 0.391634 |
| `HGBM` | 0.001955 | 0.025438 | 0.020247 | 0.037234 | 0.071251 | 0.048207 | 0.605127 | 0.337684 | 0.391634 |
| `XGBM` | 0.020549 | 0.068079 | 0.081528 | 0.07124 | 0.145159 | 0.141555 | 1.653017 | 0.90848 | 0.781412 |
| `LGBM` | 0.001928 | 0.025764 | 0.020305 | 0.03646 | 0.073436 | 0.045802 | 0.603746 | 0.346318 | 0.383523 |
| `ELM` | 0.002771 | 0.080557 | 0.089368 | 0.067536 | 0.19027 | 0.174713 | 1.703741 | 1.116297 | 0.80237 |
<!-- markdownlint-enable MD013 -->

#### Track 1

<!-- markdownlint-disable MD013 -->
| Model | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `SVM` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `MLP` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `RF` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `DT` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `ET` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `ERT` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `GBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `HGBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `XGBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `LGBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `ELM` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
<!-- markdownlint-enable MD013 -->

### Forward Table 5 - Phase RMSE

#### Paper Original

Paper-side repository-owned reconstruction:

<!-- markdownlint-disable MD013 -->
| Model | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | 0.003100 | 0.0420 | 0.0440 | 0.0970 | 0.3200 | 0.2000 | 1.800 | 1.100 | 1.100 |
| `MLP` | 0.0130 | 0.0840 | 0.0770 | 0.1100 | 0.2400 | 0.2200 | 2.200 | 1.200 | 1.100 |
| `RF` | 0.002800 | 0.0330 | 0.0430 | 0.0550 | 0.1600 | 0.0820 | 1.200 | 0.6800 | 0.6300 |
| `DT` | 0.002800 | 0.0420 | 0.0610 | 0.0610 | 0.2000 | 0.1000 | 1.300 | 0.7300 | 0.6700 |
| `ET` | 0.003300 | 0.0460 | 0.0620 | 0.0740 | 0.2300 | 0.1500 | 1.500 | 0.9300 | 0.6800 |
| `ERT` | 0.003600 | 0.0400 | 0.0440 | 0.0600 | 0.1800 | 0.1100 | 1.200 | 0.6400 | 0.5800 |
| `GBM` | 0.002600 | 0.0340 | 0.0450 | 0.0550 | 0.1800 | 0.0840 | 1.300 | 0.7100 | 0.7100 |
| `HGBM` | 0.002500 | 0.0290 | 0.0270 | 0.0600 | 0.1900 | 0.0850 | 1.300 | 0.7000 | 0.7400 |
| `XGBM` | 0.002800 | 0.0330 | 0.0430 | 0.0890 | 0.2300 | 0.1300 | 1.400 | 0.8100 | 0.7600 |
| `LGBM` | 0.002500 | 0.0300 | 0.0280 | 0.0600 | 0.1900 | 0.0820 | 1.300 | 0.7000 | 0.7100 |
<!-- markdownlint-enable MD013 -->

#### Paper Retuned

<!-- markdownlint-disable MD013 -->
| Model | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | 0.00436 | 0.054297 | 0.060574 | 0.132484 | 0.362591 | 0.241217 | 2.02453 | 1.654005 | 1.412756 |
| `MLP` | 0.032351 | 0.086326 | 0.104059 | 0.103366 | 0.212569 | 0.179317 | 1.994397 | 1.406654 | 1.202815 |
| `RF` | 0.003114 | 0.039113 | 0.060054 | 0.070686 | 0.172907 | 0.095694 | 1.225761 | 0.891621 | 0.872011 |
| `DT` | 0.003115 | 0.039113 | 0.060054 | 0.070673 | 0.151314 | 0.095694 | 1.225799 | 0.891606 | 0.872011 |
| `ET` | 0.004395 | 0.049717 | 0.05807 | 0.071786 | 0.294988 | 0.130349 | 1.092873 | 0.927118 | 0.805299 |
| `ERT` | 0.004395 | 0.049717 | 0.05807 | 0.071786 | 0.294988 | 0.130349 | 1.092873 | 0.927118 | 0.805299 |
| `GBM` | 0.002681 | 0.036307 | 0.032742 | 0.057628 | 0.139074 | 0.070305 | 1.03431 | 0.784113 | 0.888707 |
| `HGBM` | 0.002681 | 0.036307 | 0.032742 | 0.057628 | 0.139074 | 0.070305 | 1.03431 | 0.784113 | 0.888707 |
| `XGBM` | 0.032351 | 0.086326 | 0.104059 | 0.103366 | 0.212569 | 0.179317 | 1.994397 | 1.406654 | 1.202815 |
| `LGBM` | 0.002673 | 0.03642 | 0.032488 | 0.056709 | 0.145076 | 0.067668 | 1.049463 | 0.794237 | 0.883119 |
| `ELM` | 0.004207 | 0.099629 | 0.112824 | 0.098927 | 0.285837 | 0.233381 | 2.031703 | 1.636152 | 1.276826 |
<!-- markdownlint-enable MD013 -->

#### Track 1

<!-- markdownlint-disable MD013 -->
| Model | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `SVM` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `MLP` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `RF` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `DT` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `ET` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `ERT` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `GBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `HGBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `XGBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `LGBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `ELM` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
<!-- markdownlint-enable MD013 -->

## Backward Tables

### Backward Table 2 - Amplitude MAE

#### Paper Original

No backward paper-original table is available in the paper.

#### Paper Retuned

<!-- markdownlint-disable MD013 -->
| Model | `0` | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | 0.003417 | 7.05621e-05 | 6.44134e-05 | 0.000108184 | 3.99598e-05 | 0.000140876 | 3.55141e-05 | 0.000759711 | 0.000512494 | 0.000342361 |
| `MLP` | 0.016062 | 0.008565 | 0.02068 | 0.009938 | 0.009976 | 0.007135 | 0.010629 | 0.008277 | 0.011534 | 0.007464 |
| `RF` | 0.002937 | 2.37386e-05 | 2.07275e-05 | 1.72732e-05 | 2.76117e-05 | 5.1867e-05 | 1.00356e-05 | 0.000117828 | 9.1534e-05 | 6.23487e-05 |
| `DT` | 0.003504 | 2.69959e-05 | 3.42058e-05 | 2.59035e-05 | 3.23554e-05 | 0.000105717 | 1.36692e-05 | 0.000191057 | 0.000165638 | 0.000125839 |
| `ET` | 0.003322 | 2.65069e-05 | 2.63791e-05 | 2.03945e-05 | 3.03482e-05 | 7.00267e-05 | 9.3832e-06 | 0.000111551 | 9.2988e-05 | 0.000129119 |
| `ERT` | 0.003322 | 2.65069e-05 | 2.63791e-05 | 2.03945e-05 | 3.03482e-05 | 7.00267e-05 | 9.3832e-06 | 0.000111551 | 9.2988e-05 | 0.000129119 |
| `GBM` | 0.003336 | 3.32158e-05 | 2.92694e-05 | 2.23226e-05 | 2.9316e-05 | 8.58519e-05 | 1.20384e-05 | 0.000355944 | 0.000276624 | 0.000115003 |
| `HGBM` | 0.003336 | 3.32158e-05 | 2.92694e-05 | 2.23226e-05 | 2.9316e-05 | 8.58519e-05 | 1.20384e-05 | 0.000355944 | 0.000276624 | 0.000115003 |
| `XGBM` | 0.016062 | 0.008565 | 0.02068 | 0.009938 | 0.009976 | 0.007135 | 0.010629 | 0.008277 | 0.011534 | 0.007464 |
| `LGBM` | 0.006586 | 3.53015e-05 | 4.62261e-05 | 4.03759e-05 | 3.28733e-05 | 0.000230488 | 1.56541e-05 | 0.000577349 | 0.000432744 | 0.000209221 |
| `ELM` | 0.006105 | 4.0656e-05 | 6.19064e-05 | 6.94347e-05 | 3.74189e-05 | 0.000314255 | 2.18478e-05 | 0.001246 | 0.000861271 | 0.000374497 |
<!-- markdownlint-enable MD013 -->

#### Track 1

<!-- markdownlint-disable MD013 -->
| Model | `0` | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `SVM` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `MLP` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `RF` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `DT` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `ET` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `ERT` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `GBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `HGBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `XGBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `LGBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `ELM` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
<!-- markdownlint-enable MD013 -->

### Backward Table 3 - Amplitude RMSE

#### Paper Original

No backward paper-original table is available in the paper.

#### Paper Retuned

<!-- markdownlint-disable MD013 -->
| Model | `0` | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | 0.004321 | 8.92984e-05 | 7.59251e-05 | 0.000122372 | 5.24986e-05 | 0.00018634 | 4.13104e-05 | 0.002147 | 0.001733 | 0.000768566 |
| `MLP` | 0.023489 | 0.014012 | 0.034222 | 0.016157 | 0.019279 | 0.01215 | 0.018511 | 0.011909 | 0.020039 | 0.01354 |
| `RF` | 0.003822 | 4.01928e-05 | 3.95792e-05 | 2.41367e-05 | 4.08393e-05 | 7.35254e-05 | 1.45444e-05 | 0.000351421 | 0.000350566 | 0.000143677 |
| `DT` | 0.004755 | 3.89166e-05 | 4.63022e-05 | 3.5792e-05 | 4.65966e-05 | 0.000141259 | 2.1564e-05 | 0.000458745 | 0.000633652 | 0.000247847 |
| `ET` | 0.004572 | 3.78036e-05 | 4.05121e-05 | 3.04868e-05 | 4.2643e-05 | 9.56236e-05 | 1.38535e-05 | 0.000333265 | 0.000508611 | 0.000340328 |
| `ERT` | 0.004572 | 3.78036e-05 | 4.05121e-05 | 3.04868e-05 | 4.2643e-05 | 9.56236e-05 | 1.38535e-05 | 0.000333265 | 0.000508611 | 0.000340328 |
| `GBM` | 0.004305 | 5.05026e-05 | 4.01874e-05 | 3.17414e-05 | 4.19043e-05 | 0.000115062 | 1.73374e-05 | 0.00091268 | 0.000819282 | 0.000242704 |
| `HGBM` | 0.004305 | 5.05026e-05 | 4.01874e-05 | 3.17414e-05 | 4.19043e-05 | 0.000115062 | 1.73374e-05 | 0.00091268 | 0.000819282 | 0.000242704 |
| `XGBM` | 0.023489 | 0.014012 | 0.034222 | 0.016157 | 0.019279 | 0.01215 | 0.018511 | 0.011909 | 0.020039 | 0.01354 |
| `LGBM` | 0.008224 | 5.37816e-05 | 5.75288e-05 | 5.02789e-05 | 4.44481e-05 | 0.000274288 | 2.08906e-05 | 0.00103 | 0.000972133 | 0.000415477 |
| `ELM` | 0.007959 | 6.49451e-05 | 8.87046e-05 | 8.60459e-05 | 4.79292e-05 | 0.000405392 | 2.81136e-05 | 0.002354 | 0.001667 | 0.000692278 |
<!-- markdownlint-enable MD013 -->

#### Track 1

<!-- markdownlint-disable MD013 -->
| Model | `0` | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `SVM` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `MLP` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `RF` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `DT` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `ET` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `ERT` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `GBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `HGBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `XGBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `LGBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `ELM` | pending | pending | pending | pending | pending | pending | pending | pending | pending | pending |
<!-- markdownlint-enable MD013 -->

### Backward Table 4 - Phase MAE

#### Paper Original

No backward paper-original table is available in the paper.

#### Paper Retuned

<!-- markdownlint-disable MD013 -->
| Model | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | 0.003277 | 0.030147 | 1.533948 | 0.239405 | 0.16531 | 0.165708 | 0.519181 | 0.647235 | 0.934282 |
| `MLP` | 0.012577 | 0.047895 | 0.883528 | 0.223007 | 0.117947 | 0.164507 | 0.550536 | 0.633432 | 0.74779 |
| `RF` | 0.004475 | 0.020274 | 0.259613 | 0.088339 | 0.055395 | 0.100364 | 0.103195 | 0.104946 | 0.201875 |
| `DT` | 0.002297 | 0.030949 | 0.264166 | 0.109481 | 0.104082 | 0.131394 | 0.154214 | 0.138677 | 0.272296 |
| `ET` | 0.002216 | 0.024758 | 0.251627 | 0.12914 | 0.061557 | 0.117384 | 0.137711 | 0.158073 | 0.335381 |
| `ERT` | 0.002216 | 0.024758 | 0.251627 | 0.12914 | 0.061557 | 0.117384 | 0.137711 | 0.158073 | 0.335381 |
| `GBM` | 0.004355 | 0.031669 | 0.48239 | 0.11461 | 0.089437 | 0.116216 | 0.251079 | 0.198438 | 0.422011 |
| `HGBM` | 0.004355 | 0.031669 | 0.48239 | 0.11461 | 0.089437 | 0.116216 | 0.251079 | 0.198438 | 0.422011 |
| `XGBM` | 0.012577 | 0.047895 | 0.883528 | 0.223007 | 0.117947 | 0.164507 | 0.550536 | 0.633432 | 0.74779 |
| `LGBM` | 0.003988 | 0.075939 | 1.007733 | 0.159638 | 0.119033 | 0.16781 | 0.347521 | 0.403988 | 0.606608 |
| `ELM` | 0.005351 | 0.095946 | 1.401709 | 0.21804 | 0.14142 | 0.191291 | 0.566196 | 0.85855 | 0.826733 |
<!-- markdownlint-enable MD013 -->

#### Track 1

<!-- markdownlint-disable MD013 -->
| Model | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `SVM` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `MLP` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `RF` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `DT` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `ET` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `ERT` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `GBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `HGBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `XGBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `LGBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `ELM` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
<!-- markdownlint-enable MD013 -->

### Backward Table 5 - Phase RMSE

#### Paper Original

No backward paper-original table is available in the paper.

#### Paper Retuned

<!-- markdownlint-disable MD013 -->
| Model | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `SVM` | 0.004976 | 0.050379 | 1.904003 | 0.390645 | 0.302424 | 0.208329 | 0.96709 | 1.234879 | 1.739106 |
| `MLP` | 0.019934 | 0.061518 | 1.488289 | 0.387442 | 0.157908 | 0.216736 | 0.922763 | 1.028735 | 1.240815 |
| `RF` | 0.017312 | 0.031548 | 0.925908 | 0.133734 | 0.089557 | 0.134517 | 0.321643 | 0.324612 | 0.495247 |
| `DT` | 0.00395 | 0.046179 | 1.158681 | 0.159423 | 0.153046 | 0.187845 | 0.411266 | 0.488621 | 0.666233 |
| `ET` | 0.00377 | 0.037153 | 1.108501 | 0.245136 | 0.110455 | 0.16568 | 0.50731 | 0.556874 | 0.991502 |
| `ERT` | 0.00377 | 0.037153 | 1.108501 | 0.245136 | 0.110455 | 0.16568 | 0.50731 | 0.556874 | 0.991502 |
| `GBM` | 0.008257 | 0.042245 | 1.003621 | 0.175671 | 0.164139 | 0.159327 | 0.552074 | 0.448768 | 0.785715 |
| `HGBM` | 0.008257 | 0.042245 | 1.003621 | 0.175671 | 0.164139 | 0.159327 | 0.552074 | 0.448768 | 0.785715 |
| `XGBM` | 0.019934 | 0.061518 | 1.488289 | 0.387442 | 0.157908 | 0.216736 | 0.922763 | 1.028735 | 1.240815 |
| `LGBM` | 0.006405 | 0.089842 | 1.316174 | 0.239411 | 0.186768 | 0.208583 | 0.68118 | 0.644011 | 0.990548 |
| `ELM` | 0.011728 | 0.12662 | 1.852693 | 0.376851 | 0.186686 | 0.249883 | 0.946219 | 1.157153 | 1.350511 |
<!-- markdownlint-enable MD013 -->

#### Track 1

<!-- markdownlint-disable MD013 -->
| Model | `1` | `3` | `39` | `40` | `78` | `81` | `156` | `162` | `240` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `SVM` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `MLP` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `RF` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `DT` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `ET` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `ERT` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `GBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `HGBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `XGBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `LGBM` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| `ELM` | pending | pending | pending | pending | pending | pending | pending | pending | pending |
<!-- markdownlint-enable MD013 -->

## Reading Rules

- `paper original` is immutable paper-side evidence and exists only for forward.
- `paper retuned` is the current recovered-original retuned baseline.
- `Track 1` cells are intentionally empty after this reset.
- Future Track 1 closeouts must fill cells only after accepted
  family-target results are available in the repository.
- Future Track 1 forward status colors compare against the best of
  `paper original` and `paper retuned`.
- Future Track 1 backward status colors compare against `paper retuned`.
