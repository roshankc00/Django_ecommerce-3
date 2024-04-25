from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import CategorySerializer,ProductSerializer
from .renderer import ProdCatRenderer
from rest_framework import status
from rest_framework.response import Response
from .models import Category,Product
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.


class CategoryView(APIView):
    renderer_classes=[ProdCatRenderer]
    # authentication_classes=[JWTAuthentication]
    # permission_classes=[IsAuthenticatedOrReadOnly]
    def post(self,request,format=None):
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'success':True,'message':'Category created successfully'},status=status.HTTP_201_CREATED)           
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,pk=None,format=None):
        category_id = request.GET.get('category', None)
        if pk is not None:
            stu=Category.objects.get(id=pk)
            serializer=CategorySerializer(stu)
            return Response(serializer.data)
        else:
            products = Product.objects.filter(category_id=category_id)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
    def patch(self,request,pk=None,format=None):
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
        
        
class ProductView(APIView):
    renderer_classes=[ProdCatRenderer]
    # authentication_classes=[JWTAuthentication]
    # permission_classes=[IsAuthenticatedOrReadOnly]
    def post(self,request,pk=None,format=None):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'success':True,'message':'Product created successfully'},status=status.HTTP_201_CREATED)           
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)        
        
    def get(self,request,pk=None,format=None):
        if pk is not None:
            stu=Product.objects.get(id=pk)
            serializer=ProductSerializer(stu)
            return Response(serializer.data)
        else:
            product=Product.objects.all()
            serializer=ProductSerializer(product,many=True)
            return Response(serializer.data)               
    def delete(self, request,pk=None,format=None):
        if pk is not None:
          task=Product.objects.get(pk=pk)
          task.delete()
          return Response({'message':"Product Deleted successfully"})        
        else:
            return Response({'message':"Id field is required"},status=status.HTTP_400_BAD_REQUEST) 
    def patch(self,request,pk=None,format=None):
        if pk is not None:
            task=Product.objects.get(pk=pk)
            serializer=ProductSerializer(task,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':" Product Updated successfully"}) 
        else:
            return Response({'message':"Id field is required"},status=status.HTTP_400_BAD_REQUEST)     
        
        
        
        