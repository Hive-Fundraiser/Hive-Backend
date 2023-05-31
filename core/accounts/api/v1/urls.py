from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter

app_name = 'api-v1'

urlpatterns = [
    path('registration/',views.RegistrationApiView.as_view(),name='registration')
]

