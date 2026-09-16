#!/usr/bin/env python3
"""Deterministically decompose a Kore.ai XO bot export.

XO 10 and every earlier/legacy export are treated as XO 10 bot exports.
An appDefinition.json or explicit major version of 11 or later selects the
XO 11-compatible route. Both routes use the same parser for supported
single-definition schemas; routing alone does not establish version support.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parent.parent


def safe_extract(archive: Path, destination: Path) -> None:
    destination = destination.resolve()
    with zipfile.ZipFile(archive) as zf:
        for member in zf.infolist():
            target = (destination / member.filename).resolve()
            if destination != target and destination not in target.parents:
                raise ValueError(f"Unsafe path in archive: {member.filename}")
        zf.extractall(destination)


def choose_definition(root: Path) -> Path:
    if root.is_file() and root.suffix.lower() == ".json":
        return root

    candidates = [p for p in root.rglob("*.json") if "__MACOSX" not in p.parts]
    if not candidates:
        raise ValueError(f"No JSON files found under {root}")

    app_defs = [p for p in candidates if p.name.lower() == "appdefinition.json"]
    if app_defs:
        return max(app_defs, key=lambda p: p.stat().st_size)

    bot_defs = [p for p in candidates if p.name.lower() == "botdefinition.json"]
    if bot_defs:
        return max(bot_defs, key=lambda p: p.stat().st_size)

    non_config = [p for p in candidates if p.name.lower() != "config.json"]
    return max(non_config or candidates, key=lambda p: p.stat().st_size)


def major_version(value: object) -> int | None:
    if isinstance(value, (int, float)):
        return int(value)
    if isinstance(value, str):
        match = re.search(r"\d+", value)
        return int(match.group()) if match else None
    return None


def detect_version(definition: Path, requested: str | None) -> int:
    if requested:
        version = major_version(requested)
        if version is None:
            raise ValueError(f"Invalid XO version: {requested}")
        return 11 if version >= 11 else 10

    name = definition.name.lower()
    if name == "appdefinition.json":
        return 11
    if name == "botdefinition.json":
        return 10

    try:
        data = json.loads(definition.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return 10

    for key in ("xoVersion", "platformVersion", "version"):
        version = major_version(data.get(key)) if isinstance(data, dict) else None
        if version is not None:
            return 11 if version >= 11 else 10

    # Missing or ambiguous version metadata is a legacy export. Treat it as XO 10.
    return 10


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("export", type=Path, help="Bot export ZIP, JSON, or extracted folder")
    parser.add_argument("output", nargs="?", type=Path, help="Extraction output directory")
    parser.add_argument("--xo-version", help="Explicit major version; 10 and below use XO 10")
    args = parser.parse_args()

    export = args.export.expanduser().resolve()
    if not export.exists():
        parser.error(f"export does not exist: {export}")

    output = args.output.expanduser().resolve() if args.output else Path(
        tempfile.mkdtemp(prefix="xo-extracted-")
    )
    output.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="xo-bot-export-") as tmp:
        source = export
        if export.is_file() and export.suffix.lower() == ".zip":
            source = Path(tmp)
            safe_extract(export, source)

        definition = choose_definition(source)
        version = detect_version(definition, args.xo_version)
        extractor = SKILL_ROOT / "scripts" / "xo_export_parser.py"

        print(f"Definition: {definition}")
        print(f"Version route: XO {version}" + (" (XO 10 includes all earlier versions)" if version == 10 else ""))
        print(f"Output: {output}")
        completed = subprocess.run(
            [
                sys.executable,
                str(extractor),
                str(definition),
                str(output),
                "--version-route",
                f"XO {version}" + (" or earlier" if version == 10 else ""),
            ],
            check=False,
        )
        return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
