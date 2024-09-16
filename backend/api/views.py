from rest_framework import generics
from api.models import *
from api.serializers import *
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
    lookup_field = 'id__iexact'


class EntryList(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryGroupList(generics.ListCreateAPIView):
    queryset = EntryGroup.objects.all()
    serializer_class = EntryGroupSerializer


class EntryGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EntryGroup.objects.all()
    serializer_class = EntryGroupSerializer

# @require_http_methods(["GET"])
# class MNICalculation(APIView):
#     def get(self, request, format=None):
#         dict1 = {}
#         dict1["number1"] = 1
#         dict1["number2"] = 2
#         dict1["answer"] = dict1["number1"] + dict1["number2"]

#         return Response(dict1)
