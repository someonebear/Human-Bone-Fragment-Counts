from rest_framework import serializers
from api.models import *


class ElementSerializer(serializers.ModelSerializer):
    # Serializer will additionally return the element's corresponding landmarks.
    landmarks = serializers.StringRelatedField(many=True)
    # Clearer name for JSON response
    element_name = serializers.CharField(source='name')

    class Meta:
        model = Element
        fields = ['element_name', 'secondary', 'landmarks']


class LandmarkSerializer(serializers.ModelSerializer):
    bone_name = serializers.CharField(source='bone.name')
    landmark_name = serializers.CharField(source='name')

    class Meta:
        model = Landmark
        fields = ['landmark_id', 'landmark_name', 'bone_name']


class EntryMetaSerializer(serializers.ModelSerializer):

    class Meta:
        model = EntryMeta
        fields = ['pk', 'age', 'sex', 'site', 'spit']


class IndividualSerializer(serializers.ModelSerializer):

    class Meta:
        model = Individual
        fields = ['ind_code', 'meta']


class IndividualDetailSerializer(serializers.ModelSerializer):
    meta = EntryMetaSerializer(read_only=True)
    body_parts = serializers.StringRelatedField(many=True)

    class Meta:
        model = Individual
        fields = ['ind_code', 'meta', 'body_parts']


class BodyPartSerializer(serializers.ModelSerializer):

    class Meta:
        model = BodyPart
        fields = ['bp_code', 'ind', 'meta']


class BodyPartDetailSerializer(serializers.ModelSerializer):
    meta = EntryMetaSerializer(read_only=True)
    fragments = serializers.StringRelatedField(many=True)

    class Meta:
        model = BodyPart
        fields = ['bp_code', 'ind', 'meta', 'fragments']


class EntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Entry
        fields = ['acc_num', 'bone', 'side', 'size',
                  'generic', 'complete', 'notes', 'landmarks', 'meta', 'body_part']


class EntryDetailSerializer(serializers.ModelSerializer):
    bone_name = serializers.CharField(read_only=True, source='bone.name')
    landmarks = serializers.StringRelatedField(many=True)
    meta = EntryMetaSerializer(read_only=True)

    class Meta:
        model = Entry
        fields = ['acc_num', 'side', 'size', 'bone_name',
                  'generic', 'complete', 'notes', 'landmarks', 'meta', 'body_part']
