from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
)
from rest_framework import mixins
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from django.db.models import Count
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from .paginations import DefaultPagination
from .serializers import AdsSerializer, CategorySerializer, DonationSerializer
from charity.models import Advertisement, Category, Donation


class AdsModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = AdsSerializer
    queryset = Advertisement.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["category", "raiser"]
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]
    pagination_class = DefaultPagination
    
    def create(self, request, *args, **kwargs):
        # Check if the user has completed their profile before creating the advertisement
        profile = request.user.profile_set.first()  # Assuming 'profile' is the related name of the foreign key field
        if not profile or not profile.is_complete():
            return Response({"error": "Please complete your profile before posting an advertisement."}, status=400)
        
        return super().create(request, *args, **kwargs)
    
    @action(detail=True, methods=['get'])
    def donators(self, request, pk=None):
        advertisement = self.get_object()
        donators = Donation.objects.filter(advertisement=advertisement)
        serializer = DonationSerializer(donators, many=True)
        return Response(serializer.data)


class DonationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    def create(self, request, *args, **kwargs):
        # Check if the user has completed their profile before creating the advertisement
        profile = request.user.profile_set.first()  # Assuming 'profile' is the related name of the foreign key field
        if not profile or not profile.is_complete():
            return Response({"error": "Please complete your profile before donating"}, status=400)
        
        return super().create(request, *args, **kwargs)

class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ["donated_at"]
    pagination_class = DefaultPagination

class PopularAdvertisementsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Advertisement.objects.annotate(donation_count=Count('donation')).order_by('-donation_count')[:7]
    serializer_class = AdsSerializer