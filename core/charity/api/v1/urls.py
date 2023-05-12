from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('ads',views.AdsModelViewSet,basename='ads')
router.register('category',views.CategoryModelViewSet,basename='category')
app_name = 'api-v1'

urlpatterns = [
    #path('ads/',views.ads_list,name='ads-list'),
    #path('ads/',views.AdsList.as_view(),name='ads-list'),
    #path('ads/<int:id>/',views.ads_detail,name='ads-detail'),
    #path('ads/<int:pk>/',views.AdsDetail.as_view(),name='ads-detail'),
    #path('ads/',views.AdsViewSet.as_view({'get':'list','post':'create'}),name='ads-list'),
    #path('ads/<int:pk>/',views.AdsViewSet.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='ads-detail'),

]

urlpatterns += router.urls