from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from pizza.models import PizzaPost
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, pizza_slug):
    cart = Cart(request)
    product = get_object_or_404(PizzaPost, id=pizza_slug)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=1,
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, pizza_slug):
    cart = Cart(request)
    product = get_object_or_404(PizzaPost, id=pizza_slug)
    print(product)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)

    return render(request, 'cart/detail.html', context={'cart': cart})
