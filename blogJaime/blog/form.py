from django import forms

class FormContact(forms.Form):
    email = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    consult = forms.CharField(required=False)
    