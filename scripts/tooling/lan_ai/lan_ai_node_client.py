""" Call LAN AI Node Services """

from __future__ import annotations

# Disable Bytecode Cache Writes
import sys
sys.dont_write_bytecode = True

# Import Python Utilities
from dataclasses import dataclass
from pathlib import Path
import time
from typing import Any

import requests

PROJECT_PATH = Path(__file__).resolve().parents[3]
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

from scripts.tooling.video_guides.analyze_video_guides import build_ocr_region_map
from scripts.tooling.video_guides.analyze_video_guides import collapse_whitespace
from scripts.tooling.video_guides.analyze_video_guides import compute_ocr_quality_score
from scripts.tooling.video_guides.analyze_video_guides import crop_frame_region

try:
    import cv2
except ImportError:
    cv2 = None

DEFAULT_REQUEST_TIMEOUT_SECONDS = 300


@dataclass
class LanTranscriptSegment:

    """Store one transcript segment returned by the LAN AI node.

    Attributes:
        start_seconds: Segment start timestamp in seconds.
        end_seconds: Segment end timestamp in seconds.
        text: Collapsed transcript text for the segment.
    """

    start_seconds: float
    end_seconds: float
    text: str


def normalize_base_url(raw_base_url: str) -> str:

    """Normalize one service base URL.

    Args:
        raw_base_url: Raw user-provided or config-provided base URL.

    Returns:
        Trimmed base URL without a trailing slash.
    """

    return raw_base_url.strip().rstrip("/")


def build_bearer_header_map(bearer_token: str) -> dict[str, str]:

    """Build the optional bearer-authorization header map.

    Args:
        bearer_token: Optional bearer token string.

    Returns:
        Header map ready for `requests`. Returns an empty dictionary when the
        token is blank.
    """

    if not bearer_token.strip():
        return {}

    return {"Authorization": f"Bearer {bearer_token.strip()}"}


def fetch_lm_studio_model_name_list(
    lm_studio_base_url: str,
    api_key: str,
    timeout_seconds: int = DEFAULT_REQUEST_TIMEOUT_SECONDS,
) -> list[str]:

    """Fetch the visible LM Studio model identifiers.

    Args:
        lm_studio_base_url: Base URL of the LM Studio server.
        api_key: API key or token accepted by LM Studio.
        timeout_seconds: Request timeout in seconds.

    Returns:
        Visible LM Studio model identifiers. Returns an empty list when the
        server does not answer successfully.
    """

    # Request Model List
    response = requests.get(
        f"{normalize_base_url(lm_studio_base_url)}/v1/models",
        headers=build_bearer_header_map(api_key.strip() or "lm-studio"),
        timeout=timeout_seconds,
    )
    if not response.ok:
        return []

    # Parse Visible Model IDs
    payload = response.json()
    return [
        str(model_item.get("id", "")).strip()
        for model_item in payload.get("data", [])
        if isinstance(model_item, dict) and str(model_item.get("id", "")).strip()
    ]


def post_file_to_lan_ai_node(
    endpoint_url: str,
    file_field_name: str,
    upload_name: str,
    upload_bytes: bytes,
    bearer_token: str,
    data_map: dict[str, Any] | None = None,
    timeout_seconds: int = DEFAULT_REQUEST_TIMEOUT_SECONDS,
) -> dict[str, Any]:

    """Post one uploaded file to a LAN AI node endpoint.

    Args:
        endpoint_url: Full endpoint URL.
        file_field_name: Multipart field name used for the file.
        upload_name: File name exposed to the endpoint.
        upload_bytes: Raw uploaded file bytes.
        bearer_token: Optional bearer token used for authorization.
        data_map: Optional form fields sent beside the file.
        timeout_seconds: Request timeout in seconds.

    Returns:
        Parsed JSON response payload.

    Raises:
        AssertionError: If the endpoint fails or returns a non-dictionary JSON
            payload.
    """

    # Submit Multipart Request
    response = requests.post(
        endpoint_url,
        headers=build_bearer_header_map(bearer_token),
        data=data_map or {},
        files={file_field_name: (upload_name, upload_bytes)},
        timeout=timeout_seconds,
    )
    try:
        response.raise_for_status()
    except requests.HTTPError as error:
        response_body_text = collapse_whitespace(response.text)
        raise AssertionError(
            "LAN AI node request failed. "
            f"endpoint={endpoint_url!r}; "
            f"status_code={response.status_code}; "
            f"response_body={response_body_text!r}"
        ) from error

    # Parse JSON Payload
    payload = response.json()
    assert isinstance(payload, dict), "LAN AI node returned a non-dict JSON payload."
    return payload


def transcribe_audio_via_lan_ai_node(
    audio_file_path: Path,
    lan_ai_base_url: str,
    bearer_token: str,
    transcript_model: str,
    transcript_language: str,
    timeout_seconds: int = DEFAULT_REQUEST_TIMEOUT_SECONDS,
) -> str:

    """Transcribe one audio file through the LAN AI node.

    Args:
        audio_file_path: Audio file uploaded to the node.
        lan_ai_base_url: Base URL of the LAN AI node.
        bearer_token: Optional bearer token used for authorization.
        transcript_model: Transcript model requested from the node.
        transcript_language: Requested transcript language.
        timeout_seconds: Request timeout in seconds.

    Returns:
        Collapsed transcript text returned by the node.
    """

    # Request Transcript
    payload = post_file_to_lan_ai_node(
        endpoint_url=f"{normalize_base_url(lan_ai_base_url)}/transcribe",
        file_field_name="audio_file",
        upload_name=audio_file_path.name,
        upload_bytes=audio_file_path.read_bytes(),
        bearer_token=bearer_token,
        data_map={
            "model": transcript_model,
            "language": transcript_language,
        },
        timeout_seconds=timeout_seconds,
    )

    # Validate Transcript Text
    transcript_text = collapse_whitespace(str(payload.get("transcript_text", "")))
    assert transcript_text, "LAN AI node returned an empty transcript."
    return transcript_text


def transcribe_audio_via_lan_ai_node_with_segments(
    audio_file_path: Path,
    lan_ai_base_url: str,
    bearer_token: str,
    transcript_model: str,
    transcript_language: str,
    timeout_seconds: int = DEFAULT_REQUEST_TIMEOUT_SECONDS,
) -> tuple[str, list[LanTranscriptSegment]]:

    """Transcribe one audio file and retain segment boundaries.

    Args:
        audio_file_path: Audio file uploaded to the node.
        lan_ai_base_url: Base URL of the LAN AI node.
        bearer_token: Optional bearer token used for authorization.
        transcript_model: Transcript model requested from the node.
        transcript_language: Requested transcript language.
        timeout_seconds: Request timeout in seconds.

    Returns:
        Tuple containing the full transcript text and the normalized transcript
        segment list.
    """

    # Request Transcript Payload
    payload = post_file_to_lan_ai_node(
        endpoint_url=f"{normalize_base_url(lan_ai_base_url)}/transcribe",
        file_field_name="audio_file",
        upload_name=audio_file_path.name,
        upload_bytes=audio_file_path.read_bytes(),
        bearer_token=bearer_token,
        data_map={
            "model": transcript_model,
            "language": transcript_language,
        },
        timeout_seconds=timeout_seconds,
    )

    # Validate Transcript Text
    transcript_text = collapse_whitespace(str(payload.get("transcript_text", "")))
    assert transcript_text, "LAN AI node returned an empty transcript."

    # Materialize Transcript Segments
    transcript_segment_list: list[LanTranscriptSegment] = []
    for segment_map in payload.get("segments", []):
        if not isinstance(segment_map, dict):
            continue

        segment_text = collapse_whitespace(str(segment_map.get("text", "")))
        if not segment_text:
            continue

        transcript_segment_list.append(
            LanTranscriptSegment(
                start_seconds=max(0.0, float(segment_map.get("start_seconds", 0.0) or 0.0)),
                end_seconds=max(0.0, float(segment_map.get("end_seconds", 0.0) or 0.0)),
                text=segment_text,
            )
        )

    return transcript_text, transcript_segment_list


def run_lm_studio_chat_completion(
    lm_studio_base_url: str,
    api_key: str,
    model_name: str,
    prompt_text: str,
    preserve_formatting: bool = False,
    timeout_seconds: int = DEFAULT_REQUEST_TIMEOUT_SECONDS,
) -> str:

    """Run one chat-completion request against LM Studio.

    Args:
        lm_studio_base_url: Base URL of the LM Studio server.
        api_key: API key or token accepted by LM Studio.
        model_name: Model requested for the chat completion.
        prompt_text: Prompt sent to the model.
        preserve_formatting: Whether response formatting should be preserved.
        timeout_seconds: Request timeout in seconds.

    Returns:
        Response text extracted from the first returned choice.
    """

    # Resolve Available Models
    normalized_base_url = normalize_base_url(lm_studio_base_url)
    available_model_name_list = fetch_lm_studio_model_name_list(
        lm_studio_base_url=normalized_base_url,
        api_key=api_key,
        timeout_seconds=timeout_seconds,
    )
    # Execute Completion Request
    response = None
    for attempt_index in range(2):
        response = requests.post(
            f"{normalized_base_url}/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key.strip() or 'lm-studio'}",
                "Content-Type": "application/json",
            },
            json={
                "model": model_name,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt_text,
                    }
                ],
                "temperature": 0.2,
            },
            timeout=timeout_seconds,
        )
        if response.ok:
            break

        response_body_text = response.text.strip()
        if attempt_index == 0 and "Model reloaded." in response_body_text:
            time.sleep(2.0)
            continue

        available_model_text = ", ".join(available_model_name_list) if available_model_name_list else "<unavailable>"
        raise AssertionError(
            "LM Studio chat completion request failed. "
            f"status_code={response.status_code}; "
            f"requested_model={model_name!r}; "
            f"available_models={available_model_text}; "
            f"response_body={response_body_text!r}"
        )

    assert response is not None and response.ok, "LM Studio request retry loop completed without a valid response."

    # Parse Completion Payload
    payload = response.json()
    choice_list = payload.get("choices", [])
    assert choice_list, "LM Studio returned no choices."

    message_map = choice_list[0].get("message", {})
    response_text = message_map.get("content", "")
    if isinstance(response_text, list):
        response_text = "\n".join(
            str(content_item.get("text", "")).strip()
            for content_item in response_text
            if isinstance(content_item, dict)
        )
    if not str(response_text).strip():
        response_text = message_map.get("reasoning_content", "")

    normalized_response_text = str(response_text).strip() if preserve_formatting else collapse_whitespace(str(response_text))
    if not normalized_response_text:
        usage_map = payload.get("usage", {})
        raise AssertionError(
            "LM Studio returned empty text after parsing both content and reasoning_content. "
            f"requested_model={model_name!r}; "
            f"usage={usage_map!r}; "
            f"finish_reason={choice_list[0].get('finish_reason', '')!r}"
        )
    return normalized_response_text


def run_region_ocr_via_lan_ai_node(
    frame_image: Any,
    lan_ai_base_url: str,
    bearer_token: str,
    ocr_language: str,
    timeout_seconds: int = 90,
) -> tuple[str, float, str, list[str]]:

    """Run OCR on TwinCAT-oriented frame regions through the LAN AI node.

    Args:
        frame_image: OpenCV frame image already loaded in memory.
        lan_ai_base_url: Base URL of the LAN AI node.
        bearer_token: Optional bearer token used for authorization.
        ocr_language: Requested OCR language.
        timeout_seconds: Request timeout in seconds.

    Returns:
        Tuple containing the best OCR text, OCR quality score, selected region
        name, and an empty matched-term list placeholder.
    """

    assert cv2 is not None, "opencv-python-headless is required for LAN OCR crop encoding."

    # Probe Candidate Regions
    frame_height, frame_width = frame_image.shape[:2]
    region_map = build_ocr_region_map(frame_width, frame_height)
    best_candidate_text = ""
    best_candidate_score = 0.0
    best_region_name = ""

    for region_name, region_bounds in region_map.items():
        region_image = crop_frame_region(frame_image, region_bounds)
        if region_image.size == 0:
            continue

        # Encode Region Image
        encode_success, encoded_region_image = cv2.imencode(".png", region_image)
        if not encode_success:
            continue

        # Request OCR Payload
        payload = post_file_to_lan_ai_node(
            endpoint_url=f"{normalize_base_url(lan_ai_base_url)}/ocr",
            file_field_name="image_file",
            upload_name=f"{region_name}.png",
            upload_bytes=encoded_region_image.tobytes(),
            bearer_token=bearer_token,
            data_map={"language": ocr_language},
            timeout_seconds=timeout_seconds,
        )

        # Score OCR Candidate
        ocr_text = collapse_whitespace(str(payload.get("ocr_text", "")))
        average_confidence = float(payload.get("average_confidence", 0.0))
        quality_score = compute_ocr_quality_score(ocr_text, average_confidence, region_name)

        if quality_score > best_candidate_score:
            best_candidate_text = ocr_text
            best_candidate_score = quality_score
            best_region_name = region_name

    return best_candidate_text, best_candidate_score, best_region_name, []
