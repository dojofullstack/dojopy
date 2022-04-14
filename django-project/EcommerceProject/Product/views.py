from django.shortcuts import render
from django.views import  View

# Create your views here.

# def productView(request):
#     if request.method == 'GET':
#         db_data = {'email': 'hola@odojopy.com', 'id': 1}
#         return render(request, 'index.html', context=db_data)
#     elif request.method == 'POST':
#         print('se recibio una solicitud post')
#         return render(request, 'update.html', context={})
#     elif request.method == 'DELETE':
#         print('se recibio una solicitud delete')
        # return render(request, 'delete.html', context={})



class ProductView(View):
    def get(self, request):
        db_data = {'email': 'hola@odojopy.com', 'id': 1}
        return render(request, 'index.html', context=db_data)
    def post(self, request):
        print('se recibio una solicitud post')
        return render(request, 'update.html', context={})
