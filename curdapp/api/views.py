from rest_framework import viewsets
from curdapp.models import ProductData
from curdapp.api.serializers import ProductData_Serializer

class ProductDataView(viewsets.ModelViewSet):
    queryset = ProductData.objects.all()
    serializer_class = ProductData_Serializer

