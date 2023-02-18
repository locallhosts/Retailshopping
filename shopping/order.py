from django.shortcuts import render, redirect
from django.db import models

from shopping.signup import CustomerUser


class Order(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    items = models.TextField()
    total = models.DecimalField(max_digits=6, decimal_places=2)
    is_approved = models.BooleanField(default=False)
