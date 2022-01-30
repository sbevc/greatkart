from django.urls import path

from . import views

urlpatterns = [
    path("", views.cart_detail, name='cart'),
    path("add_to_cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("decrease_quantity/<int:product_id>/", views.decrease_item_quantity, name="decrease_item_quantity"),
    path("remove/<int:product_id>/", views.remove_cart_item, name="remove_cart_item"),
]
