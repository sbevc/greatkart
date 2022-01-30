from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from category.models import Category
from store.models import Product


def store(request, category_slug=None):
    products = Product.objects.filter(is_available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    products_page = paginator.get_page(page_number)
    return render(
        request,
        "store/store.html",
        context={
            "products_page": products_page,
        }
    )


def list_products(request):
    products = Product.objects.filter(is_available=True)
    return render(request, "home.html", context={"products": products})


def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    already_in_cart = request.cart.has_product(product.id)
    context = {
        "product": product,
        "already_in_cart": already_in_cart,
    }
    return render(request, "store/product_detail.html", context=context)
