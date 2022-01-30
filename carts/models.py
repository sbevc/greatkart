from __future__ import annotations

from django.db import models

from store.models import Product


class InvalidProduct(Exception):
    pass


class Cart(models.Model):
    # Carts are bound to django sessions
    session_id = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def sub_total(self):
        return sum(item.sub_total() for item in self.items.all())

    def tax(self):
        return self.sub_total() * .1

    def total(self):
        return self.sub_total() + self.tax()

    def add_item(self, product_id: str) -> None:
        product = self._find_product(product_id)
        try:
            item = self.items.get(product=product)
            item.quantity += 1
            item.save()
        except CartItem.DoesNotExist:
            CartItem.objects.create(
                cart=self,
                product=product,
                quantity=1,
                is_active=True,
            )

    def decrease_quantity(self, product_id: str) -> None:
        product = self._find_product(product_id)
        item = self.items.get(product=product)
        if item.quantity > 1:
            item.quantity -= 1
            item.save()

    def remove_item(self, product_id: str) -> None:
        product = self._find_product(product_id)
        item = self.items.get(product=product)
        item.delete()

    def has_product(self, product_id: str) -> bool:
        product = self._find_product(product_id)
        return self.items.filter(product=product).exists()

    def _find_product(self, product_id: str) -> Product:
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist as e:
            raise InvalidProduct from e


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.product

    def sub_total(self):
        return self.product.price * self.quantity
