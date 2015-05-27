from unittest import TestCase
from flask_hello import app

__author__ = 'steven.holmes'


class TestHelloWorld(TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_hello_world(self):
        result = self.client.get("/")
        assert result.status_code == 400
        assert 'duckies' in result.data

