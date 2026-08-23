"""Tests for the DeduplicationService."""
import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from app.services.deduplication_service import DeduplicationService


class TestDeduplication(unittest.TestCase):
    def setUp(self):
        self.service = DeduplicationService()

    def test_url_based_dedup(self):
        products = [
            {"url": "https://smartprix.com/laptop/1", "name": "Laptop A", "brand": "ASUS", "content_hash": "aaa"},
            {"url": "https://smartprix.com/laptop/1", "name": "Laptop A", "brand": "ASUS", "content_hash": "aaa"},
            {"url": "https://smartprix.com/laptop/2", "name": "Laptop B", "brand": "HP", "content_hash": "bbb"},
        ]
        result = self.service.deduplicate(products)
        self.assertEqual(len(result), 2)

    def test_hash_based_dedup(self):
        products = [
            {"url": "https://site1.com/laptop/1", "name": "ASUS Vivobook", "brand": "ASUS", "content_hash": "abc123"},
            {"url": "https://site2.com/laptop/1", "name": "ASUS Vivobook", "brand": "ASUS", "content_hash": "abc123"},
            {"url": "https://site3.com/laptop/2", "name": "HP Victus", "brand": "HP", "content_hash": "def456"},
        ]
        result = self.service.deduplicate(products)
        self.assertEqual(len(result), 2)

    def test_empty_list(self):
        result = self.service.deduplicate([])
        self.assertEqual(result, [])

    def test_single_product(self):
        products = [{"url": "https://site.com/1", "name": "Laptop", "brand": "X", "content_hash": "aaa"}]
        result = self.service.deduplicate(products)
        self.assertEqual(len(result), 1)

    def test_no_duplicates(self):
        products = [
            {"url": "https://site.com/1", "name": "Laptop A", "brand": "ASUS", "content_hash": "aaa"},
            {"url": "https://site.com/2", "name": "Laptop B", "brand": "HP", "content_hash": "bbb"},
            {"url": "https://site.com/3", "name": "Laptop C", "brand": "Dell", "content_hash": "ccc"},
        ]
        result = self.service.deduplicate(products)
        self.assertEqual(len(result), 3)

    def test_preserves_first_occurrence(self):
        products = [
            {"url": "https://site.com/1", "name": "First", "brand": "ASUS", "content_hash": "aaa", "price": 100},
            {"url": "https://site.com/1", "name": "Second", "brand": "ASUS", "content_hash": "aaa", "price": 200},
        ]
        result = self.service.deduplicate(products)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "First")


if __name__ == '__main__':
    unittest.main()
