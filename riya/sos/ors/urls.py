from django.urls import path
from . import views

urlpatterns = [
    path('riya/', views.riya_ors),
    path('welcome/', views.welcome),
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('', views.welcome),
]
