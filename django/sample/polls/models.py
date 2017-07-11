from django.db import models

# Create your models here.
class Question(models.Model):
    questio_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choise(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choise_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
