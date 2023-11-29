from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view,permission_classes
from API1.serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def employee(request):
    empdata=EmpolyeeTable.objects.all()
    empjasondata=EmployeeSerializedData(empdata,many=True)
    return Response(empjasondata.data)
