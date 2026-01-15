import datetime
from django.db import models
from django.utils import timezone

# Esto permite crear una api de python con acceso a la base de datos de Question o Choice por ejemplo

# models.Model signigica que la clase podrá por defecto mapearse a una base de datos, CRUD, tener campos, etc.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

