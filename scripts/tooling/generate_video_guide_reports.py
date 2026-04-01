""" Generate TwinCAT Video Guide Reports """

from __future__ import annotations

# Disable Bytecode Cache Writes
import sys
sys.dont_write_bytecode = True

# Import Python Utilities
import argparse
import json
import shutil
from dataclasses import dataclass
from pathlib import Path

PROJECT_PATH = Path(__file__).resolve().parents[2]
DEFAULT_ANALYSIS_ROOT = PROJECT_PATH / ".temp" / "video_guides" / "_analysis"
DEFAULT_REPORT_ROOT = PROJECT_PATH / "doc" / "reference_codes" / "video_guides"
DEFAULT_MAX_IMAGES = 4
DEFAULT_MAX_TRANSCRIPT_HIGHLIGHTS = 10
DEFAULT_MAX_OCR_HIGHLIGHTS = 8
TERM_GROUP_MAP = {
    "runtime": ["TwinCAT", "Beckhoff", "TestRig", "speed", "torque", "temperature", "angle"],
    "prediction": ["FB_Predict", "ML_Transmission_Error", "Predict_ML", "engine_<n>", "harmonic"],
    "data": ["TE_Calc", "DataValid", "simulation", "Matlab"],
}


@dataclass
class TranscriptSegment:

    """ Store Transcript Segment """

    start_seconds: float
    end_seconds: float
    text: str
    quality_score: float = 0.0


@dataclass
class OCRFrameRecord:

    """ Store OCR Frame Record """

    timestamp_seconds: float
    frame_path: str
    ocr_text: str
    quality_score: float = 0.0
    selected_region_name: str = ""
    matched_term_list: list[str] = None


def build_argument_parser() -> argparse.ArgumentParser:

    """ Build Argument Parser """

    argument_parser = argparse.ArgumentParser(
        description="Generate repository-owned Markdown reports from TwinCAT/TestRig video-analysis artifacts.",
    )
    argument_parser.add_argument("--analysis-root", default=str(DEFAULT_ANALYSIS_ROOT), help="Analysis artifact root.")
    argument_parser.add_argument("--report-root", default=str(DEFAULT_REPORT_ROOT), help="Repository-owned report root.")
    argument_parser.add_argument("--video-filter", default="", help="Optional case-insensitive filter for analyzed-video directory names.")
    argument_parser.add_argument("--limit-videos", type=int, default=0, help="Optional maximum number of report directories.")
    argument_parser.add_argument("--max-images", type=int, default=DEFAULT_MAX_IMAGES, help="Maximum reference images per report.")

    return argument_parser


def parse_command_line_arguments() -> argparse.Namespace:

    """ Parse Command-Line Arguments """

    return build_argument_parser().parse_args()


def ensure_directory(directory_path: Path) -> None:

    """ Ensure Directory """

    directory_path.mkdir(parents=True, exist_ok=True)


def read_json_file(input_file_path: Path) -> object:

    """ Read JSON File """

    return json.loads(input_file_path.read_text(encoding="utf-8"))


def collapse_whitespace(raw_text: str) -> str:

    """ Collapse Whitespace """

    return " ".join(str(raw_text).split()).strip()


def format_seconds(timestamp_seconds: float) -> str:

    """ Format Seconds """

    total_seconds = int(timestamp_seconds)
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def slugify_text(raw_text: str) -> str:

    """ Slugify Text """

    return "".join(character.lower() if character.isalnum() else "_" for character in raw_text).strip("_")


def normalize_markdown_spacing(markdown_line_list: list[str]) -> str:

    """ Normalize Markdown Spacing """

    normalized_line_list: list[str] = []
    previous_line_blank = False

    for markdown_line in markdown_line_list:
        current_line_blank = markdown_line == ""
        if current_line_blank and previous_line_blank:
            continue
        normalized_line_list.append(markdown_line)
        previous_line_blank = current_line_blank

    return "\n".join(normalized_line_list).rstrip() + "\n"


def collect_analysis_directory_list(analysis_root: Path, video_filter: str, limit_videos: int) -> list[Path]:

    """ Collect Analysis Directories """

    analysis_directory_list: list[Path] = []
    normalized_filter = video_filter.lower().strip()

    for directory_path in sorted(analysis_root.iterdir()):
        if not directory_path.is_dir():
            continue
        summary_file_path = directory_path / "video_analysis_summary.json"
        if not summary_file_path.exists():
            continue
        video_summary = read_json_file(summary_file_path)
        if not video_summary.get("transcript_generated") and not video_summary.get("ocr_generated"):
            continue
        if normalized_filter and normalized_filter not in directory_path.name.lower():
            continue
        analysis_directory_list.append(directory_path)

    return analysis_directory_list[:limit_videos] if limit_videos > 0 else analysis_directory_list


def load_transcript_segment_list(analysis_directory: Path) -> list[TranscriptSegment]:

    """ Load Transcript Segment List """

    transcript_file_path = analysis_directory / "transcript_segments.json"
    if not transcript_file_path.exists():
        return []

    raw_transcript_segment_list = read_json_file(transcript_file_path)
    return [
        TranscriptSegment(
            start_seconds=float(raw_segment["start_seconds"]),
            end_seconds=float(raw_segment["end_seconds"]),
            text=collapse_whitespace(raw_segment["text"]),
            quality_score=float(raw_segment.get("quality_score", 0.0)),
        )
        for raw_segment in raw_transcript_segment_list
        if collapse_whitespace(raw_segment["text"])
    ]


def load_ocr_frame_record_list(analysis_directory: Path) -> list[OCRFrameRecord]:

    """ Load OCR Frame Record List """

    frame_record_file_path = analysis_directory / "frame_ocr_records.json"
    if not frame_record_file_path.exists():
        return []

    raw_frame_record_list = read_json_file(frame_record_file_path)
    return [
        OCRFrameRecord(
            timestamp_seconds=float(raw_frame_record["timestamp_seconds"]),
            frame_path=raw_frame_record["frame_path"],
            ocr_text=collapse_whitespace(raw_frame_record["ocr_text"]),
            quality_score=float(raw_frame_record.get("quality_score", 0.0)),
            selected_region_name=raw_frame_record.get("selected_region_name", ""),
            matched_term_list=list(raw_frame_record.get("matched_term_list", [])),
        )
        for raw_frame_record in raw_frame_record_list
    ]


def extract_keyword_line_list(transcript_segment_list: list[TranscriptSegment], keyword_list: list[str], limit_items: int) -> list[str]:

    """ Extract Keyword Line List """

    transcript_line_list: list[str] = []

    for transcript_segment in transcript_segment_list:
        lowered_text = transcript_segment.text.lower()
        if not any(keyword.lower() in lowered_text for keyword in keyword_list):
            continue
        if transcript_segment.quality_score < 0.35:
            continue

        transcript_line = f"`{format_seconds(transcript_segment.start_seconds)}` | q={transcript_segment.quality_score:.2f} | {transcript_segment.text}"
        if transcript_line not in transcript_line_list:
            transcript_line_list.append(transcript_line)
        if len(transcript_line_list) >= limit_items:
            break

    return transcript_line_list


def build_summary_bullet_list(video_summary: dict, transcript_segment_list: list[TranscriptSegment], ocr_frame_record_list: list[OCRFrameRecord]) -> list[str]:

    """ Build Summary Bullet List """

    summary_bullet_list: list[str] = []
    matched_term_list = video_summary.get("matched_term_list", [])

    if "FB_Predict" in matched_term_list or "ML_Transmission_Error" in matched_term_list:
        summary_bullet_list.append("The video contains direct evidence about the PLC-side prediction blocks and how the machine-learning path is orchestrated inside TwinCAT.")

    task_highlight_list = extract_keyword_line_list(
        transcript_segment_list,
        ["task", "microsecondi", "microsecond", "ritardo", "delay", "link"],
        limit_items=2,
    )
    if task_highlight_list:
        summary_bullet_list.append("The transcript discusses multi-task execution timing and value exchange delays between the fast path and the machine-learning path.")

    if any(term in matched_term_list for term in ["speed", "torque", "temperature", "TE_Calc", "Matlab", "simulation"]):
        summary_bullet_list.append("The video is useful for understanding the practical simulation and data-interface contract used around the TwinCAT workflow.")

    if any(frame_record.ocr_text and frame_record.quality_score >= 42.0 for frame_record in ocr_frame_record_list):
        summary_bullet_list.append("Quality-gated OCR recovered readable UI text from selected TwinCAT screen regions instead of dumping unreadable full-frame text.")
    else:
        summary_bullet_list.append("Reference images were captured even when OCR did not pass the quality threshold, so the report still preserves visual checkpoints for later manual review.")

    return summary_bullet_list[:4]


def is_report_worthy_ocr_frame(frame_record: OCRFrameRecord) -> bool:

    """ Determine Whether OCR Frame Is Report Worthy """

    if not frame_record.ocr_text or frame_record.quality_score < 42.0:
        return False
    if len(frame_record.ocr_text) < 25 and not frame_record.matched_term_list:
        return False
    if frame_record.selected_region_name == "title_bar" and not frame_record.matched_term_list:
        return False
    if frame_record.selected_region_name == "title_bar" and len(frame_record.ocr_text) > 180:
        return False
    return True


def build_deployment_impact_bullet_list(video_summary: dict, transcript_segment_list: list[TranscriptSegment]) -> list[str]:

    """ Build Deployment Impact Bullet List """

    matched_term_list = video_summary.get("matched_term_list", [])
    impact_bullet_list: list[str] = []

    if "FB_Predict" in matched_term_list:
        impact_bullet_list.append("The report reinforces that future exported models must fit the Beckhoff prediction-wrapper contract already used in the TestRig PLC code.")
    if "ML_Transmission_Error" in matched_term_list or "harmonic" in matched_term_list:
        impact_bullet_list.append("The video remains relevant for deciding whether a new model can stay inside the current harmonic reconstruction structure or whether TwinCAT logic must change.")

    task_highlight_list = extract_keyword_line_list(
        transcript_segment_list,
        ["task", "microsecondi", "microsecond", "ritardo", "delay"],
        limit_items=1,
    )
    if task_highlight_list:
        impact_bullet_list.append("Any future deployment path must be evaluated together with the task-cycle and inter-task delay budget, not only with raw inference speed.")

    if any(term in matched_term_list for term in ["speed", "torque", "temperature", "TE_Calc", "Matlab"]):
        impact_bullet_list.append("The video helps preserve the practical input, sign, and reconstruction assumptions that a TwinCAT-ready model export must respect.")

    return impact_bullet_list[:4]


def select_reference_frame_record_list(ocr_frame_record_list: list[OCRFrameRecord], max_images: int) -> list[OCRFrameRecord]:

    """ Select Reference Frame Record List """

    if not ocr_frame_record_list:
        return []

    sorted_frame_record_list = sorted(
        ocr_frame_record_list,
        key=lambda frame_record: (frame_record.quality_score, len(frame_record.ocr_text), -frame_record.timestamp_seconds),
        reverse=True,
    )
    selected_frame_record_list: list[OCRFrameRecord] = []
    selected_source_path_set: set[str] = set()

    for frame_record in sorted_frame_record_list:
        if frame_record.frame_path in selected_source_path_set:
            continue
        selected_frame_record_list.append(frame_record)
        selected_source_path_set.add(frame_record.frame_path)
        if len(selected_frame_record_list) >= max_images:
            break

    if not selected_frame_record_list:
        selected_frame_record_list = ocr_frame_record_list[:max_images]

    return selected_frame_record_list


def copy_reference_image_list(selected_frame_record_list: list[OCRFrameRecord], report_asset_directory: Path) -> list[tuple[OCRFrameRecord, Path]]:

    """ Copy Reference Image List """

    copied_image_tuple_list: list[tuple[OCRFrameRecord, Path]] = []
    ensure_directory(report_asset_directory)

    for image_index, frame_record in enumerate(selected_frame_record_list):
        source_frame_path = PROJECT_PATH / Path(frame_record.frame_path)
        if not source_frame_path.exists():
            continue

        destination_frame_path = report_asset_directory / f"reference_{image_index + 1:02d}_{format_seconds(frame_record.timestamp_seconds).replace(':', '-')}.png"
        shutil.copy2(source_frame_path, destination_frame_path)
        copied_image_tuple_list.append((frame_record, destination_frame_path))

    return copied_image_tuple_list


def build_report_markdown(
    video_summary: dict,
    transcript_segment_list: list[TranscriptSegment],
    ocr_frame_record_list: list[OCRFrameRecord],
    companion_note_list: list[str],
    copied_image_tuple_list: list[tuple[OCRFrameRecord, Path]],
    report_directory: Path,
) -> str:

    """ Build Report Markdown """

    transcript_highlight_list = extract_keyword_line_list(
        transcript_segment_list,
        ["TwinCAT", "task", "microsecond", "FB", "Predict", "torque", "temperature", "velocity", "veloc", "Matlab", "TE_Calc"],
        limit_items=DEFAULT_MAX_TRANSCRIPT_HIGHLIGHTS,
    )
    if not transcript_highlight_list:
        transcript_highlight_list = [
            f"`{format_seconds(transcript_segment.start_seconds)}` | q={transcript_segment.quality_score:.2f} | {transcript_segment.text}"
            for transcript_segment in sorted(
                transcript_segment_list,
                key=lambda item: (item.quality_score, len(item.text)),
                reverse=True,
            )
            if transcript_segment.quality_score >= 0.42 and transcript_segment.text
        ][:DEFAULT_MAX_TRANSCRIPT_HIGHLIGHTS]

    ocr_highlight_list = [
        (
            format_seconds(frame_record.timestamp_seconds),
            frame_record.quality_score,
            frame_record.selected_region_name,
            frame_record.ocr_text,
        )
        for frame_record in sorted(ocr_frame_record_list, key=lambda item: item.quality_score, reverse=True)
        if is_report_worthy_ocr_frame(frame_record)
    ][:DEFAULT_MAX_OCR_HIGHLIGHTS]

    summary_bullet_list = build_summary_bullet_list(video_summary, transcript_segment_list, ocr_frame_record_list)
    deployment_impact_bullet_list = build_deployment_impact_bullet_list(video_summary, transcript_segment_list)

    markdown_line_list = [
        f"# {video_summary['file_name']}",
        "",
        "## Overview",
        "",
        f"- Source video: `{video_summary['relative_path']}`",
        f"- Source analysis directory: `{Path(video_summary['relative_path']).stem}` under `.temp/video_guides/_analysis/`",
        f"- Duration seconds: `{video_summary.get('duration_seconds')}`",
        f"- Resolution: `{video_summary.get('width')}x{video_summary.get('height')}`",
        f"- Transcript segments: `{video_summary.get('transcript_segment_count')}`",
        f"- Transcript quality summary: `{video_summary.get('transcript_quality_summary', {})}`",
        f"- OCR extracted: `{video_summary.get('ocr_generated')}`",
        f"- OCR quality summary: `{video_summary.get('ocr_quality_summary', {})}`",
        "",
        "## Video Scope",
        "",
        f"- Matched term set: `{', '.join(video_summary.get('matched_term_list', [])) if video_summary.get('matched_term_list') else 'none'}`",
        f"- Companion-note matches: `{', '.join(video_summary.get('associated_companion_file_list', [])) if video_summary.get('associated_companion_file_list') else 'none'}`",
        "",
        "## Executive Summary",
        "",
    ]

    markdown_line_list.extend([f"- {summary_bullet}" for summary_bullet in summary_bullet_list] or ["- No summary bullets were generated."])

    markdown_line_list.extend(["", "## Key Technical Findings", ""])
    for group_name, group_term_list in TERM_GROUP_MAP.items():
        matching_term_list = [term_name for term_name in video_summary.get("matched_term_list", []) if term_name in group_term_list]
        if not matching_term_list:
            continue
        markdown_line_list.append(f"- `{group_name}` terms observed: `{', '.join(matching_term_list)}`")

    markdown_line_list.extend(["", "## Important Notes And Caveats", ""])
    markdown_line_list.extend([f"- {companion_note}" for companion_note in companion_note_list] or ["- No companion-note caveats were attached to this report."])
    markdown_line_list.extend([f"- {issue}" for issue in video_summary.get("issue_list", [])] or ["- No pipeline issues were recorded for this video."])

    markdown_line_list.extend(["", "## Reference Images", ""])
    if copied_image_tuple_list:
        for image_index, (frame_record, copied_image_path) in enumerate(copied_image_tuple_list, start=1):
            relative_image_path = copied_image_path.relative_to(report_directory).as_posix()
            markdown_line_list.append(f"### Reference Image {image_index}")
            markdown_line_list.append("")
            markdown_line_list.append(f"Timestamp: `{format_seconds(frame_record.timestamp_seconds)}`")
            markdown_line_list.append("")
            markdown_line_list.append(f"![Reference image at {format_seconds(frame_record.timestamp_seconds)}]({relative_image_path})")
            markdown_line_list.append("")
    else:
        markdown_line_list.append("- No reference images were copied for this report.")

    markdown_line_list.extend(["", "## Transcript Highlights", ""])
    if transcript_highlight_list:
        for highlight_index, transcript_highlight in enumerate(transcript_highlight_list, start=1):
            highlight_timestamp, _, highlight_text = transcript_highlight.partition("` | ")
            highlight_quality = ""
            if highlight_text.startswith("q=") and " | " in highlight_text:
                highlight_quality, _, highlight_text = highlight_text.partition(" | ")
            formatted_timestamp = highlight_timestamp.strip("`")
            markdown_line_list.append(f"### Transcript Highlight {highlight_index}")
            markdown_line_list.append("")
            markdown_line_list.append(f"Timestamp: `{formatted_timestamp}`")
            if highlight_quality:
                markdown_line_list.append("")
                markdown_line_list.append(f"Quality score: `{highlight_quality.replace('q=', '')}`")
            markdown_line_list.append("")
            markdown_line_list.append("```text")
            markdown_line_list.append(highlight_text)
            markdown_line_list.append("```")
            markdown_line_list.append("")
    else:
        markdown_line_list.append("- No transcript highlights matched the tracked query terms.")

    markdown_line_list.extend(["", "## OCR Highlights", ""])
    if ocr_highlight_list:
        for highlight_index, (highlight_timestamp, highlight_score, region_name, highlight_text) in enumerate(ocr_highlight_list, start=1):
            markdown_line_list.append(f"### OCR Highlight {highlight_index}")
            markdown_line_list.append("")
            markdown_line_list.append(f"Timestamp: `{highlight_timestamp}`")
            markdown_line_list.append("")
            markdown_line_list.append(f"Quality score: `{highlight_score:.2f}`")
            if region_name:
                markdown_line_list.append("")
                markdown_line_list.append(f"Selected region: `{region_name}`")
            markdown_line_list.append("")
            markdown_line_list.append("```text")
            markdown_line_list.append(highlight_text)
            markdown_line_list.append("```")
            markdown_line_list.append("")
    else:
        markdown_line_list.append("- No OCR excerpt passed the quality threshold for this report.")

    markdown_line_list.extend(["", "## Potential Impact On TwinCAT Model Deployment", ""])
    markdown_line_list.extend([f"- {impact_bullet}" for impact_bullet in deployment_impact_bullet_list] or ["- No deployment-impact bullets were generated."])

    return normalize_markdown_spacing(markdown_line_list)


def write_report_index(report_root: Path, generated_report_path_list: list[Path]) -> None:

    """ Write Report Index """

    markdown_line_list = [
        "# Video Guide Reports",
        "",
        "This folder contains repository-owned reports generated from the",
        "TwinCAT/TestRig video-analysis artifacts.",
        "",
        "## Reports",
        "",
    ]

    for report_path in generated_report_path_list:
        relative_report_path = report_path.relative_to(report_root).as_posix()
        markdown_line_list.append(f"- [{report_path.stem}]({relative_report_path})")

    ensure_directory(report_root)
    (report_root / "README.md").write_text("\n".join(markdown_line_list) + "\n", encoding="utf-8")


def generate_single_report(analysis_directory: Path, report_root: Path, max_images: int) -> Path:

    """ Generate Single Report """

    video_summary = read_json_file(analysis_directory / "video_analysis_summary.json")
    transcript_segment_list = load_transcript_segment_list(analysis_directory)
    ocr_frame_record_list = load_ocr_frame_record_list(analysis_directory)
    report_slug = slugify_text(Path(video_summary["file_name"]).stem)
    report_directory = report_root / report_slug
    report_asset_directory = report_directory / "assets"
    ensure_directory(report_directory)

    selected_frame_record_list = select_reference_frame_record_list(ocr_frame_record_list, max_images=max_images)
    copied_image_tuple_list = copy_reference_image_list(selected_frame_record_list, report_asset_directory)
    report_markdown = build_report_markdown(
        video_summary=video_summary,
        transcript_segment_list=transcript_segment_list,
        ocr_frame_record_list=ocr_frame_record_list,
        companion_note_list=video_summary.get("associated_companion_note_list", []),
        copied_image_tuple_list=copied_image_tuple_list,
        report_directory=report_directory,
    )

    report_file_path = report_directory / f"{report_slug}_report.md"
    report_file_path.write_text(report_markdown, encoding="utf-8")

    return report_file_path


def main() -> int:

    """ Generate Video Guide Reports """

    parsed_arguments = parse_command_line_arguments()
    analysis_root = Path(parsed_arguments.analysis_root).resolve()
    report_root = Path(parsed_arguments.report_root).resolve()
    assert analysis_root.exists(), f"Analysis root does not exist | {analysis_root}"
    ensure_directory(report_root)

    analysis_directory_list = collect_analysis_directory_list(
        analysis_root=analysis_root,
        video_filter=parsed_arguments.video_filter,
        limit_videos=parsed_arguments.limit_videos,
    )
    assert analysis_directory_list, "No analyzed-video directories matched the requested scope."

    generated_report_path_list = [
        generate_single_report(
            analysis_directory=analysis_directory,
            report_root=report_root,
            max_images=parsed_arguments.max_images,
        )
        for analysis_directory in analysis_directory_list
    ]
    write_report_index(report_root, generated_report_path_list)

    print("")
    print("=" * 96)
    print("Generated TwinCAT Video Guide Reports")
    print("=" * 96)
    for generated_report_path in generated_report_path_list:
        print(generated_report_path.relative_to(PROJECT_PATH).as_posix())

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
