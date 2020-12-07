from rest_framework import serializers
from CUSTOMERAPP.models import NewCustomer



class NewCustomer_Serializer_List(serializers.ModelSerializer):


    class Meta:
            model = NewCustomer
            fields = '__all__'