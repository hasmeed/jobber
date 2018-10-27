from django.contrib import admin
from .models import Seeker, Category, Service

# admin.site.register(Identity)
admin.site.register(Seeker)
admin.site.register(Category)
admin.site.register(Service)

# Register your models here.
