from rest_framework import serializers
from .models import userData
import uuid

class userDataSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=50)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=20)
    user_id=serializers.CharField(max_length=100) 

    def create(self, validated_data):
        return userData.objects.create(**validated_data)
    
    