from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import otzyv
from .models import uslugi
from .models import news
from .models import questions

def index(request):
    showed_otzyvy= otzyv.objects.filter(showed=True)
    usl = {'righttop': uslugi.objects.get(type='прав верх', showed=True),
           'rightbot': uslugi.objects.get(type='прав ниж', showed=True),
           'lefttop': uslugi.objects.get(type='лев верх', showed=True),
           'leftbot': uslugi.objects.get(type='лев ниж', showed=True),
           'center': uslugi.objects.get(type='сред сред', showed=True)}
    showed = {'otzyvy': showed_otzyvy}
    new = {'news': news.objects.all()}
    quest = {'questions': questions.objects.all()}
    return render(request, 'home/newhome/index.html', context={**usl, **showed, **new, **quest})
