# Wave 5.1 And Wave 5.2 Embryonic Skeletons

## Overview

This technical document plans the repository work for preparing embryonic
`Wave 5.1` and `Wave 5.2` implementation skeletons while the separate `Wave 4 series`
campaign is handled elsewhere. The objective is to make the next model and
physics branches implementation-ready without making them campaign-ready.

The skeletons should cover model modules, diagnostic adapters, validators,
configuration templates, launcher drafts, and documentation notes. They must
not launch training, mutate active campaign state, or create a final queue
until the blocking evidence from `Wave 4 series`, `Wave 5.1` smoke checks, and
`Wave 5.2A` diagnostics is available.

## Technical Approach

The approved implementation pass should prepare:

- a `Wave 5.1` harmonic-prior residual model skeleton with fixed harmonic basis
  buffers, structured harmonic reconstruction, and residual-correction output;
- optional `Wave 5.1` grouped-head interfaces for low-order, stable-middle, and
  high-order harmonic groups;
- a `Wave 5.2A` MMT equation diagnostic adapter around the repository-owned MMT
  reproduction;
- placeholders for `Wave 5.2B` MMT feature generation and `Wave 5.2C` weak MMT
  soft-constraint PINN integration;
- validators and smoke commands that prove import, model construction,
  forward pass, and package consistency;
- launcher drafts that are explicitly marked disabled / dry-run only until
  campaign readiness is approved.

Context7 was checked for current PyTorch and PyTorch Lightning patterns. The
implementation should use ordinary `torch.nn.Module` subclasses, registered
submodules, and `register_buffer` for fixed harmonic basis tensors. Existing
repository Lightning training modules should remain the integration surface
instead of creating a separate training loop.

## Involved Components

Potential implementation components after approval:

- `scripts/models/wave3_harmonic_prior_residual_network.py`
- `scripts/models/wave4_mmt_diagnostic_adapter.py`
- `scripts/models/model_factory.py`
- `scripts/campaigns/wave_3/`
- `scripts/campaigns/wave_4/`
- `doc/scripts/campaigns/wave_3/`
- `doc/scripts/campaigns/wave_4/`
- `config/training/wave3_embryonic_skeleton/`
- `config/training/wave4_embryonic_skeleton/`
- `doc/reports/campaign_plans/cross_wave/wave_3_wave_4/2026-06-11-15-10-02_wave3_wave4_embryonic_skeleton_plan_report.md`
- `doc/running/te_model_live_backlog.md`
- `doc/README.md`

Protected until later approval:

- `doc/running/active_training_campaign.yaml`
- final queue YAMLs for real training runs;
- any launcher command that starts training;
- registry files under `output/registries/`;
- campaign result reports.

## Implementation Steps

1. Create and approve this technical document and the paired preliminary
   planning report.
2. Implement the Wave 5.1 harmonic-prior residual model skeleton with configurable
   losses and residual weights.
3. Implement the Wave 5.2A MMT diagnostic adapter skeleton and smoke script.
4. Add package validators for Wave 5.1 and Wave 5.2 embryonic skeletons.
5. Add dry-run launcher drafts and launcher notes marked `not campaign-ready`.
6. Add configuration templates marked `blocked_on_track2h_results`.
7. Run compile checks, import checks, forward-smoke checks, package validators,
   and Markdown QA.
8. Stop before generating final campaign queues or mutating active campaign
   state.
