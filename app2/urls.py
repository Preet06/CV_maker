from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('style', views.style, name='style'),
    path('input', views.input, name='input'),
]