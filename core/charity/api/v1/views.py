from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from .serializers import AdsSerializer,CategorySerializer
from charity.models import Advertisement,Category,Donation
from rest_framework import mixins
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .permissions import IsOwnerOrReadOnly
from .paginations import DefaultPagination
from .serializers import DonationSerializer

class AdsModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    serializer_class = AdsSerializer
    queryset = Advertisement.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['category', 'raiser']
    search_fields = ['title', 'content']
    ordering_fields = ['published_date']
    pagination_class = DefaultPagination

class DonationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


