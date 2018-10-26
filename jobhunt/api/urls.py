from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view('Friend Finder Api')

urlpatterns = [
    path('login/', obtain_jwt_token, name='api-login'),
    path('api-docs/', schema_view)
]
