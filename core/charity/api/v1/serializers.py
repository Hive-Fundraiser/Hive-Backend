from rest_framework import serializers
from charity.models import Advertisement,Category
from accounts.models import Profile
class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = "__all__"
        read_only_fields = ['raiser']
        #fields = ['id','image','title','content','status','estimated_amount','collected_amount','published_date','category']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = CategorySerializer(instance.category).data
        return rep
    
    def create(self, validated_data):
        validated_data['raiser'] = Profile.objects.get(user__id = self.context.get('request').user.id)
        return super().create(validated_data)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

