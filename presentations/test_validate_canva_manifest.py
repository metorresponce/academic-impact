"""Regression checks for README card boundaries and local PDF links."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import validate_canva_manifest as validator


CARD = "### Paper\n- **DOI**: [doi](https://doi.org/10.1234/example)\n"
LINK = "- **Academic presentation**: [View](https://www.canva.com/d/example)\n"


class ValidationTests(unittest.TestCase):
    def test_integrated_presentation(self):
        self.assertEqual(len(validator.catalogue(CARD + LINK, "README.md")), 1)

    def test_visual_boundaries_reject_detached_presentation(self):
        for boundary in ("## Section\n", "---\n", "***\n", "___\n"):
            with self.subTest(boundary=boundary), self.assertRaises(ValueError):
                validator.catalogue(CARD + boundary + LINK, "README.md")

    def test_duplicate_presentation_rejected(self):
        with self.assertRaises(ValueError):
            validator.catalogue(CARD + LINK + LINK, "README.md")

    def test_presentation_before_first_heading_rejected(self):
        with self.assertRaises(ValueError):
            validator.catalogue(LINK + CARD, "README.md")

    def test_missing_pdf_rejected(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(validator, "ROOT", Path(directory)):
            with self.assertRaises(ValueError):
                validator.validate_pdf_links("[PDF](missing.pdf)", "README.md")

    def test_encoded_pdf_and_fragment(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(validator, "ROOT", Path(directory)):
            (Path(directory) / "paper español.pdf").touch()
            validator.validate_pdf_links("[PDF](paper%20espa%C3%B1ol.pdf#page=2)", "README.md")


if __name__ == "__main__":
    unittest.main()
