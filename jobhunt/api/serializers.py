from rest_framework import serializers
from ..models import Category, Service, Seeker


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        read_only_fields = ('is_active', 'is_staff', 'slug')
        exclude = ['IsActive', 'IsDeleted', 'id']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        read_only_fields = ('is_active', 'is_staff', 'slug')
        exclude = ['IsActive', 'IsDeleted', 'id']
