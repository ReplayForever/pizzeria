from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from pizza.models import Post
from pizza.forms import PizzaForm


class ListPizza(View):
    model = Post
    included_html = 'pizza/includes/pizzas.html'
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


class ViewPizza(View):
    def get(self, request, slug):
        pizza = get_object_or_404(Post, slug=slug)

        return render(
            request,
            'pizza/pizza.html',
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
