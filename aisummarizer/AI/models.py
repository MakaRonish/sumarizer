from django.db import models


class Document(models.Model):
    Context = models.TextField(
        blank=True,
        null=True,
    )


# Create your models here.
