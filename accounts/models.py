from django.db import models
from django.contrib.auth.models import AbstractUser


class Accounts(AbstractUser):
    age = models.IntegerField(default=18)
    bio = models.TextField(null=True, blank=True)
    isblogger = models.BooleanField(default=False)
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'Accounts'

    def __str__(self):
        return self.username
