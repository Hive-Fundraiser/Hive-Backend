from django.urls import path,include
from charity import views

app_name = 'charity'

urlpatterns = [
    path('api/v1/' , include('charity.api.v1.urls'))
]