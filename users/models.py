from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    intro = models.TextField(blank=True)
    profile_image = models.ImageField(blank=True, upload_to = 'user/images')