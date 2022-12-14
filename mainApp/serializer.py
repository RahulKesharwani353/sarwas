from rest_framework import serializers
from .models import *


class GetProductDetails(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields='__all__'

class CCScoreDetails(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields=['ccScore','asin']