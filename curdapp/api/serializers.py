from rest_framework import serializers
from curdapp.models import ProductData

class ProductData_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ProductData
        fields = '__all__'