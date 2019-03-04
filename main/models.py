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

    def __str__(self):
        return f' {self.name}'


class Advice(models.Model):
    title = models.CharField(max_length=255)
    lead = models.CharField(max_length=255)
    date = models.DateTimeField()
    img = models.ImageField(blank=True, null=True)
    film = models.FileField(upload_to='videos/', null=True)
    description = models.TextField()
    # score = models.IntegerField()
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f' {self.title}'


class Training(models.Model):
    name = models.CharField(max_length=255)
    advice = models.ForeignKey(Advice, on_delete=models.CASCADE, )
    tag = models.ManyToManyField(Tag)
    total_score = models.IntegerField()
    user_done = models.ManyToManyField('MyUser')

    def __str__(self):
        return f' {self.name}'


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
    # ew. pole do trzymania informacji o tym jakie odpowiedzi dał użytkownik

    def __str__(self):
        return f' {self.question}'


class MyUser(AbstractUser):
    user_score = models.IntegerField(null=True)

    def __str__(self):
        return f' {self.username}'


class Message(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    content = models.TextField(null=True)
    relates_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f' {self.title}'
