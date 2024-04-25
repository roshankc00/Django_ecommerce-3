from rest_framework import serializers
from .models import Wishlist

class WishlistSerializer(serializers.Serializer):
    class Meta:
        model=Wishlist
        fields=['name', 'user', 'products']