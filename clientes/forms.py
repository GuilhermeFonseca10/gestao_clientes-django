from dataclasses import field
from django.forms import ModelForm
from .models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['firts_name', 'last_name', 'age', 'salary', 'bio', 'photo']

