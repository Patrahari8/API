from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
# Create your views here.

class ProductCrud(ViewSet):
    def list(self, request):
        PLO=Product.objects.all()
        SPLO=ProductModelSerializer(PLO, many=True)
        return Response(SPLO.data)
    
    def retrieve(self,request,pk):
        PLO=Product.objects.get(Pid=pk)
        SPLO=ProductModelSerializer(PLO)
        return Response(SPLO.data)
    
    def create(self,request):
        JD=request.data
        PSD=ProductModelSerializer(data=JD)
        if PSD.is_valid():
            PSD.save()
            return Response({"message": "INSERTED SUCCESSFULLY"})
        else:
            return Response({"message": "ERROR"})
    
    def update(self, request, pk):
        PO=Product.objects.get(Pid=pk)
        JD=ProductModelSerializer(PO, data=request.data)
        if JD.is_valid():
            JD.save()
            return Response({"message": "UPDATED SUCCESSFULLY"})
        else:
            return Response({"message": "ERROR"})
        
    def partial_update(self,request,pk):
        po=Product.objects.get(Pid=pk)
        pd=ProductModelSerializer(po,data=request.data,partial=True)
        if pd.is_valid():
            pd.save()
            return Response({"message": "UPDATED SUCCESSFULLY"})
        else:
            return Response({"message": "ERROR"})
        
    def destroy(self,request,pk):
        po=Product.objects.get(Pid=pk)
        po.delete()
        return Response({"message": "DELETED"})