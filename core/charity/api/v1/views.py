from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import AdsSerializer,CategorySerializer
from charity.models import Advertisement,Category
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from rest_framework import viewsets

"""@api_view(["GET","POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def ads_list(request):
    if request.method == "GET":     
        advertisments = Advertisement.objects.filter(status=True)
        serializer = AdsSerializer(advertisments,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = AdsSerializer(data=request.data)   
        serializer.is_valid(raise_exception=True)
        serializer.save()   
        return Response(serializer.data)"""

"""class AdsList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AdsSerializer

    def get(self,request):
        advertisements = Advertisement.objects.filter(status=True)
        serializer = self.serializer_class(advertisements,many=True)
        return Response(serializer.data)
     
    def post(self,request):
        serializer = AdsSerializer(data=request.data)   
        serializer.is_valid(raise_exception=True)
        serializer.save()   
        return Response(serializer.data)"""
         
"""class AdsList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AdsSerializer
    queryset = Advertisement.objects.filter(status=True)"""

"""@api_view(["GET","PUT","DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def ads_detail(request,id):
        ads = get_object_or_404(Advertisement,pk=id,status=True)
        if request.method == "GET":           
            serializer = AdsSerializer(ads)
            return Response(serializer.data)
        elif request.method == "PUT":   
            serializer = AdsSerializer(ads,data=request.data)
            serializer.is_valid(raise_exception=True)   
            serializer.save()   
            return Response(serializer.data)
        elif request.method == "DELETE":  
             ads.delete()
             return Response("Item deleted successfully",status=status.HTTP_204_NO_CONTENT)"""
             
"""class AdsDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AdsSerializer
     
    def get(self,request,id):
        ads = get_object_or_404(Advertisement,pk=id,status=True)
        serializer = self.serializer_class(ads)
        return Response(serializer.data)

    def put(self,request,id):    
        ads = get_object_or_404(Advertisement,pk=id,status=True)
        serializer =self.serializer_class(ads,data=request.data)
        serializer.is_valid(raise_exception=True)   
        serializer.save()   
        return Response(serializer.data)

    def delete(self,request,id):
        ads = get_object_or_404(Advertisement,pk=id,status=True)
        ads.delete()
        return Response("Item deleted successfully",status=status.HTTP_204_NO_CONTENT)"""
    
"""class AdsDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AdsSerializer
    queryset = Advertisement.objects.filter(status=True)"""

class AdsModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AdsSerializer
    queryset = Advertisement.objects.filter(status=True)

class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


