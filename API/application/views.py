from django.shortcuts import render

# Create your views here.


from application.models import products
from application.serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet

class ProductCUDE(ModelViewSet):
      queryset = products.objects.all()
      serializer_class = ProductSerializer
