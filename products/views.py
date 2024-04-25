from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import CategorySerializer
from .renderer import ProdCatRenderer
from rest_framework import status
from rest_framework.response import Response
from .models import Category
# Create your views here.


class CategoryView(APIView):
    renderer_classes=[ProdCatRenderer]
    def post(self,request,format=None):
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'success':True,'message':'Category created successfully'},status=status.HTTP_201_CREATED)           
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,pk=None,format=None):
        if pk is not None:
            stu=Category.objects.get(id=pk)
            serializer=CategorySerializer(stu)
            return Response(serializer.data)
        else:
            task=Category.objects.all()
            serializer=CategorySerializer(task,many=True)
            return Response(serializer.data)
    def put(self,request,pk=None,format=None):
        if pk is not None:
            task=Category.objects.get(pk=pk)
            serializer=CategorySerializer(task,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':"Complete data Updated successfully"}) 
        else:
            return Response({'message':"Id field is required"},status=status.HTTP_400_BAD_REQUEST) 
            
    def delete(self, request,pk=None,format=None):
        if pk is not None:
          task=Category.objects.get(pk=pk)
          task.delete()
          return Response({'message':"Category Deleted successfully"})        
        else:
            return Response({'message':"Id field is required"},status=status.HTTP_400_BAD_REQUEST) 