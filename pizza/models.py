from django.db import models
from django.utils.text import slugify
from time import time
from django.shortcuts import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


class PizzaPost(models.Model):
    title = models.CharField(max_length=32, db_index=True)
    price = models.FloatField()
    image = models.ImageField(default=None)
    description = models.TextField(default=None)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) + str(int(time()))

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pizza', kwargs={'slug': self.slug})

#    @login_required()
#    def add_pizza_to_order(self):
#        ShoppingCartModel.user = user.id
#        ShoppingCartModel.id_pizzas[self.title] = self.price
#
#        return


class ShoppingCartModel(models.Model):
    order_id = models.CharField(max_length=50, auto_created=True)
    order_time = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=1)
    pizza_slug = models.SlugField()
    kind_of_pizza = models.ForeignKey(PizzaPost, unique=False, on_delete=models.CASCADE)

    class Meta:
        ordering = ['order_time']

    def total(self):
        return self.count * self.kind_of_pizza.price

    def name(self):
        return self.kind_of_pizza.title

    def price(self):
        return self.kind_of_pizza.price

    def augment_count(self, count):
        self.count += self.count
        self.save()





#    address = models.TextField(max_length=128, default=None, db_index=True)
#    number = models.IntegerField(default=0)
#    user = models.CharField(max_length=150)
#    full_price = models.FloatField()
#    id_pizzas = {}
#
#    template = 'pizza/shopping_cart.html'
#
#    def __str__(self):
#        return self.user


