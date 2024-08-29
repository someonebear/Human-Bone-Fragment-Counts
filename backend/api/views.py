from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api.models import Landmark, Element
from api.serializers import LandmarkSerializer, ElementSerializer

# Create your views here.

@csrf_exempt
def element_list(request):
    if request.method == 'GET':
        elements = Element.objects.all()
        # Model object -> serializer
        serializer = ElementSerializer(elements, many=True)
        # Serializer -> JSON
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        # JSON data -> serializer
        serializer = ElementSerializer(data=data)
        if serializer.is_valid():
            # serializer -> model object
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def element_detail(request, name):
    try:
        element = Element.objects.get(name=name)
    except Element.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        # Model object -> serializer
        serializer = ElementSerializer(element)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        # Updates element with data, returns serializer 
        serializer = ElementSerializer(element, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        element.delete()
        return HttpResponse(status=204)