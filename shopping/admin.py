
from shopping.category import Category
from .CartItem import CartItem
from .cart import Cart
from .order import Order
from .product import Product
from .producttitle import ProductTitle
from .signup import CustomerUser
from django.contrib import admin


# Register your models here.
admin.site.register(CustomerUser)
admin.site.register(Category)
admin.site.register(ProductTitle)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)


