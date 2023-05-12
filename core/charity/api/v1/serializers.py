from rest_framework import serializers
from charity.models import Advertisement,Category

class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = "__all__"
        #fields = ['id','image','title','content','status','estimated_amount','collected_amount','published_date','category']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

