from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("reading/", views.generate, name="generate"),
    path("gua/", views.flipping, name= 'flipping')

]