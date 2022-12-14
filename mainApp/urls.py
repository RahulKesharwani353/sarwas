from django.urls import path
from .views import *

urlpatterns = [
    path('add-product/', ProductGet.as_view()),
    path('rate-product/', RateProduct.as_view()),
    path('product/', Search.as_view()),
]