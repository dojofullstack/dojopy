from django.db import models
from django.conf import settings
from django.contrib.auth.models import  User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class AdressBilling(models.Model):
    adress = models.CharField(max_length=200, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.adress


class Tags(models.Model):
    tags = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.tags


class BlogModel(models.Model):
    # blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    adress = models.CharField(max_length=100, null=True)
    resume = models.TextField(null=True)
    url_facebook = models.URLField(max_length=200)
    url_github = models.URLField(max_length=200)
    url_twitter = models.URLField(max_length=200, null=True)
    email = models.EmailField(max_length=200)


    def __str__(self):
        return f'{self.title} {self.adress}'

    class Meta:
        ordering = ["title"]
        db_table = 'modelblog'



class BlogArticles(models.Model):
    title_post = models.CharField(max_length=100, null=True)
    slug = models.SlugField(max_length=200, null=True, unique=True)
    resume_post = models.TextField(null=True)
    author = models.ForeignKey(
                        User,
                        blank=True,
                        on_delete=models.CASCADE,
                        null=True
                        )
    body = models.TextField()
    post_image = models.ImageField(upload_to='image')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(null=True, blank=True)

    tags = models.ManyToManyField('Tags')

    def __str__(self):
        return self.slug


class ContactModel(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20, null=True)
    message = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.email} {self.date_created.strftime("%y-%m-%d %H:%M:%S %Z")}'


