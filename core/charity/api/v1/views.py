from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from .serializers import AdsSerializer,CategorySerializer
from charity.models import Advertisement,Category
from rest_framework import mixins
from rest_framework import viewsets

class AdsModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AdsSerializer
    queryset = Advertisement.objects.filter(status=True)

class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


