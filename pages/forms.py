from django import forms 
from produits.models import Produit

class ProduitForm(forms.ModelForm):
    nom = forms.CharField(required=False,
                          widget=forms.TextInput(
                              attrs={
                                  'class': 'name',
                                  'placeholder': 'Enter the name of the product here'
                              }
                          ))
    description = forms.CharField(required=False, 
                                  widget=forms.Textarea(
                                      attrs={
                                          "rows": 30, 
                                          "cols":60, 
                                          "class": "desc",
                                          "id": "description"
                                          }
                                      )
                                  )
    prix = forms.FloatField(required=False, initial=12.66)
    active = forms.BooleanField(required=False)
    class Meta:
        model = Produit
        fields = ['nom', 'description', 'prix', 'active', 'live']
        
        
class PureProduitForm(forms.Form):
    nom = forms.CharField(required=False,
                          widget=forms.TextInput(
                              attrs={
                                  'class': 'name',
                                  'placeholder': 'Enter the name of the product here'
                              }
                          ))
    description = forms.CharField(required=False, 
                                  widget=forms.Textarea(
                                      attrs={
                                          "rows": 10, 
                                          "cols":70, 
                                          "class": "desc",
                                          "id": "description"
                                          }
                                      )
                                  )
    prix = forms.FloatField(required=False, label="prix du produit ")
    active = forms.BooleanField(required=False, help_text=" This field hepls to know if the product is active or not")