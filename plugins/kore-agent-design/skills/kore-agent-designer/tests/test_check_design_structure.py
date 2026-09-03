import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
SCRIPT = SKILL_DIR / "scripts" / "check_design_structure.py"
FIXTURES = Path(__file__).resolve().parent / "fixtures"
FUNCTIONAL_TEMPLATE = SKILL_DIR / "references" / "functional-design-template.md"
TECHNICAL_TEMPLATE = SKILL_DIR / "references" / "technical-design-template.md"


def load_checker_module():
    spec = importlib.util.spec_from_file_location("check_design_structure", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("unable to load structural checker")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def template_h2s(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"```markdown\n(.*?)\n```", text, re.DOTALL)
    if match is None:
        raise AssertionError(f"Markdown template block not found in {path}")
    return re.findall(r"^##\s+(.+?)\s*$", match.group(1), re.MULTILINE)


class CheckDesignStructureTests(unittest.TestCase):
    def run_checker(self, *args: str) -> dict:
        completed = subprocess.run(
            [sys.executable, str(SCRIPT), "--json", *args],
            check=True,
            capture_output=True,
            text=True,
        )
        return json.loads(completed.stdout)

    def test_standard_pair_passes(self) -> None:
        result = self.run_checker(
            "--functional",
            str(FIXTURES / "standard_functional.md"),
            "--technical",
            str(FIXTURES / "standard_technical.md"),
        )
        self.assertEqual(result["functional"]["status"], "PASS")
        self.assertEqual(result["technical"]["status"], "PASS")
        self.assertEqual(result["traceability"]["status"], "PASS")

    def test_checker_headings_match_template_references(self) -> None:
        checker = load_checker_module()
        self.assertEqual(checker.FUNCTIONAL_HEADINGS, template_h2s(FUNCTIONAL_TEMPLATE))
        self.assertEqual(checker.TECHNICAL_HEADINGS, template_h2s(TECHNICAL_TEMPLATE))

    def test_freeform_is_unrecognized_without_being_rejected(self) -> None:
        result = self.run_checker(
            "--functional", str(FIXTURES / "freeform_design.md")
        )
        self.assertEqual(result["functional"]["status"], "UNRECOGNIZED_FORMAT")
        self.assertTrue(result["advisory"])

    def test_recognized_document_reports_advisory_warnings(self) -> None:
        source = (FIXTURES / "standard_functional.md").read_text(encoding="utf-8")
        source = source.replace("## Scope\n", "").replace("FR-001", "FR-1")
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "functional.md"
            path.write_text(source, encoding="utf-8")
            result = self.run_checker("--functional", str(path))
        self.assertEqual(result["functional"]["status"], "WARN")
        warnings = "\n".join(result["functional"]["warnings"])
        self.assertIn("Missing required headings: Scope", warnings)
        self.assertIn("Identifiers do not use three digits: FR-1", warnings)


if __name__ == "__main__":
    unittest.main()
