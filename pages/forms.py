from django import forms 
from produits.models import Produit

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = [ 'nom', 'description', 'prix', 'active', 'live']