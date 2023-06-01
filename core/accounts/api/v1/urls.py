from django.urls import path,include
from .import views
from rest_framework.authtoken.views import ObtainAuthToken

app_name = 'api-v1'

urlpatterns = [
    path('registration/',views.RegistrationApiView.as_view(),name='registration'),
    path('token/login/',views.CustomObtainAuthToken.as_view(),name='token-login'),
    path('token/logout/',views.CustomDiscardToken.as_view(),name='token-logout'),
]

