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
                                          "rows": 10, 
                                          "cols":70, 
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
    
    
    def clean_nom(self, *args, **kwargs): # def clean_<non_chanp_defini>
        nom = self.cleaned_data.get('nom')
        print(nom)
        if nom != 'dp':
            raise forms.ValidationError("Le nom du produit doit etre donald")
        
        return nom 
    
    def clean_description(self, *args, **kwargs):
        description = self.cleaned_data.get('description')
        if description != "dp":
            raise forms.ValidationError("description doit etre donald ")
        
        return description
    
    
        
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