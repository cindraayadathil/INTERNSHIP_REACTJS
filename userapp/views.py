from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status

@api_view()
def hello_world(request):
    return Response({"message":"Hello, world!"})

@api_view(['GET'])
def category_list(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
# to post the content to the table through user
@api_view(['GET','POST'])
def category_add(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories,many=True,context={'request': request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def product_add(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True,context={'request': request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# to view based on id of single category
@api_view(['GET'])
def category_view(request,category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
@api_view(['GET'])
def product_view(request,product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)
    # to delete the content
@api_view(['GET','DELETE'])
def category_delete(request,category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'GET':
        serializer = CategorySerializer(category,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','DELETE'])
def product_delete(request,product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'GET':
        serializer = ProductSerializer(product,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','PATCH'])
def category_edit(request,category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return Response({'error':'Category not found'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CategorySerializer(category,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = CategorySerializer(category,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT'])
def category_update(request,category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return Response({'error':'Category not found'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CategorySerializer(category,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = CategorySerializer(category,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PATCH'])
def product_edit(request,product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'error':'product not found'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = ProductSerializer(product,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT'])
def product_update(request,product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'error':'product not found'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# display content with subproducts 
class CategoryWithProduct(APIView):
    def get(self, respect,category_id, format=None):
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found '}, status=status.HTTP_404_NOT_FOUND)
        
        category_serializer = CategorySerializer(category)
        products = Product.objects.filter(category=category)
        products_serializer = ProductSerializer(products, many=True)

        response_data ={
            'category': category_serializer.data,
            'products':products_serializer.data,
        }

        return Response(response_data,status=status.HTTP_200_OK)
