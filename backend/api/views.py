from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Landmark, Element
from api.serializers import LandmarkSerializer, ElementSerializer

# Create your views here.

@api_view(['GET','POST'])
def element_list(request, format=None):
    if request.method == 'GET':
        elements = Element.objects.all()
        # Model object -> serializer
        serializer = ElementSerializer(elements, many=True)
        # Serializer -> JSON
        return Response(serializer.data)

    elif request.method == 'POST':
        # JSON data -> serializer
        serializer = ElementSerializer(data=request.data)
        if serializer.is_valid():
            # serializer -> model object
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def element_detail(request, name, format=None):
    try:
        element = Element.objects.get(name=name)
    except Element.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Model object -> serializer
        serializer = ElementSerializer(element)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        # DRF request.data automatically parses incoming data.
        # Updates element with data, returns serializer 
        serializer = ElementSerializer(element, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        element.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)