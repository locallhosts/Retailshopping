from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class Dashboard(TemplateView):

    # Make a dispatch method to handle authentication
    def dispatch(self, *args, **kwargs):
        templates_name = 'myaccount.html'

        # Check if user is authenticated
        if not self.request.user.is_authenticated:
            # Redirect them to the home page if not
            return redirect('/login/')

        # Render the template if they are
        return render(self.request, templates_name)
