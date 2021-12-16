from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class Admin(AbstractBaseUser):
    name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=10)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    admin = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['national_id', 'name']

    def __str__(self):
        return self.name