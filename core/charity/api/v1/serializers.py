from rest_framework import serializers
from charity.models import Advertisement, Category, Donation
from accounts.models import Profile


class AdsSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    collected_percentage = serializers.FloatField(read_only=True)
    relative_url = serializers.URLField(
        source="get_absolute_api_url", read_only=True
    )
    absolute_url = serializers.SerializerMethodField()
    raiser_full_name = serializers.SerializerMethodField()
    class Meta:
        model = Advertisement
        read_only_fields = ["raiser"]
        fields = [
            "id",
            "image",
            "title",
            "raiser_full_name",
            "snippet",
            "content",
            "category",
            "status",
            "relative_url",
            "absolute_url",
            "estimated_amount",
            "collected_amount",
            "collected_percentage",
            "published_date",
        ]
    def get_raiser_full_name(self, obj):
        return obj.raiser.get_full_name()

    def get_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)
        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("snippet", None)
            rep.pop("relative_url", None)
            rep.pop("absolute_url", None)
        else:
            rep.pop("content", None)
        rep["category"] = CategorySerializer(
            instance.category, context={"request": request}
        ).data
        return rep

    def create(self, validated_data):
        validated_data["raiser"] = Profile.objects.get(
            user__id=self.context.get("request").user.id
        )
        return super().create(validated_data)


class DonationSerializer(serializers.ModelSerializer):
    donor_full_name = serializers.SerializerMethodField()
    class Meta:
        read_only_fields = ["donor"]
        model = Donation
        fields = ["id", "donor_full_name", "advertisement", "amount"]

    def create(self, validated_data):
        validated_data["donor"] = Profile.objects.get(
            user__id=self.context.get("request").user.id
        )
        return super().create(validated_data)
    
    def get_donor_full_name(self, obj):
        return obj.donor.get_full_name()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class DonatorSerializer(serializers.Serializer):
    donor = serializers.CharField()
    donation_count = serializers.IntegerField()