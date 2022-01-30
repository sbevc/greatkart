from carts.models import Cart


def cart_middleware(get_response):
    def middleware(request):
        session_key = request.session.session_key
        cart, _ = Cart.objects.get_or_create(session_id=session_key)
        request.cart = cart
        return get_response(request)
    return middleware
