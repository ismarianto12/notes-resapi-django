from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)


class Notes(models.Model):
    author = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    attachments = models.CharField(max_length=50)
