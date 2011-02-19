from django.test import TestCase
from django.test.client import Client

class CoreTest(TestCase):

    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        
    def test_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

