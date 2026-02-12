from django.urls import path
from product import views
urlpatterns=[
    path('',views.ViewCategories.as_view(),name='categories-list'),
    path('<int:pk>/',views.ViewCategories.as_view(),name='view-specific-category')
]