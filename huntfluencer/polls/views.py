from multiprocessing import context
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from polls.models import Influenceur


# Create your views here.
def home(request):
    return render(request,'home.html')


def trouver_mon_influenceur(request):
    return render(request,'trouver_mon_influenceur.html')
  

def contact(request):
    return render(request,'contact.html')

def forms(request):

        # return HttpResponse("This is a post request")

    list_themes =  [i[0] for i in list(Influenceur.objects.values_list('theme').distinct())]
    list_xp =  [i[0] for i in list(Influenceur.objects.values_list('experience').distinct())]
    list_genres =  [i[0] for i in list(Influenceur.objects.values_list('gender').distinct())]
    list_nationalites=  [i[0] for i in list(Influenceur.objects.values_list('nationality').distinct())]
    context={
        'list_themes':list_themes,
        'list_xp':list_xp,
        'list_genres':list_genres,
        'list_nationalites':list_nationalites,
    }
    return render(request,'forms.html',context)





   

