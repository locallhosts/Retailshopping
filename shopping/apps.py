from django.apps import AppConfig


# > The `ShoppingConfig` class is a subclass of `AppConfig` and it's used to configure the `shopping` app
class ShoppingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shopping'
