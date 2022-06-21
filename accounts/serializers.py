
from rest_framework import serializers
from accounts.models import Enpdata

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model =Enpdata
        fields='__all__'
