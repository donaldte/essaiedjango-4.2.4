from django.urls import path

from .views import *

app_name = 'produits'
urlpatterns = [
    path('product_list/', product_list_view, name='product_list'),
]