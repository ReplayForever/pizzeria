from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from pizza.models import PizzaPost
from pizza.forms import PizzaForm, ShoppingCartModel
from cart.forms import CartAddProductForm


class ListPizza(View):
    model = PizzaPost
    order_object = ShoppingCartModel
    template = 'pizza/index.html'

    def get(self, request):
        objects = self.model.objects.all()

        return render(
            request,
            'pizza/index.html',
            context={
                'objects': objects
            }
        )

    def post(self, request):
        order = self.order_object
#        order = self.order_object.id_pizzas
#        'order': order

        return


class ViewPizza(View):
    template = 'pizza/pizza.html'

    def get(self, request, slug):
        pizza = get_object_or_404(PizzaPost, slug=slug)

        return render(
            request,
            self.template,
            context={
                'pizza': pizza
            }
        )


class AddPost(View):
    form_object = PizzaForm
    template = 'pizza/add_pizza.html'

    def get(self, request):
        form = self.form_object

        return render(
            request,
            self.template,
            context={
                'form': form
            }
        )

    def post(self, request):
        form = self.form_object(request.POST, request.FILES)
        if form.is_valid():
            object_form = form.save()
            return redirect(object_form)

        return render(
            request,
            self.template,
            context={
                'form': form
            }
        )


# class ShoppingCartView(View):
#     form_object = ShoppingCartForm


def product_detail(request, id, slug):
    product = get_object_or_404(PizzaPost,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()

    return render(request,
                  'pizza/pizza.html',
                  {'product': product,
                   'cart_product_form': cart_product_form}
                  )
