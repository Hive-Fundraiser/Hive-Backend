from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("ads", views.AdsModelViewSet, basename="ads")
router.register(
    "advertisement", views.AdvertisementModelViewSet, basename="advertisement"
)
router.register("donations", views.DonationViewSet, basename="donation")
router.register("category", views.CategoryModelViewSet, basename="category")
app_name = "api-v1"

urlpatterns = []

urlpatterns += router.urls
