from rest_framework import generics
from ..models import Category, Service
from .serializers import CategorySerializer, ServiceSerializer, SeekerSerializer, IdentitySerializer
from rest_framework import permissions
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from rest_framework.response import Response

from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler


payload_handler = jwt_payload_handler
encode_handler = jwt_encode_handler

Identity = get_user_model()

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


class SignUp(generics.CreateAPIView):
    """
    Base API view that accept signup details and return token if nothing goes wrong
    """
    serializer_class = IdentitySerializer
    queryset = Identity.objects.all()
    permission_classes = []

    def perform_create(self, serializer):
        queryset = Identity.objects.filter(
            username=serializer.validated_data['username'])
        if queryset.exists():
            raise ValidationError('You have already signed up')

        serializer.save(is_verified=False)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        user = Identity.objects.get(username=serializer.data['username'])

        payload = payload_handler(user)
        token = encode_handler(payload)

        return Response({'token': token}, headers)
