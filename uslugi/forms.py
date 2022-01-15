from django.forms import ModelForm, TextInput, Textarea
from .models import applications


class apllicationForm(ModelForm):
    class Meta:
        model = applications
        fields = ['name', 'contacts', 'text']
        widgets = {'name': TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'SK Group',
                                            'type': 'name'}),
                   'contacts': TextInput(attrs={'class': 'form-control',
                                            'placeholder': '+7 777 1234567',
                                            'type': 'contacts'}),
                   'text': Textarea(attrs={'class': 'form-control',
                                                'rows': '3',
                                                'type': 'text'})
                   }
