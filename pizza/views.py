from django.shortcuts import render
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
            self.included_html
        )
