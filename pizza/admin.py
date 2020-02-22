from django.contrib import admin

from pizza.models import PizzaPost


@admin.register(PizzaPost)
class PizzaAdmin(admin.ModelAdmin):
    exclude = ('slug',)
