
# Create your models here.

from django.db import models
from django.utils import timezone


class Profile(models.Model):
    user = models.ForeignKey('auth.User')
    email = models.CharField(max_length=200)
    detail = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def __str__(self):
        return str(self.email)
