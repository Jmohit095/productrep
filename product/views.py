from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Category, Subcategory
from .serializer import ProductSerializer , CategorySerializer, SubcategorySerializer
from rest_framework.response import Response
from rest_framework import status
            
class CategoryAPI(APIView):
    def post(self, request, format= None):
        category = CategorySerializer(data=request.data)
        print(request.POST)
        context = {

        }
        if category.is_valid():
            category.save()
            context['data'] = category.data
            return Response(data = context, status = status.HTTP_200_OK)
        else:
            print(category.errors)
        return Response(data = context, status = status.HTTP_200_OK)
    
    def get(self, request, format = None):
        categories = Category.objects.all()
        category_serializer = CategorySerializer(categories, many = True)
        context = {
            "data" : category_serializer.data
        }
        return Response(data = context, status = status.HTTP_200_OK)

class SubCategoryAPI(APIView):
    
    def post(self, request, format= None):
        subcategory = SubcategorySerializer(data=request.data)
        context = {}
        
        if  subcategory.is_valid():
            sub_data = subcategory.save()
            sub_data.categoryType = request.user
            sub_data.save()
            context['data'] = SubcategorySerializer(sub_data).data
            context['error'] = ""
            return Response(data = context, status = status.HTTP_200_OK)
        else:
            print(subcategory.errors)
        return Response(data = context, status = status.HTTP_200_OK)
    
    def get(self, request, format = None):
        Subcategories = Subcategory.objects.all()
        Subcategory_serializer = SubcategorySerializer(Subcategories, many = True)
        context = {
            "data" : Subcategory_serializer.data
        }
        return Response(data = context, status = status.HTTP_200_OK)

    
class ProductAPI(APIView):
    def post(self, request, format= None):
        product = ProductSerializer(data= request.data)
        context ={}
        if  product.is_valid():
            product.save()
            context['data'] = product.data
            return Response(data = context, status = status.HTTP_200_OK)
        else:
            print(product.errors)
            return Response(data = context, status = status.HTTP_200_OK)
        
    def get(self, request, format = None):
        product = Product.objects.all()
        Product_serializer = ProductSerializer(product, many = True)
        context = {
            "data" : Product_serializer.data
        }
        return Response(data = context, status = status.HTTP_200_OK)
