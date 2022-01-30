from django.shortcuts import render, redirect


def cart_detail(request):
    return render(request, "store/cart.html", context={"cart": request.cart})


def add_to_cart(request, product_id):
    request.cart.add_item(product_id)
    return redirect('carts:cart')


def decrease_item_quantity(request, product_id):
    request.cart.decrease_quantity(product_id)
    return redirect('carts:cart')


def remove_cart_item(request, product_id):
    request.cart.remove_item(product_id)
    return redirect('carts:cart')
