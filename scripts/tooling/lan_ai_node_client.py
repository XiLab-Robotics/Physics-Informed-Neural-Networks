""" Call LAN AI Node Services """

from __future__ import annotations

# Disable Bytecode Cache Writes
import sys
sys.dont_write_bytecode = True

# Import Python Utilities
from pathlib import Path
from typing import Any

import requests

PROJECT_PATH = Path(__file__).resolve().parents[2]
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

from scripts.tooling.analyze_video_guides import build_ocr_region_map
from scripts.tooling.analyze_video_guides import collapse_whitespace
from scripts.tooling.analyze_video_guides import compute_ocr_quality_score
from scripts.tooling.analyze_video_guides import crop_frame_region

try:
    import cv2
except ImportError:
    cv2 = None

DEFAULT_REQUEST_TIMEOUT_SECONDS = 300


def normalize_base_url(raw_base_url: str) -> str:

    """ Normalize Base URL """

    return raw_base_url.strip().rstrip("/")


def build_bearer_header_map(bearer_token: str) -> dict[str, str]:

    """ Build Bearer Header Map """

    if not bearer_token.strip():
        return {}

    return {"Authorization": f"Bearer {bearer_token.strip()}"}


def post_file_to_lan_ai_node(
    endpoint_url: str,
    file_field_name: str,
    upload_name: str,
    upload_bytes: bytes,
    bearer_token: str,
    data_map: dict[str, Any] | None = None,
    timeout_seconds: int = DEFAULT_REQUEST_TIMEOUT_SECONDS,
) -> dict[str, Any]:

    """ Post File To LAN AI Node """

    response = requests.post(
        endpoint_url,
        headers=build_bearer_header_map(bearer_token),
        data=data_map or {},
        files={file_field_name: (upload_name, upload_bytes)},
        timeout=timeout_seconds,
    )
    response.raise_for_status()

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

    """ Transcribe Audio Via LAN AI Node """

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

    transcript_text = collapse_whitespace(str(payload.get("transcript_text", "")))
    assert transcript_text, "LAN AI node returned an empty transcript."
    return transcript_text


def run_lm_studio_chat_completion(
    lm_studio_base_url: str,
    api_key: str,
    model_name: str,
    prompt_text: str,
    preserve_formatting: bool = False,
    timeout_seconds: int = DEFAULT_REQUEST_TIMEOUT_SECONDS,
) -> str:

    """ Run LM Studio Chat Completion """

    normalized_base_url = normalize_base_url(lm_studio_base_url)
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
    response.raise_for_status()

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

    normalized_response_text = str(response_text).strip() if preserve_formatting else collapse_whitespace(str(response_text))
    assert normalized_response_text, "LM Studio returned empty text."
    return normalized_response_text


def run_region_ocr_via_lan_ai_node(
    frame_image: Any,
    lan_ai_base_url: str,
    bearer_token: str,
    ocr_language: str,
    timeout_seconds: int = 90,
) -> tuple[str, float, str, list[str]]:

    """ Run Region OCR Via LAN AI Node """

    assert cv2 is not None, "opencv-python-headless is required for LAN OCR crop encoding."

    frame_height, frame_width = frame_image.shape[:2]
    region_map = build_ocr_region_map(frame_width, frame_height)
    best_candidate_text = ""
    best_candidate_score = 0.0
    best_region_name = ""

    for region_name, region_bounds in region_map.items():
        region_image = crop_frame_region(frame_image, region_bounds)
        if region_image.size == 0:
            continue

        encode_success, encoded_region_image = cv2.imencode(".png", region_image)
        if not encode_success:
            continue

        payload = post_file_to_lan_ai_node(
            endpoint_url=f"{normalize_base_url(lan_ai_base_url)}/ocr",
            file_field_name="image_file",
            upload_name=f"{region_name}.png",
            upload_bytes=encoded_region_image.tobytes(),
            bearer_token=bearer_token,
            data_map={"language": ocr_language},
            timeout_seconds=timeout_seconds,
        )

        ocr_text = collapse_whitespace(str(payload.get("ocr_text", "")))
        average_confidence = float(payload.get("average_confidence", 0.0))
        quality_score = compute_ocr_quality_score(ocr_text, average_confidence, region_name)

        if quality_score > best_candidate_score:
            best_candidate_text = ocr_text
            best_candidate_score = quality_score
            best_region_name = region_name

    return best_candidate_text, best_candidate_score, best_region_name, []
