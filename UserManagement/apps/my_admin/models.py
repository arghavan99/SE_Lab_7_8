from django.contrib.auth.models import User
from django.db import models


class MyAdmin(User):
    name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=10, unique=True)

    class Meta:
        permissions = ()

    def __str__(self):
        return self.name
