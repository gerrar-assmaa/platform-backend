from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework_simplejwt import views as jwt_views
from . import views
from .views import RegisterApi

urlpatterns = [
    path('In/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('In/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('Up', RegisterApi.as_view()),
]