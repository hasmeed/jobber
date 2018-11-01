from django.contrib import admin
from .models import Category, Service, Identity, Seeker, Address, Notification

admin.site.register(Identity)
admin.site.register(Seeker)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Address)
admin.site.register(Notification)

# Register your models here.
