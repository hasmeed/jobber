from rest_framework.response import Response
from rest_framework import generics
from ..models import Category, Service
from .serializers import IdentitySerializer
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler


payload_handler = jwt_payload_handler
encode_handler = jwt_encode_handler

Identity = get_user_model()


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

        return Response({'token': token, 'Account Type': user.get_account_type()})
