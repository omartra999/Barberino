import unittest
from app import create_app, db
from app.models import User

class UserModelTestCase(unittest.TestCase):
    
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

    def test_user_creation(self):
        user = User(first_name='john',last_name='doe',username='testuser',email='test@example.com', password='password')
        db.session.add(user)
        db.session.commit()

        queried_user = User.query.filter_by(username='testuser').first()
        self.assertIsNotNone(queried_user)
        self.assertTrue(queried_user.check_password_hash('password'))

if __name__ == '__main__':
    unittest.main()
