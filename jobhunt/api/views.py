from rest_framework import generics
from ..models import Category, Service
from .serializers import CategorySerializer, ServiceSerializer
from rest_framework import permissions


# class NewCategory(generics.CreateAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()


class parentCategory(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()


class Service(generics.ListCreateAPIView):
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Service.objects.all()
