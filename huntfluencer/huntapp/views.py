from django.http import HttpResponse

def index(request):
    return HttpResponse("Slt, bienvenue sur la première page web !")