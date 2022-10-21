from django.urls import path
from . import views


urlpatterns = [
    path('',views.getRoute,name="Get Route"),
    path('products/',views.getProducts,name="Get Product"),
    path('products/<str:pk>/',views.getProduct,name="Get Product")
]
