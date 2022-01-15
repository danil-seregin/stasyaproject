from django.shortcuts import render
from uslugi.forms import apllicationForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = apllicationForm(request.POST)
        if form.is_valid():
            form.save()
    form = apllicationForm()
    return render(request, 'contacts/index.html', {'form': form})
