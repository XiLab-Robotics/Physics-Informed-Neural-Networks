# Residual Harmonic Network Video Guide Narration Outline

## Opening

Frame the model as the clearest example of a structured-neural hybrid in the TE series.

## Chapter 1 - Why A Hybrid Is Needed

- explain why a harmonic model may be too rigid;
- explain why a plain MLP may hide the structure.

## Chapter 2 - Structured Harmonic Branch

- describe the harmonic prediction path;
- explain that it captures the dominant periodic component.

## Chapter 3 - Residual Neural Branch

- describe the MLP correction path;
- explain that it captures what the harmonic branch misses.

## Chapter 4 - Additive Combination

- show the branch outputs being summed;
- explain the final TE prediction as structured plus residual.

## Chapter 5 - Training Modes

- explain frozen structured branch training;
- explain joint optimization training;
- clarify why both modes are useful.

## Chapter 6 - Repository Implementation

- identify the hybrid model module;
- explain auxiliary outputs;
- connect the architecture to the shared training pipeline.

## Closing

Summarize the model as the transition point between a structured baseline and a more flexible hybrid modeling strategy.
