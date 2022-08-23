from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('intake/', views.intake, name='intake'),
    path('natadash/', views.natadash, name='natadash'),
    path('clients/', views.clients, name='clients'),
    path('delete/', views.delete, name='delete'),
    path('accept/', views.accept, name='accept'),
    path('client/<int:id>', views.client, name='client'),
    path('delete_client', views.delete_client, name='delete_client')
    
]