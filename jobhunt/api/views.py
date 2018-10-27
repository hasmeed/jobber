from rest_framework import generics
from ..models import Category, Service
from .serializers import CategorySerializer, ServiceSerializer
from rest_framework import permissions


# class NewCategory(generics.CreateAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()


class parentCategory(generics.ListCreateAPIView):
    """
    Base API endpoint that shows all parent category and also accept post
    """
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()


class ServicesApi(generics.ListCreateAPIView):
    """
    Base API endpoint that display all services and new service can also be posted to it
    """
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Service.objects.all()


class getParentCategoryServices(generics.ListCreateAPIView):
    serializer_class = ServiceSerializer
    permission_classes = []

    def get_queryset(self, *args, **kwargs):
        query = self.kwargs.get("category_slug")
        if query is not None:
            qs = Service.objects.filter(category__slug=query)
            return qs