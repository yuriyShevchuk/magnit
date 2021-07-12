from .models import Place, Poi, Poi_category, Poi_instance
from rest_framework import serializers

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class PoiLocationSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField(many=False)
    class Meta:
        model = Poi
        id_field = False
        fields = ['location', 'name']


class Poi_instanceSerializer(serializers.ModelSerializer):
    place = serializers.StringRelatedField(many=False)
    poi = PoiLocationSerializer(many=False)
    class Meta:
        model = Poi_instance
        fields = ['id', 'place', 'distance', 'poi']

class AllPlacePoiSerializer(serializers.ModelSerializer):
    poi_instance_set = Poi_instanceSerializer(many=True)
    class Meta:
        model = Place
        fields = ['name', 'location', 'poi_instance_set']
