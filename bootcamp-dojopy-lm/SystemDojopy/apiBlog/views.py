from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from blog.models import *
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator
from django.db.models import Q
from django.db import connection
from time import time


class ApiListPost(APIView):
    def get(self, request):
        articles = BlogArticles.objects.all()
        data = SerializersPost(articles, many=True)
        return Response(data.data)


class GetPost(APIView):
    def get(self, request, id):
        # articles = BlogArticles.objects.get(id=id)
        article = get_object_or_404(BlogArticles, id=id)
        data = SerializersGetPost(article)
        return Response(data.data)


class FormContact(APIView):
    def post(self, request):
        # print(request.data)
        data = SerializersFormContact(data=request.data)
        is_data_valid = data.is_valid()
        if is_data_valid:
            contact = data.save()
            return Response({'id': contact.id, 'message': 'contact created'})
        else:
            errors = data.errors
            return Response({'message': 'data invalida validar los siguientes campos', 'fields': errors})



class ConectorCRM(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        page_size = request.query_params.get('page_size', 10)
        page_number = request.query_params.get('page_number', 1)
        phone = request.query_params.get('phone', '')
        first_name = request.query_params.get('first_name', '')

        data = ContactModel.objects.filter(
                        Q(phone__startswith=phone) |
                        Q(first_name__icontains=first_name)
                        ).order_by('first_name').exclude(
                            phone='99999'
                        )
        # cursor = connection.cursor()
        # cursor.execute("""
        # SELECT "blog_contactmodel"."id", "blog_contactmodel"."first_name", "blog_contactmodel"."last_name", "blog_contactmodel"."email", "blog_contactmodel"."phone", "blog_contactmodel"."message", "blog_contactmodel"."date_created", "blog_contactmodel"."date_updated" FROM "blog_contactmodel" WHERE (("blog_contactmodel"."phone" LIKE '99' OR "blog_contactmodel"."first_name" LIKE 'enrique') AND NOT ("blog_contactmodel"."phone" = 99999 AND "blog_contactmodel"."phone" IS NOT NULL)) ORDER BY "blog_contactmodel"."first_name" ASC
        # """)
        # rows = cursor.fetchall()
        # print(rows)


        paginator = Paginator(data, page_size)

        data = SerializersConectorCRM(paginator.page(page_number), many=True)
        print(len(connection.queries))
        print(connection.queries)

        return Response({'data': data.data})



