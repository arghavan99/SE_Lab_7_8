from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class Patient(AbstractBaseUser):
    name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=10, unique=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['national_id', 'name']

    def __str__(self):
        return self.name