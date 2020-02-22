from django import forms

from pizza.models import PizzaPost, ShoppingCartModel


class PizzaForm(forms.ModelForm):
    class Meta:
        model = PizzaPost
        fields = ['title', 'price', 'image', 'description']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'})
        }


class ShoppingCartForm(forms.ModelForm):
    class Meta:
        model = ShoppingCartModel
#        fields = ['address', 'number', 'user']
        fields = ['count', 'pizza_slug']

        widgets = {
            'count': forms.TextInput(attrs={'class': 'form-control'}),
        }

#        widgets = {
#            'address': forms.TextInput(attrs={'class': 'form-control'}),
#            'number': forms.TextInput(attrs={'class': 'form-control'})
#        }

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super(ShoppingCartForm, self).__init__(*args, **kwargs)
