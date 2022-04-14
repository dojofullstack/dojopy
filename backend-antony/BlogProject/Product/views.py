from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import *


class ListProduct(APIView):
    def get(self, request):
        product = Product.objects.all().order_by('date_created')
        product = product.values()

        return Response({
                'data': product,
                'message': 'ok',
                'StatusCode': 1
                },
                status=status.HTTP_200_OK
                )
