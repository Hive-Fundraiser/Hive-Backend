from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
)
from rest_framework import mixins
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from django.db.models import Count
from rest_framework.response import Response
from django.db.models import Sum
from accounts.api.v1.serializers import ProfileSerializer
from .permissions import IsOwnerOrReadOnly
from .paginations import DefaultPagination
from .serializers import AdsSerializer, CategorySerializer, DonationSerializer,DonatorSerializer
from charity.models import Advertisement, Category, Donation
from accounts.models import Profile


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
    
    @action(detail=False, methods=['get'])
    def total_collected_amount(self, request):
        total_collected_amount = self.queryset.aggregate(Sum('collected_amount'))['collected_amount__sum'] or 0
        return Response({"total_collected_amount": total_collected_amount}, status=200)

    @action(detail=False, methods=['get'])
    def all_donators(self, request):
        donors = Donation.objects.values('donor').annotate(donation_count=Count('donor')).distinct()
        serializer = DonatorSerializer(donors, many=True)  # Assuming you have a serializer for donor objects
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def advertisement_count(self, request):
        count = Advertisement.objects.count()
        return Response({'count': count})
class DonationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    
    @action(detail=False, methods=['get'])
    def get_last_donation_amount(self, request):
        profile = request.user.profile_set.first() # Assuming there's a one-to-one relationship between User and Profile models
        
        last_donation = Donation.objects.filter(donor=profile).order_by('-donated_at').first()
        if last_donation:
            return Response(last_donation.amount)
        return Response(0)  # If no donations found


    def create(self, request, *args, **kwargs):
        # Check if the user has completed their profile before creating the advertisement
        profile = request.user.profile_set.first()  # Assuming 'profile' is the related name of the foreign key field
        if not profile or not profile.is_complete():
            return Response({"error": "Please complete your profile before donating"}, status=400)
        last_donation_amount = self.get_last_donation_amount(request)  # Pass the entire request object here
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

class UserAdvertisementViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = AdsSerializer

    def get_queryset(self):
        user = self.request.user
        profile = Profile.objects.filter(user=user).first()
        if profile:
            return Advertisement.objects.filter(raiser=profile)
        else:
            return Advertisement.objects.none()
