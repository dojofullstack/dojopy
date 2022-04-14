from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import *
from .forms import ContactForm

# def blogGeneral(request):
#     if request.method == 'GET':
#         return render(request, 'blog/blog_general.html')


# def blog(request, slug):
#     if request.method == 'GET':
#         print(request.GET.get('id'))
#         print(slug)
#         return render(request, 'blog/blog.html', {'title': slug})


class Contact(View):
    def get(self, request):
        return render(request, 'blog/blogFree/contact.html', {})        
    def post(self, request):
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        data = ContactForm(request.POST)
        is_valid = data.is_valid()
        if is_valid:
            ContactModel.objects.create(
                email=data.cleaned_data.get('email'),
                first_name=data.cleaned_data.get('first_name'),
                last_name=data.cleaned_data.get('last_name'),
                message=data.cleaned_data.get('message'),
                phone=data.cleaned_data.get('phone')
            )
        else:
            errors = data.errors
            data = data.cleaned_data
            return render(request, 'blog/blogFree/contact.html', {'errors': errors, 'data': data}) 

        return redirect('/')



class Home(View):
    def get(self, request):
        return redirect('/blog/')


class Blog(View):
    def get(self, request):
        articles = BlogArticles.objects.all().order_by('-date_created')
        print(articles)
        return render(request, 'blog/blogFree/blog.html', {'listPost': articles})        


class Article(View):
    def get(self, request, myslug):
        article = get_object_or_404(BlogArticles, slug=myslug)
        # article = BlogArticles.objects.get(slug=myslug).order_by('-date_created')

        # article = article.last()

        # try:
        #     post = BlogArticles.objects.get(slug=slug, title_post='python')
        # except Exception as e:
        #     print(e)
        #     return render(request, 'blog/notfound.html')

        return render(request, 'blog/blogFree/article.html', {'article': article})
