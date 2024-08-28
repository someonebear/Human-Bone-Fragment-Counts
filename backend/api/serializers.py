from rest_framework import serializers
from api.models import Element, Landmark

class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = ['name']

class LandmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landmark
        fields = ['id', 'name', 'bone']
