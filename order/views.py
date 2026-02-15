from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin
from order.models import Cart
from order.serializers import CartSerializer

class CartViewSet(CreateModelMixin,GenericViewSet,RetrieveModelMixin):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer
    











# Create your views here.
#Step to build an ApI
#model
#serializer
#Viewset
#router