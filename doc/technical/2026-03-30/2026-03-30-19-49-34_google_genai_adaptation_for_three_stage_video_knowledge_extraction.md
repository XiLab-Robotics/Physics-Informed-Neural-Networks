# Google GenAI Adaptation For Three Stage Video Knowledge Extraction

## Overview

The previously prepared three-stage high-quality video workflow currently
targets an OpenAI API path for transcript generation and report synthesis.
That path is technically valid but not aligned with the user's tooling
constraints because it requires separate API quota and billing.

The repository now has a working `GOOGLE_API_KEY` and a verified code path with
the current `google-genai` SDK. The workflow therefore needs to be adapted so
that the canonical TwinCAT/TestRig video-knowledge extraction path uses Google
GenAI instead of the OpenAI API.

## Technical Approach

The adaptation will replace the provider-specific layer of the current
high-quality workflow while preserving the same three-stage repository design:

1. canonical transcript extraction and cleanup;
2. evidence-driven snapshot selection;
3. OCR-assisted analysis for final report synthesis.

The first implementation goal is not to keep the old provider abstraction
half-alive. The practical goal is to make the repository's canonical workflow
work with the user's available Google key and SDK path.

The implementation will therefore:

- remove the hard dependency on the OpenAI client in the new high-quality
  workflow entry point;
- add `google-genai` as the canonical provider dependency for the new workflow;
- implement transcript cleanup and final report synthesis through Gemini;
- verify the best feasible transcript-generation path available from the Google
  side under the current SDK and account constraints;
- keep OCR and snapshot-selection logic provider-independent so they remain
  reusable.

If direct high-quality speech transcription is not available from the current
Google SDK path in the exact same way as with a dedicated STT API, the
repository workflow should still be adapted around a practical Google-first
pipeline rather than silently falling back to the older OpenAI design.

## Involved Components

- `scripts/tooling/extract_video_guide_knowledge.py`
- `requirements.txt`
- `README.md`
- `doc/guide/project_usage_guide.md`
- `doc/reference_codes/testrig_twincat_video_guides_reference.md`
- `doc/reference_codes/video_guides/`

## Implementation Steps

1. Inspect the current provider-specific assumptions in the high-quality video
   workflow entry point.
2. Replace the OpenAI-specific integration with a Google GenAI client path.
3. Implement and validate the Google-based transcript cleanup and final report
   synthesis stages.
4. Determine the best transcript-generation path available with the current
   Google setup and integrate it into the canonical workflow.
5. Regenerate at least one real TwinCAT/TestRig video through the adapted
   Google-based pipeline.
6. Update the repository usage documentation so the canonical workflow matches
   the user's available provider path.
