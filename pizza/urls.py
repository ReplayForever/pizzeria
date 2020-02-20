from django.urls import path

from pizza import views

urlpatterns = [
    path('', views.ListPizza.as_view(), name='index')
]
