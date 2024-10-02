from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import *
# Create your views here.


class ElementList(generics.ListCreateAPIView):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer


class ElementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer
    lookup_field = 'name__iexact'


class LandmarkList(generics.ListCreateAPIView):
    queryset = Landmark.objects.all()
    serializer_class = LandmarkSerializer


class LandmarkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Landmark.objects.all()
    serializer_class = LandmarkSerializer
    lookup_field = 'landmark_id__iexact'


class EntryList(generics.ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EntryDetailSerializer
        return super().get_serializer_class()
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EntryDetailSerializer
        return super().get_serializer_class()
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryMetaList(generics.ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EntryMetaDetailSerializer
        return super().get_serializer_class()
    queryset = EntryMeta.objects.all()
    serializer_class = EntryMetaSerializer


class EntryMetaDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EntryMetaDetailSerializer
        return super().get_serializer_class()
    queryset = EntryMeta.objects.all()
    serializer_class = EntryMetaSerializer


class IndividualList(generics.ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return IndividualDetailSerializer
        return super().get_serializer_class()
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer


class IndividualDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return IndividualDetailSerializer
        return super().get_serializer_class()
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer
    lookup_field = 'ind_code__iexact'


class BodyPartList(generics.ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BodyPartDetailSerializer
        return super().get_serializer_class()
    queryset = BodyPart.objects.all()
    serializer_class = BodyPartSerializer


class BodyPartDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BodyPartDetailSerializer
        return super().get_serializer_class()
    queryset = BodyPart.objects.all()
    serializer_class = BodyPartSerializer
    lookup_field = 'bp_code__iexact'


class MNICalculation(APIView):
    def get(self, request, format=None):
        site = Site.objects.get(pk=1)
        spit = Spit.objects.get(site=site, number=2)
        element = Element.objects.get(name="Frontal")
        dict1 = get_mne(spit, element, "Infant")

        return Response(dict1)
