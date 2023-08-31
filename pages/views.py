from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProduitForm
from produits.models import Produit
# Create your views here.
def product_detail_view(request):
    obj = Produit.objects.all()
    context = {
        'objects': obj 
    }
    return render(request, 'produit/detail.html', context)


def product_create_view(request):
    form = ProduitForm(request.POST or None)
    message = ''
    if form.is_valid():
        form.save()
        message = 'le produit a été bien enregistré'
        form = ProduitForm()
        
    context = {
        'form': form,
        'message': message
    }    
    
    return render(request, 'produit/create.html', context)    
    


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