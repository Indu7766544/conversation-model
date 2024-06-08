from rest_framework.serializers import ModelSerializer

from application.models import products

class ProductSerializer(ModelSerializer):
      class Meta:
            model = products
            fields = "__all__"