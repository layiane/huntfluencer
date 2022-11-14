import datetime

from django.db import models
from django.utils import timezone
"""retenez le guide en trois étapes pour effectuer des modifications aux modèles :

Modifiez les modèles (dans models.py).
Exécutez python manage.py makemigrations pour créer des migrations correspondant à ces changements.
Exécutez python manage.py migrate pour appliquer ces modifications à la base de données."""

class Influenceur(models.Model):
    username = models.CharField(max_length=200)
    gender = models.CharField(max_length=1)
    nationality  = models.CharField(max_length=200)
    nbr_followers = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    theme = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    link = models.CharField(max_length=300)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text #pour afficher de manière lisible l'instance
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text #pour afficher de manière lisible l'instance