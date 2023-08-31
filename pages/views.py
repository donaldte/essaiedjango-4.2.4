from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

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
    
    return render(request, "about.html")


def contact_view(request, *args, **kwargs): #args, kwargs
   
    return render(request, "contact.html")