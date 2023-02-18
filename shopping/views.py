from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .CartItem import CartItem
from .cart import Cart
from .category import Category
from .product import Product
from .producttitle import ProductTitle
from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from django.http import JsonResponse

app_name = 'shopping'


def add_to_cart(request, product_id):
    """
    If the cart item exists, increase the quantity by 1, otherwise create a new cart item

    :param request: The request object is the first parameter to every view. It contains information about the current
    request, such as the method (GET or POST), the user (if any), and the GET and POST parameters
    :param product_id: This is the id of the product that we want to add to the cart
    :return: The cart_id is being returned.
    """
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(cart_id=product_id(request))
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart:view')


def cart_view(request):
    """
    It gets all the CartItem objects that are associated with the current user's cart, and passes them to the template

    :param request: The request object is a Django object that contains metadata about the request sent to the server
    :return: A dictionary with the key 'cart_items' and the value of the cart_items variable.
    """
    cart_items = CartItem.objects.filter(cart=request.session.get('cart_id'))
    return render(request, 'cart.html', {'cart_items': cart_items})


def add_to_cart(request, product_id):
    """
    If the cart key doesn't exist in the session, create it and add the product to it

    :param request: The request object is a Django object that contains metadata about the current request
    :param product_id: This is the id of the product that we want to add to the cart
    :return: The product id is being returned.
    """
    product = Product.objects.get(id=product_id)
    session_key = request.session.session_key
    session = SessionStore(session_key=session_key)
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(product.id)
    session.save()
    return redirect('cart')


def view_cart(request):
    """
    If the cart is in the session, get the product ids from the session, get the products from the database, and render the
    cart.html template with the products. If the cart is not in the session, render the cart.html template with a message
    that the cart is empty

    :param request: The request object is a standard Django object that contains metadata about the request sent to the
    server
    :return: A dictionary with the key 'products' and the value of the products variable.
    """
    session_key = request.session.session_key
    session = SessionStore(session_key=session_key)
    if 'cart' in session:
        product_ids = session['cart']
        products = Product.objects.filter(id__in=product_ids)
        return render(request, 'cart.html', {'products': products})
    else:
        return render(request, 'cart.html', {'message': 'Your cart is empty'})


def view_product(request, product_id):
    """
    It gets a product from the database, and then renders a template with that product

    :param request: The request object is the first parameter to all Django views. It contains metadata about the request,
    such as the HTTP method, the URL, the client's IP address, and so on
    :param product_id: This is the parameter that we're passing in
    :return: The product object is being returned.
    """
    product = Product.objects.get(id=product_id)
    return render(request, 'product.html', {'product': product})


# "This view will display the details of a single product title."
#
# The class inherits from Django's DetailView class
class ProductTitleDetailView(DetailView):
    model = ProductTitle
    template_name = 'fag.html'


def product_title_detail(request, pk):
    """
    It takes a request and a primary key, gets the object from the database, and renders the product.html template with the
    object as the context.

    :param request: The request is an HttpRequest object
    :param pk: The primary key of the product title
    :return: The product.html page is being returned.
    """
    object = get_object_or_404(ProductTitle, pk=pk)

    return render(request, 'product.html', {'object': object})


def product_detail(request, product_id):
    """
    It retrieves the product with the given ID, and returns the product data as a JSON response

    :param request: The request object that was sent to the view
    :param product_id: The ID of the product to retrieve
    :return: A JSON response containing the product data.
    """
    # Retrieve the product with the given ID
    product = get_object_or_404(Product, id=product_id)

    # Return the product data as a JSON response
    return JsonResponse({
        'id': product.id,
        'image': product.image.url,
        'description': product.description,
        'name': product.name,
        'price': product.price,

        # ... add any other fields you want to include in the response
    }, status=200)  # specify the HTTP status code for the response


def index(request):
    """
    It gets all the categories from the database and passes them to the template

    :param request: This is the request object that is sent to the view
    :return: The index.html file is being returned.
    """
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})


def products_by_title(request, category_title):
    """
    Get all products that have a category whose title_1 is equal to the category_title parameter.

    :param request: The request object is an instance of HttpRequest. It contains metadata about the request, such as the
    HTTP method, host, path, and more
    :param category_title: This is the parameter that will be passed to the view
    :return: A list of products that match the category title.
    """
    products = Product.objects.filter(category__title_1=category_title)
    context = {'products': products}
    return render(request, 'header.html', context)


def forgot_password(request):
    """
    It renders the forgotpassword.html template

    :param request: The request is an HttpRequest object
    :return: The render function is being returned.
    """
    templates_name = 'forgotpassword.html'
    return render(request, templates_name, {})
