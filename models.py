from django.contrib.auth.models import AbstractUser
from django.db import models

ROLES = (
    ('mentee', 'Mentee'),
    ('mentor', 'Mentor'),
    ('employer', 'Employer'),
    ('admin', 'Admin'),
)

class CustomUser(AbstractUser):
    role = models.CharField(max_length=10, choices=ROLES)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    preferred_language = models.CharField(max_length=20, default='English')

class Mentor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    industry = models.CharField(max_length=100)
    skills = models.TextField()
    languages = models.TextField()

class Mentee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    interests = models.TextField()
    preferred_language = models.CharField(max_length=20)
