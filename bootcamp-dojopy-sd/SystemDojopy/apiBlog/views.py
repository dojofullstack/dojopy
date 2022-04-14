from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response
from rest_framework import status
from blog.models import *
from .serializers import *
# from rest_framework.views import Response
# Create your views here.



class ListPost(APIView):
    def get(self, request):
        articles = BlogArticles.objects.all().order_by('-date_created')

        data =  ListPostSerializers(articles, many=True)

        return Response({'data': data.data, 'message': 'ok'})


class DetailPost(APIView):
    def get(self, request, id):
        article = get_object_or_404(BlogArticles, id=id)
        data = DetailPostSerializers(article)
        return Response({'data': data.data})


class Contact(APIView):
    def post(self, request):
        data = ContactSerializers(data=request.data)
        if data.is_valid():
            save_contact =  data.save()
        else:
            errors = data.errors
            return Response({'message': errors})

        return Response({"id": save_contact.id, 'message': 'data created'} , status=status.HTTP_201_CREATED)
