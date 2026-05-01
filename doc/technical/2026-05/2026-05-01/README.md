# 2026-05-01 Technical Documents

- [2026-05-01-22-36-34_rcim_instance_variant_file_removal.md](./2026-05-01-22-36-34_rcim_instance_variant_file_removal.md)
  Plan the final recovered RCIM instance-helper cleanup that removes
  `instance_v4.py` and `instance_v5.py` from the repository-owned workflow
  subtree and leaves `instance.py` as the sole active runtime helper.
- [2026-05-01-22-22-33_rcim_instance_unification_and_v4_deactivation.md](./2026-05-01-22-22-33_rcim_instance_unification_and_v4_deactivation.md)
  Plan the recovered RCIM instance-helper cleanup that promotes the active
  `instance_v5.py` runtime surface to `instance.py`, removes `instance_v4.py`
  from the active path, and records the migration plus future commit hash in
  the workflow README.
- [2026-05-01-19-02-56_rcim_predictorml_comment_fill_and_capitalization_normalization.md](./2026-05-01-19-02-56_rcim_predictorml_comment_fill_and_capitalization_normalization.md)
  Plan the narrow follow-up pass that fills standalone `#` comment placeholders
  and normalizes inline-comment capitalization inside the recovered RCIM
  `predictorML.py` helper without changing its logic.
- [2026-05-01-12-06-00_rcim_instance_comment_fill_and_capitalization_normalization.md](./2026-05-01-12-06-00_rcim_instance_comment_fill_and_capitalization_normalization.md)
  Plan the narrow follow-up pass that fills the standalone `#` comment
  placeholders in the recovered RCIM instance helpers and normalizes the
  capitalization of their inline comments.
- [2026-05-01-11-01-49_rcim_recovered_original_workflow_utility_visual_style_normalization.md](./2026-05-01-11-01-49_rcim_recovered_original_workflow_utility_visual_style_normalization.md)
  Plan the follow-up visual style-normalization pass over the recovered-original
  RCIM utility files so they match the repository-authored spacing, comment
  capitalization, and inline-comment density already established in the main
  workflow entrypoints.
- [2026-05-01-01-38-44_rcim_recovered_original_workflow_utility_cleanup_and_style_alignment.md](./2026-05-01-01-38-44_rcim_recovered_original_workflow_utility_cleanup_and_style_alignment.md)
  Plan the final utility-focused cleanup and style-alignment pass over the
  recovered-original RCIM workflow, limited to `instance_v4.py`,
  `instance_v5.py`, `predictorML.py`, and the adjacent workflow README.
- [2026-05-01-00-42-42_rcim_recovered_original_workflow_comment_preserving_restore.md](./2026-05-01-00-42-42_rcim_recovered_original_workflow_comment_preserving_restore.md)
  Plan a conservative restoration of the recovered-original RCIM workflow so
  the user-authored inline comments and local formatting are recovered from the
  `_old` backup copies and only minimal repository-style normalization is
  applied afterward.
