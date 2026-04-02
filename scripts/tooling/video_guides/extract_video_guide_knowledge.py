""" Extract High-Quality Knowledge From TwinCAT Video Guides """

from __future__ import annotations

# Disable Bytecode Cache Writes
import sys
sys.dont_write_bytecode = True

# Import Python Utilities
import argparse
import json
import os
import subprocess
import time
import warnings
from dataclasses import asdict
from dataclasses import dataclass
from pathlib import Path

import imageio_ffmpeg
from google import genai

try:
    from requests import RequestsDependencyWarning
except ImportError:
    RequestsDependencyWarning = Warning

PROJECT_PATH = Path(__file__).resolve().parents[3]
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

from scripts.tooling.video_guides.analyze_video_guides import TERM_PATTERN_MAP
from scripts.tooling.video_guides.analyze_video_guides import collapse_whitespace
from scripts.tooling.video_guides.analyze_video_guides import ensure_directory
from scripts.tooling.video_guides.analyze_video_guides import extract_best_ocr_text
from scripts.tooling.video_guides.analyze_video_guides import extract_video_metadata
from scripts.tooling.video_guides.analyze_video_guides import format_seconds
from scripts.tooling.video_guides.analyze_video_guides import match_companion_notes
from scripts.tooling.video_guides.analyze_video_guides import collect_companion_note_list
from scripts.tooling.video_guides.analyze_video_guides import collect_runtime_capability_map
from scripts.tooling.video_guides.analyze_video_guides import collect_video_file_path_list
from scripts.tooling.lan_ai.lan_ai_node_client import fetch_lm_studio_model_name_list
from scripts.tooling.lan_ai.lan_ai_node_client import run_lm_studio_chat_completion
from scripts.tooling.lan_ai.lan_ai_node_client import LanTranscriptSegment
from scripts.tooling.lan_ai.lan_ai_node_client import run_region_ocr_via_lan_ai_node
from scripts.tooling.lan_ai.lan_ai_node_client import transcribe_audio_via_lan_ai_node
from scripts.tooling.lan_ai.lan_ai_node_client import transcribe_audio_via_lan_ai_node_with_segments

try:
    import cv2
except ImportError:
    cv2 = None

DEFAULT_VIDEO_GUIDE_ROOT = PROJECT_PATH / "reference" / "video_guides" / "source_bundle"
DEFAULT_ANALYSIS_ROOT = PROJECT_PATH / ".temp" / "video_guides" / "_analysis_hq"
DEFAULT_REPORT_ROOT = PROJECT_PATH / "doc" / "reference_codes" / "video_guides"
DEFAULT_TRANSCRIPT_MODEL = "gemini-2.5-flash"
DEFAULT_TRANSCRIPT_CLEANUP_MODEL = "gemini-2.5-flash"
DEFAULT_REPORT_MODEL = "gemini-2.5-flash"
DEFAULT_AUDIO_CHUNK_SECONDS = 300
DEFAULT_FRAME_PROBES_PER_CHUNK = 3
DEFAULT_MAX_SNAPSHOTS = 6
DEFAULT_LM_STUDIO_MAX_CLEANUP_CHUNKS_PER_REQUEST = 1
DEFAULT_LM_STUDIO_MAX_CLEANUP_CHUNK_CHARACTERS = 900
DEFAULT_LM_STUDIO_MAX_REPORT_CHUNK_CHARACTERS = 320
DEFAULT_TRANSCRIPT_PROVIDER = "google"
DEFAULT_CLEANUP_PROVIDER = "google"
DEFAULT_REPORT_PROVIDER = "google"
DEFAULT_OCR_PROVIDER = "local"
DEFAULT_TRANSCRIPT_LANGUAGE = "it"
DEFAULT_OCR_LANGUAGE = "en"
DEFAULT_LAN_AI_BASE_URL = os.environ.get("STANDARDML_LAN_AI_BASE_URL", "").strip()
DEFAULT_LAN_AI_TOKEN = os.environ.get("STANDARDML_LAN_AI_TOKEN", "").strip()
DEFAULT_LM_STUDIO_BASE_URL = os.environ.get(
    "LM_STUDIO_LOCAL_URL",
    os.environ.get("LM_STUDIO_BASE_URL", os.environ.get("STANDARDML_LM_STUDIO_BASE_URL", "http://127.0.0.1:1234")),
).strip()
DEFAULT_LM_STUDIO_API_KEY = os.environ.get("LM_STUDIO_API_KEY", os.environ.get("STANDARDML_LM_STUDIO_API_KEY", "lm-studio")).strip()
VIDEO_SUFFIXES = {".mp4", ".mkv", ".mov", ".avi", ".m4v"}

warnings.filterwarnings("ignore", category=RequestsDependencyWarning)


@dataclass
class TranscriptChunk:

    """ Store Transcript Chunk """

    chunk_index: int
    start_seconds: float
    end_seconds: float
    audio_chunk_path: str
    raw_transcript_text: str
    corrected_transcript_text: str
    relevance_score: float


@dataclass
class SnapshotRecord:

    """ Store Snapshot Record """

    timestamp_seconds: float
    frame_path: str
    ocr_text: str
    ocr_quality_score: float
    ocr_region_name: str
    transcript_excerpt: str
    selection_reason: str
    combined_score: float


@dataclass
class TranscriptExtractionResult:

    """ Store Transcript Extraction Result """

    raw_transcript_text: str
    transcript_segment_list: list[LanTranscriptSegment]


@dataclass
class WorkflowRuntimeState:

    """ Store Workflow Runtime State """

    video_count: int
    current_video_index: int = 0
    lm_studio_model_name_list: list[str] | None = None
    cleanup_model_name: str = ""
    report_model_name: str = ""


def build_argument_parser() -> argparse.ArgumentParser:

    """ Build Argument Parser """

    argument_parser = argparse.ArgumentParser(
        description="Run the high-quality three-stage TwinCAT/TestRig video knowledge-extraction workflow.",
    )
    argument_parser.add_argument("--input-root", default=str(DEFAULT_VIDEO_GUIDE_ROOT), help="Video-guide source root.")
    argument_parser.add_argument("--analysis-root", default=str(DEFAULT_ANALYSIS_ROOT), help="Intermediate analysis root.")
    argument_parser.add_argument("--report-root", default=str(DEFAULT_REPORT_ROOT), help="Canonical report root.")
    argument_parser.add_argument("--video-filter", default="", help="Optional case-insensitive file-name filter.")
    argument_parser.add_argument("--limit-videos", type=int, default=0, help="Optional maximum number of videos.")
    argument_parser.add_argument("--transcript-provider", choices=["google", "lan"], default=DEFAULT_TRANSCRIPT_PROVIDER, help="Backend used for raw transcript extraction.")
    argument_parser.add_argument("--cleanup-provider", choices=["google", "lmstudio"], default=DEFAULT_CLEANUP_PROVIDER, help="Backend used for transcript cleanup and segmentation.")
    argument_parser.add_argument("--report-provider", choices=["google", "lmstudio"], default=DEFAULT_REPORT_PROVIDER, help="Backend used for final report synthesis.")
    argument_parser.add_argument("--ocr-provider", choices=["local", "lan"], default=DEFAULT_OCR_PROVIDER, help="Backend used for OCR during snapshot selection.")
    argument_parser.add_argument("--transcript-model", default=DEFAULT_TRANSCRIPT_MODEL, help="Primary transcription model.")
    argument_parser.add_argument("--cleanup-model", default=DEFAULT_TRANSCRIPT_CLEANUP_MODEL, help="Model used to correct transcript chunks and synthesize reports.")
    argument_parser.add_argument("--report-model", default=DEFAULT_REPORT_MODEL, help="Model used to synthesize the final per-video report.")
    argument_parser.add_argument("--transcript-language", default=DEFAULT_TRANSCRIPT_LANGUAGE, help="Spoken language for transcript extraction.")
    argument_parser.add_argument("--ocr-language", default=DEFAULT_OCR_LANGUAGE, help="Language code used by the OCR backend.")
    argument_parser.add_argument("--lan-ai-base-url", default=DEFAULT_LAN_AI_BASE_URL, help="Base URL for the LAN AI node service.")
    argument_parser.add_argument("--lan-ai-token", default=DEFAULT_LAN_AI_TOKEN, help="Bearer token for the LAN AI node service.")
    argument_parser.add_argument("--lm-studio-base-url", default=DEFAULT_LM_STUDIO_BASE_URL, help="Base URL for the LM Studio OpenAI-compatible server.")
    argument_parser.add_argument("--lm-studio-api-key", default=DEFAULT_LM_STUDIO_API_KEY, help="API key or token for LM Studio.")
    argument_parser.add_argument("--audio-chunk-seconds", type=int, default=DEFAULT_AUDIO_CHUNK_SECONDS, help="Duration of each audio chunk sent to the transcription API.")
    argument_parser.add_argument("--frame-probes-per-chunk", type=int, default=DEFAULT_FRAME_PROBES_PER_CHUNK, help="Number of frame probes evaluated inside each transcript chunk.")
    argument_parser.add_argument("--max-snapshots", type=int, default=DEFAULT_MAX_SNAPSHOTS, help="Maximum number of canonical snapshots copied into the final report assets.")
    argument_parser.add_argument("--lmstudio-max-cleanup-chunks-per-request", type=int, default=DEFAULT_LM_STUDIO_MAX_CLEANUP_CHUNKS_PER_REQUEST, help="Maximum number of transcript chunks packed into one LM Studio cleanup request.")
    argument_parser.add_argument("--lmstudio-max-cleanup-chunk-characters", type=int, default=DEFAULT_LM_STUDIO_MAX_CLEANUP_CHUNK_CHARACTERS, help="Maximum number of raw transcript characters retained per chunk inside one LM Studio cleanup request.")
    argument_parser.add_argument("--lmstudio-max-report-chunk-characters", type=int, default=DEFAULT_LM_STUDIO_MAX_REPORT_CHUNK_CHARACTERS, help="Maximum number of characters retained per transcript chunk when building LM Studio report prompts.")
    argument_parser.add_argument("--force", action="store_true", help="Recompute intermediate artifacts.")

    return argument_parser


def parse_command_line_arguments() -> argparse.Namespace:

    """ Parse Command-Line Arguments """

    return build_argument_parser().parse_args()


def require_google_client() -> genai.Client:

    """ Require Google Client """

    api_key = os.environ.get("GOOGLE_API_KEY", "").strip()
    assert api_key, "GOOGLE_API_KEY is required for the high-quality transcript workflow."
    return genai.Client(api_key=api_key)


def maybe_create_google_client(parsed_arguments: argparse.Namespace) -> genai.Client | None:

    """ Maybe Create Google Client """

    if any(
        provider_name == "google"
        for provider_name in [
            parsed_arguments.transcript_provider,
            parsed_arguments.cleanup_provider,
            parsed_arguments.report_provider,
        ]
    ):
        return require_google_client()

    return None


def require_lan_ai_base_url(parsed_arguments: argparse.Namespace) -> str:

    """ Require LAN AI Base URL """

    lan_ai_base_url = parsed_arguments.lan_ai_base_url.strip()
    assert lan_ai_base_url, "LAN AI base URL is required for transcript or OCR LAN providers."
    return lan_ai_base_url


def require_lm_studio_base_url(parsed_arguments: argparse.Namespace) -> str:

    """ Require LM Studio Base URL """

    lm_studio_base_url = parsed_arguments.lm_studio_base_url.strip()
    assert lm_studio_base_url, "LM Studio base URL is required for LM Studio cleanup or report providers."
    return lm_studio_base_url


def print_banner(title: str) -> None:

    """ Print Banner """

    print("")
    print("=" * 96)
    print(title)
    print("=" * 96)


def print_status(label: str, value: object) -> None:

    """ Print Status """

    print(f"[INFO] {label:<28} : {value}", flush=True)


def print_step(message: str) -> None:

    """ Print Step """

    print(f"[STEP] {message}", flush=True)


def print_done(message: str) -> None:

    """ Print Done """

    print(f"[DONE] {message}", flush=True)


def clip_text_for_prompt(raw_text: str, max_characters: int) -> str:

    """ Clip Text For Prompt """

    normalized_text = collapse_whitespace(raw_text)
    if len(normalized_text) <= max_characters:
        return normalized_text

    clipped_text = normalized_text[:max_characters].rstrip(" ,;:")
    return f"{clipped_text} ..."


def choose_best_lm_studio_model(
    requested_model_name: str,
    available_model_name_list: list[str],
) -> tuple[str, str]:

    """ Choose Best LM Studio Model """

    normalized_requested_model_name = requested_model_name.strip()
    if not available_model_name_list:
        return normalized_requested_model_name, "unverified"

    if normalized_requested_model_name in available_model_name_list:
        return normalized_requested_model_name, "exact"

    generative_model_name_list = [
        model_name
        for model_name in available_model_name_list
        if "embedding" not in model_name.lower()
    ]
    if not generative_model_name_list:
        return normalized_requested_model_name, "unverified"

    requested_token_list = [
        token
        for token in normalized_requested_model_name.lower().replace("/", " ").replace("-", " ").split()
        if token
    ]
    for available_model_name in generative_model_name_list:
        available_model_lower = available_model_name.lower()
        if any(requested_token in available_model_lower for requested_token in requested_token_list):
            return available_model_name, "fallback-family"

    return generative_model_name_list[0], "fallback-first-generative"


def resolve_lm_studio_model_arguments(parsed_arguments: argparse.Namespace, runtime_state: WorkflowRuntimeState) -> None:

    """ Resolve LM Studio Model Arguments """

    lm_studio_needed = any(
        provider_name == "lmstudio"
        for provider_name in [parsed_arguments.cleanup_provider, parsed_arguments.report_provider]
    )
    if not lm_studio_needed:
        return

    available_model_name_list = fetch_lm_studio_model_name_list(
        lm_studio_base_url=require_lm_studio_base_url(parsed_arguments),
        api_key=parsed_arguments.lm_studio_api_key,
    )
    runtime_state.lm_studio_model_name_list = available_model_name_list
    available_model_text = ", ".join(available_model_name_list) if available_model_name_list else "<unavailable>"
    print_status("LM Studio Models", available_model_text)

    if parsed_arguments.cleanup_provider == "lmstudio":
        resolved_cleanup_model_name, cleanup_reason = choose_best_lm_studio_model(
            requested_model_name=parsed_arguments.cleanup_model,
            available_model_name_list=available_model_name_list,
        )
        if resolved_cleanup_model_name != parsed_arguments.cleanup_model:
            print_status("Cleanup Model Requested", parsed_arguments.cleanup_model)
            print_status("Cleanup Model Resolved", f"{resolved_cleanup_model_name} ({cleanup_reason})")
            parsed_arguments.cleanup_model = resolved_cleanup_model_name

    if parsed_arguments.report_provider == "lmstudio":
        resolved_report_model_name, report_reason = choose_best_lm_studio_model(
            requested_model_name=parsed_arguments.report_model,
            available_model_name_list=available_model_name_list,
        )
        if resolved_report_model_name != parsed_arguments.report_model:
            print_status("Report Model Requested", parsed_arguments.report_model)
            print_status("Report Model Resolved", f"{resolved_report_model_name} ({report_reason})")
            parsed_arguments.report_model = resolved_report_model_name

    runtime_state.cleanup_model_name = parsed_arguments.cleanup_model
    runtime_state.report_model_name = parsed_arguments.report_model


def get_ffmpeg_executable_path() -> str:

    """ Get FFmpeg Executable Path """

    return imageio_ffmpeg.get_ffmpeg_exe()


def run_subprocess_command(command_argument_list: list[str]) -> None:

    """ Run Subprocess Command """

    completed_process = subprocess.run(
        command_argument_list,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    assert completed_process.returncode == 0, (
        f"Command failed | {' '.join(command_argument_list)}\n"
        f"STDOUT:\n{completed_process.stdout}\nSTDERR:\n{completed_process.stderr}"
    )


def slugify_text(raw_text: str) -> str:

    """ Slugify Text """

    return "".join(character.lower() if character.isalnum() else "_" for character in raw_text).strip("_")


def extract_audio_track(video_file_path: Path, output_audio_path: Path, force_recompute: bool) -> None:

    """ Extract Audio Track """

    if output_audio_path.exists() and not force_recompute:
        return

    ensure_directory(output_audio_path.parent)
    ffmpeg_executable_path = get_ffmpeg_executable_path()
    run_subprocess_command(
        [
            ffmpeg_executable_path,
            "-y",
            "-i",
            str(video_file_path),
            "-vn",
            "-ac",
            "1",
            "-ar",
            "16000",
            "-b:a",
            "32k",
            str(output_audio_path),
        ]
    )


def split_audio_track(audio_file_path: Path, chunk_directory: Path, chunk_seconds: int, force_recompute: bool) -> list[Path]:

    """ Split Audio Track """

    ensure_directory(chunk_directory)
    chunk_file_path_list = sorted(chunk_directory.glob("chunk_*.mp3"))
    if chunk_file_path_list and not force_recompute:
        return chunk_file_path_list

    for existing_chunk_file_path in chunk_directory.glob("chunk_*.mp3"):
        existing_chunk_file_path.unlink()

    ffmpeg_executable_path = get_ffmpeg_executable_path()
    run_subprocess_command(
        [
            ffmpeg_executable_path,
            "-y",
            "-i",
            str(audio_file_path),
            "-f",
            "segment",
            "-segment_time",
            str(chunk_seconds),
            "-c",
            "copy",
            str(chunk_directory / "chunk_%03d.mp3"),
        ]
    )

    return sorted(chunk_directory.glob("chunk_*.mp3"))


def transcribe_full_audio(
    google_client: genai.Client | None,
    audio_file_path: Path,
    parsed_arguments: argparse.Namespace,
) -> TranscriptExtractionResult:

    """ Transcribe Full Audio """

    if parsed_arguments.transcript_provider == "lan":
        raw_transcript_text, transcript_segment_list = transcribe_audio_via_lan_ai_node_with_segments(
            audio_file_path=audio_file_path,
            lan_ai_base_url=require_lan_ai_base_url(parsed_arguments),
            bearer_token=parsed_arguments.lan_ai_token,
            transcript_model=parsed_arguments.transcript_model,
            transcript_language=parsed_arguments.transcript_language,
        )
        return TranscriptExtractionResult(
            raw_transcript_text=raw_transcript_text,
            transcript_segment_list=transcript_segment_list,
        )

    assert google_client is not None, "Google client is required for Google transcript provider."
    uploaded_file = google_client.files.upload(file=str(audio_file_path))
    try:
        prompt_text = (
            "Trascrivi integralmente questo audio in italiano. "
            "Si tratta di una video guida tecnica su TwinCAT, Beckhoff, TestRig, "
            "FB_Predict, ML_Transmission_Error, Predict_ML, TE_Calc, DataValid, "
            "temperatura, coppia, velocita, XML, ONNX, Matlab e simulazione. "
            "Restituisci solo la trascrizione continua del parlato, senza commenti aggiuntivi."
        )
        response = google_client.models.generate_content(
            model=parsed_arguments.transcript_model,
            contents=[prompt_text, uploaded_file],
        )
        return TranscriptExtractionResult(
            raw_transcript_text=collapse_whitespace(response.text),
            transcript_segment_list=[],
        )
    finally:
        try:
            google_client.files.delete(name=uploaded_file.name)
        except Exception:
            pass


def generate_text_response(
    google_client: genai.Client | None,
    parsed_arguments: argparse.Namespace,
    provider_name: str,
    model_name: str,
    prompt_text: str,
    preserve_formatting: bool = False,
) -> str:

    """ Generate Text Response """

    if provider_name == "lmstudio":
        prompt_character_count = len(prompt_text)
        print_status("LM Studio Request", f"model={model_name} | chars={prompt_character_count}")
        return run_lm_studio_chat_completion(
            lm_studio_base_url=require_lm_studio_base_url(parsed_arguments),
            api_key=parsed_arguments.lm_studio_api_key,
            model_name=model_name,
            prompt_text=prompt_text,
            preserve_formatting=preserve_formatting,
        )

    assert google_client is not None, "Google client is required for Google text generation."
    response = google_client.models.generate_content(
        model=model_name,
        contents=prompt_text,
    )
    response_text = response.text.strip() if preserve_formatting else collapse_whitespace(response.text)
    return response_text


def transcribe_audio_chunk(google_client: genai.Client, chunk_file_path: Path, transcript_model: str) -> str:

    """ Transcribe Audio Chunk """

    uploaded_file = google_client.files.upload(file=str(chunk_file_path))
    try:
        prompt_text = (
            "Trascrivi integralmente questo audio in italiano. "
            "Si tratta di una video guida tecnica su TwinCAT, Beckhoff, TestRig, "
            "FB_Predict, ML_Transmission_Error, Predict_ML, TE_Calc, DataValid, "
            "temperatura, coppia, velocita, XML, ONNX, Matlab e simulazione. "
            "Restituisci solo la trascrizione continua del parlato, senza commenti aggiuntivi."
        )
        response = google_client.models.generate_content(
            model=transcript_model,
            contents=[prompt_text, uploaded_file],
        )
        return collapse_whitespace(response.text)
    finally:
        try:
            google_client.files.delete(name=uploaded_file.name)
        except Exception:
            pass


def correct_transcript_chunk_list(
    google_client: genai.Client | None,
    parsed_arguments: argparse.Namespace,
    cleanup_model: str,
    transcript_chunk_list: list[TranscriptChunk],
) -> list[str]:

    """ Correct Transcript Chunk List """

    corrected_text_by_index: dict[int, str] = {}
    max_chunks_per_request = max(1, int(parsed_arguments.lmstudio_max_cleanup_chunks_per_request))
    chunk_batch_size = max_chunks_per_request if parsed_arguments.cleanup_provider == "lmstudio" else len(transcript_chunk_list)
    max_cleanup_chunk_characters = max(240, int(parsed_arguments.lmstudio_max_cleanup_chunk_characters))

    for batch_start_index in range(0, len(transcript_chunk_list), chunk_batch_size):
        transcript_chunk_batch = transcript_chunk_list[batch_start_index:batch_start_index + chunk_batch_size]
        raw_chunk_payload = [
            {
                "chunk_index": transcript_chunk.chunk_index,
                "start_time": format_seconds(transcript_chunk.start_seconds),
                "end_time": format_seconds(transcript_chunk.end_seconds),
                "raw_transcript_text": (
                    clip_text_for_prompt(transcript_chunk.raw_transcript_text, max_cleanup_chunk_characters)
                    if parsed_arguments.cleanup_provider == "lmstudio"
                    else transcript_chunk.raw_transcript_text
                ),
            }
            for transcript_chunk in transcript_chunk_batch
        ]
        if parsed_arguments.cleanup_provider == "lmstudio":
            cleanup_prompt = f"""
Correggi una trascrizione tecnica italiana rumorosa.

Regole:
- Non inventare.
- Correggi solo dove il contesto e chiaro.
- Mantieni TwinCAT, Beckhoff, FB_Predict, ML_Transmission_Error, Predict_ML, TE_Calc, DataValid, ONNX, XML, Matlab.
- Un paragrafo italiano coerente per blocco.
- Restituisci solo JSON valido.

Schema:
{{"chunks":[{{"chunk_index":0,"corrected_transcript_text":"..."}}]}}

Blocchi:
{json.dumps(raw_chunk_payload, ensure_ascii=True, separators=(",", ":"))}
""".strip()
        else:
            cleanup_prompt = f"""
Sei un revisore linguistico-tecnico.

Ricevi una trascrizione automatica rumorosa di una video guida italiana su TwinCAT, Beckhoff, TestRig e machine learning.
Devi riscrivere ogni blocco in italiano corretto, lessicalmente e grammaticalmente coerente, mantenendo solo il contenuto che si puo inferire con ragionevole confidenza dal testo ricevuto.

Regole:
- Non inventare contenuto non supportato.
- Correggi parole tecniche quando il contesto lo rende chiaro.
- Mantieni identificatori tecnici rilevanti come TwinCAT, Beckhoff, FB_Predict, ML_Transmission_Error, Predict_ML, TE_Calc, DataValid, ONNX, XML, Matlab.
- Mantieni la separazione per blocchi temporali.
- Per ogni blocco restituisci un solo paragrafo coerente in italiano.
- Restituisci solo JSON valido.

Schema JSON richiesto:
{{
  "chunks": [
    {{
      "chunk_index": 0,
      "corrected_transcript_text": "..."
    }}
  ]
}}

Trascrizione grezza per blocchi:
{json.dumps(raw_chunk_payload, ensure_ascii=True, indent=2)}
""".strip()

        batch_end_index = batch_start_index + len(transcript_chunk_batch) - 1
        print_step(
            "Cleanup Transcript Chunks "
            f"| batch={batch_start_index}-{batch_end_index} "
            f"| provider={parsed_arguments.cleanup_provider} "
            f"| model={cleanup_model}"
        )

        response_text = generate_text_response(
            google_client=google_client,
            parsed_arguments=parsed_arguments,
            provider_name=parsed_arguments.cleanup_provider,
            model_name=cleanup_model,
            prompt_text=cleanup_prompt,
        )
        response_text = response_text.strip()
        json_start_index = response_text.find("{")
        json_end_index = response_text.rfind("}")
        assert json_start_index >= 0 and json_end_index >= 0, "Cleanup model did not return JSON."
        cleaned_payload = json.loads(response_text[json_start_index:json_end_index + 1])

        corrected_text_by_index.update(
            {
                int(chunk_map["chunk_index"]): collapse_whitespace(chunk_map["corrected_transcript_text"])
                for chunk_map in cleaned_payload.get("chunks", [])
                if str(chunk_map.get("corrected_transcript_text", "")).strip()
            }
        )

    corrected_text_list: list[str] = []
    for transcript_chunk in transcript_chunk_list:
        corrected_text_list.append(
            corrected_text_by_index.get(
                transcript_chunk.chunk_index,
                collapse_whitespace(transcript_chunk.raw_transcript_text),
            )
        )

    return corrected_text_list


def build_transcript_chunk_list_from_lan_segments(
    transcript_segment_list: list[LanTranscriptSegment],
    audio_file_path: Path,
    duration_seconds: float,
    target_chunk_seconds: int,
) -> list[TranscriptChunk]:

    """ Build Transcript Chunk List From LAN Segments """

    if not transcript_segment_list:
        return []

    transcript_chunk_list: list[TranscriptChunk] = []
    current_chunk_segment_text_list: list[str] = []
    current_chunk_start_seconds = transcript_segment_list[0].start_seconds
    current_chunk_end_seconds = transcript_segment_list[0].end_seconds
    current_chunk_index = 0

    for transcript_segment in transcript_segment_list:
        current_chunk_duration = transcript_segment.end_seconds - current_chunk_start_seconds
        should_flush_chunk = (
            current_chunk_segment_text_list
            and current_chunk_duration >= float(target_chunk_seconds)
        )
        if should_flush_chunk:
            raw_chunk_text = collapse_whitespace(" ".join(current_chunk_segment_text_list))
            transcript_chunk_list.append(
                TranscriptChunk(
                    chunk_index=current_chunk_index,
                    start_seconds=current_chunk_start_seconds,
                    end_seconds=current_chunk_end_seconds,
                    audio_chunk_path=audio_file_path.relative_to(PROJECT_PATH).as_posix(),
                    raw_transcript_text=raw_chunk_text,
                    corrected_transcript_text="",
                    relevance_score=0.0,
                )
            )
            current_chunk_index += 1
            current_chunk_segment_text_list = []
            current_chunk_start_seconds = transcript_segment.start_seconds

        current_chunk_segment_text_list.append(transcript_segment.text)
        current_chunk_end_seconds = max(current_chunk_end_seconds, transcript_segment.end_seconds)

    if current_chunk_segment_text_list:
        raw_chunk_text = collapse_whitespace(" ".join(current_chunk_segment_text_list))
        transcript_chunk_list.append(
            TranscriptChunk(
                chunk_index=current_chunk_index,
                start_seconds=current_chunk_start_seconds,
                end_seconds=min(duration_seconds or current_chunk_end_seconds, current_chunk_end_seconds),
                audio_chunk_path=audio_file_path.relative_to(PROJECT_PATH).as_posix(),
                raw_transcript_text=raw_chunk_text,
                corrected_transcript_text="",
                relevance_score=0.0,
            )
        )

    for transcript_chunk_index, transcript_chunk in enumerate(transcript_chunk_list):
        transcript_chunk.chunk_index = transcript_chunk_index
        if transcript_chunk_index < len(transcript_chunk_list) - 1:
            transcript_chunk.end_seconds = max(
                transcript_chunk.start_seconds,
                min(transcript_chunk.end_seconds, transcript_chunk_list[transcript_chunk_index + 1].start_seconds),
            )
        else:
            transcript_chunk.end_seconds = max(
                transcript_chunk.start_seconds,
                min(float(duration_seconds or transcript_chunk.end_seconds), transcript_chunk.end_seconds),
            )

    return transcript_chunk_list


def correct_and_segment_full_transcript(
    google_client: genai.Client | None,
    parsed_arguments: argparse.Namespace,
    cleanup_model: str,
    raw_transcript_text: str,
    duration_seconds: float,
    target_chunk_seconds: int,
) -> list[TranscriptChunk]:

    """ Correct And Segment Full Transcript """

    approximate_chunk_count = max(1, int(round(duration_seconds / max(float(target_chunk_seconds), 1.0))))
    cleanup_prompt = f"""
Sei un revisore linguistico-tecnico.

Ricevi la trascrizione automatica rumorosa dell'intero audio di una video guida italiana su TwinCAT, Beckhoff, TestRig e machine learning.
Devi:
1. correggere lessico, grammatica e terminologia tecnica;
2. suddividere il discorso in blocchi temporali coerenti;
3. assegnare a ogni blocco un intervallo temporale approssimativo ma plausibile, coerente con la durata totale.

Regole:
- Non inventare contenuto non supportato.
- Correggi parole tecniche quando il contesto lo rende chiaro.
- Mantieni identificatori tecnici rilevanti come TwinCAT, Beckhoff, FB_Predict, ML_Transmission_Error, Predict_ML, TE_Calc, DataValid, ONNX, XML, Matlab.
- I blocchi devono coprire l'intero video senza sovrapposizioni e in ordine crescente.
- Ogni blocco deve contenere un singolo paragrafo coerente in italiano.
- Durata totale video: {duration_seconds:.3f} secondi.
- Numero di blocchi desiderato: circa {approximate_chunk_count}.
- Restituisci solo JSON valido.

Schema JSON richiesto:
{{
  "chunks": [
    {{
      "chunk_index": 0,
      "start_seconds": 0.0,
      "end_seconds": 300.0,
      "corrected_transcript_text": "..."
    }}
  ]
}}

Trascrizione grezza completa:
{raw_transcript_text}
""".strip()

    response_text = generate_text_response(
        google_client=google_client,
        parsed_arguments=parsed_arguments,
        provider_name=parsed_arguments.cleanup_provider,
        model_name=cleanup_model,
        prompt_text=cleanup_prompt,
    )
    response_text = response_text.strip()
    json_start_index = response_text.find("{")
    json_end_index = response_text.rfind("}")
    assert json_start_index >= 0 and json_end_index >= 0, "Cleanup model did not return JSON."
    cleaned_payload = json.loads(response_text[json_start_index:json_end_index + 1])

    transcript_chunk_list: list[TranscriptChunk] = []
    cleaned_chunk_list = cleaned_payload.get("chunks", [])
    assert cleaned_chunk_list, "Cleanup model returned no transcript chunks."

    for cleaned_chunk_map in cleaned_chunk_list:
        chunk_index = int(cleaned_chunk_map["chunk_index"])
        start_seconds = max(0.0, float(cleaned_chunk_map["start_seconds"]))
        end_seconds = min(float(duration_seconds), float(cleaned_chunk_map["end_seconds"]))
        if transcript_chunk_list and start_seconds < transcript_chunk_list[-1].end_seconds:
            start_seconds = transcript_chunk_list[-1].end_seconds
        if end_seconds <= start_seconds:
            end_seconds = min(float(duration_seconds), start_seconds + max(float(target_chunk_seconds), 1.0))

        corrected_transcript_text = collapse_whitespace(cleaned_chunk_map["corrected_transcript_text"])
        transcript_chunk_list.append(
            TranscriptChunk(
                chunk_index=chunk_index,
                start_seconds=start_seconds,
                end_seconds=end_seconds,
                audio_chunk_path="",
                raw_transcript_text="",
                corrected_transcript_text=corrected_transcript_text,
                relevance_score=compute_text_relevance_score(corrected_transcript_text),
            )
        )

    transcript_chunk_list = sorted(transcript_chunk_list, key=lambda item: item.start_seconds)
    for transcript_chunk_index, transcript_chunk in enumerate(transcript_chunk_list):
        transcript_chunk.chunk_index = transcript_chunk_index
        if transcript_chunk_index < len(transcript_chunk_list) - 1:
            transcript_chunk.end_seconds = max(
                transcript_chunk.start_seconds,
                min(transcript_chunk.end_seconds, transcript_chunk_list[transcript_chunk_index + 1].start_seconds),
            )
        else:
            transcript_chunk.end_seconds = float(duration_seconds)

    return transcript_chunk_list


def compute_text_relevance_score(raw_text: str) -> float:

    """ Compute Text Relevance Score """

    collapsed_text = collapse_whitespace(raw_text)
    if not collapsed_text:
        return 0.0

    matched_term_count = sum(1 for term_pattern in TERM_PATTERN_MAP.values() if term_pattern.search(collapsed_text))
    relevance_score = float(matched_term_count)

    if "task" in collapsed_text.lower() or "microsecond" in collapsed_text.lower():
        relevance_score += 2.0
    if "fb_predict" in collapsed_text.lower() or "predict" in collapsed_text.lower():
        relevance_score += 2.0
    if "xml" in collapsed_text.lower() or "onnx" in collapsed_text.lower():
        relevance_score += 1.5
    if "simul" in collapsed_text.lower():
        relevance_score += 1.0

    return relevance_score


def write_json_file(output_file_path: Path, payload: object) -> None:

    """ Write JSON File """

    ensure_directory(output_file_path.parent)
    output_file_path.write_text(json.dumps(payload, indent=2, ensure_ascii=True), encoding="utf-8")


def load_json_file(input_file_path: Path) -> object:

    """ Load JSON File """

    return json.loads(input_file_path.read_text(encoding="utf-8"))


def build_transcript_markdown(video_file_name: str, transcript_chunk_list: list[TranscriptChunk]) -> str:

    """ Build Transcript Markdown """

    markdown_line_list = [
        f"# {video_file_name} Transcript",
        "",
        "This transcript is the canonical cleaned Italian transcript for the video.",
        "",
    ]

    for transcript_chunk in transcript_chunk_list:
        markdown_line_list.append(
            f"## {format_seconds(transcript_chunk.start_seconds)} - {format_seconds(transcript_chunk.end_seconds)}"
        )
        markdown_line_list.append("")
        markdown_line_list.append(transcript_chunk.corrected_transcript_text)
        markdown_line_list.append("")

    return "\n".join(markdown_line_list).rstrip() + "\n"


def capture_frame(video_file_path: Path, timestamp_seconds: float, output_frame_path: Path) -> None:

    """ Capture Frame """

    assert cv2 is not None, "opencv-python-headless is required for snapshot extraction."
    ensure_directory(output_frame_path.parent)

    capture = cv2.VideoCapture(str(video_file_path))
    assert capture.isOpened(), f"Could not open video | {video_file_path}"
    capture.set(cv2.CAP_PROP_POS_MSEC, timestamp_seconds * 1000.0)
    read_success, frame_image = capture.read()
    capture.release()
    assert read_success, f"Could not capture frame at {timestamp_seconds:.3f}s"
    cv2.imwrite(str(output_frame_path), frame_image)


def infer_snapshot_reason(transcript_text: str, ocr_text: str) -> str:

    """ Infer Snapshot Reason """

    lowered_text = f"{transcript_text} {ocr_text}".lower()
    if "task" in lowered_text or "microsecond" in lowered_text:
        return "Task timing and inter-task communication evidence."
    if "fb_predict" in lowered_text or "predict_ml" in lowered_text or "ml_transmission_error" in lowered_text:
        return "TwinCAT prediction blocks and PLC-side ML orchestration evidence."
    if "xml" in lowered_text or "onnx" in lowered_text or "model manager" in lowered_text:
        return "Model export or Beckhoff model-manager workflow evidence."
    if "simul" in lowered_text or "matlab" in lowered_text or "te_calc" in lowered_text:
        return "Simulation and TE reconstruction workflow evidence."
    return "Relevant TwinCAT/TestRig screen for the deployment workflow."


def select_snapshot_record_list(
    video_file_path: Path,
    analysis_directory: Path,
    transcript_chunk_list: list[TranscriptChunk],
    capability_map: dict[str, object],
    parsed_arguments: argparse.Namespace,
    frame_probes_per_chunk: int,
    max_snapshots: int,
) -> list[SnapshotRecord]:

    """ Select Snapshot Record List """

    snapshot_candidate_list: list[SnapshotRecord] = []
    frames_directory = analysis_directory / "selected_frames"
    ensure_directory(frames_directory)

    for transcript_chunk in transcript_chunk_list:
        chunk_duration_seconds = max(transcript_chunk.end_seconds - transcript_chunk.start_seconds, 1.0)
        probe_ratio_list = [((probe_index + 1) / (frame_probes_per_chunk + 1)) for probe_index in range(frame_probes_per_chunk)]

        for probe_index, probe_ratio in enumerate(probe_ratio_list):
            timestamp_seconds = transcript_chunk.start_seconds + chunk_duration_seconds * probe_ratio
            frame_file_path = frames_directory / f"chunk_{transcript_chunk.chunk_index:03d}_probe_{probe_index:02d}_{int(timestamp_seconds):05d}.png"
            capture_frame(video_file_path, timestamp_seconds, frame_file_path)

            frame_image = cv2.imread(str(frame_file_path))
            if parsed_arguments.ocr_provider == "lan":
                ocr_text, ocr_quality_score, ocr_region_name, _ = run_region_ocr_via_lan_ai_node(
                    frame_image=frame_image,
                    lan_ai_base_url=require_lan_ai_base_url(parsed_arguments),
                    bearer_token=parsed_arguments.lan_ai_token,
                    ocr_language=parsed_arguments.ocr_language,
                )
            else:
                ocr_text, ocr_quality_score, ocr_region_name, _ = extract_best_ocr_text(frame_image, capability_map)
            combined_score = transcript_chunk.relevance_score + ocr_quality_score / 30.0
            selection_reason = infer_snapshot_reason(transcript_chunk.corrected_transcript_text, ocr_text)

            snapshot_candidate_list.append(
                SnapshotRecord(
                    timestamp_seconds=timestamp_seconds,
                    frame_path=frame_file_path.relative_to(PROJECT_PATH).as_posix(),
                    ocr_text=ocr_text,
                    ocr_quality_score=ocr_quality_score,
                    ocr_region_name=ocr_region_name,
                    transcript_excerpt=transcript_chunk.corrected_transcript_text[:260],
                    selection_reason=selection_reason,
                    combined_score=combined_score,
                )
            )

    sorted_snapshot_candidate_list = sorted(snapshot_candidate_list, key=lambda item: item.combined_score, reverse=True)
    selected_snapshot_record_list: list[SnapshotRecord] = []
    selected_bucket_set: set[int] = set()

    for snapshot_candidate in sorted_snapshot_candidate_list:
        bucket_index = int(snapshot_candidate.timestamp_seconds // max(DEFAULT_AUDIO_CHUNK_SECONDS, 1))
        if bucket_index in selected_bucket_set:
            continue
        selected_snapshot_record_list.append(snapshot_candidate)
        selected_bucket_set.add(bucket_index)
        if len(selected_snapshot_record_list) >= max_snapshots:
            break

    return selected_snapshot_record_list


def synthesize_report_markdown(
    google_client: genai.Client | None,
    parsed_arguments: argparse.Namespace,
    report_model: str,
    video_file_path: Path,
    transcript_chunk_list: list[TranscriptChunk],
    snapshot_record_list: list[SnapshotRecord],
    companion_note_excerpt_list: list[str],
) -> str:

    """ Synthesize Report Markdown """

    max_report_chunk_characters = max(80, int(parsed_arguments.lmstudio_max_report_chunk_characters))
    transcript_context = "\n".join(
        [
            (
                f"[{format_seconds(chunk.start_seconds)} - {format_seconds(chunk.end_seconds)}] "
                f"{chunk.corrected_transcript_text[:max_report_chunk_characters]}"
            )
            for chunk in transcript_chunk_list
        ]
    )
    snapshot_context = "\n".join(
        [
            f"- {format_seconds(snapshot.timestamp_seconds)} | reason={snapshot.selection_reason} | ocr_region={snapshot.ocr_region_name} | ocr_text={snapshot.ocr_text[:240]}"
            for snapshot in snapshot_record_list
        ]
    )
    companion_context = "\n".join([f"- {excerpt}" for excerpt in companion_note_excerpt_list]) or "- none"

    report_prompt = f"""
Write an English technical Markdown report for one TwinCAT/TestRig video guide.

Constraints:
- Use only the supplied evidence.
- Be specific and engineering-oriented.
- Do not include a raw OCR dump section.
- Mention the transcript file and the selected reference snapshots conceptually.
- Focus on what is useful for understanding TwinCAT ML export, PLC integration, Beckhoff tooling, TestRig structure, model input/output assumptions, and code-adaptation implications.

Required sections:
## Overview
## Why This Video Matters
## Main Technical Findings
## TwinCAT And Deployment Implications
## Reference Snapshots
## Open Questions Or Uncertain Points

Video: {video_file_path.name}

Companion notes:
{companion_context}

Transcript evidence:
{transcript_context}

Snapshot and OCR-assisted evidence:
{snapshot_context}
""".strip()

    print_step(
        "Synthesize Report "
        f"| provider={parsed_arguments.report_provider} "
        f"| model={report_model}"
    )
    report_body_text = generate_text_response(
        google_client=google_client,
        parsed_arguments=parsed_arguments,
        provider_name=parsed_arguments.report_provider,
        model_name=report_model,
        prompt_text=report_prompt,
        preserve_formatting=True,
    ).strip()
    if not report_body_text.startswith("# "):
        report_body_text = f"# {video_file_path.name} Report\n\n{report_body_text}"
    return report_body_text + "\n"


def process_single_video(
    google_client: genai.Client | None,
    video_file_path: Path,
    analysis_root: Path,
    report_root: Path,
    capability_map: dict[str, object],
    companion_note_list: list[object],
    parsed_arguments: argparse.Namespace,
    runtime_state: WorkflowRuntimeState,
) -> None:

    """ Process Single Video """

    runtime_state.current_video_index += 1
    print_banner(
        f"Video {runtime_state.current_video_index}/{runtime_state.video_count} | {video_file_path.name}"
    )

    video_slug = slugify_text(video_file_path.stem)
    analysis_directory = analysis_root / video_slug
    report_directory = report_root / video_slug
    asset_directory = report_directory / "assets"
    ensure_directory(analysis_directory)
    ensure_directory(report_directory)
    ensure_directory(asset_directory)

    metadata_map = extract_video_metadata(video_file_path)
    audio_file_path = analysis_directory / f"{video_slug}.mp3"
    raw_transcript_file_path = analysis_directory / "raw_full_transcript.txt"
    corrected_transcript_cache_path = analysis_directory / "corrected_transcript_cache.json"
    print_step("Extract Audio Track")
    extract_audio_track(video_file_path, audio_file_path, parsed_arguments.force)
    corrected_transcript_cache_map: dict[str, str] = {}

    if corrected_transcript_cache_path.exists() and not parsed_arguments.force:
        corrected_transcript_cache_map = {
            str(cache_key): str(cache_value)
            for cache_key, cache_value in dict(load_json_file(corrected_transcript_cache_path)).items()
        }
    raw_full_transcript_text = ""
    if raw_transcript_file_path.exists() and not parsed_arguments.force:
        raw_full_transcript_text = collapse_whitespace(raw_transcript_file_path.read_text(encoding="utf-8"))
    if not raw_full_transcript_text:
        print_step(
            "Transcribe Full Audio "
            f"| provider={parsed_arguments.transcript_provider} "
            f"| model={parsed_arguments.transcript_model}"
        )
        transcript_extraction_result = transcribe_full_audio(google_client, audio_file_path, parsed_arguments)
        raw_full_transcript_text = transcript_extraction_result.raw_transcript_text
        raw_transcript_file_path.write_text(raw_full_transcript_text + "\n", encoding="utf-8")
        print_done(f"Transcript Extracted | chars={len(raw_full_transcript_text)}")
    else:
        transcript_extraction_result = TranscriptExtractionResult(
            raw_transcript_text=raw_full_transcript_text,
            transcript_segment_list=[],
        )
        print_done(f"Loaded Cached Transcript | chars={len(raw_full_transcript_text)}")

    transcript_chunk_list: list[TranscriptChunk] = []
    if corrected_transcript_cache_map:
        print_step("Load Corrected Transcript Cache")
        for chunk_index_key, corrected_transcript_text in sorted(corrected_transcript_cache_map.items(), key=lambda item: item[0]):
            chunk_index = int(chunk_index_key)
            chunk_start_seconds = float(chunk_index * parsed_arguments.audio_chunk_seconds)
            chunk_end_seconds = min(
                chunk_start_seconds + float(parsed_arguments.audio_chunk_seconds),
                float(metadata_map["duration_seconds"] or (chunk_start_seconds + parsed_arguments.audio_chunk_seconds)),
            )
            transcript_chunk_list.append(
                TranscriptChunk(
                    chunk_index=chunk_index,
                    start_seconds=chunk_start_seconds,
                    end_seconds=chunk_end_seconds,
                    audio_chunk_path=audio_file_path.relative_to(PROJECT_PATH).as_posix(),
                    raw_transcript_text="",
                    corrected_transcript_text=corrected_transcript_text,
                    relevance_score=compute_text_relevance_score(corrected_transcript_text),
                )
            )
        print_done(f"Loaded Cached Chunks | count={len(transcript_chunk_list)}")
    else:
        if parsed_arguments.transcript_provider == "lan" and transcript_extraction_result.transcript_segment_list:
            print_step(
                "Build LAN Transcript Chunks "
                f"| segments={len(transcript_extraction_result.transcript_segment_list)} "
                f"| target_seconds={parsed_arguments.audio_chunk_seconds}"
            )
            transcript_chunk_list = build_transcript_chunk_list_from_lan_segments(
                transcript_segment_list=transcript_extraction_result.transcript_segment_list,
                audio_file_path=audio_file_path,
                duration_seconds=float(metadata_map["duration_seconds"] or 0.0),
                target_chunk_seconds=parsed_arguments.audio_chunk_seconds,
            )
            print_done(f"Built Transcript Chunks | count={len(transcript_chunk_list)}")
            corrected_text_list = correct_transcript_chunk_list(
                google_client=google_client,
                parsed_arguments=parsed_arguments,
                cleanup_model=parsed_arguments.cleanup_model,
                transcript_chunk_list=transcript_chunk_list,
            )
            for transcript_chunk, corrected_text in zip(transcript_chunk_list, corrected_text_list):
                transcript_chunk.corrected_transcript_text = corrected_text
                transcript_chunk.relevance_score = compute_text_relevance_score(corrected_text)
        else:
            print_step("Correct And Segment Full Transcript")
            transcript_chunk_list = correct_and_segment_full_transcript(
                google_client=google_client,
                parsed_arguments=parsed_arguments,
                cleanup_model=parsed_arguments.cleanup_model,
                raw_transcript_text=raw_full_transcript_text,
                duration_seconds=float(metadata_map["duration_seconds"] or 0.0),
                target_chunk_seconds=parsed_arguments.audio_chunk_seconds,
            )
            for transcript_chunk in transcript_chunk_list:
                transcript_chunk.audio_chunk_path = audio_file_path.relative_to(PROJECT_PATH).as_posix()
                transcript_chunk.raw_transcript_text = raw_full_transcript_text
        print_done(f"Prepared Transcript Chunks | count={len(transcript_chunk_list)}")
        corrected_transcript_cache_map = {
            f"{transcript_chunk.chunk_index:03d}": transcript_chunk.corrected_transcript_text
            for transcript_chunk in transcript_chunk_list
        }
        write_json_file(corrected_transcript_cache_path, corrected_transcript_cache_map)

    write_json_file(analysis_directory / "transcript_chunks.json", [asdict(chunk) for chunk in transcript_chunk_list])
    transcript_markdown = build_transcript_markdown(video_file_path.name, transcript_chunk_list)
    transcript_file_path = report_directory / f"{video_slug}_transcript.md"
    transcript_file_path.write_text(transcript_markdown, encoding="utf-8")

    print_step(
        "Select Reference Snapshots "
        f"| provider={parsed_arguments.ocr_provider} "
        f"| max_snapshots={parsed_arguments.max_snapshots}"
    )
    snapshot_record_list = select_snapshot_record_list(
        video_file_path=video_file_path,
        analysis_directory=analysis_directory,
        transcript_chunk_list=transcript_chunk_list,
        capability_map=capability_map,
        parsed_arguments=parsed_arguments,
        frame_probes_per_chunk=parsed_arguments.frame_probes_per_chunk,
        max_snapshots=parsed_arguments.max_snapshots,
    )
    print_done(f"Selected Reference Snapshots | count={len(snapshot_record_list)}")

    canonical_snapshot_record_list: list[SnapshotRecord] = []
    for snapshot_index, snapshot_record in enumerate(snapshot_record_list, start=1):
        source_frame_path = PROJECT_PATH / snapshot_record.frame_path
        destination_frame_path = asset_directory / f"reference_{snapshot_index:02d}_{format_seconds(snapshot_record.timestamp_seconds).replace(':', '-')}.png"
        destination_frame_path.write_bytes(source_frame_path.read_bytes())
        canonical_snapshot_record_list.append(
            SnapshotRecord(
                timestamp_seconds=snapshot_record.timestamp_seconds,
                frame_path=destination_frame_path.relative_to(PROJECT_PATH).as_posix(),
                ocr_text=snapshot_record.ocr_text,
                ocr_quality_score=snapshot_record.ocr_quality_score,
                ocr_region_name=snapshot_record.ocr_region_name,
                transcript_excerpt=snapshot_record.transcript_excerpt,
                selection_reason=snapshot_record.selection_reason,
                combined_score=snapshot_record.combined_score,
            )
        )

    write_json_file(analysis_directory / "snapshot_records.json", [asdict(snapshot) for snapshot in canonical_snapshot_record_list])

    matched_companion_note_list = match_companion_notes(video_file_path, companion_note_list)
    companion_note_excerpt_list = [collapse_whitespace(companion_note.text)[:260] for companion_note in matched_companion_note_list]
    report_markdown = synthesize_report_markdown(
        google_client=google_client,
        parsed_arguments=parsed_arguments,
        report_model=parsed_arguments.report_model,
        video_file_path=video_file_path,
        transcript_chunk_list=transcript_chunk_list,
        snapshot_record_list=canonical_snapshot_record_list,
        companion_note_excerpt_list=companion_note_excerpt_list,
    )
    report_file_path = report_directory / f"{video_slug}_report.md"
    report_file_path.write_text(report_markdown, encoding="utf-8")
    print_done(f"Saved Transcript Markdown | {transcript_file_path.relative_to(PROJECT_PATH).as_posix()}")
    print_done(f"Saved Report Markdown | {report_file_path.relative_to(PROJECT_PATH).as_posix()}")


def write_report_index(report_root: Path) -> None:

    """ Write Report Index """

    report_file_path_list = sorted(report_root.rglob("*_report.md"))
    transcript_file_path_list = sorted(report_root.rglob("*_transcript.md"))

    markdown_line_list = [
        "# Video Guide Reports",
        "",
        "This folder contains the canonical high-quality outputs generated from the",
        "TwinCAT/TestRig video-guide workflow.",
        "",
        "## Reports",
        "",
    ]
    for report_file_path in report_file_path_list:
        relative_report_path = report_file_path.relative_to(report_root).as_posix()
        markdown_line_list.append(f"- [{report_file_path.stem}]({relative_report_path})")

    markdown_line_list.extend(["", "## Corrected Transcripts", ""])
    for transcript_file_path in transcript_file_path_list:
        relative_transcript_path = transcript_file_path.relative_to(report_root).as_posix()
        markdown_line_list.append(f"- [{transcript_file_path.stem}]({relative_transcript_path})")

    (report_root / "README.md").write_text("\n".join(markdown_line_list).rstrip() + "\n", encoding="utf-8")


def main() -> int:

    """ Run High-Quality Video Workflow """

    parsed_arguments = parse_command_line_arguments()
    workflow_start_time = time.time()
    input_root = Path(parsed_arguments.input_root).resolve()
    analysis_root = Path(parsed_arguments.analysis_root).resolve()
    report_root = Path(parsed_arguments.report_root).resolve()
    assert input_root.exists(), f"Input root does not exist | {input_root}"
    ensure_directory(analysis_root)
    ensure_directory(report_root)

    google_client = maybe_create_google_client(parsed_arguments)
    companion_note_list = collect_companion_note_list(input_root)
    capability_map = collect_runtime_capability_map(
        disable_transcription=True,
        disable_frames=False,
        disable_ocr=parsed_arguments.ocr_provider != "local",
    )
    video_file_path_list = collect_video_file_path_list(input_root, parsed_arguments.video_filter, parsed_arguments.limit_videos)
    video_file_path_list = [video_file_path for video_file_path in video_file_path_list if video_file_path.suffix.lower() in VIDEO_SUFFIXES]
    assert video_file_path_list, "No video files matched the requested scope."

    runtime_state = WorkflowRuntimeState(video_count=len(video_file_path_list))

    print_banner("High-Quality TwinCAT Video Knowledge Extraction")
    print_status("Input Root", input_root)
    print_status("Analysis Root", analysis_root)
    print_status("Report Root", report_root)
    print_status("Video Filter", parsed_arguments.video_filter or "<none>")
    print_status("Transcript Provider", parsed_arguments.transcript_provider)
    print_status("Cleanup Provider", parsed_arguments.cleanup_provider)
    print_status("Report Provider", parsed_arguments.report_provider)
    print_status("OCR Provider", parsed_arguments.ocr_provider)
    print_status("Transcript Model", parsed_arguments.transcript_model)
    print_status("Cleanup Model", parsed_arguments.cleanup_model)
    print_status("Report Model", parsed_arguments.report_model)
    if parsed_arguments.transcript_provider == "lan" or parsed_arguments.ocr_provider == "lan":
        print_status("LAN AI Base URL", require_lan_ai_base_url(parsed_arguments))
    if parsed_arguments.cleanup_provider == "lmstudio" or parsed_arguments.report_provider == "lmstudio":
        print_status("LM Studio Base URL", require_lm_studio_base_url(parsed_arguments))
        resolve_lm_studio_model_arguments(parsed_arguments, runtime_state)
    print_status("Matched Videos", len(video_file_path_list))

    for video_file_path in video_file_path_list:
        process_single_video(
            google_client=google_client,
            video_file_path=video_file_path,
            analysis_root=analysis_root,
            report_root=report_root,
            capability_map=capability_map,
            companion_note_list=companion_note_list,
            parsed_arguments=parsed_arguments,
            runtime_state=runtime_state,
        )

    write_report_index(report_root)

    elapsed_seconds = time.time() - workflow_start_time
    print_banner("Workflow Summary")
    print_status("Processed Videos", len(video_file_path_list))
    print_status("Elapsed Seconds", f"{elapsed_seconds:.2f}")
    for video_file_path in video_file_path_list:
        print(f"[DONE] {video_file_path.name}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
