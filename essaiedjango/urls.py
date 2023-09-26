
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('', include('produits.urls')),
    path('cours/', include('cours.urls')),
    path('tache/', include('tache.urls')),
   
]
