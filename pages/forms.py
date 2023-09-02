from django import forms 
from produits.models import Produit

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'description', 'prix', 'active', 'live']
        
        
class PureProduitForm(forms.Form):
    nom = forms.CharField(required=False, initial='produit nouveau')
    description = forms.CharField(required=False)
    prix = forms.FloatField(required=False, initial=12.66)
    active = forms.BooleanField(required=False)