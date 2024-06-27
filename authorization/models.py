from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomerUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

