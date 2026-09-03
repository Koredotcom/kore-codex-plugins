#!/usr/bin/env python3
"""Advisory structural preflight for Kore Agent Designer Markdown files."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


MARKER = "<!-- kore-agent-design-template:v1 -->"
FUNCTIONAL_HEADINGS = [
    "Document Control",
    "Agent Purpose and Business Outcome",
    "Agent Type and Operating Model",
    "Users, Stakeholders, and Roles",
    "Scope",
    "Channels, Languages, and Experience Constraints",
    "Assumptions and Dependencies",
    "User Goals and Use-Case Inventory",
    "Functional SOPs",
    "Long-Running Workflows, Human Tasks, and Approvals",
    "Knowledge and Content Requirements",
    "Functional Integration Requirements",
    "Human Handoff and Escalation",
    "Guardrails, Privacy, and Compliance",
    "Non-Functional Requirements",
    "Success Measures and Acceptance Criteria",
    "Risks, Decisions, and Open Questions",
]
TECHNICAL_HEADINGS = [
    "Document Control",
    "Functional Design Traceability",
    "Solution Context and Architecture",
    "Kore.ai Product and Component Mapping",
    "Environments and Deployment Model",
    "Conversation and Workflow Orchestration",
    "Channel and Locale Design",
    "Knowledge and Retrieval Design",
    "Prompt, Model, Tool, and Guardrail Design",
    "Integration Architecture",
    "Authentication and Authorization",
    "Data, Context, and Session State",
    "Workflow Persistence and Resumption",
    "Human Tasks and Approval Architecture",
    "Error Handling, Retries, and Recovery",
    "Human Handoff Design",
    "Security, Privacy, and Compliance",
    "Observability and Operational Support",
    "Testing Strategy",
    "Release and Rollback Plan",
    "Technical Risks, Decisions, and Open Questions",
]
TRACE_PREFIXES = {"UC", "FR", "BR", "NFR", "INT", "AC"}
ID_RE = re.compile(r"\b(UC|FR|BR|NFR|INT|AC|TD|OQ)-(\d+)\b")
ANGLE_PLACEHOLDER_RE = re.compile(r"<[^>\n]{1,120}>")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run advisory structural checks on Kore Agent Designer files."
    )
    parser.add_argument("--functional", type=Path, help="Functional design Markdown file")
    parser.add_argument("--technical", type=Path, help="Technical design Markdown file")
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    if not args.functional and not args.technical:
        parser.error("provide --functional, --technical, or both")
    return args


def markdown_h2_sections(text: str) -> tuple[list[str], dict[str, list[str]]]:
    headings: list[str] = []
    sections: dict[str, list[str]] = {}
    current: str | None = None
    fence: str | None = None

    for raw_line in text.splitlines():
        stripped = raw_line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            token = stripped[:3]
            if fence is None:
                fence = token
            elif fence == token:
                fence = None
            if current is not None:
                sections[current].append(raw_line)
            continue

        if fence is None:
            match = re.match(r"^##\s+(.+?)\s*$", raw_line)
            if match:
                current = match.group(1).strip()
                headings.append(current)
                sections.setdefault(current, [])
                continue

        if current is not None:
            sections[current].append(raw_line)

    return headings, sections


def recognize(text: str, kind: str, headings: list[str]) -> tuple[bool, str]:
    expected = FUNCTIONAL_HEADINGS if kind == "functional" else TECHNICAL_HEADINGS
    declared = re.search(r"\*\*Document type:\*\*\s*(Functional|Technical)\b", text, re.I)
    declared_matches = bool(declared and declared.group(1).lower() == kind)
    overlap = len(set(headings) & set(expected)) / len(expected)

    if MARKER in text and declared_matches:
        return True, "template marker and document type"
    if declared_matches and overlap >= 0.6:
        return True, "document type and heading overlap"
    if overlap >= 0.8:
        return True, "high heading overlap"
    return False, f"only {overlap:.0%} of expected headings recognized"


def identifiers(text: str) -> tuple[set[str], list[str]]:
    valid: set[str] = set()
    malformed: list[str] = []
    for prefix, digits in ID_RE.findall(text):
        token = f"{prefix}-{digits}"
        if len(digits) == 3:
            valid.add(token)
        else:
            malformed.append(token)
    return valid, sorted(set(malformed))


def inspect(path: Path, kind: str) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    headings, sections = markdown_h2_sections(text)
    expected = FUNCTIONAL_HEADINGS if kind == "functional" else TECHNICAL_HEADINGS
    recognized, recognition = recognize(text, kind, headings)
    result: dict[str, Any] = {
        "path": str(path),
        "documentType": kind,
        "status": "UNRECOGNIZED_FORMAT",
        "recognition": recognition,
        "warnings": [],
        "inventory": {},
    }
    if not recognized:
        return result

    missing = [heading for heading in expected if heading not in headings]
    duplicate = sorted({heading for heading in headings if headings.count(heading) > 1})
    unexpected = [heading for heading in headings if heading not in expected]
    found_expected = [heading for heading in headings if heading in expected]
    order_ok = found_expected == [heading for heading in expected if heading in headings]
    empty = [
        heading
        for heading in expected
        if heading in sections and not "".join(sections[heading]).strip()
    ]
    valid_ids, malformed_ids = identifiers(text)
    tbd_count = len(re.findall(r"\bTBD\b", text, re.I))
    placeholder_text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    placeholder_count = len(ANGLE_PLACEHOLDER_RE.findall(placeholder_text))

    warnings: list[str] = []
    if missing:
        warnings.append("Missing required headings: " + ", ".join(missing))
    if duplicate:
        warnings.append("Duplicate level-two headings: " + ", ".join(duplicate))
    if unexpected:
        warnings.append("Unexpected level-two headings: " + ", ".join(unexpected))
    if not order_ok:
        warnings.append("Required headings are not in the template order")
    if empty:
        warnings.append("Empty required sections: " + ", ".join(empty))
    if malformed_ids:
        warnings.append("Identifiers do not use three digits: " + ", ".join(malformed_ids))
    if tbd_count:
        warnings.append(f"Tracked TBD occurrences: {tbd_count}")
    if placeholder_count:
        warnings.append(f"Possible unresolved angle-bracket placeholders: {placeholder_count}")

    result["status"] = "WARN" if warnings else "PASS"
    result["warnings"] = warnings
    result["inventory"] = {
        "requiredHeadingCount": len(expected),
        "recognizedRequiredHeadingCount": len(set(headings) & set(expected)),
        "identifiers": sorted(valid_ids),
        "tbdCount": tbd_count,
        "anglePlaceholderCount": placeholder_count,
    }
    return result


def add_traceability(functional: dict[str, Any], technical: dict[str, Any]) -> dict[str, Any]:
    if functional["status"] == "UNRECOGNIZED_FORMAT" or technical["status"] == "UNRECOGNIZED_FORMAT":
        return {
            "status": "NOT_CHECKED",
            "reason": "both documents must use a recognized format",
        }

    functional_ids = set(functional["inventory"]["identifiers"])
    technical_ids = set(technical["inventory"]["identifiers"])
    functional_trace = {item for item in functional_ids if item.split("-", 1)[0] in TRACE_PREFIXES}
    technical_trace = {item for item in technical_ids if item.split("-", 1)[0] in TRACE_PREFIXES}
    unreferenced = sorted(functional_trace - technical_trace)
    orphaned = sorted(technical_trace - functional_trace)
    warnings: list[str] = []
    if unreferenced:
        warnings.append("Functional identifiers not referenced technically: " + ", ".join(unreferenced))
    if orphaned:
        warnings.append("Technical references absent from the functional design: " + ", ".join(orphaned))
    return {
        "status": "WARN" if warnings else "PASS",
        "warnings": warnings,
        "functionalTraceIdentifiers": sorted(functional_trace),
        "technicalTraceIdentifiers": sorted(technical_trace),
    }


def human_report(report: dict[str, Any]) -> str:
    lines = ["Kore Agent Designer structural preflight"]
    for key in ("functional", "technical"):
        item = report.get(key)
        if not item:
            continue
        lines.append(f"{key.capitalize()}: {item['status']} — {item['path']}")
        lines.append(f"  Recognition: {item['recognition']}")
        for warning in item["warnings"]:
            lines.append(f"  Warning: {warning}")
    trace = report.get("traceability")
    if trace:
        lines.append(f"Traceability: {trace['status']}")
        if trace.get("reason"):
            lines.append(f"  {trace['reason']}")
        for warning in trace.get("warnings", []):
            lines.append(f"  Warning: {warning}")
    lines.append("Advisory only: complete semantic review is still required.")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    report: dict[str, Any] = {"schemaVersion": "1.0", "advisory": True}
    try:
        if args.functional:
            report["functional"] = inspect(args.functional, "functional")
        if args.technical:
            report["technical"] = inspect(args.technical, "technical")
    except (OSError, UnicodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if "functional" in report and "technical" in report:
        report["traceability"] = add_traceability(report["functional"], report["technical"])

    if args.as_json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(human_report(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
