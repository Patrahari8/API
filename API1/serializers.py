from rest_framework import serializers
from app.models import *

class EmployeeSerializedData(serializers.ModelSerializer):
    class Meta:
        model=EmpolyeeTable
        fields='__all__'