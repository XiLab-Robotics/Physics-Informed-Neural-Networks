# Concept Video Package Command Archive

## Overview

This document canonizes the temporary command collection previously stored in:

- `.temp/comandi_concept_video_package.txt`

The goal is to preserve the already-generated `concept_video_package`
NotebookLM command texts in a repository-owned technical note and make their
structure reusable for future model guides.

## Source Status

The archived examples below are preserved as they appeared in the temporary
source file.

Important scope note:

- the archived source content currently contains English command bodies;
- the project workflow also uses an Italian counterpart for each topic, where
  the opening instruction changes from:
  - `Create a didactic video overview in English for beginners and junior engineers.`
  to:
  - `Create a didactic video overview in Italian for beginners and junior engineers.`

This means:

- the archived examples remain as-is;
- the bilingual reuse rule is preserved explicitly in the template section.

## Archived Commands

### Neural Network Foundations

```text
Create a didactic video overview in English for beginners and junior engineers.

Goal:
Explain the fundamental ideas behind neural networks in a neutral, general way: what a neuron is, how layers form a network, why activations matter, how prediction and loss interact, how training works, and why generalization is more important than memorization.

Requirements:
- Follow the narration outline and required chapter order from the uploaded concept package.
- Present neural networks as parameterized functions learned from data, not as mysterious black boxes.
- Explain clearly: weighted sum, bias, activation, hidden layers, forward pass, loss, gradient-based learning, overfitting, and generalization.
- Keep the explanation general and educational, not repository-specific.
- Use the terminology sheet as the source of truth for wording.
- Respect the fact-boundary notes and avoid unsupported claims.
- Do not collapse the explanation into one implementation or one application only.
- Use the available visual material to support the explanation when possible.

Desired output style:
- 4 to 6 minutes
- calm technical teaching tone
- beginner-friendly but precise
- intuitive first, compact formalism second
- strong educational clarity, minimal jargon overload
```

### Training, Validation, And Testing

```text
Create a didactic video overview in English for beginners and junior engineers.

Goal:
Explain in a neutral, practical way why supervised-learning workflows need separate training, validation, and test phases, what each phase is responsible for, and how leakage or misuse can make model results unreliable.

Requirements:
- Follow the narration outline and required chapter order from the uploaded concept package.
- Explain clearly the different roles of training set, validation set, and test set.
- Explain model selection, early stopping, and final unbiased evaluation in simple engineering language.
- Clarify why validation and testing are not interchangeable.
- Explain what data leakage is and why it breaks trust in results.
- Keep the explanation general and broadly reusable outside this repository.
- Use the terminology sheet as the source of truth for wording.
- Respect the fact-boundary notes and avoid unsupported claims.
- Use the available visual material to support the split logic and workflow interpretation.

Desired output style:
- 4 to 6 minutes
- calm technical teaching tone
- beginner-friendly but precise
- workflow-centered explanation
- strong practical clarity over theory overload
```

### TE Model Curriculum

```text
Create a didactic video overview in English for beginners and junior engineers.

Goal:
Explain a neutral curriculum for transmission-error model families: why simpler baselines come first, how structured and hybrid families build on them, and why a curriculum is a learning map rather than a promise that every family is already implemented.

Requirements:
- Follow the narration outline and required chapter order from the uploaded concept package.
- Present the curriculum as an ordered study map across model families.
- Explain why baseline models matter before more advanced families.
- Distinguish clearly among baseline, structured, temporal, hybrid, and roadmap-oriented families.
- Explain why more advanced models should not automatically be considered the best starting point.
- Keep the explanation educational and not tied too strongly to one repository status discussion.
- Use the terminology sheet as the source of truth for wording.
- Respect the fact-boundary notes and avoid unsupported claims.
- Do not imply that every family shown in the curriculum is already implemented.
- Use the curriculum visual material strongly.

Desired output style:
- 4 to 6 minutes
- calm technical teaching tone
- beginner-friendly but precise
- map-like explanation with strong visual guidance
- emphasis on family progression and comparison logic
```

### FeedForward Network

```text
Create a didactic video overview in English for beginners and junior engineers.

Goal:
Explain in a neutral, general way what a FeedForward Network is, how it computes a prediction, how training, validation, and testing typically work for this model class, and why it is the standard baseline neural architecture for many supervised-learning tasks.

Requirements:
- Follow the narration outline and required chapter order from the uploaded concept package.
- Present the model as a one-way multilayer perceptron with dense layers and nonlinear activations.
- Explain the prediction flow in simple engineering language:
input features, dense transformations, activation functions, and final output.
- Explain that the architecture is flexible but generic.
- Explain what it usually learns well:
nonlinear mappings from input variables to target values.
- Explain what it does not encode explicitly:
special domain structure, periodicity, temporal memory, or physics constraints unless those are added separately.
- Keep the explanation general and not repository-centered.
- Use the terminology sheet as the source of truth for wording.
- Respect the fact-boundary notes and avoid unsupported claims.
- Use the available visual material strongly.

Desired output style:
- 4 to 6 minutes
- calm technical teaching tone
- beginner-friendly but precise
- conceptual first, practical workflow second
- strong visual use of the diagrams
```

### Harmonic Regression

```text
Create a didactic video overview in English for beginners and junior engineers.

Goal:
Explain in a neutral, general way what Harmonic Regression is, how periodic behavior can be represented with sine and cosine terms, how the model is fitted and evaluated, and why it is attractive when interpretability and periodic structure matter.

Requirements:
- Follow the narration outline and required chapter order from the uploaded concept package.
- Explain clearly why cyclic phenomena motivate harmonic models.
- Introduce sine and cosine basis functions in simple engineering language.
- Explain coefficient meaning, basis order, and periodic structure assumption.
- Explain how training, validation, and testing work for this model class.
- Emphasize interpretability and compactness.
- Explain the main limitations:
model-order choice matters and non-periodic residual behavior may be missed.
- Keep the explanation general and not repository-centered.
- Use the terminology sheet as the source of truth for wording.
- Respect the fact-boundary notes and avoid unsupported claims.
- Use the available visual material when present.

Desired output style:
- 4 to 6 minutes
- calm technical teaching tone
- beginner-friendly but precise
- intuitive periodic-model explanation first
- compact mathematical intuition, not heavy formal derivations
```

### Periodic Feature Network

```text
Create a didactic video overview in English for beginners and junior engineers.

Goal:
Explain in a neutral, general way what a Periodic Feature Network is, how explicit periodic feature expansion works, how those engineered features are used by a downstream regressor, and why this is a useful middle-ground model between generic neural networks and fully structured periodic models.

Requirements:
- Follow the narration outline and required chapter order from the uploaded concept package.
- Explain why some inputs deserve explicit periodic encoding.
- Explain in simple terms how periodic feature expansion is built.
- Clarify that the final predictor still learns nonlinear interactions on top of those features.
- Explain how training, validation, and testing apply to this hybrid model.
- Emphasize the middle-ground character of the architecture:
more structured than a plain MLP, less rigid than a pure basis model.
- Keep the explanation general and not repository-centered.
- Use the terminology sheet as the source of truth for wording.
- Respect the fact-boundary notes and avoid unsupported claims.
- Use the available visual material strongly.

Desired output style:
- 4 to 6 minutes
- calm technical teaching tone
- beginner-friendly but precise
- hybrid-model intuition first
- clear comparison framing against plain MLP and pure harmonic models
```

### Residual Harmonic Network

```text
Create a didactic video overview in English for beginners and junior engineers.

Goal:
Explain in a neutral, general way what a Residual Harmonic Network is, how it combines a structured harmonic backbone with a learned residual correction, how the final prediction is formed, and why decomposition can balance interpretability and flexibility.

Requirements:
- Follow the narration outline and required chapter order from the uploaded concept package.
- Explain the core decomposition idea:
structured main signal plus learned residual correction.
- Clarify how the harmonic backbone and residual branch complement each other.
- Explain how training, validation, and testing apply to the combined model.
- Emphasize the balance between structure and flexibility.
- Explain the limitations:
higher complexity, partial interpretability only, and need for disciplined validation.
- Keep the explanation general and not repository-centered.
- Use the terminology sheet as the source of truth for wording.
- Respect the fact-boundary notes and avoid unsupported claims.
- Use the available visual material strongly.

Desired output style:
- 4 to 6 minutes
- calm technical teaching tone
- beginner-friendly but precise
- decomposition intuition first
- clear structured-plus-residual visual explanation
```

### Multilayer Perceptrons

```text
Create a didactic video overview in English for beginners and junior engineers.

Goal:
Explain in a neutral, general way what Multilayer Perceptrons are, how stacked dense layers and activations create nonlinear function approximation, how MLPs are typically trained, validated, and tested, and why they are such a common starting point in supervised learning.

Requirements:
- Follow the narration outline and required chapter order from the uploaded concept package.
- Present the MLP as a general model class built from hidden layers and nonlinear activations.
- Explain clearly the difference between a single neuron and a multilayer perceptron.
- Explain in simple engineering language how forward computation, loss minimization, and gradient-based updates work.
- Explain what MLPs are good at and where they can struggle.
- Keep the explanation neutral and broadly reusable outside this repository.
- Use the terminology sheet as the source of truth for wording.
- Respect the fact-boundary notes and avoid unsupported claims.
- Do not imply that this topic already has a full canonical guide in the repository.
- Use the uploaded concept media as visual support where available.

Desired output style:
- 4 to 6 minutes
- calm technical teaching tone
- beginner-friendly but precise
- conceptual progression from neuron to MLP
- practical training interpretation near the end
```

## Reuse Pattern For Future Topics

For a new guide-local `concept_video_package`, keep the command structure stable
and vary only the topic-specific content.

## Language Toggle

Use exactly one of these opening lines:

### English

```text
Create a didactic video overview in English for beginners and junior engineers.
```

### Italian

```text
Create a didactic video overview in Italian for beginners and junior engineers.
```

## Reusable Skeleton

```text
<LANGUAGE_OPENING_LINE>

Goal:
<TOPIC_GOAL_PARAGRAPH>

Requirements:
- Follow the narration outline and required chapter order from the uploaded concept package.
- <TOPIC_REQUIREMENT_1>
- <TOPIC_REQUIREMENT_2>
- <TOPIC_REQUIREMENT_3>
- Keep the explanation general and not repository-centered.
- Use the terminology sheet as the source of truth for wording.
- Respect the fact-boundary notes and avoid unsupported claims.
- Use the available visual material strongly.

Desired output style:
- 4 to 6 minutes
- calm technical teaching tone
- beginner-friendly but precise
- <TOPIC_STYLE_POINT_1>
- <TOPIC_STYLE_POINT_2>
```

## Recommended Future Workflow

For a future model or guide topic:

1. start from the reusable skeleton above;
2. choose the language opening line:
   - Italian
   - English
3. adapt only the topic-specific `Goal`, topic-specific requirement bullets, and
   topic-specific style emphasis;
4. keep the shared guardrails unchanged unless the repository workflow evolves;
5. archive the final new command in the same stable style so the command family
   remains consistent over time.
