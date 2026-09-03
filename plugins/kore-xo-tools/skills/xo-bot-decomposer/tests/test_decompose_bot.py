from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
ENTRY_POINT = SKILL_DIR / "scripts" / "decompose_bot.py"
PARSER_PATH = SKILL_DIR / "scripts" / "xo_export_parser.py"
FIXTURE = Path(__file__).resolve().parent / "fixtures" / "botDefinition.json"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"unable to load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class DecomposeBotTests(unittest.TestCase):
    def test_common_export_is_deterministic_and_redacts_credentials(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            first = root / "first"
            second = root / "second"
            for output in (first, second):
                subprocess.run(
                    [sys.executable, str(ENTRY_POINT), str(FIXTURE), str(output)],
                    check=True,
                    capture_output=True,
                    text=True,
                )

            self.assertEqual(
                (first / "_inventory.json").read_bytes(),
                (second / "_inventory.json").read_bytes(),
            )
            inventory = json.loads((first / "_inventory.json").read_text())
            self.assertEqual(inventory["version_route"], "XO 10 or earlier")
            self.assertEqual(inventory["summary"]["services"], 1)
            self.assertEqual(inventory["summary"]["scripts"], 1)

            combined = "\n".join(
                path.read_text(encoding="utf-8")
                for path in first.iterdir()
                if path.is_file()
            )
            for private_value in (
                "private-query-value",
                "private-header-value",
                "private-api-value",
                "private-payload-value",
                "private-preprocessor-value",
                "private-script-value",
            ):
                self.assertNotIn(private_value, combined)
            self.assertIn("[REDACTED]", combined)
            self.assertIn("{{env.service_host}}", combined)

    def test_app_definition_routes_to_xo_11(self) -> None:
        entry = load_module(ENTRY_POINT, "decompose_bot")
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "appDefinition.json"
            path.write_text("{}", encoding="utf-8")
            self.assertEqual(entry.detect_version(path, None), 11)

    def test_zip_slip_is_rejected(self) -> None:
        entry = load_module(ENTRY_POINT, "decompose_bot_safe_extract")
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            archive = root / "unsafe.zip"
            with zipfile.ZipFile(archive, "w") as stream:
                stream.writestr("../outside.txt", "unsafe")
            with self.assertRaises(ValueError):
                entry.safe_extract(archive, root / "output")

    def test_redaction_preserves_portable_references(self) -> None:
        parser = load_module(PARSER_PATH, "xo_export_parser")
        headers = parser._redact_structure(
            {
                "Authorization": "Bearer private-value",
                "X-API-Key": "{{env.api_key}}",
            }
        )
        self.assertEqual(headers["Authorization"], "[REDACTED]")
        self.assertEqual(headers["X-API-Key"], "{{env.api_key}}")


if __name__ == "__main__":
    unittest.main()

