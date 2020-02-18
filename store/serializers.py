from rest_framework import serializers
from .models import Shop, Address, Coordinates

class ShopSerializer(serializers.ModelSerializer):
  class Meta:
    model = Shop
    fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
  class Meta:
    model = Address
    fields = '__all__'

class CoordinatesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Coordinates
    fields = '__all__'