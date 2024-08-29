from rest_framework import serializers
from api.models import Element, Landmark

class ElementSerializer(serializers.ModelSerializer):
    # Serializer will additionally return the element's corresponding landmarks.
    landmarks = serializers.StringRelatedField(many=True)
    # Clearer name for JSON response
    element_name = serializers.CharField(source='name')
    class Meta:
        model = Element
        fields = ['element_name', 'landmarks']

class LandmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landmark
        fields = ['id', 'name', 'bone']
