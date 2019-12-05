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
        for data in data:
            writer.writerow([data.longitude,
                            data.Latitude,
                            data.Squirrel_ID,
                            data.Shift,
                            data.Date,
                            data.Age,
                            data.Primary_Fur_Color,
                            data.Location,
                            data.Specific_Location,
                            data.Running,
                            data.Chasing,
                            data.Climbing,
                            data.Eating,
                            data.Foraging,
                            data.Other_Activities,
                            data.Kuks,
                            data.Quaas,
                            data.Moans,
                            data.Tail_flags,
                            data.Tail_twitches,
                            data.Approaches,
                            data.Indifferent,
                            data.Runs_from,
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
