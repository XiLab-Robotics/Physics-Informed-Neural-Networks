# Reference Code Notes

This folder contains detailed notes extracted from the Git submodules stored under `reference/codes/`.

The purpose of these documents is to preserve the most useful implementation patterns from the reference repositories before developing the RV-reducer neural-network code in this project.

## Available Documents

- [blind_handover_controller_reference.md](./blind_handover_controller_reference.md)
  Main style baseline for naming, comments, progressive implementation, ROS node structure, and PyTorch Lightning training flow.
- [mediapipe_gesture_recognition_reference.md](./mediapipe_gesture_recognition_reference.md)
  Supporting reference for Hydra-based configuration, Lightning training structure, and reusable utility patterns.
- [multimodal_fusion_reference.md](./multimodal_fusion_reference.md)
  Supporting reference for compact multimodal ROS pipelines, explicit command mapping, and straightforward Lightning baselines.

## Usage

- Treat `blind_handover_controller_reference.md` as the strict default when implementation details are undecided.
- Use the other two documents to reinforce or confirm patterns already compatible with the main baseline.
- Use these notes together with `doc/reference_summaries/06_Programming_Style_Guide.md` when writing new ML or utility code in this repository.
