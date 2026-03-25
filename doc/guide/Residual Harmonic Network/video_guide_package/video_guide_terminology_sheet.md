# Residual Harmonic Network Video Guide Terminology Sheet

| Term | Preferred Definition | Allowed Synonym | Avoid |
| --- | --- | --- | --- |
| Residual harmonic network | Hybrid model combining harmonic structure with learned residual correction. | Structured residual model | Pure MLP |
| Structured branch | Component that models the main harmonic TE part. | Harmonic branch | Noise filter |
| Residual branch | Component that learns what the structured part does not explain. | Correction branch | Second baseline |
| Additive merge | Final sum of structured and residual outputs. | Residual addition | Concatenation |
| Frozen branch | Branch kept fixed during training. | Fixed component | Dead branch |
| Auxiliary outputs | Extra branch-level outputs returned for inspection. | Diagnostics | Hidden logits |
