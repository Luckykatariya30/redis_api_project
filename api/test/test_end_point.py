from rest_framework.test import APITestCase,APIClient
from api.models import Register
from django.urls import reverse
from rest_framework import status

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from api.views import get_tokens_for_user


class End_Point_TestCase(APITestCase):
    def setUp(self):
        user = User.objects.latest('id')
        self.user = get_tokens_for_user(user=user)
        self.token = Token.objects.get(user__username = self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token.key)

        
        

        # Include an appropriate `Authorization:` header on all requests.
        # token = Token.objects.get(user__username='lauren')
        # client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        
    def test_get_request(self):
        response =self.client.get(reverse('retrivealldata') , format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
