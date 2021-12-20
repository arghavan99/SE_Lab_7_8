from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import datetime


class Doctor(User):
    name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=10, unique=True)
    date_joint = models.DateField(default=datetime.now)
    class Meta:
        permissions = ()

    def __str__(self):
        return self.name
