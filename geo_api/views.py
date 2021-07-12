from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PlaceSerializer, Poi_instanceSerializer, AllPlacePoiSerializer
from .models import Place, Poi_instance

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_endpoints = {
        'api endpoints': '/api/',
        'view starting places': '/api/places/',
        'view particular starting place': '/api/places/<str:name>/',
        'view pois of particular starting place:': '/api/places/<str:name>/pois/',
        'view parks around all places': '/api/places/pois/'
    }
    return Response(api_endpoints)

@api_view(['GET'])
def placeList(request):
    places = Place.objects.all()
    serializer = PlaceSerializer(places, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def placeDetail(request, name):
    place = Place.objects.get(name=name)
    serializer = PlaceSerializer(place, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def placePoisList(request, name):
    poi_instances = Poi_instance.objects.filter(place__name=name)
    serializer = Poi_instanceSerializer(poi_instances, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def allPlacesPoisList(request):
    places = Place.objects.all()
    serializer = AllPlacePoiSerializer(places, many=True)
    return Response(serializer.data)
