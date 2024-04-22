from django.urls import path
from deliveryapp.views import *

urlpatterns = [
    path('delivery_list', delivery,name='delivery_list')


]