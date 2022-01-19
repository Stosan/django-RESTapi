from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

# Create your tests here.
class ViewTesCase(TestCase):
   
    def setUp(self):
        """
        define the test client and other test variables
        """
        self.client = APIClient()
        self.payload_data={'device':'4545jhhf88','time':'23:23:00','data':'56 C','seqNumber':'222 nbf','deviceTypeId':'jiihhf88',}
        self.response = self.client.post(
            reverse('create'),
            self.payload_data,
            format="json"
        )

    def test_api_can_create_a_payload(self):
        """
        Test that the API can create payload data
        """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)