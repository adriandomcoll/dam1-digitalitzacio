import json
import unittest
from flask import Flask
from flask.testing import FlaskClient
from src.app import app

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app: Flask = app
        self.client: FlaskClient = self.app.test_client()
        self.app.config['TESTING'] = True

    def test_login_success(self):
        response = self.client.post('/login', json={
            'username': 'mare',
            'password': 'mare'
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['coderesponse'], "1")
        self.assertIn('data', data)
        self.assertEqual(data['data']['username'], 'mare')

    def test_login_failure(self):
        response = self.client.post('/login', json={
            'username': 'mare',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['coderesponse'], "0")
        self.assertEqual(data['msg'], "No validat")

    def test_login_with_token_success(self):
        token = "token12345"  # This should be a valid token from your application logic
        response = self.client.post('/login', headers={
            'Authorization': token
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['coderesponse'], "1")
        self.assertIn('username', data)
        self.assertEqual(data['username'], 'mare')

    def test_login_with_token_failure(self):
        response = self.client.post('/login', headers={
            'Authorization': 'invalidtoken'
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['coderesponse'], "0")
        self.assertEqual(data['msg'], "No validat")

if __name__ == '__main__':
    unittest.main()