from rest_framework import generics
from ..models import Category, Service
from .serializers import CategorySerializer, ServiceSerializer, SeekerSerializer
from rest_framework import permissions
# from rest_framework_jwt.settings import api_settings
# from django.contrib.auth import get_user_model
# from django.core.exceptions import ValidationError
from rest_framework.response import Response

# from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler


# payload_handler = jwt_payload_handler
# encode_handler = jwt_encode_handler

# Identity = get_user_model()

# class NewCategory(generics.CreateAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()


class parentCategory(generics.ListCreateAPIView):
    """
    Base API endpoint that shows all parent category and also accept post for authenticated user
    """
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()


class ServicesApi(generics.ListCreateAPIView):
    """
    Base API endpoint that display all services and new service can also be posted to it by authenticated user
    """
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Service.objects.all()


class getParentCategoryServices(generics.ListCreateAPIView):
    """
    Base API endpoint that lists all services in a specified category and also accept new category
    """
    serializer_class = ServiceSerializer
    permission_classes = []

    def get_queryset(self, *args, **kwargs):
        query = self.kwargs.get("category_slug")
        if query is not None:
            qs = Service.objects.filter(category__slug=query)
            return qs
