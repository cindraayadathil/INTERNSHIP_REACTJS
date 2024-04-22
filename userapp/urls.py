from django.urls import path
from userapp.views import *

urlpatterns = [
    path('hello',hello_world,name='hello_world'),
    path('category/list',category_list,name='category_list'),
    path('category/add',category_add,name='category_add'),
    path('product/list',product_list,name='product_list'),
    path('product/add',product_add,name='product_add'),
    path('category/<int:category_id>/view/',category_view,name='category_view'),
    path('product/<int:product_id>/view/',product_view,name='product_view'),
    path('category/<int:category_id>/delete/',category_delete,name='category_delete'),
    path('product/<int:product_id>/delete/',product_delete,name='product_delete'),
    path('category/<int:category_id>/edit/',category_edit,name='category_edit'),
    path('category/<int:category_id>/update/',category_update,name='category_update'),
    path('product/<int:product_id>/edit/',product_edit,name='product_edit'),
    path('product/<int:product_id>/update/',product_update,name='product_update'),



]