from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect

from shopping.signup import CustomerUser

"""
    If the request method is POST, then get the email and password from the request, check if they are empty, if they are
    empty, return an error message, if they are not empty, try to get the user from the database, if the user does not
    exist, return an error message, if the user does exist, check if the password is correct, if the password is correct,
    check if the user is staff, if the user is staff, return an error message, if the user is not staff, log the user in and
    redirect them to the dashboard
    
    :param request: The request is an HttpRequest object. It contains metadata about the request, including the HTTP method
    :return: The login view is being returned.
"""


@csrf_protect
def login_view(request):
    """
    If the request method is POST, then get the email and password from the request, check if they are empty, if they are
    empty, return an error message, if they are not empty, try to get the user from the database, if the user does not
    exist, return an error message, if the user does exist, check if the password is correct, if the password is correct,
    check if the user is staff, if the user is staff, return the login page, if the user is not staff, log the user in and
    redirect them to the dashboard

    :param request: The request is an HttpRequest object
    :return: The login view is being returned.
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not email or not password:
            return render(request, 'login.html', {'error_message': 'Email and password are required fields'})

        try:
            user = CustomerUser.objects.get(email=email)
        except CustomerUser.DoesNotExist:
            return render(request, 'login.html', {'error_message': '    Invalid Login Try again'})

        if user.check_password(password):
            if user.is_staff:
                return render(request, 'login.html', {})

            else:
                login(request, user)
                return redirect('/dashboard')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid Email or Password'})

    return render(request, 'login.html')
