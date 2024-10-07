from rest_framework import generics, status
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import *
from django.shortcuts import get_object_or_404
import pdb
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

    def create(self, request, *args, **kwargs):
        relative_landmarks = request.data['landmarks']
        landmarks_in_element = Landmark.objects.filter(
            bone__name=request.data['bone'])
        absolute_landmarks = []
        for landmark in relative_landmarks:
            landmark_obj = landmarks_in_element[landmark-1]
            absolute_landmarks.append(landmark_obj.pk)
        request.data['landmarks'] = absolute_landmarks
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

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
    def get(self, request, site_pk, format=None):
        site = get_object_or_404(Site, pk=site_pk)
        sex_split = bool(request.path.find("sex") != -1)
        calc = get_mne_by_spit(site, sex_split)
        return Response(calc)
