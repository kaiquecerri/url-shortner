from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import CustomLoginForm

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='users/login.html',
            authentication_form=CustomLoginForm),
        name='login'
    ),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register')
]
