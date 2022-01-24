from django.db import models
from django.urls import reverse
from django.utils.text import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    image = models.ImageField(upload_to="photos/categories", blank=True)

    class Meta:
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name

    def get_products_url(self):
        return reverse('store:products_by_category', kwargs={"category_slug": self.slug})
