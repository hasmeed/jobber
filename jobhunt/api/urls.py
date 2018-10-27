from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import parentCategory, Service

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view('JobErrand Api developed by hasmeed')

urlpatterns = [
    path('login/', obtain_jwt_token, name='api-login'),
    path('api-docs/', schema_view),
    # path('addcategory/', NewCategory.as_view()),
    path('parentCategory/', parentCategory.as_view()),
    path('services/', Service.as_view())
]
