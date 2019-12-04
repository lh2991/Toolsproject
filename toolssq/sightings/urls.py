from django.urls import path, include

from . import views

urlpatterns = [
        path('',views.all_squirrel),
        path('<squirrel_id>/',views.squirrel_details),
]
