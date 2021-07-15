from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# applicant:
# - user_id -> 1x1 User
# - created_by -> varchar

class Applicant(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=150)

    def __str__(self):
        return self.created_by
