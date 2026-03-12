# Training Queue

Queue a training campaign by copying YAML files into:

- `pending/`

The batch runner moves each YAML through:

1. `pending/`
2. `running/`
3. `completed/` or `failed/`

Recommended workflow:

1. keep reusable presets under `config/training/feedforward/presets/`;
2. copy the selected preset YAML files into `pending/`;
3. launch `training/run_training_campaign.py`;
4. inspect the generated campaign report under `output/training_campaigns/`.
