from rest_framework import serializers
from .models import remainderData
import uuid

class remainderDataSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    date = serializers.DateField()
    quota = serializers.CharField(max_length=1000)
    user_id=serializers.CharField(max_length=100)

    # photoName = serializers.ImageField(upload_to='myImage',max_length=100,blank=True)
    # added_by = serializers.ForeignKey(userData, on_delete=models.CASCADE)

    
    def create(self, validated_data):
        return remainderData.objects.create(**validated_data)
    
# 'name','date','quota','photoName'
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.date = validated_data.get('date',instance.date)
        instance.quota = validated_data.get('quota',instance.quota)
        instance.photoName = validated_data.get('photoName',instance.photoName)
        instance.save()
        return instance
    