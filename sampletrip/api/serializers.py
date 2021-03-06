from django.db.models import fields
from rest_framework import serializers
from ..models import Applicant

class ApplicantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Applicant
        fields = ['id', 'user_id', 'created_by']