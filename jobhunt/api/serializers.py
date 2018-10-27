from rest_framework import serializers
from ..models import Category, Service, Seeker


class CategoryService(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return Category.objects.all()


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
