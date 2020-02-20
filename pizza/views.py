from django.shortcuts import render, get_object_or_404
from django.views import View

from pizza.models import Post


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