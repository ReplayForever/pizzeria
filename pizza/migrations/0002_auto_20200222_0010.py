# Generated by Django 3.0.3 on 2020-02-21 21:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoppingcartmodel',
            options={'ordering': ['order_time']},
        ),
        migrations.RemoveField(
            model_name='shoppingcartmodel',
            name='address',
        ),
        migrations.RemoveField(
            model_name='shoppingcartmodel',
            name='full_price',
        ),
        migrations.RemoveField(
            model_name='shoppingcartmodel',
            name='number',
        ),
        migrations.RemoveField(
            model_name='shoppingcartmodel',
            name='user',
        ),
        migrations.AddField(
            model_name='shoppingcartmodel',
            name='count',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='shoppingcartmodel',
            name='kind_of_pizza',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pizza.PizzaPost'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoppingcartmodel',
            name='order_id',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoppingcartmodel',
            name='pizza_slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
