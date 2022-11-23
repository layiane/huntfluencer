from django.forms import ModelForm
from . import models
from .models import Arbre
from django import forms


class ArbreForm(ModelForm):
	class Meta:
		model = Arbre
		fields = ('nationality', 'experiment', 'gender','type_infl')