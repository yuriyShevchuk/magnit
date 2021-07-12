from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


class Place(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField(geography=True, default=Point(0.0, 0.0))

    def __str__(self):
        return self.name

    @property
    def longitude(self):
        return self.location.x

    @property
    def latitude(self):
        return self.location.y


class Poi_category(models.Model):
    name = models.CharField(max_length=50)
    cat_id = models.PositiveSmallIntegerField(blank=True)

    def __str__(self):
        return self.name


class Poi(models.Model):
    location = models.PointField(geography=True, default=Point(0.0, 0.0))
    name = models.ForeignKey('Poi_category', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name.name

    @property
    def longitude(self):
        return self.location.x

    @property
    def latitude(self):
        return self.location.y


class Poi_instance(models.Model):
    distance = models.DecimalField(max_digits=6, decimal_places=2)
    place = models.ForeignKey('Place', on_delete=models.CASCADE)
    poi = models.ForeignKey('Poi', on_delete=models.CASCADE)
