from django.urls import path, include

from . import views

app_name = 'sightings'
urlpatterns = [
        path('sightings/',views.all_squirrel),
        path('sightings/<squirrel_id>/',views.squirrel_details),
        path('sightings/add',views.add_squirrel),
        path('sightings/stats',views.stats),
        path('map/',views.map),
]
