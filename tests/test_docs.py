import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_docs import counterpart, validate


class TestDocumentation(unittest.TestCase):
    def test_local_links_and_translations(self):
        self.assertEqual([], validate())

    def test_language_counterpart_is_symmetric(self):
        # This particular uppercase extension is part of the existing repo.
        # Test with real files rather than arbitrary paths that do not exist.
        folder = Path(__file__).resolve().parents[1] / "Enterprise-1"
        self.assertEqual(folder / "README.en.md", counterpart(folder / "README.MD"))
        self.assertEqual(folder / "README.MD", counterpart(folder / "README.en.md"))


if __name__ == "__main__":
    unittest.main()
