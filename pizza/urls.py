from django.urls import path

from pizza import views

urlpatterns = [
    path('', views.ListPizza.as_view(), name='index'),
    path('add/', views.AddPost.as_view(), name='add_pizza'),
    path('<slug:slug>/', views.ViewPizza.as_view(), name='pizza')
]
