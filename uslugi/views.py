from django.shortcuts import render
from .models import ates1
from .models import center1
from .models import iso1
from .models import ispyt1
from .models import prombez1
from .models import rad1
from .models import sootvet1
from .forms import apllicationForm
# Create your views here.


def index(request):
    return render(request, 'uslugi/index.html')

def prombez(request):
    if request.method == 'POST':
        form = apllicationForm(request.POST)
        if form.is_valid():
            form.save()
    data = prombez1.objects.all()
    form = apllicationForm
    return render(request, 'uslugi/prombez/prombez.html', {'data': data, 'form': form})


def ates(request):
    if request.method == 'POST':
        form = apllicationForm(request.POST)
        if form.is_valid():
            form.save()
    data = ates1.objects.all()
    form = apllicationForm()
    return render(request, 'uslugi/ates/ates.html', {'data': data, 'form': form})


def ispyt(request):
    if request.method == 'POST':
        form = apllicationForm(request.POST)
        if form.is_valid():
            form.save()
    data = ispyt1.objects.all()
    form = apllicationForm
    return render(request, 'uslugi/ispyt/ispyt.html', {'data': data, 'form': form})


def sootvet(request):
    if request.method == 'POST':
        form = apllicationForm(request.POST)
        if form.is_valid():
            form.save()
    data = sootvet1.objects.all()
    form = apllicationForm
    return render(request, 'uslugi/sootvet/sootvet.html', {'data': data, 'form': form})


def iso(request):
    if request.method == 'POST':
        form = apllicationForm(request.POST)
        if form.is_valid():
            form.save()
    data = iso1.objects.all()
    form = apllicationForm
    return render(request, 'uslugi/iso/iso.html', {'data': data, 'form': form})


def rad(request):
    if request.method == 'POST':
        form = apllicationForm(request.POST)
        if form.is_valid():
            form.save()
    data = rad1.objects.all()
    form = apllicationForm
    return render(request, 'uslugi/rad/rad.html', {'data': data, 'form': form})


def center(request):
    if request.method == 'POST':
        form = apllicationForm(request.POST)
        if form.is_valid():
            form.save()
    data = center1.objects.all()
    form = apllicationForm
    return render(request, 'uslugi/center/center.html', {'data': data, 'form': form})

