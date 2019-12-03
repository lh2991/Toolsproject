from django.core.management.base import BaseCommand, CommandError
import csv
from sightings.models import Squirrel_attr
import datetime
import os
import sys

def import_(path):
    with open(path) as csv_file:
        readCSV = csv.reader(csv_file, delimiter=',')
        type(readCSV)
        data = []
        for thing in readCSV:
            data.append(thing)
    data = data[1:]
    for rows in data:
        try:
            squirrel = Squirrel_attr()
            squirrel.Longitude = rows[0]
            squirrel.Lattitude = rows[1]
            squirrel.Squirrel_ID = rows[2]
            squirrel.Shift = rows[4]
            squirrel.Date = datetime.datetime.strptime(rows[5],'%m%d%Y')
            if rows[7] != '?':
                squirrel.Age = rows[7]
            else:
                pass
            squirrel.Primary_Fur_Color = rows[8]
            squirrel.Location = rows[12]
            squirrel.Specific_Location = rows[14]
            squirrel.Running = rows[15]
            squirrel.Chasing = rows[16]
            squirrel.Climbing = rows[17]
            squirrel.Eating = rows[18]
            squirrel.Foraging = rows[19]
            squirrel.Other_Activities =rows[20]
            squirrel.Kuks = rows[21]
            squirrel.Quaas = rows[22]
            squirrel.Moans = rows[23]
            squirrel.Tail_flags = rows[24]
            squirrel.Tail_twitches = rows[25]
            squirrel.Approaches = rows[26]
            squirrel.Indifferent = rows[27]
            squirrel.Runs_from = rows[28]
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
