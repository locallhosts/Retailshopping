from django import forms


class CheckoutForm(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='Email')
    address = forms.CharField(label='Address')
    city = forms.CharField(label='City')
    state = forms.CharField(label='State')
    zip_code = forms.CharField(label='Zip code')
    payment_method = forms.ChoiceField(label='Payment method', choices=(
        ('credit_card', 'Credit card'),
        ('paypal', 'PayPal'),
    ))
    card_number = forms.CharField(label='Card number', required=False)
    card_expiration = forms.CharField(label='Expiration', required=False)
    card_cvc = forms.CharField(label='CVC', required=False)
    paypal_username = forms.CharField(label='PayPal username', required=False)
    paypal_password = forms.CharField(label='PayPal password', required=False, widget=forms.PasswordInput)
