from django.db import models



class Contact(models.Model):
    name = models.CharField(max_length=200, default='', null=True)
    last_name = models.CharField(max_length=200, default='', null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=200, default='')
    message = models.TextField(default="")

    def __str__(self):
        return f'{self.name} {self.email}' 