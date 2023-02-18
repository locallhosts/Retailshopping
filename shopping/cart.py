from django.db import models

from shopping.product import Product


# A Cart is a collection of products, each with a quantity
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        The __str__ method returns a string representation of the object
        :return: The quantity of the product.
        """
        return f'{self.quantity} of {self.product.name}'
