from rest_framework import serializers
from api.models import Element, Landmark

class ElementSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)

    def create(self, validated_data):
        return Element.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)

class LandmarkSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=20)
    name = serializers.CharField(max_length=100)
    bone = ElementSerializer()

    def create(self, validated_data):
        return Landmark.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)