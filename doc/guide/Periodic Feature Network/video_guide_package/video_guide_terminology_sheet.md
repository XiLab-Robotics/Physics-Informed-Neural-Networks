# Periodic Feature Network Video Guide Terminology Sheet

| Term | Preferred Definition | Allowed Synonym | Avoid |
| --- | --- | --- | --- |
| Periodic feature network | Neural model that expands angle into periodic basis features before dense regression. | Periodic MLP | Harmonic regression |
| Feature expansion | Transformation that adds derived basis channels before modeling. | Basis expansion | Random augmentation |
| Concatenation | Joining feature channels into one input vector. | Merge | Summation |
| Feedforward backbone | Dense network used after the periodic expansion. | MLP backend | Recurrent module |
| Middle-ground architecture | Model that combines explicit structure with neural flexibility. | Hybrid compromise | Weak model |

