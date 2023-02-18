from django.shortcuts import render, redirect

from shopping.signupform import CustomUserCreationForm

#
# def signup(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return redirect('/login/')
#         else:
#             error_message = form.errors
#             return render(request, 'register.html', {'form': form, 'error_message': error_message})
#     else:
#         form = CustomUserCreationForm()
#         return render(request, 'register.html', {'form': form})

from django.db import IntegrityError

def signup(request):
    """
    If the form is valid, save it, otherwise, return the form with the errors

    :param request: The request is an HttpRequest object
    :return: The form is being returned.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            try:
                form.save()
            except IntegrityError:
                error_message = 'Username already taken. Please choose a different one.'
                return render(request, 'register.html', {'form': form, 'error_message': error_message})
            else:
                return redirect('/login/')
        else:
            error_message = form.errors
            return render(request, 'register.html', {'form': form, 'error_message': error_message})
    else:
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})
