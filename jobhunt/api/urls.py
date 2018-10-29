from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from .views import parentCategory, ServicesApi, getParentCategoryServices, SignUp

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view('JobErrand Api developed by hasmeed')

app_name = 'api'
urlpatterns = [
    path('login/', obtain_jwt_token, name='api-login'),
    path('refresh-token/', refresh_jwt_token, name='refresh-token'),
    path('verify-token/', verify_jwt_token, name='verify-token'),


    path('signup/', SignUp.as_view(), name='signup'),
    path('api-docs/', schema_view),
    path('parentCategory/', parentCategory.as_view(), name='categories'),
    path('<category_slug>/services/',
         getParentCategoryServices.as_view(), name='categoryServices'),
    path('services/', ServicesApi.as_view(), name='services'),
]
