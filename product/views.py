from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product, Category
from product.serializers import ProductSerializer

@api_view()
def view_products(request):
    product=Product.objects.select_related('category').all()
    serializer=ProductSerializer(product,many=True)
    return Response(serializer.data)

@api_view()
def view_specific_product(request, id):
    product = get_object_or_404(Product,pk=id)
    serializer=ProductSerializer(product)
    return Response(serializer.data)


@api_view()
def view_categories(request,id):
    product=get_object_or_404(product,pk=id)
    serializer=ProductSerializer(product)
    return Response(serializer.data)
