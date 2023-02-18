from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models


# It's a subclass of AbstractUser that adds the fields name, email, phone, country, city, and address
class CustomerUser(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.TextField()
    groups = models.ManyToManyField(
        Group,
        related_name='customeruser',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions '
                  'granted to each of their groups.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customeruser',
        blank=True,
        help_text='Specific permissions for this user.'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone', 'country', 'city', 'address']

