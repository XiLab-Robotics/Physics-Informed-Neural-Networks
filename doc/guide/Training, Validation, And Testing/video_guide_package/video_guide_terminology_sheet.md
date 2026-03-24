# Training, Validation, And Testing Video Guide Terminology Sheet

| Term | Preferred Definition | Allowed Synonym | Avoid |
| --- | --- | --- | --- |
| Training set | Dataset subset used to update model parameters. | Train split | Full dataset |
| Validation set | Dataset subset used for model selection and tuning decisions. | Validation split | Final benchmark |
| Test set | Dataset subset reserved for the final unbiased evaluation. | Holdout test split | Tuning set |
| Training loop | Repeated optimization cycle across batches and epochs. | Optimization loop | Evaluation procedure |
| Checkpoint | Saved model state at a specific training stage. | Saved state | Final model by default |
| Early stopping | Stopping training when validation behavior stops improving. | Validation-based stopping | Undertraining |
| Leakage | Information from evaluation data indirectly influencing training or selection. | Data leakage | Small overlap only |
| Generalization | Performance on unseen but relevant data. | Out-of-sample performance | Training accuracy |
| Metric | Numeric score used to quantify prediction quality. | Evaluation score | Loss, unless the score is the loss |
| MAE | Mean absolute error between prediction and target. | Absolute error metric | Percentage error |
| RMSE | Root mean squared error, more sensitive to large errors. | Squared-error metric | MAE |
| Operating-condition coverage | Whether train, validation, and test sets span the relevant speed, torque, and temperature ranges. | Condition coverage | Randomness only |
| Valid window | TE segment marked usable according to repository filtering logic. | Accepted segment | Any raw window |
| Curve leakage | Closely related points from the same TE curve appearing across splits. | Intra-curve leakage | Normal random split behavior |
