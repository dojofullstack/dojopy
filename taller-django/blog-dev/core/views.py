from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class ApiPublica(APIView):

    def get(self, request):
        return Response({
            'statusCode': 1,
            'message': 'ok',
            'data': "api publica"
            },
            status=status.HTTP_200_OK
            )




class ApiPrivada(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response({
            'statusCode': 1,
            'message': 'ok',
            'data': "api privada"
            },
            status=status.HTTP_200_OK
            )
    
    def post(self, request):
        nombre = request.data.get('nombre')

        print(nombre)
        return Response({
            'statusCode': 1,
            'message': 'ok',
            'nombre': nombre,
            'data': "api privada desde POST"
            },
            status=status.HTTP_200_OK
            )






