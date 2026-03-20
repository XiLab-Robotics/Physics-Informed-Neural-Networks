# FeedForward Network Video Guide Narration Outline

## Opening

Start by framing the feedforward network as the simplest useful neural baseline for TE regression. The goal is not to teach every neural-network variant at once, but to give the viewer a stable reference point for the rest of the curriculum.

## Chapter 1 - The Baseline Question

- explain why the repository needs a generic neural baseline;
- connect that need to model comparison and later architectural improvements.

## Chapter 2 - What The Model Is

- describe the feedforward network as a point-wise MLP;
- list the TE input features;
- stress that one sample is processed independently.

## Chapter 3 - How It Computes A Prediction

- explain normalization;
- show the dense layer stack;
- explain activation, dropout, and output head in plain language.

## Chapter 4 - What It Can Learn

- emphasize flexible nonlinear regression;
- explain that it can capture generic operating-variable interactions;
- note that it must discover periodicity indirectly.

## Chapter 5 - What It Does Not Encode

- no explicit harmonic basis;
- no residual decomposition;
- no temporal memory;
- no physics constraint.

## Chapter 6 - Repository Mapping

- point to the backbone implementation;
- point to the model factory registration;
- point to the shared training script and regression module.

## Closing

End by saying that the feedforward network is the simplest baseline, not the end goal. It is the architecture against which the structured and hybrid models will be judged.
