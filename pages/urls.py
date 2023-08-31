from django.urls import path 
from .views import *
urlpatterns = [
    path('', home_view, name='home'), # path,url 
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('product_detail/', product_detail_view, name='product_detail'),
    path('product_create/', product_create_view, name='product_create'),
]
