import json
from ..models import Applicant
from django.http import response
from django.urls import reverse, resolve
from django.utils import timezone
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

# headers =  = {'content-type': 'application/json'}

class TestApi(APITestCase):

    def setUp(self):

        self.user = User.objects.create(
            username='John',
            password='@123abc'
        )
        self.user.save()

        self.applicant = Applicant.objects.create(
            user_id=self.user,
            created_by='samplemed'
        )
        self.applicant.save()

    def test_get_applicant(self):

        url = reverse('sampletrip:applicant-list')

        response = self.client.get(url,headers = {'content-type': 'application/json'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_applicant(self):

        data = {
            'user_id':self.user.id,
            'created_by': 'Ramon',
        }
        url = reverse('sampletrip:applicant-list')

        response = self.client.post(url, data, headers = {'content-type': 'application/json'}, format='json')
        print("RESPONSE =>", response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        