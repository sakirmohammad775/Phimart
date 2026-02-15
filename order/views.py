from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,DestroyModelMixin
from order.models import Cart,CartItem
from order.serializers import CartSerializer

class CartViewSet(CreateModelMixin,DestroyModelMixin,GenericViewSet,RetrieveModelMixin):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer
    
class CartItemViewSet(ModelViewSet):
    serializer_class=CartSerializer
    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs['cart_pk'])
                                                        
    










# Create your views here.
#Step to build an ApI
#model
#serializer
#Viewset
#router