#!/usr/bin/env python3
"""Reject staged or repository files that look local, private, or sensitive."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import PurePosixPath


ALLOWED_ENV_FILES = {".env.example", ".env.sample", ".env.template"}
BLOCKED_FILENAMES = {
    ".env",
    ".git-credentials",
    ".netrc",
    ".npmrc",
    ".pypirc",
    "agents.local.md",
    "agents.override.md",
    "claude.md",
    "claude.local.md",
    "claude.override.md",
    "credentials.json",
    "id_dsa",
    "id_ecdsa",
    "id_ed25519",
    "id_rsa",
    "memory.md",
    "service-account.json",
}
BLOCKED_SUFFIXES = {
    ".jks",
    ".key",
    ".keystore",
    ".p12",
    ".pem",
    ".pfx",
    ".ovpn",
}
BLOCKED_PATH_PARTS = {
    ".aws",
    ".docker",
    ".gnupg",
    ".kube",
    ".ssh",
    "customer-data",
    "customer_data",
    "local-data",
    "memories",
    "private-data",
    "secrets",
}
ALLOW_MARKER = "safety-scan: allow-local-path"


def run_git(*args: str) -> bytes:
    return subprocess.run(
        ["git", *args],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout


def listed_files(mode: str) -> list[str]:
    if mode == "staged":
        raw = run_git(
            "diff",
            "--cached",
            "--name-only",
            "--diff-filter=ACMR",
            "-z",
        )
    else:
        raw = run_git("ls-files", "--cached", "--others", "--exclude-standard", "-z")
    return [item.decode("utf-8", "surrogateescape") for item in raw.split(b"\0") if item]


def file_bytes(path: str, mode: str) -> bytes:
    if mode == "staged":
        return run_git("show", f":{path}")
    with open(path, "rb") as handle:
        return handle.read()


def filename_problem(path: str) -> str | None:
    pure_path = PurePosixPath(path)
    lowered_parts = {part.lower() for part in pure_path.parts}
    filename = pure_path.name.lower()

    if lowered_parts & BLOCKED_PATH_PARTS:
        return "file is inside a private or local-data directory"
    if filename in BLOCKED_FILENAMES:
        return "sensitive filename"
    if filename.startswith(".env.") and filename not in ALLOWED_ENV_FILES:
        return "environment-specific file"
    if pure_path.suffix.lower() in BLOCKED_SUFFIXES:
        return "credential or private-key file extension"
    if filename.startswith("credentials.") and filename.endswith(".json"):
        return "credential file"
    if filename.startswith("service-account") and filename.endswith(".json"):
        return "service-account credential file"
    return None


def local_path_patterns() -> list[tuple[str, re.Pattern[str]]]:
    return [
        (
            "macOS user-home path",
            re.compile(r"(?<![A-Za-z0-9_])/(?:Users)/[^/\s\"']+/"),
        ),
        (
            "Linux user-home path",
            re.compile(r"(?<![A-Za-z0-9_])/(?:home)/[^/\s\"']+/"),
        ),
        (
            "macOS per-user temporary path",
            re.compile(r"(?<![A-Za-z0-9_])/(?:private/var/folders)/[^\s\"']+"),
        ),
        (
            "Windows user-home path",
            re.compile(r"(?i)(?<![A-Za-z0-9_])[A-Z]:\\Users\\[^\\\s\"']+\\"),
        ),
        (
            "temporary filesystem path",
            re.compile(r"(?<![A-Za-z0-9_])/(?:private/)?tmp/[^\s\"']+"),
        ),
    ]


def content_problems(path: str, data: bytes) -> list[tuple[int, str]]:
    if b"\0" in data:
        return []

    text = data.decode("utf-8", "replace")
    patterns = local_path_patterns()
    findings: list[tuple[int, str]] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        if ALLOW_MARKER in line:
            continue
        for label, pattern in patterns:
            if pattern.search(line):
                findings.append((line_number, label))
    return findings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check staged or local repository files for unsafe filenames and local paths."
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--staged", action="store_true", help="scan the staged snapshot")
    mode.add_argument(
        "--all-files",
        action="store_true",
        help="scan tracked and unignored files in the working tree",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    mode = "staged" if args.staged else "all-files"
    findings: list[str] = []

    try:
        paths = listed_files(mode)
        for path in paths:
            problem = filename_problem(path)
            if problem:
                findings.append(f"{path}: {problem}")
                continue

            try:
                data = file_bytes(path, mode)
            except (OSError, subprocess.CalledProcessError):
                findings.append(f"{path}: unable to inspect file contents")
                continue

            for line_number, label in content_problems(path, data):
                findings.append(f"{path}:{line_number}: {label}")
    except subprocess.CalledProcessError as exc:
        detail = exc.stderr.decode("utf-8", "replace").strip()
        print(f"repository-safety scan failed: {detail}", file=sys.stderr)
        return 2

    if findings:
        print("Repository-safety scan blocked the operation:", file=sys.stderr)
        for finding in findings:
            print(f"  - {finding}", file=sys.stderr)
        print(
            "Remove the file/path or replace it with a portable placeholder. "
            f"For an intentional documented example, add '{ALLOW_MARKER}' to that line.",
            file=sys.stderr,
        )
        return 1

    print(f"Repository-safety scan passed ({len(paths)} {mode} files checked).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
