from django.contrib import admin

from .models import Place, Poi_category, Poi_instance, Poi

admin.site.register(Place)
admin.site.register(Poi_instance)
admin.site.register(Poi_category)
admin.site.register(Poi)
