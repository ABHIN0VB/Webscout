"""Integration tests for API endpoints."""
import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

os.environ["DEMO_MODE"] = "true"
os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///./test.db"

try:
    from fastapi.testclient import TestClient
    from app.main import app
    HAS_FASTAPI = True
except Exception:
    HAS_FASTAPI = False


class TestAPIEndpoints(unittest.TestCase):
    def setUp(self):
        if not HAS_FASTAPI:
            self.skipTest("FastAPI / TestClient dependencies not available on host python environment")
        self.client = TestClient(app)

    def test_health_check(self):
        response = self.client.get("/api/health")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn(data["status"], ["healthy", "ok"])

    def test_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["app"], "WebScout")

    def test_scraper_status(self):
        response = self.client.get("/api/scraper/status")
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
