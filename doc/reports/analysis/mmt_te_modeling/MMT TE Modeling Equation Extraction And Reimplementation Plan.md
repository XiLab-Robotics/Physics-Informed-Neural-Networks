# MMT TE Modeling Equation Extraction And Reimplementation Plan

## Source Boundary

Primary source: `reference/MMT_TEModeling.pdf`.

Existing repository summary:
`doc/reference_summaries/02_MMT_TEModeling_Project_Summary.md`.

The paper is `A modelling approach for kinematic equivalent mechanism and
rotational transmission error of RV reducer`, by Yuhu Yang, Guocheng Zhou,
Le Chang, and Gang Chen, published in `Mechanism and Machine Theory 163
(2021) 104384`.

This document records what the paper says, extracts the numbered equations,
and explains how the analytical model can be evaluated against this
repository's measured transmission-error curves.

## What The Paper Does

The paper builds an analytical model for rotational transmission error (`RTE`)
of an `RV` reducer. Its main contribution is not a learned predictor. It is a
mechanism-equivalent analytical model that turns original manufacturing and
assembly errors into explicit `RTE` contributions.

The reducer is difficult to model directly because the cycloidal gear rotation
and revolution share three crankshafts. This creates an over-constrained
multi-crank actuation structure. The paper avoids a purely numerical
compatibility-equation model by replacing higher pairs with lower pairs and
building an instantaneous equivalent multi-loop mechanism.

The resulting model:

- represents the three crankshafts as equivalent parallelogram loops;
- replaces involute and cycloid-pin tooth contacts with virtual linkages;
- derives loop equations and velocity ratios;
- applies a loop incremental method to propagate linkage-length and angle
  errors into the whole-machine output error;
- separates the final `RTE` into contributions from high-speed involute
  gearing, low-speed cycloid-pin gearing, and crankshaft feedback paths.

## Inputs

The analytical model needs mechanical geometry, instantaneous kinematic state,
contact geometry, and original-error equivalents.

| Input Group | Variables | Meaning |
| --- | --- | --- |
| Tooth counts | `z_1`, `z_2`, `z_4`, `z_5` | Sun, planetary, cycloidal, and pin gear counts. |
| Main geometry | `l_Hi`, `l_ai`, `l_R`, `l_b1`, `l_b2`, `l_n`, `l_v`, `l_k`, `l_rho` | Equivalent mechanism link lengths. |
| Angles | `theta_1`, `theta_2`, `theta_3`, `theta_4`, `theta_5`, `theta_H` | Sun, planetary, crankshaft, cycloidal gear, pin gear, and carrier/output angles. |
| Virtual linkage angles | `theta_ai`, `theta_Hi`, `theta_b1`, `theta_n`, `theta_b2`, `theta_rho`, `theta_k`, `theta_v`, `theta_ci`, `theta_p` | Equivalent-link orientations in the multi-loop mechanism. |
| Coordinates | `(x_c, y_c)`, `(x_k, y_k)`, `(x_O4, y_O4)` | Curvature center, pin center, and cycloidal-gear center. |
| Original errors | `Delta l_x`, `Delta theta_x`, `E_H`, `E_c`, `E_a`, `E_v`, `Delta l_R`, `AP`, `E_b1`, `E_b2`, `delta`, `Delta r`, `A_o` | Manufacturing and assembly errors mapped into equivalent link-length or angle errors. |

## Outputs

The main output is:

- `Delta theta_H`: rotational transmission error of the whole reducer.

Intermediate outputs are:

- `f_1`: `RTE` from the involute gear subsystem;
- `f_2i`: crankshaft error contribution when the crankshafts act in the input
  path;
- `f_3`: `RTE` from the cycloid-pin subsystem;
- `f_4i`: crankshaft error contribution when the crankshafts act in the output
  path;
- `g_1`, `g_2`, `g_3`, `g_4`: error transfer coefficients between subsystem
  loops.

## Paper Results

The paper validates the model on two `RV-80E` prototypes.

| Prototype | Simulation RTE Range | Test RTE Range |
| --- | --- | --- |
| Prototype `#1` | `-28.83''` to `27.32''` | `-29.68''` to `30.39''` |
| Prototype `#2` | `-32.16''` to `32.87''` | `-31.51''` to `33.13''` |

The frequency-domain comparison shows strong components at `40`, `80`, `120`,
`160`, and higher multiples. The paper interprets these as multiples of the
cycloidal gear and pin meshing frequency. The component at normalized
frequency `1` is attributed to position deviation of holes on the output disc.

The individual-error analysis reports that low-speed-stage errors dominate the
whole-machine `RTE`. These include cycloidal profile error, accumulated pin
pitch error, cycloidal gear hole-position error, crankshaft eccentricity error,
output disc hole-position error, pin-gear pitch-circle radius error, and pin
radius error. The high-speed involute-stage pitch-circle eccentricity has a
smaller influence in the reported prototype case. The paper also reports that
the feedback error in the illustrated cycloidal profile-error case is about
`3%`.

## Equation Extraction

This section transcribes the numbered equations from the paper into
implementation-oriented notation. The paper uses `theta_{x,y}=theta_x-theta_y`.

### Speed Ratio Definitions

Equation `(1)`:

```math
i^H_{12} = \frac{\theta_1-\theta_H}{\theta_2-\theta_H}
         = -\frac{z_2}{z_1},
\qquad
i^3_{45} = \frac{\theta_4-\theta_3}{\theta_5-\theta_3}
         = \frac{z_5}{z_4}
```

Equation `(2)`:

```math
\theta_H =
\frac{z_1(z_5-z_4)}{z_2z_5+z_1(z_5-z_4)}\theta_1,
\qquad
\theta_3 = -\frac{z_4}{z_5-z_4}\theta_H
```

### Virtual Linkage Angles

Equation `(3)`:

```math
\theta_{ai}=2\pi-\theta_3,
\qquad
\theta_{Hi}=\theta_H+\frac{\pi}{2}+\frac{2\pi}{3}(i-1),
\qquad
i=1,2,3
```

Equation `(4)`:

```math
\theta_{b1}=\theta_{H1}-\alpha',
\qquad
\theta_n=\theta_{H1}-\alpha'+\frac{\pi}{2},
\qquad
\theta_{b2}=\theta_{H1}-\alpha'+\pi
```

Equation `(5)`:

```math
\theta_\rho=\arctan\frac{y_k-y_c}{x_k-x_c},
\qquad
\theta_k=\arctan\frac{y_c-y_{O4}}{x_c-x_{O4}}
```

Implementation note: the scripts use `atan2(y, x)` rather than a single-ratio
`atan(...)`, because `atan2` preserves quadrant information.

Equation `(6)`:

```math
x_k=l_R\cos\theta_p,\qquad y_k=l_R\sin\theta_p
```

```math
x_{O4}=l_a\cos\theta_a,\qquad y_{O4}=l_a\sin\theta_a
```

Equation `(7)`:

```math
\theta_p=(k-1)\frac{2\pi}{z_5},
\qquad k=1,2,3,\dots,z_5
```

### Closed-Loop Vector Equations

Equation `(8)`:

```math
l_{b1}e^{j\theta_{b1}}+l_ne^{j\theta_n}
=l_{H1}e^{j\theta_{H1}}+l_{b2}e^{j\theta_{b2}}
```

Equation `(9)`:

```math
l_ve^{j\theta_v}+l_ke^{j\theta_k}+l_\rho e^{j\theta_\rho}
=l_Re^{j\theta_p}
```

Equation `(10)`:

```math
l_{Hi}e^{j\theta_{Hi}}+l_{ai}e^{j\theta_{ai}}
=l_ve^{j\theta_v}+l_{ci}e^{j\theta_{ci}}
```

### Velocity Equations

Equation `(11)`:

```math
j\dot{\theta}_{b1}l_{b1}e^{j\theta_{b1}}
+j\dot{\theta}_nl_ne^{j\theta_n}
=j\dot{\theta}_{H1}l_{H1}e^{j\theta_{H1}}
+j\dot{\theta}_{b2}l_{b2}e^{j\theta_{b2}}
```

Equation `(12)`:

```math
j\dot{\theta}_vl_ve^{j\theta_v}
+j\dot{\theta}_kl_ke^{j\theta_k}
+j\dot{\theta}_\rho l_\rho e^{j\theta_\rho}
=j\dot{\theta}_pl_Re^{j\theta_p}
```

Equation `(13)`:

```math
j\dot{\theta}_{Hi}l_{Hi}e^{j\theta_{Hi}}
+j\dot{\theta}_{ai}l_{ai}e^{j\theta_{ai}}
=j\dot{\theta}_vl_ve^{j\theta_v}
+j\dot{\theta}_{ci}l_{ci}e^{j\theta_{ci}}
```

Equation `(14)`:

```math
l_{b1}\dot{\theta}_{b1}\sin\theta_{b1,n}
=l_{H1}\dot{\theta}_{H1}\sin\theta_{H1,n}
+l_{b2}\dot{\theta}_{b2}\sin\theta_{b2,n}
```

Equation `(15)`:

```math
l_v\dot{\theta}_v\sin\theta_{v,\rho}
+l_k\dot{\theta}_k\sin\theta_{k,\rho}
=l_R\dot{\theta}_p\sin\theta_{p,\rho}
```

Equation `(16)`:

```math
l_{Hi}\dot{\theta}_{Hi}\sin\theta_{Hi,ai}
=l_v\dot{\theta}_v\sin\theta_{v,ai}
+l_{ci}\dot{\theta}_{ci}\sin\theta_{ci,ai}
```

Equation `(17)`:

```math
l_{Hi}\dot{\theta}_{Hi}\sin\theta_{Hi,ci}
+l_{ai}\dot{\theta}_{ai}\sin\theta_{ai,ci}
=l_v\dot{\theta}_v\sin\theta_{v,ci}
```

Equation `(18)`:

```math
\dot{\theta}_{b1}=\dot{\theta}_{b2},
\qquad
\dot{\theta}_{Hi}=\dot{\theta}_{ci},
\qquad
\dot{\theta}_{ai}=\dot{\theta}_v
```

### Error Transfer Ratios

Equation `(19)`:

```math
g_1=\frac{\dot{\theta}_{b2}}{\dot{\theta}_{H1}}
=\frac{l_{H1}\sin\theta_{H1,n}}{l_{b2}\sin\theta_{b2,n}}
=-\frac{z_1+z_2}{z_2}
```

Equation `(20)`:

```math
g_2=\frac{\dot{\theta}_v}{\dot{\theta}_{ai}}
=\frac{l_{ai}\sin\theta_{ai,ci}}{l_v\sin\theta_{v,ci}}
=1
```

Equation `(21)`:

```math
g_3=\frac{\dot{\theta}_k}{\dot{\theta}_v}
=-\frac{l_v\sin\theta_{v,\rho}}{l_k\sin\theta_{k,\rho}}
=-\frac{z_5-z_4}{z_4}
```

Equation `(22)`:

```math
g_4=\frac{\dot{\theta}_{Hi}}{\dot{\theta}_{ci}}
=\frac{l_{ci}\sin\theta_{ci,ai}}{l_{Hi}\sin\theta_{Hi,ai}}
=1
```

### Loop-Incremental Equations

Equation `(23)`:

```math
\Delta l_{b1}\cos\theta_{b1,n}
-\Delta\theta_{b1}l_{b1}\sin\theta_{b1,n}
+\Delta l_n
=\Delta l_{H1}\cos\theta_{H1,n}
-\Delta\theta_{H1}l_{H1}\sin\theta_{H1,n}
+\Delta l_{b2}\cos\theta_{b2,n}
-\Delta\theta_{b2}l_{b2}\sin\theta_{b2,n}
```

Equation `(24)`:

```math
\Delta l_v\cos\theta_{v,\rho}
-\Delta\theta_v l_v\sin\theta_{v,\rho}
+\Delta l_k\cos\theta_{k,\rho}
-\Delta\theta_k l_k\sin\theta_{k,\rho}
+\Delta l_\rho
=\Delta l_R\cos\theta_{p,\rho}
-\Delta\theta_p l_R\sin\theta_{p,\rho}
```

Equation `(25)`:

```math
\Delta l_{Hi}\cos\theta_{Hi,ai}
-\Delta\theta_{Hi}l_{Hi}\sin\theta_{Hi,ai}
+\Delta l_{ai}
=\Delta l_v\cos\theta_{v,ai}
-\Delta\theta_v l_v\sin\theta_{v,ai}
+\Delta l_{ci}\cos\theta_{ci,ai}
-\Delta\theta_{ci}l_{ci}\sin\theta_{ci,ai}
```

Equation `(26)`:

```math
\Delta l_{Hi}\cos\theta_{Hi,ci}
-\Delta\theta_{Hi}l_{Hi}\sin\theta_{Hi,ci}
+\Delta l_{ai}\cos\theta_{ai,ci}
-\Delta\theta_{ai}l_{ai}\sin\theta_{ai,ci}
=\Delta l_v\cos\theta_{v,ci}
-\Delta\theta_vl_v\sin\theta_{v,ci}
+\Delta l_{ci}
```

Equation `(27)`:

```math
\Delta\theta_{b2}=\Delta\theta_{ai}
```

Equation `(28)`:

```math
\Delta\theta_{ci}=\Delta\theta_k
```

### Whole-Machine RTE

Equation `(29)`:

```math
\Delta\theta_H =
\frac{g_2g_3g_4}{1+g_1g_2g_3g_4}f_1
+\frac{g_3g_4}{1+g_1g_2g_3g_4}\frac{1}{3}\sum_{i=1}^{3}f_{2i}
+\frac{g_4}{1+g_1g_2g_3g_4}f_3
+\frac{1}{1+g_1g_2g_3g_4}\frac{1}{3}\sum_{i=1}^{3}f_{4i}
```

Equation `(30)` for a one-tooth-difference cycloid-pin drive:

```math
\Delta\theta_H =
\frac{
-\frac{1}{z_4}f_1
-\frac{1}{3z_4}\sum_{i=1}^{3}f_{2i}
+f_3
+\frac{1}{3}\sum_{i=1}^{3}f_{4i}
}{
1+\frac{z_1+z_2}{z_2z_4}
}
```

Equation `(31)`:

```math
f_1 =
\frac{1}{\sin\theta_{b2,n}}
\left(
-\frac{\Delta l_{b1}}{l_{b2}}\cos\theta_{b1,n}
+\frac{l_{b1}}{l_{b2}}\Delta\theta_{b1}\sin\theta_{b1,n}
-\frac{\Delta l_n}{l_{b2}}
+\frac{\Delta l_{H1}}{l_{b2}}\cos\theta_{H1,n}
+\frac{\Delta l_{b2}}{l_{b2}}\cos\theta_{b2,n}
\right)
```

Equation `(32)`:

```math
f_{2i} =
\frac{1}{\sin\theta_{v,ci}}
\left(
-\frac{\Delta l_{Hi}}{l_v}\cos\theta_{Hi,ci}
-\frac{\Delta l_{ai}}{l_v}\cos\theta_{ai,ci}
+\frac{\Delta l_v}{l_v}\cos\theta_{v,ci}
+\frac{\Delta l_{ci}}{l_v}
\right)
```

Equation `(33)`:

```math
f_3 =
\frac{1}{\sin\theta_{k,\rho}}
\left(
\frac{\Delta l_v}{l_k}\cos\theta_{v,\rho}
+\frac{\Delta l_k}{l_k}\cos\theta_{k,\rho}
+\frac{\Delta l_\rho}{l_k}
-\frac{\Delta l_R}{l_k}\cos\theta_{p,\rho}
+\frac{l_R}{l_k}\Delta\theta_p\sin\theta_{p,\rho}
\right)
```

Equation `(34)`:

```math
f_{4i} =
\frac{1}{\sin\theta_{Hi,ai}}
\left(
\frac{\Delta l_{Hi}}{l_{Hi}}\cos\theta_{Hi,ai}
+\frac{\Delta l_{ai}}{l_{Hi}}
-\frac{\Delta l_v}{l_{Hi}}\cos\theta_{v,ai}
-\frac{\Delta l_{ci}}{l_{Hi}}\cos\theta_{ci,ai}
\right)
```

### Original-Error Mappings

The paper maps most original errors into equivalent link-length errors.

```math
\Delta l_H=E_H\cos\beta_H,\qquad
\Delta l_c=E_c\cos\beta_c,\qquad
\Delta l_a=E_a\cos\beta_a,\qquad
\Delta l_v=E_v\cos\beta_v
```

```math
\Delta\theta_p=\frac{AP}{l_R}
```

```math
\Delta l_{b1}=E_{b1}\cos\beta_{b1},
\qquad
\Delta l_{b2}=E_{b2}\cos\beta_{b2}
```

```math
\Delta l_n =
E_{b1}\cos(\theta_{b1}+\beta_{b1}-\theta_n)
+E_{b2}\cos(\theta_{b2}+\beta_{b2}-\theta_n)
```

Equation `(35)`:

```math
\Delta\theta_c=\frac{\delta+\Delta r}{l_k\sin\theta_{k,\rho}}
```

Equation `(36)`:

```math
\Delta l_k =
(-1)^n\frac{\delta+\Delta r}{\sin^2\theta_{k,\rho}}
\cos\theta_{k,\rho}
```

```math
\Delta l_\rho =
(-1)^{n+1}\frac{\delta+\Delta r}{\sin^2\theta_{k,\rho}},
\qquad
n=0\ \mathrm{if}\ \rho_c\ge0,\quad n=1\ \mathrm{if}\ \rho_c<0
```

Equation `(37)`:

```math
\Delta l_H=-A_o\cos(\gamma_o-\theta_H),
\qquad
\Delta l_v=-A_o\cos(\gamma_o-\theta_v)
```

### Test-Bench RTE Equation

Equation `(38)`:

```math
\Delta\theta_H=\theta_H-\frac{\theta_1}{I}
```

where `I` is the whole-machine speed ratio.

## Reimplementation Files

The repository reproduction scripts are:

- `scripts/paper_reimplementation/mmt_te_modeling/mmt_te_modeling_reproduction.py`
- `scripts/paper_reimplementation/mmt_te_modeling/mmt_te_modeling_reproduction.m`

They implement the equation groups above as explicit functions. The Python
script also prints a small `RV-80E` demonstration summary and dominant
harmonic bins for a synthetic equivalent-error sweep.

Important limitation: the paper gives the analytical equivalent mechanism and
prototype parameters, but it does not provide a complete machine-readable
cycloidal contact-geometry table for every sample. Therefore the scripts
implement the complete analytical propagation equations and accept contact
angles/link values as inputs. The included demo uses a transparent
engineering placeholder contact sweep so the numerical chain is executable;
it is not a claimed reproduction of Figs. `9`-`14`.

## Dataset Evaluation Plan

### Goal

Evaluate whether the analytical `MMT_TEModeling` formulation can predict or
explain measured `TE` curves in the repository dataset, and whether its
intermediate physical contributions can improve future structured or
physics-informed models.

### Phase 1: Dataset And Parameter Inventory

Map each repository curve to the variables required by the paper:

| Paper Need | Repository Availability | Action |
| --- | --- | --- |
| Output angle grid | TE curve angle samples | Use existing curve angle domain after confirming units and wrap convention. |
| Measured `Delta theta_H` | TE target curve | Use as validation target. |
| Speed | Dataset operating variable | Use for stratification; the analytical static model is not speed-dynamic by itself. |
| Torque | Dataset operating variable | Use for load-regime stratification and residual analysis. |
| Oil temperature | Dataset operating variable | Use for thermal-regime stratification and residual analysis. |
| Direction | Repository `Fw` / `Bw` surfaces | Keep direction-separated evaluation mandatory. |
| Geometry constants | Reducer design data | Fill from drawings, datasheets, or measured rig documentation. |
| Original component errors | Mostly unavailable in dataset | Treat as measured inputs if available; otherwise calibrate equivalent errors. |

### Phase 2: Geometry-Locked Analytical Baseline

Build one reducer-geometry configuration from known constants. Keep all
geometry fixed and evaluate only the paper-style deterministic propagation for
candidate equivalent-error sets.

Required outputs:

- predicted `TE` curve per measured curve;
- raw curve `MAE`, `RMSE`, and peak-to-peak error;
- mean-centered `MAE` and `RMSE`;
- signed mean offset;
- dominant harmonic amplitude and phase differences;
- direction-separated `Fw`, `Bw`, and optional `global` summaries.

### Phase 3: Equivalent-Error Calibration

Because the dataset likely does not contain measured component manufacturing
errors for every curve, fit a small set of equivalent-error parameters. Keep
the calibrated parameters physically interpretable:

- output disc hole deviation channel;
- cycloidal gear hole-position channel;
- crankshaft eccentricity channel;
- pin pitch accumulation channel;
- cycloidal tooth profile plus pin-radius channel;
- optional high-speed involute eccentricity channel.

Use a train/validation split by condition groups rather than by adjacent
samples from the same curve, so the calibration is tested on unseen operating
conditions.

### Phase 4: Compare Against Current Repository Models

Compare the analytical and calibrated analytical predictors against accepted
Track 2 reference surfaces:

- current direction-aware Track 2 leaders;
- paper-reference harmonic models;
- Wave 1 and later curve-aware candidates;
- mean-centered and raw evaluations.

The analytical model should be treated as useful if it improves at least one
of the following without breaking the others:

- offset explainability;
- dominant harmonic attribution;
- direction-stable curve shape;
- physically interpretable failure labels;
- feature or loss design for future Wave 3 or Wave 4 branches.

### Phase 5: Implementation Decision

Use the evaluation to choose one of four outcomes:

| Outcome | Meaning | Repository Action |
| --- | --- | --- |
| Direct predictor viable | Calibrated analytical model predicts curves competitively. | Promote as a structured baseline and add Track 2 matrix entry. |
| Feature generator viable | Analytical terms correlate with residual structure but are not accurate alone. | Add physical features to hybrid structured models. |
| Loss/regularizer viable | Analytical model captures harmonic or periodic constraints. | Use in physics-informed loss design. |
| Diagnostic only | Prediction is weak but error attribution is useful. | Keep as reporting/interpretability tooling. |

### Risks

- Missing measured component errors may make the model underdetermined.
- The paper's low-speed, low-load test condition differs from loaded dataset
  regimes.
- Thermal and torque effects in the repository dataset may dominate residuals
  not represented in the static kinematic model.
- Contact geometry must be reconstructed or parameterized carefully before
  claiming figure-level reproduction.

## Immediate Next Step

Run the Python reproduction smoke check:

```powershell
python -B scripts/paper_reimplementation/mmt_te_modeling/mmt_te_modeling_reproduction.py
```

Then replace the demo contact sweep with reducer-specific measured or
reconstructed contact geometry before using the script for quantitative
dataset claims.
