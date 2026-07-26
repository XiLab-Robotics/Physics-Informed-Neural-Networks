"""Build a configuration-driven Wave 5.2 physics portfolio audit."""

from __future__ import annotations

import argparse
import csv
import hashlib
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[3]

EVIDENCE_FIELD_NAME_LIST = [
    "evidence_id",
    "path",
    "role",
    "required",
    "executable_oracle",
    "exists",
    "size_bytes",
    "sha256",
]
QUANTITY_FIELD_NAME_LIST = [
    "quantity",
    "availability_class",
    "causal_runtime",
    "online_model_input",
    "evidence",
]
FORMULATION_FIELD_NAME_LIST = [
    "formulation_id",
    "name",
    "feasibility_class",
    "full_pinn_eligible",
    "reason",
]
ALLOWED_FEASIBILITY_CLASS_SET = {
    "real_data_trainable",
    "offline_oracle_only",
    "synthetic_oracle_only",
    "blocked_by_data_contract",
}


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        type=Path,
        required=True,
        help="Phase-specific portfolio YAML configuration.",
    )
    return parser.parse_args()


def resolve_project_path(path_value: str | Path) -> Path:
    """Resolve a repository-relative path."""

    path = Path(path_value)
    return path if path.is_absolute() else PROJECT_ROOT / path


def project_relative_path(path: Path) -> str:
    """Return a forward-slash repository-relative path."""

    return path.resolve().relative_to(PROJECT_ROOT.resolve()).as_posix()


def load_yaml_mapping(path: Path) -> dict[str, Any]:
    """Load one YAML mapping."""

    with path.open("r", encoding="utf-8") as stream:
        payload = yaml.safe_load(stream)
    if not isinstance(payload, dict):
        raise ValueError(f"Expected YAML mapping: {path}")
    return payload


def sha256_file(path: Path) -> str:
    """Return one file's SHA-256 digest."""

    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_csv(
    path: Path,
    field_name_list: list[str],
    row_list: list[dict[str, Any]],
) -> None:
    """Write one deterministic CSV artifact."""

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames=field_name_list,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(row_list)


def build_evidence_rows(
    configuration: dict[str, Any],
) -> list[dict[str, Any]]:
    """Verify and describe every configured evidence file."""

    row_list: list[dict[str, Any]] = []
    for evidence in configuration["evidence_files"]:
        evidence_path = resolve_project_path(evidence["path"])
        exists = evidence_path.is_file()
        if bool(evidence["required"]) and not exists:
            raise FileNotFoundError(evidence_path)
        row_list.append(
            {
                "evidence_id": evidence["evidence_id"],
                "path": project_relative_path(evidence_path),
                "role": evidence["role"],
                "required": bool(evidence["required"]),
                "executable_oracle": bool(evidence["executable_oracle"]),
                "exists": exists,
                "size_bytes": evidence_path.stat().st_size if exists else 0,
                "sha256": sha256_file(evidence_path) if exists else "",
            }
        )
    return row_list


def build_report(
    summary: dict[str, Any],
    evidence_row_list: list[dict[str, Any]],
    quantity_row_list: list[dict[str, Any]],
    formulation_row_list: list[dict[str, Any]],
) -> str:
    """Build the canonical phase report."""

    phase_number = int(summary["phase_number"])
    lines = [
        f"# Phase {phase_number} {summary['phase_title']} Report",
        "",
        "## Decision",
        "",
        summary["decision"]["summary"],
        "",
        "No training campaign was prepared because no formulation is both",
        "`real_data_trainable` and full-PINN eligible.",
        "",
        "## Evidence Files",
        "",
        "| ID | Role | Exists | Executable oracle | Path |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in evidence_row_list:
        lines.append(
            f"| `{row['evidence_id']}` | {row['role']} | "
            f"`{str(bool(row['exists'])).lower()}` | "
            f"`{str(bool(row['executable_oracle'])).lower()}` | "
            f"`{row['path']}` |"
        )

    lines.extend(
        [
            "",
            "## Required Quantities",
            "",
            "| Quantity | Availability | Causal runtime | Online input | Evidence |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in quantity_row_list:
        lines.append(
            f"| `{row['quantity']}` | `{row['availability_class']}` | "
            f"`{str(bool(row['causal_runtime'])).lower()}` | "
            f"`{str(bool(row['online_model_input'])).lower()}` | "
            f"{row['evidence']} |"
        )

    lines.extend(
        [
            "",
            "## Candidate Decisions",
            "",
            "| Candidate | Feasibility | Full PINN eligible | Decision basis |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in formulation_row_list:
        lines.append(
            f"| `{row['formulation_id']}` | "
            f"`{row['feasibility_class']}` | "
            f"`{str(bool(row['full_pinn_eligible'])).lower()}` | "
            f"{row['reason']} |"
        )

    lines.extend(["", "## Key Findings", ""])
    lines.extend(
        f"- {finding}" for finding in summary["decision"]["key_findings"]
    )
    lines.extend(
        [
            "",
            "## Exit Gate",
            "",
            f"- `status: {summary['decision']['status']}`",
            "- `full_pinn_training_authorized: false`",
            f"- `physical_residual_promoted: "
            f"{str(bool(summary['decision']['physical_residual_promoted'])).lower()}`",
            f"- `advance_to_phase{summary['decision']['next_phase_number']}: "
            f"{str(bool(summary['decision']['advance_to_next_phase'])).lower()}`",
            "",
            f"Next: Phase {summary['decision']['next_phase_number']}, "
            f"{summary['decision']['next_phase_title']}.",
            "",
            "## Reproduction",
            "",
            "```powershell",
            "python -B scripts/analysis/pinn_program_portfolios/build_physics_portfolio_feasibility_audit.py `",
            f"  --config {summary['source_configuration']['path']}",
            "python -B scripts/analysis/pinn_program_portfolios/validate_physics_portfolio_feasibility_audit.py `",
            f"  --config {summary['source_configuration']['path']}",
            "```",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    """Execute a phase-specific portfolio feasibility audit."""

    arguments = parse_arguments()
    configuration_path = resolve_project_path(arguments.config)
    configuration = load_yaml_mapping(configuration_path)
    metadata = configuration["metadata"]

    evidence_row_list = build_evidence_rows(configuration)
    quantity_row_list = [
        dict(row) for row in configuration["required_quantities"]
    ]
    formulation_row_list = [
        dict(row) for row in configuration["candidate_formulations"]
    ]
    for row in formulation_row_list:
        if row["feasibility_class"] not in ALLOWED_FEASIBILITY_CLASS_SET:
            raise ValueError(
                f"Unsupported feasibility class: {row['feasibility_class']}"
            )

    output_path_map = {
        key: resolve_project_path(value)
        for key, value in configuration["outputs"].items()
    }
    write_csv(
        output_path_map["evidence_csv"],
        EVIDENCE_FIELD_NAME_LIST,
        evidence_row_list,
    )
    write_csv(
        output_path_map["quantity_csv"],
        QUANTITY_FIELD_NAME_LIST,
        quantity_row_list,
    )
    write_csv(
        output_path_map["formulation_csv"],
        FORMULATION_FIELD_NAME_LIST,
        formulation_row_list,
    )

    full_pinn_training_authorized = any(
        row["feasibility_class"] == "real_data_trainable"
        and bool(row["full_pinn_eligible"])
        for row in formulation_row_list
    )
    decision = dict(configuration["decision"])
    if full_pinn_training_authorized:
        raise ValueError(
            "A real-data full-PINN candidate requires a campaign gate, "
            "not a non-training portfolio closeout"
        )
    summary = {
        "schema_version": 1,
        "phase_number": int(metadata["phase_number"]),
        "audit_id": metadata["audit_id"],
        "phase_title": metadata["phase_title"],
        "domain_slug": metadata["domain_slug"],
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_configuration": {
            "path": project_relative_path(configuration_path),
            "sha256": sha256_file(configuration_path),
        },
        "evidence_file_count": len(evidence_row_list),
        "required_evidence_file_count": sum(
            bool(row["required"]) for row in evidence_row_list
        ),
        "all_required_evidence_files_exist": all(
            bool(row["exists"])
            for row in evidence_row_list
            if bool(row["required"])
        ),
        "executable_oracle_count": sum(
            bool(row["executable_oracle"]) for row in evidence_row_list
        ),
        "required_quantity_count": len(quantity_row_list),
        "availability_class_count": {
            availability_class: sum(
                row["availability_class"] == availability_class
                for row in quantity_row_list
            )
            for availability_class in sorted(
                {row["availability_class"] for row in quantity_row_list}
            )
        },
        "candidate_formulation_count": len(formulation_row_list),
        "formulation_class_count": {
            feasibility_class: sum(
                row["feasibility_class"] == feasibility_class
                for row in formulation_row_list
            )
            for feasibility_class in sorted(
                {row["feasibility_class"] for row in formulation_row_list}
            )
        },
        "full_pinn_training_authorized": full_pinn_training_authorized,
        "decision": decision,
    }
    output_path_map["audit_yaml"].parent.mkdir(parents=True, exist_ok=True)
    with output_path_map["audit_yaml"].open("w", encoding="utf-8") as stream:
        yaml.safe_dump(summary, stream, sort_keys=False)

    report_text = build_report(
        summary,
        evidence_row_list,
        quantity_row_list,
        formulation_row_list,
    )
    output_path_map["report_markdown"].parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    output_path_map["report_markdown"].write_text(
        report_text,
        encoding="utf-8",
    )
    print(
        "PHYSICS_PORTFOLIO_FEASIBILITY_AUDIT_OK "
        f"phase={summary['phase_number']} "
        f"evidence={len(evidence_row_list)} "
        f"quantities={len(quantity_row_list)} "
        f"formulations={len(formulation_row_list)} "
        "training_authorized=false"
    )


if __name__ == "__main__":
    main()
