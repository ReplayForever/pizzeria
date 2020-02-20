from django.db import models
from django.utils.text import slugify
from time import time
from django.shortcuts import reverse


class Post(models.Model):
    title = models.CharField(max_length=32, db_index=True)
    price = models.FloatField()
    image = models.ImageField(default=None)
    description = models.TextField(default=None)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) + str(int(time()))

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pizza', kwargs={'slug': self.slug})
