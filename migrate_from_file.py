from django.db import migrations
import json
from django.contrib.gis.geos import fromstr
from pathlib import Path

DATA_FILENAME = 'pois.geojson'
POI_CATEGORIES = {'parks': '280'}
def get_point(long, lat):
    return fromstr(f'POINT({long} {lat})', srid=4326)

def load_data(apps, schema_editor):
    Place = apps.get_model('geo_api', 'Place')
    Poi = apps.get_model('geo_api', 'Poi')
    Poi_instance = apps.get_model('geo_api', 'Poi_instance')
    Poi_category = apps.get_model('geo_api', 'Poi_category')
    filepath = Path(__file__).parents[2] / DATA_FILENAME
    for name, id in POI_CATEGORIES.items():
        Poi_category(name=name, cat_id=int(id)).save()

    with open(str(filepath)) as fp:
        places = json.load(fp)
    for place_name, place_data in places.items():
        location = get_point(place_data['location']['long'],
                             place_data['location']['lat'])
        place = Place(name=place_name, location=location)
        place.save()
        for cat_name, cat_id in POI_CATEGORIES.items():
            cat_obj = Poi_category.objects.filter(name=cat_name)[0]
            for point in place_data['pois'][cat_name]['geojson']:
                location = get_point(point['geometry']['coordinates'][0],
                                     point['geometry']['coordinates'][1])
                poi = Poi.objects.filter(location__coveredby=location)
                if poi:
                    poi = poi[0]
                if not poi:
                    poi = Poi(location=location, name=cat_obj)
                    poi.save()
                dist = point['properties']['distance']
                Poi_instance(distance=dist, place=place, poi=poi).save()



class Migration(migrations.Migration):

    dependencies = [
        ('geo_api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
