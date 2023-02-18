from django.db import models
from django.urls import reverse
from .category import Category



"""
The Product class is a model that has a name, brand, product_title, description, size, color, price, discount_price,
 category, image, and slug

"""
class Product(models.Model):
    name = models.CharField(max_length=60)
    brand = models.CharField(max_length=60)
    product_title = models.ForeignKey('ProductTitle', on_delete=models.CASCADE, related_name='products')
    description = models.TextField()
    size = models.CharField(max_length=2, choices=[
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    ])
    color = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    discount_price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='uploads/products/')
    slug = models.SlugField(max_length=60, unique=True)

    @staticmethod
    def get_products_by_id(ids):
        """
        Get all products with an id in the list of ids.

        :param ids: a list of product ids
        :return: A list of products that match the ids in the ids list.
        """
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        """
        Return all products.
        :return: All the products in the database
        """
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        """
        If the category_id is not None, return all products that belong to the category_id, otherwise return all products

        :param category_id: The id of the category to filter by
        :return: A list of products that are in the category with the given category_id.
        """
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

    def get_absolute_url(self):
        """
        It returns the URL of the product detail page for the product instance
        :return: The reverse function is being used to return the url of the product detail page.
        """
        return reverse('product_detail', args=[str(self.category.slug), str(self.slug)])
