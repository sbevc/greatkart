from django.shortcuts import render, get_object_or_404

from category.models import Category
from store.models import Product


def store(request, category_slug=None):
    products = Product.objects.filter(is_available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(
        request,
        "store/store.html",
        context={"products": products}
    )


def list_products(request):
    products = Product.objects.filter(is_available=True)
    return render(request, "home.html", context={"products": products})


def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, "store/product_detail.html", context={"product": product})
