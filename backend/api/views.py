from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.http import require_http_methods
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
    queryset = EntryMeta.objects.all()
    serializer_class = EntryMetaSerializer


class EntryMetaDetail(generics.RetrieveUpdateDestroyAPIView):
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

# @require_http_methods(["GET"])
# class MNICalculation(APIView):
#     def get(self, request, format=None):
#         dict1 = {}
#         dict1["number1"] = 1
#         dict1["number2"] = 2
#         dict1["answer"] = dict1["number1"] + dict1["number2"]

#         return Response(dict1)
