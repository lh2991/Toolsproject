from django.core.management.base import BaseCommand, CommandError
import csv
from sightings.models import Squirrel_attr
import datetime
import os
import sys

def import_(path):
    with open(path) as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)
    for rows in data:
        try:
            squirrel = Squirrel_attr()
            squirrel.Longitude = float(rows['X'])
            squirrel.Lattitude = float(rows['Y'])
            squirrel.Squirrel_ID = rows['Unique Squirrel ID']
            squirrel.Shift = rows['Shift']
            squirrel.Date = datetime.datetime.strptime(rows['Date'],'%m%d%Y')
            if rows['Age'] != '?':
                squirrel.Age = rows['Age']
            else:
                pass
            squirrel.Primary_Fur_Color = rows['Primary Fur Color']
            squirrel.Location = rows['Location']
            squirrel.Specific_Location = rows['Specific Location']
            squirrel.Running = rows['Running']
            squirrel.Chasing = rows['Chasing']
            squirrel.Climbing = rows['Climbing']
            squirrel.Eating = rows['Eating']
            squirrel.Foraging = rows['Foraging']
            squirrel.Other_Activities =rows['Other Activities']
            squirrel.Kuks = rows['Kuks']
            squirrel.Quaas = rows['Quaas']
            squirrel.Moans = rows['Moans']
            squirrel.Tail_flags = rows['Tail flags']
            squirrel.Tail_twitches = rows['Tail twitches']
            squirrel.Approaches = rows['Approaches']
            squirrel.Indifferent = rows['Indifferent']
            squirrel.Runs_from = rows['Runs from']
            squirrel.save()
        except:
            pass

class Command(BaseCommand):
    help = 'Importing squirrel data into Django'
    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type = str)

    def handle(self, *args, **options):
        for path in options['path']:
            import_(path)
