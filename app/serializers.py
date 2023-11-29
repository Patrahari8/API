from .models import *
from rest_framework import serializers

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'