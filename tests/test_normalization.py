"""Tests for the NormalizationService."""
import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from app.services.normalization_service import NormalizationService


class TestNormalization(unittest.TestCase):
    def setUp(self):
        self.service = NormalizationService()

    def test_price_normalization(self):
        self.assertEqual(self.service.normalize_price("₹74,990"), 74990.0)
        self.assertEqual(self.service.normalize_price("Rs. 74990"), 74990.0)
        self.assertEqual(self.service.normalize_price("Rs.74,990"), 74990.0)
        self.assertEqual(self.service.normalize_price("74990"), 74990.0)
        self.assertEqual(self.service.normalize_price("₹74,990.00"), 74990.0)
        self.assertEqual(self.service.normalize_price("INR 74,990"), 74990.0)
        self.assertIsNone(self.service.normalize_price(None))
        self.assertIsNone(self.service.normalize_price(""))
        self.assertIsNone(self.service.normalize_price("Contact for price"))
        self.assertEqual(self.service.normalize_price(74990), 74990.0)
        self.assertEqual(self.service.normalize_price(74990.5), 74990.5)

    def test_ram_normalization(self):
        self.assertEqual(self.service.normalize_ram("16 GB DDR5"), "16 GB")
        self.assertEqual(self.service.normalize_ram("16GB"), "16 GB")
        self.assertEqual(self.service.normalize_ram("RAM: 16GB"), "16 GB")
        self.assertEqual(self.service.normalize_ram("16GB Memory"), "16 GB")
        self.assertEqual(self.service.normalize_ram("16 gb"), "16 GB")
        self.assertEqual(self.service.normalize_ram("8GB DDR4"), "8 GB")
        self.assertIsNone(self.service.normalize_ram(None))
        self.assertIsNone(self.service.normalize_ram(""))

    def test_storage_normalization(self):
        self.assertEqual(self.service.normalize_storage("1TB SSD"), "1 TB SSD")
        self.assertEqual(self.service.normalize_storage("512GB SSD"), "512 GB SSD")
        self.assertEqual(self.service.normalize_storage("1 TB HDD"), "1 TB HDD")
        self.assertEqual(self.service.normalize_storage("512GB"), "512 GB")
        result = self.service.normalize_storage("512GB NVMe SSD")
        self.assertIn("512 GB", result)
        self.assertIsNone(self.service.normalize_storage(None))

    def test_cpu_normalization(self):
        result = self.service.normalize_cpu("Intel Core i7-13700H")
        self.assertIn("i7", result)
        result = self.service.normalize_cpu("AMD Ryzen 7 7735HS")
        self.assertIn("Ryzen 7", result)
        self.assertIsNone(self.service.normalize_cpu(None))

    def test_gpu_normalization(self):
        result = self.service.normalize_gpu("NVIDIA GeForce RTX 4050")
        self.assertIn("RTX 4050", result)
        result = self.service.normalize_gpu("Intel Iris Xe Graphics")
        self.assertIsNotNone(result)
        self.assertIsNone(self.service.normalize_gpu(None))

    def test_content_hash(self):
        p1 = {"brand": "ASUS", "model_name": "Vivobook", "name": "ASUS Vivobook Pro"}
        p2 = {"brand": "ASUS", "model_name": "Vivobook", "name": "ASUS Vivobook Pro"}
        p3 = {"brand": "HP", "model_name": "Victus", "name": "HP Victus 15"}
        self.assertEqual(self.service.generate_content_hash(p1), self.service.generate_content_hash(p2))
        self.assertNotEqual(self.service.generate_content_hash(p1), self.service.generate_content_hash(p3))


if __name__ == '__main__':
    unittest.main()
