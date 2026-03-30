# Local LAN AI Infrastructure Options for Video Knowledge Extraction

## Overview

This report evaluates how to replace quota-limited cloud transcription with a
local or LAN-accessible AI stack while preserving the current working pattern:
the repository remains on the current workstation, while a second stronger PC
can serve transcript, OCR, LLM, and future inference workloads over the local
network.

The decision is driven by the current TwinCAT/TestRig video-guide workflow
already documented in:

- [`doc/reference_codes/testrig_twincat_video_guides_reference.md`](../../reference_codes/testrig_twincat_video_guides_reference.md)
- [`doc/reference_codes/testrig_twincat_ml_reference.md`](../../reference_codes/testrig_twincat_ml_reference.md)

The immediate objective is to produce good Italian technical transcripts and
use them to support repository-owned TwinCAT deployment documentation. The
broader objective is to define an AI-serving architecture that can later support:

- transcript extraction for long technical videos;
- LLM cleanup and report generation;
- OCR-assisted screen understanding;
- optional vision analysis on snapshots;
- future repository tooling that should run on a stronger LAN node.

## What The Repository Actually Needs

The video workflow does not require one monolithic multimodal platform.
Practically, it needs three distinct capabilities:

1. speech-to-text for long Italian technical audio;
2. text cleanup and report synthesis;
3. OCR or vision support for TwinCAT/TestRig screenshots.

These capabilities do not have to come from the same runtime.

That distinction matters because the strongest local STT options are not the
same tools that provide the best local LLM serving experience.

## Key Constraints

### Current Cloud Constraint

The Google GenAI path was technically functional, but the observed free-tier
quota was too small for repeated multi-video processing. For the current
repository workflow, this makes it unsuitable as the canonical pipeline.

### Current Workstation Constraint

The current workstation already has `faster-whisper` and `ctranslate2`
installed, and a real smoke test on a `Machine_Learning_2` audio chunk showed:

- `faster-whisper` `tiny` on CPU was too noisy for serious use;
- `faster-whisper` `small` on CPU was materially more readable and technically
  useful;
- the current machine is not immediately ready for CUDA-accelerated
  `faster-whisper`, because the local runtime failed to load `cublas64_12.dll`.

This means a fully local fallback on the current PC is possible, but not ideal.

### Second Workstation Opportunity

The second PC has:

- `Intel Core i9-14900K`
- `64 GB RAM`
- `NVIDIA RTX A4000 16 GB`

That hardware is a good fit for:

- larger Whisper-family STT models;
- local LLM inference through quantized models;
- OCR pipelines with optional GPU acceleration;
- serving those capabilities back to the current workstation over LAN.

## Important Clarification About Codex And ChatGPT

For one-off assisted work, only the transcript step truly needs a heavy backend.
Cleanup and report synthesis can be done interactively in a Codex session, as we
already did.

However, that is not enough for a reproducible autonomous repository workflow.
If the pipeline should run later without depending on a live Codex session, then
cleanup and report generation also need a callable local service.

ChatGPT Team does not solve this. OpenAI states that ChatGPT billing and API
billing are separate, and ChatGPT subscriptions do not transfer to the API
platform. Therefore the existing ChatGPT Team plan is not a repository-owned
batch backend for transcript or report generation.

## Option 1: Faster-Whisper For STT, Codex For Cleanup, Existing OCR

### Description

This is the lowest-setup path:

- run `faster-whisper` locally or on the second PC for transcript extraction;
- keep OCR in the repository pipeline;
- keep cleanup and report synthesis manual or semi-manual through Codex.

### Strengths

- zero additional paid API dependency;
- easiest migration from the current state;
- preserves privacy and offline processing for transcript extraction;
- enough for research work when the user is actively supervising the process.

### Weaknesses

- not autonomous;
- transcript cleanup quality still depends on an interactive human-in-the-loop
  workflow;
- not suitable as the long-term repository-owned batch pipeline.

### Verdict

Useful as a fallback, but not the recommended canonical architecture.

## Option 2: Faster-Whisper Plus LM Studio On The Second PC

### Description

This is the most balanced architecture for the repository:

- `faster-whisper` handles transcript extraction;
- `LM Studio` serves one or more local LLMs over a LAN-visible API;
- OCR remains a dedicated local step in repository tooling;
- the current workstation orchestrates the workflow and stores artifacts.

### Why LM Studio Is Strong Here

LM Studio officially supports:

- serving models on `localhost` or on the local network;
- OpenAI-compatible endpoints;
- authentication via API tokens;
- remote model loading and unloading;
- JIT loading and auto-unload behaviors.

This makes it well suited as a reusable LAN inference server for:

- transcript cleanup;
- report generation;
- optional future repository assistants;
- general OpenAI-compatible local inference without building everything from
  scratch.

### Strengths

- very good fit for the requirement "continue working from this PC";
- cleaner serving UX than a custom stack;
- OpenAI-compatible endpoints simplify client code;
- strong candidate for future non-video local LLM usage as well;
- can be secured with tokens and limited to the local network.

### Weaknesses

- STT still needs a separate service or script, because LM Studio is primarily
  an LLM server, not a dedicated Whisper-style transcription backend;
- introduces two runtime surfaces instead of one:
  `faster-whisper` and `LM Studio`.

### Verdict

This is the recommended default architecture.

## Option 3: Faster-Whisper Plus Ollama On The Second PC

### Description

This is similar to the LM Studio approach, but with `Ollama` serving the local
LLM side instead of LM Studio.

### Why Ollama Is Interesting

Ollama officially provides:

- a local API server;
- OpenAI-compatible endpoints;
- support for local and remote exposure through `OLLAMA_HOST`;
- a documented integration path with the Codex CLI.

This means Ollama is a strong candidate when the priority is:

- easy local model serving;
- simple OpenAI-compatible client integration;
- future experimentation with coding-agent or tool-using local models.

### Strengths

- simple serving model;
- strong ecosystem and broad community adoption;
- direct documented path for Codex CLI usage with `--oss`;
- very practical for local reasoning, cleanup, report writing, and vision.

### Weaknesses

- no clear official STT/audio-transcription path comparable to a dedicated
  Whisper endpoint;
- for this project it still needs a separate STT service;
- somewhat less convenient than LM Studio for remote model management and
  GUI-driven model lifecycle control.

### Verdict

Very strong alternative to LM Studio, especially if Codex CLI integration
becomes a first-class requirement. Still not sufficient as the only backend.

## Option 4: LocalAI As A Unified OpenAI-Compatible Stack

### Description

LocalAI is attractive because it exposes an OpenAI-compatible API and
explicitly supports `/v1/audio/transcriptions` with multiple backends,
including:

- `whisper.cpp`
- `moonshine`
- `faster-whisper`

It can therefore unify:

- STT;
- LLM serving;
- vision;
- embeddings;
- some additional OpenAI-like endpoints.

### Strengths

- closest match to "one local API for everything";
- direct transcription endpoint is highly relevant to the current workflow;
- easier to treat as one remote AI appliance in LAN.

### Weaknesses

- more operations-heavy than LM Studio or Ollama;
- more configuration complexity;
- broader platform surface means more maintenance burden when something breaks;
- for this repository, the simplicity advantage of a single API may be offset
  by higher setup and debugging cost.

### Verdict

Technically powerful and highly relevant, but best treated as the
single-platform option only if you explicitly prefer one self-hosted API over a
cleaner multi-service design.

## Option 5: WhisperX Instead Of Plain Faster-Whisper

### Description

WhisperX builds on Whisper-family transcription and adds:

- stronger word-level timestamps;
- alignment;
- optional diarization;
- batching through a faster-whisper backend.

It officially documents support for Italian alignment models.

### Strengths

- potentially better segment boundaries and timing accuracy;
- useful when exact alignment matters for report traceability;
- more sophisticated than bare Whisper for sentence timing.

### Weaknesses

- more setup complexity;
- larger dependency footprint;
- diarization is not central to the current single-speaker video-guide use case;
- not clearly necessary unless plain `faster-whisper` quality proves
  insufficient after moving to the stronger PC.

### Verdict

Treat this as the upgrade path after a first stable `faster-whisper` rollout,
not as the initial default.

## Option 6: Whisper.cpp As CPU-Oriented Fallback

### Description

`whisper.cpp` is the lean, dependency-light fallback for local transcription.
It is valuable because it:

- runs without a full Python ML stack;
- supports timestamps and multiple output formats;
- remains usable when GPU support is limited or unavailable.

### Strengths

- robust offline fallback;
- relatively portable;
- lower operational weight than a larger Python stack.

### Weaknesses

- less attractive than GPU-backed `faster-whisper` on the stronger PC;
- not the best choice when you already have a suitable NVIDIA workstation.

### Verdict

Keep it as a fallback path, not as the primary plan.

## Option 7: Keep Google GenAI As A Fallback Only

### Description

Google GenAI was the first provider that worked in this repository without new
OpenAI API billing.

### Strengths

- no immediate new stack to learn;
- already partly integrated.

### Weaknesses

- free-tier request limits are too restrictive for repeated multi-video work;
- fails the autonomy requirement;
- encourages pipeline design around quota avoidance instead of quality and
  reproducibility.

### Verdict

Do not keep it as the canonical solution. At most, keep it as an optional
fallback for spot checks.

## OCR Recommendation

The repository should stop treating OCR as a report-visible output stream and
continue treating it as an internal evidence source.

For OCR, `PaddleOCR` is the most interesting next step because it is a strong
local OCR stack with multilingual support and deployment-oriented tooling. It is
better aligned with the repository goal than keeping Tesseract as the only OCR
backend.

The recommended OCR role is:

- detect TwinCAT UI text when it is actually useful;
- support snapshot ranking and metadata extraction;
- avoid dumping noisy OCR text into the final report.

## Can The Second PC Be A LAN AI Server?

Yes. This is not only possible, it is the recommended deployment shape.

The clean architectural split is:

### Current Workstation

- stores the repository;
- launches the workflow scripts;
- manages report generation and final artifact placement;
- remains the human-facing development machine.

### Second Workstation

- hosts STT;
- hosts one or more local LLMs;
- optionally hosts OCR and vision inference;
- exposes APIs or job endpoints over LAN.

This lets the current workstation stay lightweight and stable while the second
PC becomes a reusable inference and job node.

## Recommended Architecture

### Recommended Default Stack

The best overall fit is:

1. `faster-whisper` on the second PC for transcript extraction;
2. `LM Studio` on the second PC for cleanup and report-generation LLM calls;
3. `PaddleOCR` on the second PC or in a dedicated local environment for OCR;
4. repository tooling on the current PC orchestrating the end-to-end workflow.

### Why This Is The Best Fit

- it avoids paid API dependence;
- it preserves the current "work from this PC" workflow;
- it isolates heavy inference on the stronger node;
- it keeps transcript and LLM services replaceable instead of hard-coupled;
- it scales naturally to future repository tooling.

### Recommended Networking Shape

- `LM Studio` server exposed on the local network with authentication enabled;
- a small repository-owned `FastAPI` service on the second PC for STT and OCR;
- the current repository scripts call those endpoints by LAN IP;
- model lifecycle is handled on the second PC where the hardware lives.

This is better than trying to force every capability into a single off-the-shelf
runtime.

## Alternate Architecture If Codex CLI Integration Becomes Important

If local coding-agent workflows become a first-class requirement, the best
alternative is:

1. `faster-whisper` for STT;
2. `Ollama` for local LLM serving;
3. `PaddleOCR` for OCR;
4. optional Codex CLI integration through the documented Ollama path.

This is slightly less polished than the LM Studio route for generic remote LLM
operations, but stronger if the priority shifts toward local coding-assistant
integration.

## What Should Stay Out Of Scope

### Do Not Depend On ChatGPT Team As The Backend

That plan does not satisfy the autonomy requirement because ChatGPT Team is not
a local or callable repository service.

### Do Not Force One Tool To Do Everything

The strongest STT tools and the strongest local LLM serving tools are not the
same products. The architecture should reflect that.

### Do Not Keep OCR As A Report Dump

OCR should remain a support signal, not a reader-facing noise source.

## Practical Recommendation

Proceed in this order:

1. use the second workstation as the LAN inference node;
2. make `faster-whisper` the canonical transcript backend;
3. make `LM Studio` the canonical local LLM server;
4. add `PaddleOCR` as the next OCR backend;
5. keep `Ollama` as a valid alternate path, especially for future local coding
   workflows;
6. keep `LocalAI` only if you later decide that a single unified API is worth
   the higher setup and maintenance cost.

## Sources

- [TestRig TwinCAT Video Guides Reference](../../reference_codes/testrig_twincat_video_guides_reference.md)
- [TestRig TwinCAT ML Reference](../../reference_codes/testrig_twincat_ml_reference.md)
- [LM Studio: Local LLM API Server](https://lmstudio.ai/docs/developer/core/server)
- [LM Studio: Serve on Local Network](https://lmstudio.ai/docs/developer/core/server/serve-on-network)
- [LM Studio: Server Settings](https://lmstudio.ai/docs/developer/core/server/settings)
- [LM Studio: OpenAI-Compatible Responses](https://lmstudio.ai/docs/developer/openai-compat/responses)
- [Ollama: API Introduction](https://docs.ollama.com/api)
- [Ollama: OpenAI Compatibility](https://docs.ollama.com/api/openai-compatibility)
- [Ollama: FAQ](https://docs.ollama.com/faq)
- [Ollama: Codex Integration](https://docs.ollama.com/integrations/codex)
- [LocalAI: Quickstart](https://localai.io/basics/getting_started/index.html)
- [LocalAI: Audio to Text](https://localai.io/features/audio-to-text/)
- [Faster-Whisper README](https://github.com/SYSTRAN/faster-whisper)
- [WhisperX README](https://github.com/m-bain/whisperX)
- [whisper.cpp CLI README](https://github.com/ggml-org/whisper.cpp/blob/master/examples/cli/README.md)
- [PaddleOCR Documentation](https://www.paddleocr.ai/main/en/index/index.html)
- [OpenAI Help: Billing Settings In ChatGPT Vs Platform](https://help.openai.com/en/articles/9039756-billing-settings-in-chatgpt-vs-platform)
- [OpenAI Help: ChatGPT Subscription To API](https://help.openai.com/en/articles/8156019)
