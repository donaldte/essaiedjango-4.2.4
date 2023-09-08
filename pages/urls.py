from django.urls import path 
from .views import *

app_name = 'pages'

urlpatterns = [
    path('', home_view, name='home'), # path,url 
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('product_deta/<int:my_id>/', product_detail_view, name='product_detail'),
    path('product_create/', product_create_view, name='product_create'),
    path('product_delete/<int:my_id>/', product_delete_view, name='product_delete'),
    path('product_list/', product_list_view, name='product_list'),
    
]
