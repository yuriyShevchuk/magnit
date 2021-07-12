from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('places/', views.placeList, name='place-list'),
    path('places/<str:name>/', views.placeDetail, name='place-detail'),
    path('places/<str:name>/pois/', views.placePoisList, name='one-place-pois'),
    path('allplaces/pois/', views.allPlacesPoisList, name='all-places-pois'),
]
