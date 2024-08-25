import unittest
from app.mail_utilis.utilis import send_verification_email 
from unittest.mock import patch

class UtilsTestCase(unittest.TestCase):
    
    @patch('app.utils.send_email')
    def test_send_verification_email(self, mock_send_email):
        with patch('flask.current_app.config') as mock_config:
            mock_config['BASE_URL'] = 'http://localhost'
            mock_config['MAIL_DEFAULT_SENDER'] = 'test@example.com'

            send_verification_email('user@example.com', 'test_token')

            mock_send_email.assert_called_once_with(
                'user@example.com',
                'Verify Your Email',
                'Please verify your email by clicking on the following link: http://localhost/api/verify-email?token=test_token'
            )

if __name__ == '__main__':
    unittest.main()
