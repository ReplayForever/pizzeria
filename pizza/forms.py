from django import forms

from pizza.models import Post


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Post
