from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index,name='index'),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact'),
    path('accounts/profile', views.ProfileView.as_view(),name='profile'),

    #django auth
    path('accounts/login',auth_views.LoginView.as_view(template_name="accounts/login.html"),name="login"),
    path('accounts/logout',auth_views.LogoutView.as_view(),name="logout"),
]