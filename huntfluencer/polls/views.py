from multiprocessing import context
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def home(request):
    return render(request,'home.html')


def trouver_mon_influenceur(request):
    return render(request,'trouver_mon_influenceur.html')
  

def contact(request):
    return render(request,'contact.html')

def forms(request):
    return render(request,'forms.html')
   

