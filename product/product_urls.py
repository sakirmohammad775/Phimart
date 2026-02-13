from django.urls import path
from product import views
urlpatterns=[
    path('',views.ProductList.as_view(),name='product-list'),
    path('<int:id>/',views.CategoryDetails.as_view(),name='product-list'),
    
]