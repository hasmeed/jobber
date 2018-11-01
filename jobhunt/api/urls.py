from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from .views import parentCategory, ServicesApi, getParentCategoryServices, NewSeeker, Seeker, AllSeeker


app_name = 'api'
urlpatterns = [
    # path('login/', obtain_jwt_token, name='api-login'),
    # path('refresh-token/', refresh_jwt_token, name='refresh-token'),
    # path('verify-token/', verify_jwt_token, name='verify-token'),


    # path('signup/', SignUp.as_view(), name='signup'),

    path('parentCategory/', parentCategory.as_view(), name='categories'),
    path('<category_slug>/services/',
         getParentCategoryServices.as_view(), name='categoryServices'),
    path('services/', ServicesApi.as_view(), name='services'),
    path('newworker/', NewSeeker.as_view(), name='seeker'),
    path('worker/<slug>', Seeker.as_view(), name='workerInfo'),
    path('workers/', AllSeeker.as_view(), name='allworker'),
]
