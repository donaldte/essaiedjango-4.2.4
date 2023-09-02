from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProduitForm, PureProduitForm
from produits.models import Produit
# Create your views here.
def product_detail_view(request):
    obj = Produit.objects.all()
    context = {
        'objects': obj 
    }
    return render(request, 'produit/detail.html', context)


# def product_create_view(request):
#     form = ProduitForm(request.POST or None)
#     message = ''
#     if form.is_valid():
#         form.save()
#         message = 'le produit a été bien enregistré'
#         form = ProduitForm()
        
#     context = {
#         'form': form,
#         'message': message
#     }    
    
#     return render(request, 'produit/create.html', context)    
    
# def product_create_view(request):
#     message = ''
#     if request.method =='POST':
#         data = request.POST 
#         nom = data.get('nom') # nom = request.POST.get('nom')
#         prix = data.get('prix')
    
#         description = data.get('description')
    
#         Produit.objects.create(nom=nom, prix=prix, description=description)
#         message = 'produit cree avec success'
#     return render(request, 'produit/create.html', {'message': message})


def product_create_view(request, *args, **kwargs):
    message = ''
    form = PureProduitForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        Produit.objects.create(**data)
        message = 'donnee enregistrees '
        form = PureProduitForm()
    return render(request, 'produit/create.html', {'message': message, 'form': form})


def home_view(request, *args, **kwargs): #args, kwargs
    liste  = ['son', 'maman', 'papa', 'frere', 'soeur']
    
    user = request.user 
    print(user)
    context = {
        "liste": liste,
        'user': user
    }
    
        
    return render(request, "home.html", context)

def about_view(request, *args, **kwargs): #args, kwargs
    
    liste_numbre = [1,2,3,4,5,6,7,8,9,10]
    
    context = {
        'liste_numbre': liste_numbre,
        'title': 'about us',
        'my_number': 123,
        'html': '<center>hello world</center>'
        }
    
    return render(request, "about.html", context)


def contact_view(request, *args, **kwargs): #args, kwargs
   
    return render(request, "contact.html")