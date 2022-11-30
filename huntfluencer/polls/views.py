from multiprocessing import context
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from polls.models import Influenceur
from bs4 import BeautifulSoup
import pandas as pd
import random
import requests


# Create your views here.
def home(request):
    return render(request,'home.html')


def trouver_mon_influenceur(request):
    return render(request,'trouver_mon_influenceur.html')
  

def contact(request):
    return render(request,'contact.html')

def forms(request):

        # return HttpResponse("This is a post request")

    list_themes =  ["beauty","crypto","gaming","science","lifestyle"]
    #list_xp =  [i[0] for i in list(Influenceur.objects.values_list('experience').distinct())]
    #list_genres =  [i[0] for i in list(Influenceur.objects.values_list('gender').distinct())]
    #list_nationalites=  [i[0] for i in list(Influenceur.objects.values_list('nationality').distinct())]
    list_nationalites=  ["france","united-states","brazil","japan","united-kingdom"]
    list_followers_min = [0,10000,500000, 1000000]
    list_followers_max = [10000,500000, 1000000, 10000000]
    context={
        'list_themes':list_themes,
        #'list_xp':list_xp,
        #'list_genres':list_genres,
        'list_nationalites':list_nationalites,
        'list_followers_min':list_followers_min,
        'list_followers_max':list_followers_max,
    }
    return render(request,'forms.html',context)


def results_form(request):
    choix_theme=request.POST.get('theme',None)
    #choix_xp=request.POST.get('experience',None)
    #choix_genre=request.POST.get('gender',None)
    choix_nationalite=request.POST.get('langue',None)
    choix_followers_min=request.POST.get('follower_min',None)
    choix_followers_max=request.POST.get('follower_max',None)
    print([int(choix_followers_min),choix_followers_max,choix_nationalite,choix_theme])
    #print(choix_theme,choix_xp,choix_genre,choix_nationalite)
    #results= Influenceur.objects.filter(gender=choix_genre,nationality=choix_nationalite,theme=choix_theme,experience = choix_xp)
    results= recup_country_category(choix_nationalite,choix_theme,int(choix_followers_min), int(choix_followers_max))
    results_2 = results.values.tolist()
    #print(results)
    print(results_2)
    for row in results_2:
        for i in row:
            print(i)
    context = {
        'theme' : choix_theme,
        #'xp' : choix_xp,
        #'genre' : choix_genre,
        'nationalite' : choix_nationalite,
        'followers_min':choix_followers_min,
        'followers_max': choix_followers_max,
        'results_2' : results

    }
    return render(request,'results.html',context)

def text_to_num(liste):
    d = {
        'K': 3,
        'M': 6,
        'B': 9
        }

    liste_retour = []
    for i in liste:
        if i[-1] in d:
            num, magnitude = i[:-1], i[-1]
            liste_retour.append(int(float(num) * 10 ** d[magnitude]))
        else:
            liste_retour.append(int(float(i)))
    return liste_retour
def recup_country_category(country, category,n,j):
    #1ere page
    if country == "united-states":
        country_name = "United States"
    elif country == "united-kingdom":
        country_name = " United Kingdom"
    else: 
        country_name = country.title()
    print(country_name)
    r = requests.get(f"https://hypeauditor.com/top-instagram-{category}-{country}/")
    soup = BeautifulSoup(r.content) 
    name = [tr.text for tr in soup.find_all(class_="contributor__name-content")]
    followers = text_to_num([tr.text for tr in soup.find_all(class_="row-cell authentic")])
    country = [tr.text for tr in soup.find_all(class_="row-cell audience")]
    like = text_to_num([tr.text for tr in soup.find_all(class_="row-cell engagement")])
    dataset_1 = pd.DataFrame(
    {"name": name,
     "country": country,
     "followers": followers,
     "category" : f"{category}",
     "like_average" : like
    })
    print(dataset_1)
    #2e page
    r = requests.get(f"https://hypeauditor.com/top-instagram-{category}-{country}/?p=2")
    soup = BeautifulSoup(r.content) 
    name = [tr.text for tr in soup.find_all(class_="contributor__name-content")]
    followers = text_to_num([tr.text for tr in soup.find_all(class_="row-cell authentic")])
    country = [tr.text for tr in soup.find_all(class_="row-cell audience")]
    like = text_to_num([tr.text for tr in soup.find_all(class_="row-cell engagement")])
    dataset_2 = pd.DataFrame(
    {"name": name,
     "country": country,
     "followers": followers,
     "category" : f"{category}",
     "like_average" : like
    })
    print(dataset_2)
    #fusion
    dataset = pd.concat([dataset_1,dataset_2])
    print(dataset)
    print(f"test: {country_name}")
    df = dataset[(dataset.followers>n) & (dataset.followers <j) & (dataset.country == country_name)]
    print(df['country'].value_counts())
    print(df[df['country'] == country_name])
    return df.sample(5).sort_values(by=['followers'])
