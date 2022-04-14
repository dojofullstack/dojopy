from django import forms
# from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.formfields import PhoneNumberField


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    phone = PhoneNumberField()
    message = forms.CharField(max_length=300)
