from django.shortcuts import render
from .models import questionsbig
# Create your views here.

def index(request):
    quest = questionsbig.objects.all()
    questions = []
    types = []
    for i in quest:
        if i.type not in types:
            types.append(i.type)
    for i in types:
        a = []
        a.append(i)
        for i1 in quest:
            if i1.type == i:
                a.append(i1)
        questions.append(a)
    print(questions)
    return render(request, 'questions/index.html', {'data': questions, 'type': types})
