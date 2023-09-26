from django.urls import path 
from .views import TacheListView, TacheDetailView, TacheModifyView

app_name = 'tache'
urlpatterns = [
    path('list/', TacheListView.as_view(), name='tache_list'),
    path('detail/<int:pk>/', TacheDetailView.as_view(), name='tache_detail'),
    path('modify/<int:pk>/', TacheModifyView.as_view(), name='tache_modify'),
]
