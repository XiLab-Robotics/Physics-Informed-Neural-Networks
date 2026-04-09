""" Serve Faster-Whisper And PaddleOCR Over LAN """

from __future__ import annotations

# Disable Bytecode Cache Writes
import sys
sys.dont_write_bytecode = True

# Import Python Utilities
import argparse
import errno
import os
import subprocess
import tempfile
import time
from pathlib import Path
from typing import Any

import uvicorn
from fastapi import FastAPI
from fastapi import File
from fastapi import Form
from fastapi import Header
from fastapi import HTTPException
from fastapi import UploadFile

PROJECT_PATH = Path(__file__).resolve().parents[3]
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

from scripts.tooling.video_guides.analyze_video_guides import collapse_whitespace

try:
    from faster_whisper import WhisperModel
except ImportError:
    WhisperModel = None

try:
    from paddleocr import PaddleOCR
except ImportError:
    PaddleOCR = None

DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 8765
DEFAULT_WHISPER_MODEL = "large-v3"
DEFAULT_WHISPER_DEVICE = "auto"
DEFAULT_WHISPER_COMPUTE_TYPE = "auto"
DEFAULT_BEARER_TOKEN = os.environ.get("STANDARDML_LAN_AI_TOKEN", "").strip()

WHISPER_MODEL_CACHE: dict[tuple[str, str, str], Any] = {}
PADDLE_OCR_CACHE: dict[str, Any] = {}


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse the LAN AI node server command-line arguments.

    Returns:
        Parsed command-line namespace for the LAN AI server entry point.
    """

    # Build Argument Parser
    argument_parser = argparse.ArgumentParser(
        description="Serve Faster-Whisper and PaddleOCR endpoints for the LAN AI node.",
    )
    argument_parser.add_argument("--host", default=DEFAULT_HOST, help="Host interface for the LAN AI node server.")
    argument_parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="TCP port for the LAN AI node server.")
    argument_parser.add_argument("--bearer-token", default=DEFAULT_BEARER_TOKEN, help="Optional bearer token required by the API.")
    argument_parser.add_argument("--whisper-model", default=DEFAULT_WHISPER_MODEL, help="Default Faster-Whisper model name.")
    argument_parser.add_argument("--whisper-device", default=DEFAULT_WHISPER_DEVICE, help="Faster-Whisper device, such as auto, cuda, or cpu.")
    argument_parser.add_argument("--whisper-compute-type", default=DEFAULT_WHISPER_COMPUTE_TYPE, help="Faster-Whisper compute type, such as auto, float16, int8, or int8_float16.")

    return argument_parser.parse_args()


def ensure_authorized(authorization_header: str | None, expected_bearer_token: str) -> None:

    """Validate the optional bearer token for one request.

    Args:
        authorization_header: Incoming `Authorization` header value.
        expected_bearer_token: Configured expected bearer token.

    Raises:
        HTTPException: If bearer-token authorization is enabled and the
            provided header does not match.
    """

    # Skip Authorization When Disabled
    if not expected_bearer_token.strip():
        return

    # Validate Authorization Header
    expected_header = f"Bearer {expected_bearer_token.strip()}"
    if authorization_header != expected_header:
        raise HTTPException(status_code=401, detail="Unauthorized")


def get_whisper_model(model_name: str, whisper_device: str, whisper_compute_type: str) -> Any:

    """Resolve or create one cached Faster-Whisper model instance.

    Args:
        model_name: Faster-Whisper model name.
        whisper_device: Execution device such as `cpu` or `cuda`.
        whisper_compute_type: Faster-Whisper compute type.

    Returns:
        Cached Faster-Whisper model instance.
    """

    assert WhisperModel is not None, "faster-whisper is not installed on this node."
    # Resolve Cache Entry
    cache_key = (model_name, whisper_device, whisper_compute_type)
    if cache_key not in WHISPER_MODEL_CACHE:
        WHISPER_MODEL_CACHE[cache_key] = WhisperModel(
            model_name,
            device=whisper_device,
            compute_type=whisper_compute_type,
        )

    return WHISPER_MODEL_CACHE[cache_key]


def get_paddle_ocr(language: str) -> Any:

    """Resolve or create one cached PaddleOCR instance.

    Args:
        language: Requested OCR language.

    Returns:
        Cached PaddleOCR instance.
    """

    assert PaddleOCR is not None, "PaddleOCR is not installed on this node."
    # Resolve Cache Entry
    normalized_language = language.strip() or "en"
    if normalized_language not in PADDLE_OCR_CACHE:
        initialization_error_message_list: list[str] = []
        constructor_argument_map_list = [
            {
                "lang": normalized_language,
                "use_textline_orientation": True,
            },
            {
                "lang": normalized_language,
                "use_angle_cls": True,
            },
            {
                "lang": normalized_language,
            },
        ]

        # Probe Compatible Constructor Signatures
        for constructor_argument_map in constructor_argument_map_list:
            try:
                PADDLE_OCR_CACHE[normalized_language] = PaddleOCR(**constructor_argument_map)
                break
            except (TypeError, ValueError) as error:
                initialization_error_message_list.append(
                    f"{constructor_argument_map!r} -> {error}"
                )

        if normalized_language not in PADDLE_OCR_CACHE:
            error_summary_text = " | ".join(initialization_error_message_list)
            raise RuntimeError(
                "Failed to initialize PaddleOCR for "
                f"language={normalized_language!r}. Attempts: {error_summary_text}"
            )

    return PADDLE_OCR_CACHE[normalized_language]


def collect_paddle_ocr_text_and_confidence(ocr_result: Any) -> tuple[str, float]:

    """Collect normalized OCR text and mean confidence from PaddleOCR output.

    Args:
        ocr_result: Raw PaddleOCR output structure.

    Returns:
        Tuple containing collapsed OCR text and average confidence.
    """

    # Collect Accepted OCR Lines
    accepted_text_list: list[str] = []
    confidence_value_list: list[float] = []

    for page_result in ocr_result or []:
        if not page_result:
            continue

        for line_result in page_result:
            if not line_result or len(line_result) < 2:
                continue

            text_confidence_pair = line_result[1]
            if not isinstance(text_confidence_pair, (list, tuple)) or len(text_confidence_pair) < 2:
                continue

            candidate_text = collapse_whitespace(str(text_confidence_pair[0]))
            candidate_confidence = float(text_confidence_pair[1])

            if not candidate_text:
                continue

            accepted_text_list.append(candidate_text)
            confidence_value_list.append(candidate_confidence * 100.0 if candidate_confidence <= 1.0 else candidate_confidence)

    average_confidence = sum(confidence_value_list) / len(confidence_value_list) if confidence_value_list else 0.0
    return collapse_whitespace(" ".join(accepted_text_list)), round(average_confidence, 3)


def find_windows_pid_listening_on_port(port: int) -> list[int]:

    """Find Windows process IDs that listen on one TCP port.

    Args:
        port: TCP port to inspect.

    Returns:
        Listening process IDs discovered through `netstat`.
    """

    # Inspect TCP Listeners
    netstat_result = subprocess.run(
        ["netstat", "-ano", "-p", "tcp"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert netstat_result.returncode == 0, "Failed to inspect TCP listeners with netstat."

    listening_pid_list: list[int] = []
    target_suffix = f":{port}"

    # Parse Matching Listener Rows
    for output_line in netstat_result.stdout.splitlines():
        normalized_line = " ".join(output_line.split())
        if "LISTENING" not in normalized_line:
            continue

        line_token_list = normalized_line.split(" ")
        if len(line_token_list) < 5:
            continue

        local_address = line_token_list[1]
        process_id_text = line_token_list[-1]
        if not local_address.endswith(target_suffix):
            continue

        if not process_id_text.isdigit():
            continue

        listening_pid_list.append(int(process_id_text))

    return listening_pid_list


def read_windows_process_command_line(process_id: int) -> str:

    """Read the command line of one Windows process.

    Args:
        process_id: Windows process identifier.

    Returns:
        Process command line text, or an empty string when it cannot be read.
    """

    # Query Process Metadata
    powershell_command = (
        f"$process = Get-CimInstance Win32_Process -Filter \"ProcessId = {process_id}\"; "
        "if ($process) { $process.CommandLine }"
    )
    process_result = subprocess.run(
        ["powershell", "-NoProfile", "-Command", powershell_command],
        capture_output=True,
        text=True,
        check=False,
    )
    if process_result.returncode != 0:
        return ""

    return process_result.stdout.strip()


def terminate_windows_process(process_id: int) -> None:

    """Terminate one Windows process forcibly.

    Args:
        process_id: Windows process identifier.

    Raises:
        AssertionError: If `taskkill` fails.
    """

    # Execute Forced Termination
    termination_result = subprocess.run(
        ["taskkill", "/PID", str(process_id), "/F"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert termination_result.returncode == 0, (
        f"Failed to terminate stale process {process_id}: "
        f"{termination_result.stdout.strip()} {termination_result.stderr.strip()}"
    )


def release_stale_lan_ai_node_process_on_port(port: int) -> bool:

    """Release a stale Windows LAN AI node process when it owns the target port.

    Args:
        port: TCP port that should be free before server startup.

    Returns:
        Whether a stale process was terminated.
    """

    if os.name != "nt":
        return False

    # Inspect Listening Processes
    released_process = False
    for process_id in find_windows_pid_listening_on_port(port):
        command_line_text = read_windows_process_command_line(process_id)
        lowered_command_line_text = command_line_text.lower()
        if "lan_ai_node_server.py" not in lowered_command_line_text:
            raise RuntimeError(
                f"Port {port} is already in use by PID {process_id}, and it does not look like a stale LAN AI node process."
            )

        print(f"Reclaiming port {port} from stale LAN AI node process PID {process_id}.")
        # Terminate Matching Stale Server
        terminate_windows_process(process_id)
        released_process = True

    return released_process


def build_application(parsed_arguments: argparse.Namespace) -> FastAPI:

    """Build the FastAPI application for the LAN AI node.

    Args:
        parsed_arguments: Parsed server command-line arguments.

    Returns:
        Configured FastAPI application.
    """

    application = FastAPI(title="StandardML LAN AI Node", version="1.0.0")

    @application.get("/health")
    def read_health(authorization: str | None = Header(default=None)) -> dict[str, Any]:

        """Serve the LAN node healthcheck response."""

        ensure_authorized(authorization, parsed_arguments.bearer_token)

        return {
            "status": "ok",
            "faster_whisper_available": WhisperModel is not None,
            "paddleocr_available": PaddleOCR is not None,
            "default_whisper_model": parsed_arguments.whisper_model,
            "default_whisper_device": parsed_arguments.whisper_device,
            "default_whisper_compute_type": parsed_arguments.whisper_compute_type,
        }

    @application.post("/transcribe")
    async def transcribe_audio(
        audio_file: UploadFile = File(...),
        model: str = Form(default=DEFAULT_WHISPER_MODEL),
        language: str = Form(default="it"),
        beam_size: int = Form(default=5),
        vad_filter: bool = Form(default=True),
        authorization: str | None = Header(default=None),
    ) -> dict[str, Any]:

        """Transcribe uploaded audio through Faster-Whisper."""

        # Authorize Request
        ensure_authorized(authorization, parsed_arguments.bearer_token)

        if WhisperModel is None:
            raise HTTPException(status_code=503, detail="faster-whisper is not installed on this node.")

        # Persist Uploaded Audio
        start_time = time.time()
        suffix = Path(audio_file.filename or "upload.bin").suffix or ".bin"
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temporary_file:
            temporary_file_path = Path(temporary_file.name)
            temporary_file.write(await audio_file.read())

        try:
            # Run Transcript Model
            whisper_model = get_whisper_model(
                model_name=model.strip() or parsed_arguments.whisper_model,
                whisper_device=parsed_arguments.whisper_device,
                whisper_compute_type=parsed_arguments.whisper_compute_type,
            )
            segment_iterator, transcript_info = whisper_model.transcribe(
                str(temporary_file_path),
                language=(language.strip() or None),
                beam_size=beam_size,
                vad_filter=vad_filter,
            )
            # Collect Transcript Segments
            segment_payload_list: list[dict[str, Any]] = []
            transcript_segment_text_list: list[str] = []
            for segment in segment_iterator:
                segment_text = collapse_whitespace(segment.text)
                if not segment_text:
                    continue

                transcript_segment_text_list.append(segment_text)
                segment_payload_list.append(
                    {
                        "start_seconds": round(float(getattr(segment, "start", 0.0) or 0.0), 3),
                        "end_seconds": round(float(getattr(segment, "end", 0.0) or 0.0), 3),
                        "text": segment_text,
                    }
                )

            # Build Transcript Payload
            transcript_text = collapse_whitespace(" ".join(transcript_segment_text_list))

            return {
                "transcript_text": transcript_text,
                "segments": segment_payload_list,
                "language": getattr(transcript_info, "language", ""),
                "language_probability": float(getattr(transcript_info, "language_probability", 0.0) or 0.0),
                "elapsed_seconds": round(time.time() - start_time, 3),
            }
        finally:
            temporary_file_path.unlink(missing_ok=True)

    @application.post("/ocr")
    async def run_ocr(
        image_file: UploadFile = File(...),
        language: str = Form(default="en"),
        authorization: str | None = Header(default=None),
    ) -> dict[str, Any]:

        """Run OCR on one uploaded image through PaddleOCR."""

        # Authorize Request
        ensure_authorized(authorization, parsed_arguments.bearer_token)

        if PaddleOCR is None:
            raise HTTPException(status_code=503, detail="PaddleOCR is not installed on this node.")

        # Persist Uploaded Image
        suffix = Path(image_file.filename or "upload.png").suffix or ".png"
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temporary_file:
            temporary_file_path = Path(temporary_file.name)
            temporary_file.write(await image_file.read())

        try:
            try:
                # Resolve OCR Model
                paddle_ocr = get_paddle_ocr(language)
            except Exception as error:
                raise HTTPException(
                    status_code=503,
                    detail=f"PaddleOCR initialization failed: {error}",
                ) from error

            try:
                # Execute OCR
                ocr_result = paddle_ocr.ocr(str(temporary_file_path), cls=True)
            except Exception as error:
                raise HTTPException(
                    status_code=503,
                    detail=f"PaddleOCR execution failed: {error}",
                ) from error

            # Build OCR Payload
            ocr_text, average_confidence = collect_paddle_ocr_text_and_confidence(ocr_result)

            return {
                "ocr_text": ocr_text,
                "average_confidence": average_confidence,
            }
        finally:
            temporary_file_path.unlink(missing_ok=True)

    return application


def main() -> int:

    """Run the LAN AI node server entry point.

    Returns:
        Process exit code.
    """

    # Parse CLI Arguments
    parsed_arguments = parse_command_line_arguments()
    # Build Application
    application = build_application(parsed_arguments)

    try:
        uvicorn.run(
            application,
            host=parsed_arguments.host,
            port=parsed_arguments.port,
        )
    except OSError as error:
        port_already_in_use = error.errno in {errno.EADDRINUSE, 10048}
        if not port_already_in_use:
            raise

        # Retry After Releasing Stale Listener
        released_process = release_stale_lan_ai_node_process_on_port(parsed_arguments.port)
        if not released_process:
            raise

        uvicorn.run(
            application,
            host=parsed_arguments.host,
            port=parsed_arguments.port,
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
