from django.urls import path

from . import views

urlpatterns = [
    path("", views.store, name="store"),
    path("products/", views.list_products, name="products"),
    path("products/<slug:product_slug>", views.product_detail, name="product_detail"),
    path("products/cat/<slug:category_slug>/", views.store, name="products_by_category"),
]