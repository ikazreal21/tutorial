from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index, name='index1'),
    path('login', views.Login, name='login'),
    path('register', views.Register, name='register'),
    path('logout', views.Logout, name='logout'),
]
