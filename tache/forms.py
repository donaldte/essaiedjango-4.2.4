from .models import Tache
from django import forms 

class TacheFrom(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ('nom', 'description', 'date_creation', 'fait')