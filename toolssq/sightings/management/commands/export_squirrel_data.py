from django.core.management.base import BaseCommand, CommandError
import csv
from sightings.models import Squirrel_attr
import datetime
from django.http import HttpResponse

class Command(BaseCommand):
    help = 'Export 2018 squirrel data to csv '

    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='+', type=str)

    def handele(self,*args, **options):
        path = str(options['csv_file'][0])
        writer = csv.writer (open(path,'w'))
        headers = []
        for field in Squirrel_attr._meta.fields:
            headers.append(field.name)
        writer.writerow(headers)

        data = Squirrel_attr.objects.all()
        for squirrel in data:
            writer.writerow([squirrel.longitude,
                            squirrel.Latitude,
                            squirrel.Squirrel_ID,
                            squirrel.Shift,
                            squirrel.Date,
                            squirrel.Age,
                            squirrel.Primary_Fur_Color,
                            squirrel.Location,
                            squirrel.Specific_Location,
                            squirrel.Running,
                            squirrel.Chasing,
                            squirrel.Climbing,
                            squirrel.Eating,
                            squirrel.Foraging,
                            squirrel.Other_Activities,
                            squirrel.Kuks,
                            squirrel.Quaas,
                            squirrel.Moans,
                            squirrel.Tail_flags,
                            squirrel.Tail_twitches,
                            squirrel.Approaches,
                            squirrel.Indifferent,
                            squirrel.Runs_from,
                            ])
        # headers = ['longitude',
        #         'Latitude',
        #         'Unique Squirrel ID',
        #         'Shift',
        #         'Date',
        #         'Age',
        #         'Primary Fur Color',
        #         'Location',
        #         'Specific Location',
        #         'Running',
        #         'Chasing',
        #         'Climbing',
        #         'Eating',
        #         'Foraging',
        #         'Other Activities',
        #         'Kuks',
        #         'Quaas',
        #         'Moans',
        #         'Tail flags',
        #         'Tail twitches',
        #         'Approaches',
        #         'Indifferent',
        #         'Runs from',
        #     ]
