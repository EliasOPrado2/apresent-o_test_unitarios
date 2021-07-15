from django.utils import timezone
from django.test import TestCase
from ..models import Applicant
from django.contrib.auth.models import User


class TestModels(TestCase): 

    def setUp(self):
        self.user = User.objects.create(
            username='John',
            password='@123abc'
        )
        self.user.save()


    def test_applicant_model(self):

        applicant = Applicant.objects.create(
            user_id=self.user,
            created_by='samplemed'
        )
        applicant.save()
        self.assertEqual(applicant.user_id, self.user)
        self.assertEqual(applicant.created_by, 'samplemed')
