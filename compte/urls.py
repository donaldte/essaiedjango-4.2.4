from django.urls import path 

from . import views

app_name = 'compte'
urlpatterns = [
    path('register/', views.user_registration_view, name='register'),
    path('login/', views.user_login_view, name='login'),
    path('password-reset/<uidb64>/<token>/', views.activate_account_view, name='password_reset'),
    path('logout/', views.logout_view, name='logout'),
]
