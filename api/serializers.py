from rest_framework import serializers
from api.models import *


class ElementSerializer(serializers.ModelSerializer):
    # Serializer will additionally return the element's corresponding landmarks.
    landmarks = serializers.StringRelatedField(many=True, read_only=True)
    # Clearer name for JSON response
    element_name = serializers.CharField(source='name')

    class Meta:
        model = Element
        fields = ['element_name', 'landmarks', 'pk']


class LandmarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Landmark
        fields = ['pk', 'landmark_id', 'name', 'bone']


class EntryMetaSerializer(serializers.ModelSerializer):

    class Meta:
        model = EntryMeta
        fields = ['pk', 'age', 'sex', 'site', 'spit', 'notes']


class IndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Individual
        fields = ['ind_code', 'meta']


class IndividualDetailSerializer(serializers.ModelSerializer):
    meta = EntryMetaSerializer(read_only=True)
    body_parts = serializers.StringRelatedField(many=True)
    fragments = serializers.StringRelatedField(many=True)

    class Meta:
        model = Individual
        fields = ['ind_code', 'meta', 'body_parts', 'fragments']


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
        fields = ['pk', 'acc_num', 'bone', 'side', 'size',
                  'generic', 'complete', 'landmarks', 'meta', 'body_part', 'ind']


class EntryDetailSerializer(serializers.ModelSerializer):
    landmarks = serializers.StringRelatedField(many=True)
    meta = EntryMetaSerializer(read_only=True)

    class Meta:
        model = Entry
        fields = ['pk', 'acc_num', 'side', 'size', 'bone',
                  'generic', 'complete', 'landmarks', 'meta', 'body_part', 'ind']


class EntryMetaDetailSerializer(serializers.ModelSerializer):
    site = serializers.StringRelatedField()
    individuals = serializers.StringRelatedField(many=True)
    body_parts = serializers.StringRelatedField(many=True)
    fragments = serializers.StringRelatedField(many=True)

    class Meta:
        model = EntryMeta
        fields = ['pk', 'age', 'sex', 'site',
                  'spit', 'individuals', 'body_parts', 'fragments', 'notes']


class SiteSerializer(serializers.ModelSerializer):
    spits = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Site
        fields = ['pk', 'name', 'city', 'country', 'description', 'spits']


class SpitSerializer(serializers.ModelSerializer):
    site_name = serializers.CharField(source='site.name', read_only=True)

    class Meta:
        model = Spit
        fields = ['pk', 'number', 'site', 'site_name']
