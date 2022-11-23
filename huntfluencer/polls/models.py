from django.db import models

# Create your models here.

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

