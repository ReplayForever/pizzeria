from django.contrib import admin

from pizza.models import Post


@admin.register(Post)
class PizzaAdmin(admin.ModelAdmin):
    exclude = ('slug',)
