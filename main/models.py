from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
ANSWERS = (
    (1, 'A'),
    (2, 'B'),
    (3, 'C')
)


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Advice(models.Model):
    title = models.CharField(max_length=255)
    lead = models.CharField(max_length=255)
    date = models.DateTimeField()
    img = models.ImageField(blank=True, null=True)
    film = models.FileField(upload_to='videos/', null=True)
    description = models.TextField()
    score = models.IntegerField()
    tag = models.ManyToManyField(Tag)


class Training(models.Model):
    name = models.CharField(max_length=255)
    advice = models.ForeignKey(Advice, on_delete=models.CASCADE, )
    tag = models.ManyToManyField(Tag)
    total_score = models.IntegerField()


class Question(models.Model):
    question = models.CharField(max_length=255)
    training = models.ForeignKey(Training, on_delete=models.CASCADE, )
    answer1 = models.TextField()
    answer1file = models.FileField(upload_to='videos/', null=True)
    answer2 = models.TextField()
    answer2file = models.FileField(upload_to='videos/', null=True)
    answer3 = models.TextField()
    answer3file = models.FileField(upload_to='videos/', null=True)
    correct_answer = models.IntegerField(choices=ANSWERS)
    tag = models.ManyToManyField(Tag)
    score = models.IntegerField()


class MyUser(AbstractUser):
    user_score = models.IntegerField()

    def __str__(self):
        return f' {self.username}'


class Message(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
