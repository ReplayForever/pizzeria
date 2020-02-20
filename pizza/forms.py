from django import forms

from pizza.models import Post


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'price', 'image', 'description']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'})
        }
