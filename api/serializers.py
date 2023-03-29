from rest_framework import serializers
from .models import Product, Category
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class CategorySerializer(serializers.ModelSerializer):
    """
    serializer for categories that serialize all of the fields
    based on Category model

    """

    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    """
    serializer for products that serialize:
    (id', 'url', "name",, "sku", "slug", "category", "price", "discount", "available",
    "quantity", "created", "image", "description")
    and add relation to category serializer \nbased on Product model

    """
    category = CategorySerializer(many=True)
    class Meta:
        model = Product
        fields = (
            "id",
            "url",
            "name",
            "sku",
            "slug",
            "category",
            "price",
            "discount",
            "available",
            "quantity",
            "created",
            "image",
            "description",
        )
class UserSerializer(serializers.ModelSerializer):
    """
    serializer for user that serialize :
    ('id', 'username', 'first_name', 'last_name', 'email', 'image',
    'is_staff', 'is_active', 'is_superuser')\nbased on default 'User' model

    """

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "image",
            "is_staff",
            "is_active",
            "is_superuser",
        )

    image = serializers.ImageField(source="profile.image", required=False)
