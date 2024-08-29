from rest_framework import generics
from api.models import Landmark, Element
from api.serializers import LandmarkSerializer, ElementSerializer

# Create your views here.

class ElementList(generics.ListCreateAPIView):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer

class ElementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer
