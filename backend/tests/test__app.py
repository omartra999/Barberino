import unittest
from app import create_app

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

    def test_home(self):
        response = self.client.get('/api/register')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'hello'})


if __name__ == '__main__':
    unittest.main()