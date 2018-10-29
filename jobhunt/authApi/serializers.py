from rest_framework import serializers
from django.contrib.auth import get_user_model
Identity = get_user_model()


class IdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Identity
        exclude = ['id', 'last_login', 'is_superuser',
                   'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions', 'is_verified']
