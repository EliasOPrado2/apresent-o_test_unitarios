from django.urls import path, include
from rest_framework import routers
from .api.viewsets import ApplicantViewSet

router = routers.DefaultRouter()
router.register(r'applicant', ApplicantViewSet, basename='applicant')

app_name = 'sampletrip'

urlpatterns = [
    path('', include(router.urls)),
]