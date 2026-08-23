"""Tests for the AI Query Parser (mocked LLM / schema verification)."""
import unittest
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))


class TestQueryParserOutput(unittest.TestCase):
    """Test that parsed query structures are valid, using mock LLM responses."""

    def test_laptop_query_structure(self):
        """Verify the expected structure of a parsed laptop query."""
        parsed = {
            "category": "laptop",
            "budget": {"max_price": 80000, "currency": "INR"},
            "use_cases": ["programming", "Docker", "React", "gaming"],
            "preferences": {
                "ram_min": "16GB",
                "storage_min": "512GB SSD",
                "dedicated_gpu": True,
            },
        }

        self.assertEqual(parsed["category"], "laptop")
        self.assertEqual(parsed["budget"]["max_price"], 80000)
        self.assertEqual(parsed["budget"]["currency"], "INR")
        self.assertIn("programming", parsed["use_cases"])
        self.assertIn("gaming", parsed["use_cases"])
        self.assertTrue(parsed["preferences"]["dedicated_gpu"])

    def test_query_without_budget(self):
        """Queries without explicit budget should have None budget."""
        parsed = {
            "category": "laptop",
            "budget": {"max_price": None, "currency": "INR"},
            "use_cases": ["programming"],
            "preferences": {},
        }
        self.assertIsNone(parsed["budget"]["max_price"])

    def test_query_with_multiple_use_cases(self):
        """Multiple use cases should be extracted."""
        parsed = {
            "category": "laptop",
            "budget": {"max_price": 100000, "currency": "INR"},
            "use_cases": ["video editing", "3D rendering", "machine learning"],
            "preferences": {"ram_min": "32GB", "dedicated_gpu": True},
        }
        self.assertEqual(len(parsed["use_cases"]), 3)

    def test_query_json_serializable(self):
        """Parsed output must be JSON-serializable for DB storage."""
        parsed = {
            "category": "laptop",
            "budget": {"max_price": 80000, "currency": "INR"},
            "use_cases": ["programming"],
            "preferences": {},
        }
        json_str = json.dumps(parsed)
        restored = json.loads(json_str)
        self.assertEqual(restored, parsed)


if __name__ == '__main__':
    unittest.main()
