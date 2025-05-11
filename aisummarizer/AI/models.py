from django.db import models
from django.contrib.auth.models import User
import uuid


class Document(models.Model):

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )

    Context = models.TextField(
        blank=True,
        null=True,
    )
    summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.Context


# Create your models here.
