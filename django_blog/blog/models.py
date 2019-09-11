from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# from django.utils import timezone

# class Post(models.Model):
#     title=models.CharField(max_length=200)
#     slug=models.CharField(max_length=200)
#     body=models.TextField()
#     pub_date=models.DateTimeField(default=timezone.now)

#     class Meta:
#         ordering=('-pub_date',)
    
#     def __str__(self):
#         return self.title