from django.shortcuts import render

from .models import Squirrel_attr

def all_squirrel(request):
    squirrels= Squirrel_attr.objects.all()
    context = {
            ' squirrels ': squirrels,
    }
    return render(request, 'sightings/all.html', context)

def squirrel_details(request, Squirrel_ID):
    squirrel = Squirrel_attr.objects.get(id= Squirrel_ID)
    return HttpResponse(f"Hi, I'm Squirrel { Squirrel_ID }")
