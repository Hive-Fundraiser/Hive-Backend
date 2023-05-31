from rest_framework import serializers
from ...models import User

class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email','password']

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        return super().create(validated_data)    
