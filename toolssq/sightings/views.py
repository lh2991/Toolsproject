from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from django.db.models import Avg, Max, Min, Q

from .forms import SquirrelForm
from .models import Squirrel_attr

def all_squirrel(request):
    squirrels= Squirrel_attr.objects.all()
    context = {
            'squirrels': squirrels,
    }
    return render(request, 'sightings/all.html', context)

def squirrel_details(request,squirrel_id):
    squirrels=get_object_or_404(Squirrel_attr,pk = squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST,instance = squirrels)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{squirrel_id}')
    else:
        form = SquirrelForm(instance = squirrels)
    context = {
            'squirrels':squirrels,
            'form':form
    }
    return render(request,'sightings/detail.html',context)

def add_squirrel(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SquirrelForm()
    context = {
            'form':form
    }
    return render(request,'sightings/add.html',context)

def stats(request):
    squirrels= Squirrel_attr.objects.all()
    count = len(squirrels)

    am= len(Squirrel_attr.objects.exclude(Shift='PM'))
    pm= len(Squirrel_attr.objects.exclude(Shift='AM'))

    ADULT= len(Squirrel_attr.objects.exclude(Age='').exclude(Age='Juvenile'))
    JUVENILE = len(Squirrel_attr.objects.exclude(Age='').exclude(Age='Adult'))

    color_black= len(Squirrel_attr.objects.exclude(Primary_Fur_Color='').exclude(Primary_Fur_Color='Gray').exclude(Primary_Fur_Color='Cinnamon'))
    color_gray= len(Squirrel_attr.objects.exclude(Primary_Fur_Color='').exclude(Primary_Fur_Color='Black').exclude(Primary_Fur_Color='Cinnamon'))
    color_cinnamon= len(Squirrel_attr.objects.exclude(Primary_Fur_Color='').exclude(Primary_Fur_Color='Gray').exclude(Primary_Fur_Color='Black'))

    lattitude = list(Squirrel_attr.objects.all().aggregate(Avg('Lattitude')).values())[0]
    longitude = list(Squirrel_attr.objects.all().aggregate(Avg('Longitude')).values())[0]

    # eat_t = len(Squirrel_attr.objects.exclude(Eating='False'))
    # eat_f = len(Squirrel_attr.objects.exclude(Eating='True'))
    context = {
            'count': count,
            'am': am,
            'pm': pm,
            'ADULT': ADULT,
            'JUVENILE': JUVENILE,
            'color_black': color_black,
            'color_gray': color_gray,
            'color_cinnamon': color_cinnamon,
            'lattitude': lattitude,
            'longitude': longitude,
            # 'eat_t': eat_t,
            # 'eat_f': eat_f,
    }
    return render(request, 'sightings/stats.html', context)

def map(request):
    sightings= Squirrel_attr.objects.all()[:250]
    context = {'sightings':sightings}
    return render(request, 'sightings/map.html', context)
