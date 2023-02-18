from django.shortcuts import render, redirect
from django.views.generic import TemplateView

"""
The Dashboard class inherits from the TemplateView class, which is a generic class-based view that helps developers
create a view for a specific template without re-inventing the wheel
"""

class Dashboard(TemplateView):


    def dispatch(self, *args, **kwargs):
        """
        If the user is not authenticated, redirect to the login page. Otherwise, render the myaccount.html template
        :return: The user is being redirected to the login page if they are not authenticated.
        """
        templates_name = 'myaccount.html'


        if not self.request.user.is_authenticated:

            return redirect('/login/')


        return render(self.request, templates_name)
