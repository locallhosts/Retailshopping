from django.contrib.auth.forms import UserCreationForm
from django import forms

from shopping.signup import CustomerUser


# form validation form signup

"""
It's a form that inherits from UserCreationForm, and adds the fields that I want to be required
"""

class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)
    country = forms.CharField(max_length=30, required=True)
    city = forms.CharField(max_length=30, required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(), required=True)

    class Meta:
        model = CustomerUser
        fields = ('email', 'name', 'first_name', 'last_name', 'phone', 'country', 'city', 'address')

    def clean(self):
        """
        If the email already exists in the database, raise a validation error. If the passwords don't match, raise a
        validation error
        """
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if CustomerUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists.')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

    def save(self, commit=True):
        """
        The function takes in the form data, creates a user object, sets the username, email, password, and other fields,
        and then saves the user object

        :param commit: If True, then the changes to the object are saved to the database. If False, then the changes are
        made in memory but not persisted to the database, defaults to True (optional)
        :return: The user object
        """
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # set username as the email
        user.name = self.cleaned_data['name']
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        user.phone = self.cleaned_data['phone']
        user.country = self.cleaned_data['country']
        user.city = self.cleaned_data['city']
        user.address = self.cleaned_data['address']

        if commit:
            user.save()

        return user
