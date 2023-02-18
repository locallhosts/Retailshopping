from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .checkout import Checkout
from .login import login_view
from .logout import logout_view
from .my_accounts import Dashboard
from .signup_view import signup

app_name = 'shopping'

"""
A list of url patterns.
"""

urlpatterns = [
                  path('', views.index, name="index"),

                  path('register/', signup, name='register'),
                  path('login/', login_view, name='login'),
                  path('logout/', logout_view, name='logout'),
                  path('cart/', views.cart_view, name='cart'),
                  path('checkout/', Checkout.as_view(), name='checkout'),
                  path('dashboard/', Dashboard.as_view(), name='dashboard'),
                  path('reset-password/', views.forgot_password, name='reset-password'),

                  path('title/<str:category_title>', views.products_by_title, name='products_by_title'),
                  path('prod_title/<str:pk>/', views.product_title_detail, name='product_title_detail'),
                  path('product/<int:product_id>/', views.product_detail, name='product_detail'),
                  # use product_id instead of pk

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
