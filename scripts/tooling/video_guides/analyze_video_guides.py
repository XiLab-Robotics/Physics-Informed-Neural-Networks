""" Analyze TwinCAT Video Guides """

from __future__ import annotations

# Disable Bytecode Cache Writes
import sys
sys.dont_write_bytecode = True

# Import Python Utilities
import argparse
import json
import re
import shutil
from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field
from pathlib import Path
from typing import Any

# Optional Imports
try:
    import cv2
except ImportError:
    cv2 = None

try:
    from faster_whisper import WhisperModel
except ImportError:
    WhisperModel = None

try:
    import pytesseract
except ImportError:
    pytesseract = None

PROJECT_PATH = Path(__file__).resolve().parents[3]
DEFAULT_VIDEO_GUIDE_ROOT = PROJECT_PATH / "reference" / "video_guides" / "source_bundle"
DEFAULT_ANALYSIS_ROOT = PROJECT_PATH / ".temp" / "video_guides" / "_analysis"
DEFAULT_TRANSCRIPTION_MODEL = "medium"
DEFAULT_TRANSCRIPTION_BEAM_SIZE = 8
DEFAULT_TRANSCRIPTION_BEST_OF = 5
DEFAULT_TRANSCRIPTION_TEMPERATURE = 0.0
DEFAULT_TRANSCRIPTION_COMPUTE_TYPE = "int8"
DEFAULT_FRAME_INTERVAL_SECONDS = 30.0
DEFAULT_MAX_FRAMES_PER_VIDEO = 40
DEFAULT_TRANSCRIPT_LANGUAGE = "it"
DEFAULT_TRANSCRIPT_MIN_QUALITY_SCORE = 0.35
DEFAULT_OCR_MIN_QUALITY_SCORE = 42.0
VIDEO_SUFFIXES = {".mp4", ".mkv", ".mov", ".avi", ".m4v"}
TEXT_SUFFIXES = {".txt", ".md"}
PREFERRED_TESSERACT_PATH_LIST = [
    r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
]
TERM_PATTERN_MAP = {
    "TwinCAT": re.compile(r"\bTwinCAT\b", flags=re.IGNORECASE),
    "Beckhoff": re.compile(r"\bBeckhoff\b", flags=re.IGNORECASE),
    "TestRig": re.compile(r"\bTest\s*Rig\b", flags=re.IGNORECASE),
    "FB_Predict": re.compile(r"\bFB[_\s-]*Predict\b", flags=re.IGNORECASE),
    "ML_Transmission_Error": re.compile(r"\bML[_\s-]*Transmission[_\s-]*Error\b", flags=re.IGNORECASE),
    "Predict_ML": re.compile(r"\bPredict[_\s-]*ML\b", flags=re.IGNORECASE),
    "TE_Calc": re.compile(r"\bTE[_\s-]*Calc\b", flags=re.IGNORECASE),
    "DataValid": re.compile(r"\bDataValid\b", flags=re.IGNORECASE),
    "engine_<n>": re.compile(r"\bengine[_\s-]*\d+\b", flags=re.IGNORECASE),
    "speed": re.compile(r"\b(speed|velocit[aà])\b", flags=re.IGNORECASE),
    "torque": re.compile(r"\b(torque|coppia)\b", flags=re.IGNORECASE),
    "temperature": re.compile(r"\b(temperature|temperatura)\b", flags=re.IGNORECASE),
    "angle": re.compile(r"\b(angle|angolo|posizione)\b", flags=re.IGNORECASE),
    "harmonic": re.compile(r"\b(harmonic|armonic|frequenz|component)\b", flags=re.IGNORECASE),
    "simulation": re.compile(r"\b(simulation|simulazione|generator|cam)\b", flags=re.IGNORECASE),
    "Matlab": re.compile(r"\bMatlab\b", flags=re.IGNORECASE),
}


@dataclass
class CompanionNote:

    """Store a repository-local companion note matched to one video.

    Attributes:
        file_name: Original companion-note file name.
        relative_path: Project-relative path used in generated artifacts.
        text: Full normalized companion-note content.
        normalized_stem: Stem used for fuzzy matching against video names.
    """

    file_name: str
    relative_path: str
    text: str
    normalized_stem: str


@dataclass
class TranscriptSegment:

    """Store one transcript segment produced by the rough analysis workflow.

    Attributes:
        start_seconds: Segment start timestamp in seconds.
        end_seconds: Segment end timestamp in seconds.
        text: Collapsed transcript text for the segment.
        quality_score: Repository-defined transcript quality heuristic.
    """

    start_seconds: float
    end_seconds: float
    text: str
    quality_score: float = 0.0


@dataclass
class OCRFrameRecord:

    """Store OCR evidence extracted from one sampled video frame.

    Attributes:
        timestamp_seconds: Frame timestamp in seconds.
        frame_path: Project-relative path of the saved frame image.
        ocr_text: Highest-quality OCR text recovered from the sampled regions.
        quality_score: OCR quality heuristic used for later filtering.
        selected_region_name: Region that produced the retained OCR result.
        matched_term_list: Tracked TwinCAT/TestRig terms detected in the OCR text.
    """

    timestamp_seconds: float
    frame_path: str
    ocr_text: str
    quality_score: float = 0.0
    selected_region_name: str = ""
    matched_term_list: list[str] = field(default_factory=list)


@dataclass
class VideoAnalysisRecord:

    """Store the summarized outputs for one analyzed video.

    Attributes:
        file_name: Source video file name.
        relative_path: Project-relative source path.
        size_bytes: Source file size in bytes.
        duration_seconds: Video duration when it can be resolved.
        fps: Source frame rate when available.
        frame_count: Source frame count when available.
        width: Source video width when available.
        height: Source video height when available.
        associated_companion_file_list: Matched companion-note file names.
        associated_companion_note_list: Short excerpts from matched companion notes.
        transcript_generated: Whether transcript segments were produced.
        transcript_language: Detected transcript language.
        transcript_language_probability: Confidence for detected language.
        transcript_segment_count: Number of generated transcript segments.
        transcript_excerpt_list: Quality-gated transcript excerpts.
        transcript_quality_summary: Min, median, and max transcript scores.
        frame_extraction_generated: Whether frames were sampled successfully.
        frame_record_count: Number of saved frame records.
        ocr_generated: Whether report-worthy OCR text was recovered.
        ocr_excerpt_list: Quality-gated OCR excerpts.
        ocr_quality_summary: Min, median, and max OCR scores.
        matched_term_list: Tracked terms found across transcript, OCR, and notes.
        issue_list: Non-fatal issues recorded during analysis.
    """

    file_name: str
    relative_path: str
    size_bytes: int
    duration_seconds: float | None = None
    fps: float | None = None
    frame_count: int | None = None
    width: int | None = None
    height: int | None = None
    associated_companion_file_list: list[str] = field(default_factory=list)
    associated_companion_note_list: list[str] = field(default_factory=list)
    transcript_generated: bool = False
    transcript_language: str | None = None
    transcript_language_probability: float | None = None
    transcript_segment_count: int = 0
    transcript_excerpt_list: list[str] = field(default_factory=list)
    transcript_quality_summary: dict[str, float] = field(default_factory=dict)
    frame_extraction_generated: bool = False
    frame_record_count: int = 0
    ocr_generated: bool = False
    ocr_excerpt_list: list[str] = field(default_factory=list)
    ocr_quality_summary: dict[str, float] = field(default_factory=dict)
    matched_term_list: list[str] = field(default_factory=list)
    issue_list: list[str] = field(default_factory=list)


def build_argument_parser() -> argparse.ArgumentParser:

    """Build the command-line parser for rough video-guide analysis.

    Returns:
        Configured parser exposing inventory, transcript, frame, and OCR options.
    """

    argument_parser = argparse.ArgumentParser(
        description="Analyze repository-local TwinCAT/TestRig video guides into reusable inventory, transcript, frame, and note artifacts.",
    )
    argument_parser.add_argument("--input-root", default=str(DEFAULT_VIDEO_GUIDE_ROOT), help="Video-guide source root.")
    argument_parser.add_argument("--output-root", default=str(DEFAULT_ANALYSIS_ROOT), help="Analysis artifact root.")
    argument_parser.add_argument("--video-filter", default="", help="Optional case-insensitive file-name filter.")
    argument_parser.add_argument("--limit-videos", type=int, default=0, help="Optional maximum number of videos.")
    argument_parser.add_argument("--frame-interval-seconds", type=float, default=DEFAULT_FRAME_INTERVAL_SECONDS, help="Seconds between sampled frames.")
    argument_parser.add_argument("--max-frames-per-video", type=int, default=DEFAULT_MAX_FRAMES_PER_VIDEO, help="Maximum sampled frames per video.")
    argument_parser.add_argument("--transcription-model", default=DEFAULT_TRANSCRIPTION_MODEL, help="Faster-Whisper model size.")
    argument_parser.add_argument("--transcription-language", default=DEFAULT_TRANSCRIPT_LANGUAGE, help="Expected transcript language or 'auto'.")
    argument_parser.add_argument("--transcription-beam-size", type=int, default=DEFAULT_TRANSCRIPTION_BEAM_SIZE, help="Beam size for Faster-Whisper decoding.")
    argument_parser.add_argument("--transcription-best-of", type=int, default=DEFAULT_TRANSCRIPTION_BEST_OF, help="Best-of count for Faster-Whisper decoding.")
    argument_parser.add_argument("--transcription-temperature", type=float, default=DEFAULT_TRANSCRIPTION_TEMPERATURE, help="Decoding temperature for Faster-Whisper.")
    argument_parser.add_argument("--transcription-compute-type", default=DEFAULT_TRANSCRIPTION_COMPUTE_TYPE, help="Compute type for Faster-Whisper.")
    argument_parser.add_argument("--transcript-min-quality-score", type=float, default=DEFAULT_TRANSCRIPT_MIN_QUALITY_SCORE, help="Minimum transcript quality score kept for report excerpts.")
    argument_parser.add_argument("--ocr-min-quality-score", type=float, default=DEFAULT_OCR_MIN_QUALITY_SCORE, help="Minimum OCR quality score kept for report excerpts.")
    argument_parser.add_argument("--disable-transcription", action="store_true", help="Skip transcription.")
    argument_parser.add_argument("--disable-frames", action="store_true", help="Skip frame extraction.")
    argument_parser.add_argument("--disable-ocr", action="store_true", help="Skip OCR.")
    argument_parser.add_argument("--force", action="store_true", help="Recompute artifacts.")

    return argument_parser


def parse_command_line_arguments() -> argparse.Namespace:

    """ Parse Command-Line Arguments """

    return build_argument_parser().parse_args()


def ensure_directory(directory_path: Path) -> None:

    """ Ensure Directory """

    directory_path.mkdir(parents=True, exist_ok=True)


def normalize_file_stem(file_name: str) -> str:

    """ Normalize File Stem """

    return re.sub(r"[^a-z0-9]+", "", Path(file_name).stem.lower())


def tokenize_file_stem(file_name: str) -> set[str]:

    """ Tokenize File Stem """

    normalized_source_text = Path(file_name).stem.lower().replace("_", " ").replace("-", " ")
    token_set = {token for token in re.split(r"[^a-z0-9]+", normalized_source_text) if len(token) >= 2}

    return token_set


def collapse_whitespace(raw_text: str) -> str:

    """ Collapse Whitespace """

    return re.sub(r"\s+", " ", raw_text).strip()


def clamp_score(raw_score: float, minimum_value: float = 0.0, maximum_value: float = 1.0) -> float:

    """ Clamp Score """

    return max(minimum_value, min(maximum_value, raw_score))


def compute_text_alpha_ratio(raw_text: str) -> float:

    """ Compute Text Alpha Ratio """

    if not raw_text:
        return 0.0

    alpha_character_count = sum(1 for character in raw_text if character.isalpha())
    return alpha_character_count / max(len(raw_text), 1)


def compute_text_digit_ratio(raw_text: str) -> float:

    """ Compute Text Digit Ratio """

    if not raw_text:
        return 0.0

    digit_character_count = sum(1 for character in raw_text if character.isdigit())
    return digit_character_count / max(len(raw_text), 1)


def count_matched_terms_in_text(raw_text: str) -> int:

    """ Count Matched Terms In Text """

    return sum(1 for term_pattern in TERM_PATTERN_MAP.values() if term_pattern.search(raw_text))


def compute_transcript_quality_score(raw_text: str, average_log_probability: float | None) -> float:

    """ Compute Transcript Quality Score """

    collapsed_text = collapse_whitespace(raw_text)
    if not collapsed_text:
        return 0.0

    alpha_ratio = compute_text_alpha_ratio(collapsed_text)
    digit_ratio = compute_text_digit_ratio(collapsed_text)
    matched_term_bonus = min(count_matched_terms_in_text(collapsed_text) * 0.08, 0.24)
    length_bonus = 0.08 if 20 <= len(collapsed_text) <= 220 else 0.0
    log_probability_bonus = 0.0 if average_log_probability is None else clamp_score((average_log_probability + 1.5) / 1.5) * 0.35
    ratio_score = clamp_score(alpha_ratio * 0.7 + (1.0 - min(digit_ratio, 0.4)) * 0.3)
    noise_penalty = 0.18 if "Ã" in collapsed_text or "�" in collapsed_text else 0.0

    return round(clamp_score(log_probability_bonus + matched_term_bonus + length_bonus + ratio_score * 0.33 - noise_penalty), 4)


def summarize_quality_score_list(score_list: list[float]) -> dict[str, float]:

    """ Summarize Quality Score List """

    if not score_list:
        return {}

    sorted_score_list = sorted(score_list)
    midpoint_index = len(sorted_score_list) // 2
    median_score = (
        sorted_score_list[midpoint_index]
        if len(sorted_score_list) % 2 == 1
        else (sorted_score_list[midpoint_index - 1] + sorted_score_list[midpoint_index]) / 2.0
    )

    return {
        "min": round(sorted_score_list[0], 4),
        "median": round(median_score, 4),
        "max": round(sorted_score_list[-1], 4),
    }


def collect_companion_note_list(input_root: Path) -> list[CompanionNote]:

    """ Collect Companion Notes """

    companion_note_list: list[CompanionNote] = []

    for file_path in sorted(input_root.iterdir()):
        if not file_path.is_file() or file_path.suffix.lower() not in TEXT_SUFFIXES:
            continue

        companion_note_list.append(
            CompanionNote(
                file_name=file_path.name,
                relative_path=file_path.relative_to(PROJECT_PATH).as_posix(),
                text=file_path.read_text(encoding="utf-8", errors="replace").strip(),
                normalized_stem=normalize_file_stem(file_path.name),
            )
        )

    return companion_note_list


def collect_video_file_path_list(input_root: Path, video_filter: str, limit_videos: int) -> list[Path]:

    """ Collect Video File Paths """

    video_file_path_list: list[Path] = []
    normalized_filter = video_filter.lower().strip()

    for file_path in sorted(input_root.iterdir()):
        if not file_path.is_file() or file_path.suffix.lower() not in VIDEO_SUFFIXES:
            continue
        if normalized_filter and normalized_filter not in file_path.name.lower():
            continue
        video_file_path_list.append(file_path)

    return video_file_path_list[:limit_videos] if limit_videos > 0 else video_file_path_list


def resolve_tesseract_executable_path() -> Path | None:

    """ Resolve Tesseract Executable Path """

    if pytesseract is None:
        return None

    tesseract_from_path = shutil.which("tesseract")
    if tesseract_from_path:
        return Path(tesseract_from_path)

    for candidate_path in PREFERRED_TESSERACT_PATH_LIST:
        if Path(candidate_path).exists():
            return Path(candidate_path)

    return None


def collect_runtime_capability_map(disable_transcription: bool, disable_frames: bool, disable_ocr: bool) -> dict[str, Any]:

    """Resolve which optional backends are available for this run.

    Args:
        disable_transcription: Whether transcript extraction was disabled explicitly.
        disable_frames: Whether frame extraction was disabled explicitly.
        disable_ocr: Whether OCR was disabled explicitly.

    Returns:
        Capability flags and resolved executable paths used by the pipeline.
    """

    tesseract_executable_path = None if disable_ocr else resolve_tesseract_executable_path()

    capability_map = {
        "opencv_available": cv2 is not None and not disable_frames,
        "faster_whisper_available": WhisperModel is not None and not disable_transcription,
        "pytesseract_available": pytesseract is not None and not disable_ocr,
        "tesseract_executable": str(tesseract_executable_path) if tesseract_executable_path else None,
    }

    if capability_map["pytesseract_available"] and tesseract_executable_path is not None:
        pytesseract.pytesseract.tesseract_cmd = str(tesseract_executable_path)

    capability_map["ocr_available"] = capability_map["pytesseract_available"] and tesseract_executable_path is not None

    return capability_map


def safely_cast_float(raw_value: float | int) -> float | None:

    """ Safely Cast Float """

    numeric_value = float(raw_value)
    return numeric_value if numeric_value > 0 else None


def safely_cast_int(raw_value: float | int) -> int | None:

    """ Safely Cast Int """

    numeric_value = int(raw_value)
    return numeric_value if numeric_value > 0 else None


def extract_video_metadata(video_file_path: Path) -> dict[str, Any]:

    """Read lightweight video metadata through OpenCV.

    Args:
        video_file_path: Source video file to inspect.

    Returns:
        Metadata dictionary with duration, FPS, frame count, and resolution.
        Missing values remain `None` when OpenCV is unavailable or the file
        cannot be opened.
    """

    metadata_map = {
        "duration_seconds": None,
        "fps": None,
        "frame_count": None,
        "width": None,
        "height": None,
    }

    if cv2 is None:
        return metadata_map

    capture = cv2.VideoCapture(str(video_file_path))
    if not capture.isOpened():
        return metadata_map

    fps = safely_cast_float(capture.get(cv2.CAP_PROP_FPS))
    frame_count = safely_cast_int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    duration_seconds = frame_count / fps if fps and frame_count else None
    metadata_map.update(
        {
            "duration_seconds": duration_seconds,
            "fps": fps,
            "frame_count": frame_count,
            "width": safely_cast_int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
            "height": safely_cast_int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        }
    )
    capture.release()

    return metadata_map


def build_frame_timestamp_list(duration_seconds: float | None, interval_seconds: float, max_frames_per_video: int) -> list[float]:

    """ Build Frame Timestamp List """

    if duration_seconds is None or duration_seconds <= 0:
        return []

    timestamp_seconds_list: list[float] = []
    current_timestamp_seconds = 0.0

    while current_timestamp_seconds < duration_seconds and len(timestamp_seconds_list) < max_frames_per_video:
        timestamp_seconds_list.append(round(current_timestamp_seconds, 3))
        current_timestamp_seconds += interval_seconds

    final_timestamp_seconds = round(max(duration_seconds - 0.5, 0.0), 3)
    if final_timestamp_seconds not in timestamp_seconds_list and len(timestamp_seconds_list) < max_frames_per_video:
        timestamp_seconds_list.append(final_timestamp_seconds)

    return timestamp_seconds_list


def preprocess_frame_for_ocr(frame_image: Any, variant_name: str) -> Any:

    """ Preprocess Frame For OCR """

    if cv2 is None:
        return frame_image

    grayscale_image = cv2.cvtColor(frame_image, cv2.COLOR_BGR2GRAY)
    upscaled_image = cv2.resize(grayscale_image, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)

    if variant_name == "adaptive":
        return cv2.adaptiveThreshold(
            upscaled_image,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            31,
            11,
        )

    if variant_name == "inverted":
        _, thresholded_image = cv2.threshold(upscaled_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        return thresholded_image

    _, thresholded_image = cv2.threshold(upscaled_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresholded_image


def build_ocr_region_map(frame_width: int, frame_height: int) -> dict[str, tuple[int, int, int, int]]:

    """ Build OCR Region Map """

    return {
        "title_bar": (0, 0, frame_width, int(frame_height * 0.13)),
        "left_navigation": (0, int(frame_height * 0.12), int(frame_width * 0.34), int(frame_height * 0.88)),
        "center_workspace": (int(frame_width * 0.24), int(frame_height * 0.10), int(frame_width * 0.82), int(frame_height * 0.84)),
        "right_properties": (int(frame_width * 0.67), int(frame_height * 0.10), frame_width, int(frame_height * 0.84)),
        "lower_panel": (0, int(frame_height * 0.78), frame_width, frame_height),
    }


def crop_frame_region(frame_image: Any, region_bounds: tuple[int, int, int, int]) -> Any:

    """ Crop Frame Region """

    start_x, start_y, end_x, end_y = region_bounds
    return frame_image[start_y:end_y, start_x:end_x]


def build_ocr_text_from_data(ocr_data: dict[str, list[Any]], min_confidence: float = 38.0) -> tuple[str, float]:

    """ Build OCR Text From Data """

    accepted_word_list: list[str] = []
    accepted_confidence_list: list[float] = []

    for raw_text, raw_confidence in zip(ocr_data.get("text", []), ocr_data.get("conf", [])):
        cleaned_text = collapse_whitespace(raw_text)
        if not cleaned_text:
            continue

        try:
            confidence_value = float(raw_confidence)
        except (TypeError, ValueError):
            continue

        if confidence_value < min_confidence:
            continue

        accepted_word_list.append(cleaned_text)
        accepted_confidence_list.append(confidence_value)

    average_confidence = sum(accepted_confidence_list) / len(accepted_confidence_list) if accepted_confidence_list else 0.0
    return collapse_whitespace(" ".join(accepted_word_list)), average_confidence


def compute_ocr_quality_score(ocr_text: str, average_confidence: float, region_name: str) -> float:

    """ Compute OCR Quality Score """

    collapsed_text = collapse_whitespace(ocr_text)
    if not collapsed_text:
        return 0.0

    alpha_ratio = compute_text_alpha_ratio(collapsed_text)
    digit_ratio = compute_text_digit_ratio(collapsed_text)
    matched_term_bonus = min(count_matched_terms_in_text(collapsed_text) * 8.0, 24.0)
    length_bonus = 6.0 if 12 <= len(collapsed_text) <= 260 else 0.0
    region_bonus = 5.0 if region_name in {"center_workspace", "right_properties", "title_bar"} else 0.0
    noise_penalty = 14.0 if "Ã" in collapsed_text or "�" in collapsed_text else 0.0
    symbol_penalty = 12.0 if alpha_ratio < 0.45 else 0.0
    browser_penalty = 0.0
    if re.search(r"\b(google|scholar|deepl|translate|scopus|download)\b", collapsed_text, flags=re.IGNORECASE):
        browser_penalty += 35.0
    if region_name == "title_bar" and len(collapsed_text) > 120:
        browser_penalty += 18.0
    if region_name == "title_bar" and count_matched_terms_in_text(collapsed_text) < 2:
        browser_penalty += 12.0
    density_penalty = 8.0 if digit_ratio > 0.18 else 0.0

    return round(
        max(
            0.0,
            min(
                100.0,
                average_confidence + matched_term_bonus + length_bonus + region_bonus - noise_penalty - symbol_penalty - browser_penalty - density_penalty,
            ),
        ),
        3,
    )


def extract_best_ocr_text(frame_image: Any, capability_map: dict[str, Any]) -> tuple[str, float, str, list[str]]:

    """Recover the strongest OCR candidate from a sampled TwinCAT frame.

    Args:
        frame_image: OpenCV frame image already loaded in memory.
        capability_map: Runtime capability flags built for the current run.

    Returns:
        Tuple containing the best OCR text, its quality score, the selected
        region name, and the matched tracked-term list.
    """

    if not capability_map["ocr_available"] or cv2 is None:
        return "", 0.0, "", []

    frame_height, frame_width = frame_image.shape[:2]
    region_map = build_ocr_region_map(frame_width, frame_height)
    best_candidate_text = ""
    best_candidate_score = 0.0
    best_region_name = ""
    best_matched_term_list: list[str] = []

    for region_name, region_bounds in region_map.items():
        cropped_image = crop_frame_region(frame_image, region_bounds)
        if cropped_image.size == 0:
            continue

        for preprocess_variant_name in ["binary", "adaptive", "inverted"]:
            preprocessed_image = preprocess_frame_for_ocr(cropped_image, preprocess_variant_name)

            for page_segmentation_mode in [6, 11]:
                try:
                    ocr_data = pytesseract.image_to_data(
                        preprocessed_image,
                        lang="eng",
                        config=f"--oem 3 --psm {page_segmentation_mode}",
                        timeout=20,
                        output_type=pytesseract.Output.DICT,
                    )
                except Exception:
                    continue

                candidate_text, average_confidence = build_ocr_text_from_data(ocr_data)
                if not candidate_text:
                    continue

                candidate_score = compute_ocr_quality_score(candidate_text, average_confidence, region_name)
                if candidate_score <= best_candidate_score:
                    continue

                best_candidate_text = candidate_text
                best_candidate_score = candidate_score
                best_region_name = region_name
                best_matched_term_list = [
                    term_name
                    for term_name, term_pattern in TERM_PATTERN_MAP.items()
                    if term_pattern.search(candidate_text)
                ]

    return best_candidate_text, best_candidate_score, best_region_name, best_matched_term_list


def build_whisper_initial_prompt() -> str:

    """ Build Whisper Initial Prompt """

    return (
        "Contesto tecnico TwinCAT Beckhoff PLC TestRig machine learning. "
        "Possibili termini: FB_Predict, ML_Transmission_Error, Predict_ML, "
        "Transmission Error, TE_Calc, DataValid, TwinCAT 3 Machine Learning, "
        "temperatura, coppia, velocita, encoder, armoniche, simulation, "
        "generator cam, Matlab, Beckhoff, model manager, engine_40, engine_78."
    )


def transcribe_video_file(
    video_file_path: Path,
    model_name: str,
    language_code: str,
    beam_size: int,
    best_of: int,
    temperature: float,
    compute_type: str,
    capability_map: dict[str, Any],
) -> tuple[list[TranscriptSegment], dict[str, Any], list[str]]:

    """Transcribe a source video through Faster-Whisper when available.

    Args:
        video_file_path: Source video file to transcribe.
        model_name: Faster-Whisper model name.
        language_code: Requested transcript language or `auto`.
        beam_size: Beam-search width for decoding.
        best_of: Best-of count for decoding.
        temperature: Decoding temperature.
        compute_type: Faster-Whisper compute type.
        capability_map: Runtime capability flags for optional backends.

    Returns:
        Tuple containing the transcript segments, detected-language metadata,
        and a non-fatal issue list.
    """

    if not capability_map["faster_whisper_available"]:
        return [], {"language": None, "language_probability": None}, ["Faster-Whisper not available -> transcription skipped."]

    try:
        whisper_model = WhisperModel(model_name, device="cpu", compute_type=compute_type)
        requested_language = None if language_code.lower() == "auto" else language_code
        transcript_segments, transcript_info = whisper_model.transcribe(
            str(video_file_path),
            beam_size=beam_size,
            best_of=best_of,
            temperature=temperature,
            language=requested_language,
            vad_filter=True,
            word_timestamps=True,
            condition_on_previous_text=True,
            initial_prompt=build_whisper_initial_prompt(),
        )

        transcript_segment_list = [
            TranscriptSegment(
                start_seconds=segment.start,
                end_seconds=segment.end,
                text=collapse_whitespace(segment.text),
                quality_score=compute_transcript_quality_score(
                    raw_text=segment.text,
                    average_log_probability=getattr(segment, "avg_logprob", None),
                ),
            )
            for segment in transcript_segments
            if collapse_whitespace(segment.text)
        ]
        return (
            transcript_segment_list,
            {
                "language": getattr(transcript_info, "language", None),
                "language_probability": getattr(transcript_info, "language_probability", None),
            },
            [],
        )
    except Exception as exception:
        return [], {"language": None, "language_probability": None}, [f"Transcription failed | {exception}"]


def extract_frame_and_ocr_records(
    video_file_path: Path,
    output_root: Path,
    duration_seconds: float | None,
    interval_seconds: float,
    max_frames_per_video: int,
    capability_map: dict[str, Any],
    force_recompute: bool,
) -> tuple[list[OCRFrameRecord], list[str]]:

    """Sample frames and attach OCR evidence for one video.

    Args:
        video_file_path: Source video file being analyzed.
        output_root: Analysis directory for the current video.
        duration_seconds: Video duration used to place frame probes.
        interval_seconds: Seconds between sampled frames.
        max_frames_per_video: Maximum number of sampled frames.
        capability_map: Runtime capability flags for OpenCV and OCR.
        force_recompute: Whether cached frame images should be regenerated.

    Returns:
        Tuple containing the collected frame records and a non-fatal issue list.
    """

    if not capability_map["opencv_available"]:
        return [], ["OpenCV not available -> frame extraction skipped."]

    # Resolve Sampling Timeline
    timestamp_seconds_list = build_frame_timestamp_list(duration_seconds, interval_seconds, max_frames_per_video)
    if not timestamp_seconds_list:
        return [], ["Video duration unavailable -> frame extraction skipped."]

    frame_output_directory = output_root / "frames"
    ensure_directory(frame_output_directory)

    capture = cv2.VideoCapture(str(video_file_path))
    if not capture.isOpened():
        return [], ["OpenCV could not open video for frame extraction."]

    # Iterate Sampled Frames
    issue_list: list[str] = []
    frame_record_list: list[OCRFrameRecord] = []
    missing_tesseract_notice_emitted = False

    for frame_index, timestamp_seconds in enumerate(timestamp_seconds_list):
        frame_file_name = f"frame_{frame_index:03d}_{timestamp_seconds:010.3f}s.png".replace(".", "_", 1)
        frame_file_path = frame_output_directory / frame_file_name
        capture.set(cv2.CAP_PROP_POS_MSEC, timestamp_seconds * 1000.0)
        read_success, frame_image = capture.read()
        if not read_success:
            issue_list.append(f"Frame read failed at {timestamp_seconds:.3f}s.")
            continue

        # Persist Frame Evidence
        if force_recompute or not frame_file_path.exists():
            cv2.imwrite(str(frame_file_path), frame_image)

        # Extract OCR Evidence
        extracted_ocr_text = ""
        extracted_quality_score = 0.0
        selected_region_name = ""
        matched_term_list: list[str] = []
        if capability_map["ocr_available"]:
            try:
                extracted_ocr_text, extracted_quality_score, selected_region_name, matched_term_list = extract_best_ocr_text(
                    frame_image=frame_image,
                    capability_map=capability_map,
                )
            except Exception as exception:
                issue_list.append(f"OCR failed at {timestamp_seconds:.3f}s | {exception}")
        elif capability_map["pytesseract_available"] and not missing_tesseract_notice_emitted:
            issue_list.append("pytesseract installed but Tesseract executable missing -> OCR skipped.")
            missing_tesseract_notice_emitted = True

        # Record Frame Outcome
        frame_record_list.append(
            OCRFrameRecord(
                timestamp_seconds=timestamp_seconds,
                frame_path=frame_file_path.relative_to(PROJECT_PATH).as_posix(),
                ocr_text=extracted_ocr_text,
                quality_score=extracted_quality_score,
                selected_region_name=selected_region_name,
                matched_term_list=matched_term_list,
            )
        )

    capture.release()

    return frame_record_list, issue_list


def write_json_file(output_file_path: Path, payload: Any) -> None:

    """ Write JSON File """

    ensure_directory(output_file_path.parent)
    output_file_path.write_text(json.dumps(payload, indent=2, ensure_ascii=True), encoding="utf-8")


def format_seconds(timestamp_seconds: float) -> str:

    """ Format Seconds """

    total_seconds = int(timestamp_seconds)
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def write_transcript_markdown(output_file_path: Path, transcript_segment_list: list[TranscriptSegment]) -> None:

    """ Write Transcript Markdown """

    markdown_line_list = ["# Transcript", ""]
    if not transcript_segment_list:
        markdown_line_list.append("No transcript segments were generated.")
    else:
        for transcript_segment in transcript_segment_list:
            markdown_line_list.append(
                f"- `{format_seconds(transcript_segment.start_seconds)}` -> `{format_seconds(transcript_segment.end_seconds)}` | q={transcript_segment.quality_score:.2f} | {transcript_segment.text}"
            )

    ensure_directory(output_file_path.parent)
    output_file_path.write_text("\n".join(markdown_line_list) + "\n", encoding="utf-8")


def extract_excerpt_list(raw_text_block_list: list[str], max_excerpt_count: int = 8, excerpt_length: int = 220) -> list[str]:

    """ Extract Excerpt List """

    excerpt_list: list[str] = []

    for raw_text_block in raw_text_block_list:
        collapsed_text = collapse_whitespace(raw_text_block)
        if not collapsed_text:
            continue
        excerpt_text = collapsed_text[:excerpt_length]
        if excerpt_text not in excerpt_list:
            excerpt_list.append(excerpt_text)
        if len(excerpt_list) >= max_excerpt_count:
            break

    return excerpt_list


def extract_transcript_excerpt_list(
    transcript_segment_list: list[TranscriptSegment],
    min_quality_score: float,
    max_excerpt_count: int = 8,
    excerpt_length: int = 220,
) -> list[str]:

    """ Extract Transcript Excerpt List """

    excerpt_list: list[str] = []
    sorted_segment_list = sorted(
        transcript_segment_list,
        key=lambda transcript_segment: (transcript_segment.quality_score, len(transcript_segment.text)),
        reverse=True,
    )

    for transcript_segment in sorted_segment_list:
        if transcript_segment.quality_score < min_quality_score:
            continue

        excerpt_text = collapse_whitespace(transcript_segment.text)[:excerpt_length]
        if excerpt_text and excerpt_text not in excerpt_list:
            excerpt_list.append(excerpt_text)
        if len(excerpt_list) >= max_excerpt_count:
            break

    return excerpt_list


def extract_ocr_excerpt_list(
    frame_record_list: list[OCRFrameRecord],
    min_quality_score: float,
    max_excerpt_count: int = 8,
    excerpt_length: int = 220,
) -> list[str]:

    """ Extract OCR Excerpt List """

    excerpt_list: list[str] = []
    sorted_frame_record_list = sorted(frame_record_list, key=lambda frame_record: frame_record.quality_score, reverse=True)

    for frame_record in sorted_frame_record_list:
        if frame_record.quality_score < min_quality_score:
            continue

        excerpt_text = collapse_whitespace(frame_record.ocr_text)[:excerpt_length]
        if excerpt_text and excerpt_text not in excerpt_list:
            excerpt_list.append(excerpt_text)
        if len(excerpt_list) >= max_excerpt_count:
            break

    return excerpt_list


def extract_matched_term_list(*text_block_lists: list[str]) -> list[str]:

    """ Extract Matched Term List """

    matched_term_list: list[str] = []
    for term_name, term_pattern in TERM_PATTERN_MAP.items():
        if any(term_pattern.search(text_block) for text_block_list in text_block_lists for text_block in text_block_list):
            matched_term_list.append(term_name)

    return matched_term_list


def write_video_note_markdown(output_file_path: Path, video_analysis_record: VideoAnalysisRecord) -> None:

    """ Write Video Note Markdown """

    markdown_line_list = [
        f"# {video_analysis_record.file_name}",
        "",
        "## Overview",
        "",
        f"- Source video: `{video_analysis_record.relative_path}`",
        f"- File size bytes: `{video_analysis_record.size_bytes}`",
        f"- Duration seconds: `{video_analysis_record.duration_seconds}`",
        f"- Resolution: `{video_analysis_record.width}x{video_analysis_record.height}`",
        f"- FPS: `{video_analysis_record.fps}`",
        "",
        "## Companion Evidence",
        "",
    ]

    if video_analysis_record.associated_companion_file_list:
        for companion_file_name in video_analysis_record.associated_companion_file_list:
            markdown_line_list.append(f"- `{companion_file_name}`")
    else:
        markdown_line_list.append("- No directly matched companion note.")

    if video_analysis_record.associated_companion_note_list:
        markdown_line_list.extend(["", "## Companion Notes", ""])
        for companion_note in video_analysis_record.associated_companion_note_list:
            markdown_line_list.append(f"- {companion_note}")

    markdown_line_list.extend(["", "## Transcript Quality", ""])
    markdown_line_list.append(f"- `{video_analysis_record.transcript_quality_summary}`")
    markdown_line_list.extend(["", "## Transcript Excerpts", ""])
    markdown_line_list.extend([f"- {excerpt}" for excerpt in video_analysis_record.transcript_excerpt_list] or ["- No transcript excerpts passed the quality threshold."])

    markdown_line_list.extend(["", "## OCR Quality", ""])
    markdown_line_list.append(f"- `{video_analysis_record.ocr_quality_summary}`")
    markdown_line_list.extend(["", "## OCR Excerpts", ""])
    markdown_line_list.extend([f"- {excerpt}" for excerpt in video_analysis_record.ocr_excerpt_list] or ["- No OCR excerpts passed the quality threshold."])

    markdown_line_list.extend(["", "## Matched Terms", ""])
    markdown_line_list.extend([f"- `{matched_term}`" for matched_term in video_analysis_record.matched_term_list] or ["- No tracked terms matched."])

    markdown_line_list.extend(["", "## Issues", ""])
    markdown_line_list.extend([f"- {issue}" for issue in video_analysis_record.issue_list] or ["- No issues recorded."])

    ensure_directory(output_file_path.parent)
    output_file_path.write_text("\n".join(markdown_line_list) + "\n", encoding="utf-8")


def build_inventory_markdown(
    input_root: Path,
    output_root: Path,
    capability_map: dict[str, Any],
    video_analysis_record_list: list[VideoAnalysisRecord],
    companion_note_list: list[CompanionNote],
) -> str:

    """Build the inventory note for one rough-analysis run.

    Args:
        input_root: Video-source root used for the run.
        output_root: Analysis-artifact root used for the run.
        capability_map: Runtime capability flags recorded for the run.
        video_analysis_record_list: Per-video summary records.
        companion_note_list: Repository-local companion notes discovered beside
            the source videos.

    Returns:
        Markdown text describing the analyzed scope and runtime environment.
    """

    markdown_line_list = [
        "# TwinCAT Video Guides Inventory",
        "",
        "## Source Root",
        "",
        f"- `{input_root.relative_to(PROJECT_PATH).as_posix()}`",
        "",
        "## Output Root",
        "",
        f"- `{output_root.relative_to(PROJECT_PATH).as_posix()}`",
        "",
        "## Runtime Capabilities",
        "",
        f"- `opencv_available`: `{capability_map['opencv_available']}`",
        f"- `faster_whisper_available`: `{capability_map['faster_whisper_available']}`",
        f"- `ocr_available`: `{capability_map['ocr_available']}`",
        f"- `tesseract_executable`: `{capability_map['tesseract_executable']}`",
        "",
        "## Companion Notes",
        "",
    ]

    markdown_line_list.extend(
        [f"- `{companion_note.file_name}` | {collapse_whitespace(companion_note.text)[:180]}" for companion_note in companion_note_list]
        or ["- No companion notes found."]
    )

    markdown_line_list.extend(["", "## Video Files", ""])
    for video_analysis_record in video_analysis_record_list:
        markdown_line_list.append(
            f"- `{video_analysis_record.file_name}` | duration={video_analysis_record.duration_seconds} | transcript={video_analysis_record.transcript_generated} ({video_analysis_record.transcript_segment_count}) | transcript_quality={video_analysis_record.transcript_quality_summary} | frames={video_analysis_record.frame_extraction_generated} ({video_analysis_record.frame_record_count}) | ocr={video_analysis_record.ocr_generated} | ocr_quality={video_analysis_record.ocr_quality_summary} | matched_terms={', '.join(video_analysis_record.matched_term_list) if video_analysis_record.matched_term_list else 'none'}"
        )

    return "\n".join(markdown_line_list) + "\n"


def match_companion_notes(video_file_path: Path, companion_note_list: list[CompanionNote]) -> list[CompanionNote]:

    """ Match Companion Notes """

    video_stem = normalize_file_stem(video_file_path.name)
    video_token_set = tokenize_file_stem(video_file_path.name)
    matched_companion_note_list: list[CompanionNote] = []

    for companion_note in companion_note_list:
        companion_token_set = tokenize_file_stem(companion_note.file_name)
        direct_match = companion_note.normalized_stem and (
            companion_note.normalized_stem in video_stem or video_stem in companion_note.normalized_stem
        )
        token_overlap_count = len(video_token_set.intersection(companion_token_set))

        if direct_match or token_overlap_count >= 2:
            matched_companion_note_list.append(companion_note)

    return matched_companion_note_list


def analyze_single_video(
    video_file_path: Path,
    output_root: Path,
    companion_note_list: list[CompanionNote],
    capability_map: dict[str, Any],
    parsed_arguments: argparse.Namespace,
) -> VideoAnalysisRecord:

    """Analyze one source video into reusable rough artifacts.

    Args:
        video_file_path: Source video file to analyze.
        output_root: Root analysis directory for this run.
        companion_note_list: Candidate notes used for fuzzy matching.
        capability_map: Runtime capability flags for optional backends.
        parsed_arguments: Parsed command-line arguments for the run.

    Returns:
        Completed per-video summary record.
    """

    video_output_directory = output_root / normalize_file_stem(video_file_path.name)
    ensure_directory(video_output_directory)

    video_analysis_record = VideoAnalysisRecord(
        file_name=video_file_path.name,
        relative_path=video_file_path.relative_to(PROJECT_PATH).as_posix(),
        size_bytes=video_file_path.stat().st_size,
    )

    # Match Companion Notes
    matched_companion_note_list = match_companion_notes(video_file_path, companion_note_list)
    video_analysis_record.associated_companion_file_list = [companion_note.file_name for companion_note in matched_companion_note_list]
    video_analysis_record.associated_companion_note_list = extract_excerpt_list([companion_note.text for companion_note in matched_companion_note_list], max_excerpt_count=6)

    # Resolve Video Metadata
    metadata_map = extract_video_metadata(video_file_path)
    video_analysis_record.duration_seconds = metadata_map["duration_seconds"]
    video_analysis_record.fps = metadata_map["fps"]
    video_analysis_record.frame_count = metadata_map["frame_count"]
    video_analysis_record.width = metadata_map["width"]
    video_analysis_record.height = metadata_map["height"]

    # Extract Rough Transcript
    transcript_segment_list, transcript_metadata_map, transcript_issue_list = transcribe_video_file(
        video_file_path=video_file_path,
        model_name=parsed_arguments.transcription_model,
        language_code=parsed_arguments.transcription_language,
        beam_size=parsed_arguments.transcription_beam_size,
        best_of=parsed_arguments.transcription_best_of,
        temperature=parsed_arguments.transcription_temperature,
        compute_type=parsed_arguments.transcription_compute_type,
        capability_map=capability_map,
    ) if not parsed_arguments.disable_transcription else ([], {"language": None, "language_probability": None}, ["Transcription disabled by command-line flag."])
    video_analysis_record.issue_list.extend(transcript_issue_list)
    video_analysis_record.transcript_generated = len(transcript_segment_list) > 0
    video_analysis_record.transcript_language = transcript_metadata_map["language"]
    video_analysis_record.transcript_language_probability = transcript_metadata_map["language_probability"]
    video_analysis_record.transcript_segment_count = len(transcript_segment_list)
    transcript_text_block_list = [segment.text for segment in transcript_segment_list]
    video_analysis_record.transcript_excerpt_list = extract_transcript_excerpt_list(
        transcript_segment_list=transcript_segment_list,
        min_quality_score=parsed_arguments.transcript_min_quality_score,
    )
    video_analysis_record.transcript_quality_summary = summarize_quality_score_list(
        [segment.quality_score for segment in transcript_segment_list]
    )
    write_json_file(video_output_directory / "transcript_segments.json", [asdict(segment) for segment in transcript_segment_list])
    write_transcript_markdown(video_output_directory / "transcript.md", transcript_segment_list)

    # Sample Frames And OCR
    frame_record_list, frame_issue_list = extract_frame_and_ocr_records(
        video_file_path=video_file_path,
        output_root=video_output_directory,
        duration_seconds=video_analysis_record.duration_seconds,
        interval_seconds=parsed_arguments.frame_interval_seconds,
        max_frames_per_video=parsed_arguments.max_frames_per_video,
        capability_map=capability_map,
        force_recompute=parsed_arguments.force,
    ) if not parsed_arguments.disable_frames else ([], ["Frame extraction disabled by command-line flag."])
    video_analysis_record.issue_list.extend(frame_issue_list)
    video_analysis_record.frame_extraction_generated = len(frame_record_list) > 0
    video_analysis_record.frame_record_count = len(frame_record_list)
    frame_text_block_list = [frame_record.ocr_text for frame_record in frame_record_list if frame_record.ocr_text]
    video_analysis_record.ocr_generated = any(
        frame_record.ocr_text and frame_record.quality_score >= parsed_arguments.ocr_min_quality_score
        for frame_record in frame_record_list
    )
    video_analysis_record.ocr_excerpt_list = extract_ocr_excerpt_list(
        frame_record_list=frame_record_list,
        min_quality_score=parsed_arguments.ocr_min_quality_score,
    )
    video_analysis_record.ocr_quality_summary = summarize_quality_score_list(
        [frame_record.quality_score for frame_record in frame_record_list if frame_record.ocr_text]
    )
    write_json_file(video_output_directory / "frame_ocr_records.json", [asdict(frame_record) for frame_record in frame_record_list])

    # Merge Cross-Artifact Term Signals
    companion_text_block_list = [companion_note.text for companion_note in matched_companion_note_list]
    video_analysis_record.matched_term_list = extract_matched_term_list(
        transcript_text_block_list,
        frame_text_block_list,
        companion_text_block_list,
    )

    # Persist Per-Video Artifacts
    write_json_file(video_output_directory / "video_analysis_summary.json", asdict(video_analysis_record))
    write_video_note_markdown(video_output_directory / "video_analysis_summary.md", video_analysis_record)

    return video_analysis_record


def print_terminal_summary(video_analysis_record_list: list[VideoAnalysisRecord]) -> None:

    """ Print Terminal Summary """

    print("")
    print("=" * 96)
    print("TwinCAT Video Guide Analysis")
    print("=" * 96)
    for video_analysis_record in video_analysis_record_list:
        print(
            f"{video_analysis_record.file_name} | duration={video_analysis_record.duration_seconds} | transcript={video_analysis_record.transcript_generated} ({video_analysis_record.transcript_segment_count}) | transcript_quality={video_analysis_record.transcript_quality_summary} | frames={video_analysis_record.frame_extraction_generated} ({video_analysis_record.frame_record_count}) | ocr={video_analysis_record.ocr_generated} | ocr_quality={video_analysis_record.ocr_quality_summary} | terms={', '.join(video_analysis_record.matched_term_list) if video_analysis_record.matched_term_list else 'none'}"
        )


def main() -> int:

    """Run the rough TwinCAT/TestRig video-guide analysis workflow.

    Returns:
        Process exit code.
    """

    parsed_arguments = parse_command_line_arguments()
    input_root = Path(parsed_arguments.input_root).resolve()
    output_root = Path(parsed_arguments.output_root).resolve()
    assert input_root.exists(), f"Input root does not exist | {input_root}"
    ensure_directory(output_root)

    # Resolve Input Scope
    companion_note_list = collect_companion_note_list(input_root)
    video_file_path_list = collect_video_file_path_list(input_root, parsed_arguments.video_filter, parsed_arguments.limit_videos)
    assert video_file_path_list, "No video files matched the requested scope."

    # Resolve Runtime Capabilities
    capability_map = collect_runtime_capability_map(
        disable_transcription=parsed_arguments.disable_transcription,
        disable_frames=parsed_arguments.disable_frames,
        disable_ocr=parsed_arguments.disable_ocr,
    )

    # Process Videos
    video_analysis_record_list = [
        analyze_single_video(
            video_file_path=video_file_path,
            output_root=output_root,
            companion_note_list=companion_note_list,
            capability_map=capability_map,
            parsed_arguments=parsed_arguments,
        )
        for video_file_path in video_file_path_list
    ]

    # Persist Run-Level Outputs
    write_json_file(output_root / "video_inventory.json", [asdict(video_record) for video_record in video_analysis_record_list])
    write_json_file(output_root / "runtime_capabilities.json", capability_map)
    (output_root / "video_inventory.md").write_text(
        build_inventory_markdown(
            input_root=input_root,
            output_root=output_root,
            capability_map=capability_map,
            video_analysis_record_list=video_analysis_record_list,
            companion_note_list=companion_note_list,
        ),
        encoding="utf-8",
    )
    print_terminal_summary(video_analysis_record_list)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
