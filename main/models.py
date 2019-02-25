from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Training(models.Model):
    name = models.CharField(max_length=255)


class Advice(models.Model):
    name = models.CharField(max_length=255)


class Tag(models.Model):
    name = models.CharField(max_length=255)


class MyUser(AbstractUser):
    pass

class Message(models.Model):
    name = models.CharField(max_length=255)


class Test(models.Model):
    name = models.CharField(max_length=255)
