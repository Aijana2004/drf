from django.urls import path
from .views import ProductViewsets


urlpatterns = [
    path('',ProductViewsets.as_view({'get':'list','post':'create'}),name='product_list'),
    path('<int:pk>/', ProductViewsets.as_view({'get': 'retrieve',
                                               'put': 'update',
                                               'delete':'destroy'}), name='product_detail'),


]