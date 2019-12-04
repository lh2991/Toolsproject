from django.urls import path, include

from . import views

urlpatterns = [
        path('',views.all_squirrel),
        # path('<int: Squirrel_ID>/',views.squirrel_details),
]
