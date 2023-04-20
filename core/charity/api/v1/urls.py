from django.urls import path,include
from . import views


app_name = 'api-v1'

urlpatterns = [
    path('ads/',views.ads_list,name='ads-list'),

]