from rest_framework import serializers
from ..models import Category, Service, Seeker, Address
from django.contrib.auth import get_user_model
from ..authApi.serializers import IdentitySerializer


Identity = get_user_model()


class CategoryService(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return Category.objects.all()


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ['IsActive', 'IsDeleted', 'id', 'slug']


class CategorySerializer(serializers.ModelSerializer):
    services_uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        read_only_fields = ('is_active', 'is_staff', 'slug')
        exclude = ['IsActive', 'IsDeleted', 'id']

    def get_services_uri(self, obj):
        request = self.context.get('request')
        return obj.get_services_uri(request=request)


class ServiceSerializer(serializers.ModelSerializer):
    category = CategoryService()
    # cat = serializers.SerializerMethodField()

    class Meta:
        model = Service
        read_only_fields = ('IsActive', 'IsDeleted', 'slug')
        # fields = '__all__'
        exclude = ['IsActive', 'IsDeleted', 'id']

    def __init__(self, user=None, *args, **kwargs):
        super(ServiceSerializer, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = None

    # def get_cat(self, obj):
    #     # request = self.context.get("request")
    #     return obj.get_cat()


class SeekerSerializer(serializers.ModelSerializer):
    identity = IdentitySerializer(required=False)
    address = AddressSerializer(required=False)

    class Meta:
        model = Seeker
        fields = ['identity', 'address', 'about', 'profileImage',
                  'takingJob', 'securityQuestion', 'securityAnswer', 'enableTwoStepVerification', 'facebook', 'google', 'phonenumber']
        # exclude = ['IsActive', 'IsDeleted', 'id', 'identity']
        read_only_fields = ('phoneIsVerified', 'identity',
                            'emailIsVerified', 'facebookIsVerified', 'online', 'slug')

    # def create(self, validated_data):
    #     if validated_data.pop('is_provider'):
    #         pass
    #     elif validated_data.pop('is_seeker'):
    #         Seeker.objects
