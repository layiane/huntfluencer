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


def results_form(request):
    choix_theme=request.POST.get('theme',None)
    choix_xp=request.POST.get('experience',None)
    choix_genre=request.POST.get('gender',None)
    choix_nationalite=request.POST.get('langue',None)
    test = request.POST.get('your_name')
    print(test)
    print(choix_theme,choix_xp,choix_genre,choix_nationalite)
    results= Influenceur.objects.filter(gender=choix_genre,nationality=choix_nationalite,theme=choix_theme,experience = choix_xp)
    print(results)
    context = {
        'theme' : choix_theme,
        'xp' : choix_xp,
        'genre' : choix_genre,
        'nationalite' : choix_nationalite,
        'results' : results

    }
    return render(request,'results.html',context)


   

