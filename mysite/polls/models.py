from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    date_pub = models.DateTimeField(auto_now_add=True)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    voice = models.IntegerField(default=0)