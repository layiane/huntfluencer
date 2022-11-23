import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

"""retenez le guide en trois étapes pour effectuer des modifications aux modèles :

Modifiez les modèles (dans models.py).
Exécutez python manage.py makemigrations pour créer des migrations correspondant à ces changements.
Exécutez python manage.py migrate pour appliquer ces modifications à la base de données."""

NATION_CHOICES = (
    ("French", "French"),
    ("English", "English"),
)

Experiment_CHOICES = (
    ("Advanced", "Advanced"),
    ("Intermediate", "Intermediate"),
)

Gender_CHOICES = (
    ("Man", "Man"),
    ("Women", "Women"),
)

Type_CHOICES = (
    ("Food", "Food"),
    ("Beauty", "Beauty"),
    ("Travel", "Travel"),
    ("Lifestyle", "Lifestyle"),
    ("High_Tech", "High_Tech"),
    ("Sport", "Sport"),
)
  
  
class Arbre(models.Model):
      nationality = models.CharField(
        max_length = 20,
        choices = NATION_CHOICES,
        default = '1'
        )
      experiment=models.CharField(
        max_length = 20,
        choices = Experiment_CHOICES,
        default = '1'
        )
      gender=models.CharField(
        max_length = 20,
        choices = Gender_CHOICES,
        default = '1'
        )
      type_infl=models.CharField(
        max_length = 20,
        choices = Type_CHOICES,
        default = '1'
        )



class Influenceur(models.Model):
  username = models.CharField(max_length=200)
  gender = models.CharField(max_length=1)
  nationality  = models.CharField(max_length=200)
  nbr_followers = models.IntegerField(default=0)
  #pub_date = models.DateTimeField('date published')
  theme = models.CharField(max_length=200)
  experience = models.CharField(max_length=200)
  link = models.CharField(max_length=300)
  photo = models.CharField(max_length=300, null = True )
  def __str__(self):
    return self.username