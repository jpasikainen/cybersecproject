from django.db import models

class Accounts(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=30)
    admin = models.BooleanField(default=False)

class Posts(models.Model):
    author = models.CharField(max_length=10)
    body = models.CharField(max_length=300)