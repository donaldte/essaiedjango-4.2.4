
from django.contrib import admin
from django.urls import path

from pages.views import home_view, about_view, contact_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'), # path,url 
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
]