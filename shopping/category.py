
from django.db import models


# The Category class is a model that has a name, logo, and four titles
class Category(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='media/category_logos/')
    title_1 = models.CharField(max_length=50, blank=True)
    title_2 = models.CharField(max_length=50, blank=True)
    title_3 = models.CharField(max_length=50, blank=True)
    title_4 = models.CharField(max_length=50, blank=True)

    @staticmethod
    def get_all_categories():
        """
        It returns all the categories in the database
        :return: All the categories in the database.
        """
        return Category.objects.all()

    def title_choices(self):
        """
        It returns a list of tuples, where each tuple is a pair of strings
        :return: A list of tuples.
        """
        return [(self.title_1, self.title_1), (self.title_2, self.title_2), (self.title_3, self.title_3),
                (self.title_4, self.title_4)]

    def __str__(self):
        return self.name



