from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from .views import SignUp

app_name = 'authApi'
urlpatterns = [
    path('login/', obtain_jwt_token, name='api-login'),
    path('refresh-token/', refresh_jwt_token, name='refresh-token'),
    path('verify-token/', verify_jwt_token, name='verify-token'),
    path('signup/', SignUp.as_view(), name='signup'),

]
