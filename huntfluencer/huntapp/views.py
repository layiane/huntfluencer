from django.http import HttpResponse
from models import Question

def index(request):
    questions = Question.objects.all()
    return HttpResponse("Slt, bienvenue sur la première page web !")