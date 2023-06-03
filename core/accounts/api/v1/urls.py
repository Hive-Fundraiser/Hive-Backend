from django.urls import path,include
from .import views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = 'api-v1'

urlpatterns = [
    #token
    path('registration/',views.RegistrationApiView.as_view(),name='registration'),
    path('token/login/',views.CustomObtainAuthToken.as_view(),name='token-login'),
    path('token/logout/',views.CustomDiscardToken.as_view(),name='token-logout'),

    #jwt
    path('jwt/create/',views.CustomTokenObtainPairView.as_view(),name='jwt-create'),
    path('jwt/refresh/',TokenRefreshView.as_view(),name='jwt-refresh'),
    path('jwt/verify/',TokenVerifyView.as_view(),name='jwt-verify')
]

