"""pizzeria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView, FormView
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django import forms
from django.db import models


class PizzaUserCreationForm(UserCreationForm):
    number = models.CharField(max_length=9, blank=True)
    address = models.CharField(max_length=100, blank=True)

    class Meta:
        model = User

        fields = ('username', 'first_name', 'email',)
        field_classes = {
            'username': UsernameField
        }
        widgets = {
            'email': forms.EmailInput(attrs={'required': 'required'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class RegisterUser(FormView):
    form_class = PizzaUserCreationForm
    template_name = 'registration/register.html'
    success_url = '/login/'

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('pizza/', include('pizza.urls')),
    path('', include('django.contrib.auth.urls')),
    path('register/', RegisterUser.as_view(), name='register')
]
