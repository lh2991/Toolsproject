from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from .forms import SquirrelForm
from .models import Squirrel_attr

def all_squirrel(request):
    squirrels= Squirrel_attr.objects.all()
    context = {
            'squirrels': squirrels,
    }
    return render(request, 'sightings/all.html', context)

# def squirrel_details(request,squirrel_id):
#     squirrels=get_object_or_404(Squirrel_attr,pk = squirrel_id)
#     form = SquirrelForm(instance = squirrels)
#     context = {
#             'squirrels':squirrels,
#             'form':form
#     }
#     return render(request,'sightings/detail.html',context)

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
#
# def add_squirrel(request):
#     if request.method == 'POST':
#         form = SquirrelForm(request.POST,instance = squirrels)
#         if form.is_valid():
#             form.save()
#             return redirect(f'/sightings/{squirrel_id}')
#     else:
#         form = SquirrelForm()
#     context = {
#             'squirrels':squirrels,
#             'form':form
#     }
#     return render(request,'sightings/detail.html',context)

# request.POST or None,
