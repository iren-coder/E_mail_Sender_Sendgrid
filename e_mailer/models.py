from django.db import models

# Create your models here.

from django.db import models


class Mail(models.Model):
    email = models.EmailField(max_length=254)
    text = models.TextField()
    title = models.CharField(max_length=256)
    seconds = models.PositiveIntegerField(default=0)
    status = models.BooleanField()

    def __str__(self):
        return self.title