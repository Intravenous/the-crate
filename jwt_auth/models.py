# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    # custom fields here...
    avatar = models.CharField(blank=True, max_length=200)
    user_bio = models.TextField(blank=True)
