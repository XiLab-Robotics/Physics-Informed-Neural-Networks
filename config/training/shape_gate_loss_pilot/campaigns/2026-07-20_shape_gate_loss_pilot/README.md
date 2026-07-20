# Shape-Gate Loss Pilot Campaign Package

This package materializes the approved shape-gate loss pilot on
`polished_dataset` with `setpoints` inputs and the `Fw` surface.

The package is intentionally not a promotable full campaign. Promotion of this
profile requires a later full `3 x 3` campaign over `simplified_setpoints`,
`polished_setpoints`, and `polished_actual_values`, each with `global`, `Fw`,
and `Bw` surfaces.

Queue files:

- `queue/001_shape_gate_loss_periodic_gru_sequence_fw.yaml`

Launcher:

- `scripts/campaigns/cross_wave/run_shape_gate_loss_pilot_campaign.ps1`
