"""Tests for the RankingService."""
import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from app.services.ranking_service import RankingService


class TestRanking(unittest.TestCase):
    def setUp(self):
        self.service = RankingService()
        self.sample_requirements = {
            "category": "laptop",
            "budget": {"max_price": 80000, "currency": "INR"},
            "use_cases": ["programming", "Docker", "React", "gaming"],
            "preferences": {
                "ram_min": "16GB",
                "storage_min": "512GB SSD",
                "dedicated_gpu": True,
            },
        }

    def test_budget_scoring(self):
        self.assertEqual(self.service.score_budget_fit(70000, 80000), 100.0)
        self.assertEqual(self.service.score_budget_fit(80000, 80000), 100.0)
        self.assertTrue(50 < self.service.score_budget_fit(85000, 80000) < 100)
        self.assertTrue(self.service.score_budget_fit(200000, 80000) < 50)
        self.assertEqual(self.service.score_budget_fit(70000, None), 100.0)
        self.assertEqual(self.service.score_budget_fit(None, 80000), 50.0)

    def test_ram_scoring(self):
        self.assertGreaterEqual(self.service.score_ram("16 GB", "16GB"), 90)
        self.assertEqual(self.service.score_ram("32 GB", "16GB"), 100.0)
        self.assertLess(self.service.score_ram("8 GB", "16GB"), 80)
        self.assertGreaterEqual(self.service.score_ram("16 GB", None), 70)

    def test_storage_scoring(self):
        self.assertGreaterEqual(self.service.score_storage("512 GB SSD", "512GB SSD"), 90)
        self.assertEqual(self.service.score_storage("1 TB SSD", "512GB SSD"), 100.0)
        self.assertLess(self.service.score_storage("256 GB SSD", "512GB SSD"), 80)

    def test_gpu_scoring(self):
        self.assertGreaterEqual(self.service.score_gpu("NVIDIA RTX 4050", True), 80)
        self.assertLess(self.service.score_gpu("Intel Iris Xe", True), 50)
        self.assertGreaterEqual(self.service.score_gpu("Intel Iris Xe", False), 60)

    def test_cpu_scoring(self):
        self.assertGreaterEqual(self.service.score_cpu("Intel Core i7-13700H", ["programming", "Docker"]), 85)
        self.assertGreaterEqual(self.service.score_cpu("Intel Core i5-13420H", ["programming"]), 60)
        self.assertEqual(self.service.score_cpu(None, ["programming"]), 50.0)

    def test_overall_ranking(self):
        products = [
            {
                "name": "Budget Laptop",
                "price": 45000,
                "specifications": {"processor": "i3-1215U", "ram": "8 GB", "storage": "256 GB SSD", "gpu": "Integrated"},
            },
            {
                "name": "Gaming Laptop",
                "price": 75000,
                "specifications": {"processor": "Ryzen 7 7735HS", "ram": "16 GB", "storage": "1 TB SSD", "gpu": "RTX 4050"},
            },
            {
                "name": "Mid Range",
                "price": 65000,
                "specifications": {"processor": "i5-13420H", "ram": "16 GB", "storage": "512 GB SSD", "gpu": "RTX 3050"},
            },
        ]
        ranked = self.service.rank_products(products, self.sample_requirements)
        self.assertEqual(len(ranked), 3)
        self.assertEqual(ranked[0]["name"], "Gaming Laptop")
        for p in ranked:
            self.assertIn("score", p)
            self.assertIn("score_breakdown", p)
            self.assertTrue(0 <= p["score"] <= 100)


if __name__ == '__main__':
    unittest.main()
