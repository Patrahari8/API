from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class ProductCrud(APIView):
    def get(self, request, Pid):
        
        PLO=Product.objects.all()
        SPLO=ProductModelSerializer(PLO, many=True)
        return Response(SPLO.data)
        
        # PLO=Product.objects.get(Pid=Pid)
        # SPLO=ProductModelSerializer(PLO)
        # return Response(SPLO.data)
    
    def post(self,request,Pid):
        JD=request.data
        PSD=ProductModelSerializer(data=JD)
        if PSD.is_valid():
            PSD.save()
            return Response({"message": "INSERTED SUCCESSFULLY"})
        else:
            return Response({"message": "ERROR"})
        
    def put(self, request, Pid):
        id=request.data['Pid']
        PO=Product.objects.get(Pid=id)
        JD=ProductModelSerializer(PO, data=request.data)
        if JD.is_valid():
            JD.save()
            return Response({"message": "UPDATED SUCCESSFULLY"})
        else:
            return Response({"message": "ERROR"})
        



