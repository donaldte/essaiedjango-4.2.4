from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request, *args, **kwargs): #args, kwargs
    liste  = [3,4,5,6,7,7]
    
    user = request.user 
    context = {
        "liste": liste
    }
    if user.is_authenticated:
        context['user'] = user.username
        
    else:
        context['user'] = "Pas connecté"
        
    return render(request, "home.html", context)

def about_view(request, *args, **kwargs): #args, kwargs
    
    return render(request, "about.html")


def contact_view(request, *args, **kwargs): #args, kwargs
   
    return render(request, "contact.html")