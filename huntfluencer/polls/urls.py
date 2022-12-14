from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('trouver_mon_influenceur', views.trouver_mon_influenceur, name='trouver_mon_influenceur'),
    path('contact', views.contact, name='contact'),
    path('trouver_mon_influenceur/forms', views.forms, name='forms'), #url du form
    path('trouver_mon_influenceur/results', views.results_form, name='results'), # url des résultats avec les critères du form  
]
