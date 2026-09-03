from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).parents[1] / "scripts" / "check_repository_safety.py"
SPEC = importlib.util.spec_from_file_location("check_repository_safety", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
SAFETY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SAFETY)


class RepositorySafetyTests(unittest.TestCase):
    def test_blocks_machine_local_paths(self) -> None:
        samples = [
            "/" + "Users/alice/work/plugin.txt",
            "/" + "home/alice/work/plugin.txt",
            "/" + "private/var/folders/ab/local/cache.txt",
            "/" + "tmp/local-output.txt",
            "C:" + "\\Users\\alice\\work\\plugin.txt",
        ]
        for sample in samples:
            with self.subTest(sample=sample):
                self.assertTrue(SAFETY.content_problems("example.md", sample.encode()))

    def test_allows_portable_paths_and_placeholders(self) -> None:
        samples = [
            "${PLUGIN_ROOT}/skills/example/scripts/run.py",
            "./plugins/example",
            "<repo-root>/plugins/example",
            "https://github.com/Koredotcom/kore-codex-plugins",
        ]
        for sample in samples:
            with self.subTest(sample=sample):
                self.assertEqual([], SAFETY.content_problems("example.md", sample.encode()))

    def test_allow_marker_suppresses_an_intentional_example(self) -> None:
        sample = "/" + "Users/example/project  # " + SAFETY.ALLOW_MARKER
        self.assertEqual([], SAFETY.content_problems("example.md", sample.encode()))

    def test_blocks_sensitive_filenames(self) -> None:
        blocked = [
            ".env.production",
            ".npmrc",
            "AGENTS.local.md",
            "AGENTS.override.md",
            "CLAUDE.md",
            "CLAUDE.local.md",
            "CLAUDE.override.md",
            "MEMORY.md",
            "memories/session-notes.md",
            "customer-data/export.json",
            "keys/service.pem",
            ".ssh/id_ed25519",
        ]
        for path in blocked:
            with self.subTest(path=path):
                self.assertIsNotNone(SAFETY.filename_problem(path))

    def test_allows_shared_project_guidance(self) -> None:
        self.assertIsNone(SAFETY.filename_problem("AGENTS.md"))

    def test_allows_documented_environment_templates(self) -> None:
        for path in [".env.example", ".env.sample", ".env.template"]:
            with self.subTest(path=path):
                self.assertIsNone(SAFETY.filename_problem(path))


if __name__ == "__main__":
    unittest.main()
