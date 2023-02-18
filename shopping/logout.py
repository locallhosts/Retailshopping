from django.contrib.auth import logout
from django.shortcuts import redirect


def logout_view(request):
    """
    It logs out the user and redirects them to the homepage

    :param request: The request object is passed to the view by Django. It contains metadata about the request, including
    the HTTP method
    :return: The user is being logged out and redirected to the home page.
    """
    logout(request)
    return redirect('/')
