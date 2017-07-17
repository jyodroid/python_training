from django.db import models
# To support python 2: from django.utils.encoding import python_2_unicode_compatible and add @python_2_unicode_compatible before model declaration

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # Override the to string method
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # Override the to string method
    def __str__(self):
        return self.choice_text
