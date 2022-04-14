from django import forms
from .models import (
        ModelContact,
        ModelPago
        )
from phonenumber_field.formfields import PhoneNumberField



class RegistrarContacto(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    number_phone = PhoneNumberField(required=False)
    message = forms.CharField(label='Mensaje', max_length=250,
                              widget=forms.Textarea, required=False)

    def registrar_contact(self):
        nombre = self.data.get('name', '')
        email = self.data.get('email', '')
        phone = self.data.get('number_phone', '')
        message = self.data.get('message', '')

        ModelContact.objects.create(name=nombre,
                                    email=email,
                                    number_phone=phone,
                                    message=message
                                    )
        return True


class RegistrarPago(forms.Form):
    CHOICES = (
        ('pe', 'Perú'),
        ('mx', 'México'),
        ('co', 'Colombia'),
    )
    name = forms.CharField(label='Nombre', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    number_phone = PhoneNumberField(required=False)
    message = forms.CharField(label='Mensaje', max_length=250,
                              widget=forms.Textarea, required=False)
    # country = forms.CharField(widget=forms.Select(choices=CHOICES))
    country = forms.ChoiceField(choices=CHOICES)

    def registrar_pago(self):
        nombre = self.data.get('name', '')
        email = self.data.get('email', '')
        phone = self.data.get('number_phone', '')
        message = self.data.get('message', '')
        country = self.data.get('country', '')

        ModelPago.objects.create(name=nombre,
                                    email=email,
                                    number_phone=phone,
                                    message=message,
                                    country=country
                                    )
        return True
