from django.db import models

from shopping.category import Category

"""
I want to create a dropdown menu that contains all the titles from the Category class
"""


class ProductTitle(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category_title = models.CharField(max_length=50, choices=[
                                                                 (cat.title_1, cat.title_1) for cat in
                                                                 Category.objects.filter()
                                                             ] + [
                                                                 (cat.title_2, cat.title_2) for cat in
                                                                 Category.objects.all()
                                                             ] + [
                                                                 (cat.title_3, cat.title_3) for cat in
                                                                 Category.objects.all()
                                                             ] + [
                                                                 (cat.title_4, cat.title_4) for cat in
                                                                 Category.objects.all()
                                                             ])
