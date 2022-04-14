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
        return render(request, 'blog/blogFree/contact.html', {'form_error': ''})        
    def post(self, request):
        form = ContactForm(request.POST)
        is_valid = form.is_valid()
        if is_valid:
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            message = form.cleaned_data.get('message')
            print(first_name, last_name, email)

            print('save data in table Contact')
            ContactModel.objects.create(
                            first_name=first_name,
                            last_name=last_name,
                            email=email,
                            message=message,
                            phone=phone,
                            )
        else:
            return render(request, 'blog/blogFree/contact.html', {'form_error': form.errors})        

        return redirect('/')



class Home(View):
    def get(self, request):
        return redirect('/blog/')


class Blog(View):
    def get(self, request):
        articles = BlogArticles.objects.all()
        print(articles)
        return render(request, 'blog/blogFree/blog.html', {'listPost': articles})        


class Article(View):
    def get(self, request, slug):
        # article = get_object_or_404(BlogArticles, slug=slug)
        article = BlogArticles.objects.filter(slug=slug).order_by('-date_created')
        print(article)
        article = article.last()

        # try:
        #     post = BlogArticles.objects.get(slug=slug, title_post='python')
        # except Exception as e:
        #     print(e)
        #     return render(request, 'blog/notfound.html')

        return render(request, 'blog/blogFree/article.html', {'article': article})
