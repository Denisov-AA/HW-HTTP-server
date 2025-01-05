import unittest

from src.application import app


class TestServer(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_request(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "This is response from server!")

    def test_head_request(self):
        response = self.app.head("/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) == 0)


if __name__ == "__main__":
    unittest.main()
