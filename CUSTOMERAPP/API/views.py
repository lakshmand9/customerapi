from rest_framework import viewsets
from CUSTOMERAPP.models import NewCustomer
from CUSTOMERAPP.API.serializers import NewCustomer_Serializer_List

class NewCustomer_Serializer_ListView(viewsets.ModelViewSet):
    queryset = NewCustomer.objects.all()
    serializer_class = NewCustomer_Serializer_List




