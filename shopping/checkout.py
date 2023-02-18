
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib import messages

from shopping.checkoutform import CheckoutForm


class Checkout(TemplateView):
    template_name = 'checkout.html'

    # Make a dispatch method to handle authentication
    def dispatch(self, *args, **kwargs):
        # Check if user is authenticated
        if not self.request.user.is_authenticated:
            # Redirect them to the login page if not
            return redirect('/login/')
        return super().dispatch(*args, **kwargs)

    # Override the post method to handle the form submission
    def post(self, request, *args, **kwargs):
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Process payment using selected payment method (credit card, PayPal, etc.)
            # Update order status to "pending"
            # Send notification email to customer and admin
            messages.success(request, 'Order placed successfully!')
            return redirect('home')
        else:
            # If form is not valid, render the template with the errors
            context = {'form': form}
            return render(request, self.template_name, context)

    # Override the get method to initialize the form
    def get(self, request, *args, **kwargs):
        form = CheckoutForm()
        context = {'form': form}
        return render(request, self.template_name, context)

