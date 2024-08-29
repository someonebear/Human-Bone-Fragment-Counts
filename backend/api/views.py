from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from api.models import Landmark, Element
from api.serializers import LandmarkSerializer, ElementSerializer

# Create your views here.

class ElementList(APIView):
    def get(self, request, format=None):
        elements = Element.objects.all()
        # Model object -> serializer
        serializer = ElementSerializer(elements, many=True)
        # Serializer -> JSON
        return Response(serializer.data)
    
    def post(self, request, format=None):
        # JSON data -> serializer
        # DRF request.data automatically parses incoming data.
        serializer = ElementSerializer(data=request.data)
        if serializer.is_valid():
            # serializer -> model object
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ElementDetail(APIView):
    def get_object(self, name):
        try:
            return Element.objects.get(name=name)
        except Element.DoesNotExist:
            raise Http404

    def get(self, request, name, format=None):
        element = self.get_object(name)
        serializer = ElementSerializer(element)
        return Response(serializer.data)

    def put(self, request, name, format=None):
        element = self.get_object(name)
        serializer = ElementSerializer(element, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name, format=None):
        element = self.get_object(name)
        element.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)