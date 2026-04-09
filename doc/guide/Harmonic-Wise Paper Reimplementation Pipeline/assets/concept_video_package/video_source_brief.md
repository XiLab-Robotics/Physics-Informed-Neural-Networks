# Harmonic-Wise Pipeline Concept Video Source Brief

## Audience

- learners who want a neutral explanation of harmonic-wise TE modeling
- students who need to understand how a TE curve becomes harmonic targets
- viewers who need conceptual clarity before repository-specific details

## Video Goal

Explain the harmonic-wise pipeline as a general modeling workflow that turns
full TE curves into harmonic targets, predicts those targets from operating
conditions, and reconstructs the TE curve for evaluation.

## Target Depth

- intuitive signal-processing view first
- machine-learning workflow second
- practical benchmark interpretation third

## Required Chapter Order

1. Why one may model TE through harmonics instead of direct point-wise outputs.
2. How TE curves are decomposed into selected harmonic terms.
3. How coefficient form relates to amplitude and phase.
4. How the supervised dataset changes in the harmonic-wise setting.
5. How prediction, reconstruction, and evaluation fit together.
6. What this approach gains and what it does not solve yet.

## Required Takeaways

- A harmonic-wise pipeline predicts compact curve descriptors rather than direct point-wise TE values.
- Harmonic coefficients and amplitude-phase views describe the same periodic content in different parameterizations.
- Reconstruction is the bridge from learned harmonic targets back to the physical TE curve.
- This approach is useful when interpretability and structured periodic modeling matter.

## Concepts That Must Stay Brief

- repository file-by-file bookkeeping
- long detours into unrelated model families
- online compensation details that are not part of the offline concept path

## Concepts That Must Not Be Omitted

- decomposition logic
- target transformation
- reconstruction logic
- evaluation metrics
- strengths and limitations
