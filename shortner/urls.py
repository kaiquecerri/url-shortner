from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_url/', views.create_url, name='create_url'),
    path('edit_url/<str:shortned_url>/', views.edit_url, name='edit_url'),
    path('delete_url/<str:shortned_url>/', views.delete_url, name='delete_url'),
    path('acess_url/<str:shortned_url>/', views.acess_url, name='acess_url'),
]
