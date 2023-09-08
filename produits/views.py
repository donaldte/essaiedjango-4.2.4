from django.shortcuts import render
from .models import Produit
# Create your views here.


def product_list_view(request):
    queryset = Produit.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'produit/liste.html', context)