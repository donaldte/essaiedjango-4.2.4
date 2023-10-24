from django import forms 
from .models import Profile

class FromProfile(forms.ModelForm):
    
    email = forms.EmailField()
    
    class Meta:
        model = Profile
        
        fields = '__all__'
       
        