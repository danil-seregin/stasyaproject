from django.shortcuts import render

# Create your views here.
from .models import sertificates

def index(request):
    data = sertificates.objects.all()
    types = []
    for i in data:
        if i.type not in types:
            types.append(i.type)
    dat = []
    for i in types:
        datinside = []
        for i1 in data:
            if i == i1.type:
                datinside.append(i1.image)
        dat.append(datinside)
    print(dat)


    return render(request, 'documents/index.html', {'types': types, 'data': dat})
