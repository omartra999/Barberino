import unittest
import json
from app import create_app, db

class RegisterRouteTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        db.drop_all()
        cls.app_context.pop()

    def test_register(self):
        response = self.client.post('/api/register', 
            data=json.dumps({
                'first_name': 'John',
                'last_name': 'Doe',
                'username': 'johndoe',
                'email': 'john.doe@example.com',
                'password': 'password',
                'confirmPassword': 'password'
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'User registered successfully', response.data)

    def test_register_user_exists(self):
        # Add a user first
        self.client.post('/api/register', 
            data=json.dumps({
                'first_name': 'John',
                'last_name': 'Doe',
                'username': 'johndoe',
                'email': 'john.doe@example.com',
                'password': 'password',
                'confirmPassword': 'password'
            }),
            content_type='application/json'
        )
        # Attempt to register the same user again
        response = self.client.post('/api/register', 
            data=json.dumps({
                'first_name': 'Jane',
                'last_name': 'Doe',
                'username': 'johndoe',
                'email': 'jane.doe@example.com',
                'password': 'password',
                'confirmPassword': 'password'
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Username already exists', response.data)

if __name__ == '__main__':
    unittest.main()
