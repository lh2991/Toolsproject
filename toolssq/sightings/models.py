from django.db import models

class Squirrel_attr(models.Model):

    Lattitude = models.FloatField(
    help_text=('Latitude of Squirrel'),
    max_length = 40,
    )

    Longitude = models.FloatField(
    help_text=('Longitude of Squirrel'),
    max_length = 40,
    )

    Squirrel_ID = models.CharField(
    max_length = 20,
    unique = True,
    primary_key=True,
    )

    AM = 'AM'
    PM = 'PM'
    Shift_CHOICES = (
            (AM,'AM'),
            (PM, 'PM'),
    )
    Shift = models.CharField(
                max_length = 4,
                choices= Shift_CHOICES,
                default = AM,
    )

    Date = models.DateField(
                help_text=('Date spotted'),
    )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    BLANK = ''
    Age_CHOICES =(
            (ADULT,'Adult'),
            (JUVENILE,'Juvenile'),
            (BLANK,''),
    )
    Age = models.CharField(
                max_length = 16,
                choices= Age_CHOICES,
                blank = True,
                null=True,
    )

    BLACK ='Black'
    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLANK = ''
    Primary_Fur_Color_CHOICES =(
        (BLACK,'Black'),
        (GRAY,'Gray'),
        (CINNAMON,'Cinnamon'),
        (BLANK,''),
    )
    Primary_Fur_Color = models.CharField(
                max_length = 16,
                choices= Primary_Fur_Color_CHOICES,
                blank= True,
                null = True,
    )

    ABOVE = 'Above Ground'
    PLANE = 'Ground Plane'
    BLANK = ''
    Location_CHOICES =(
        (ABOVE,'Above Ground'),
        (PLANE,'Ground Plane'),
        (BLANK,''),
    )
    Location = models.CharField(
                max_length = 40,
                choices= Location_CHOICES,
                blank = True,
                null = True,
    )

    Specific_Location = models.CharField(
                max_length = 100,
                blank = True,
                null = True,
    )

    Running = models.BinaryField(null = True)

    Chasing = models.BinaryField(null = True)

    Climbing = models.BinaryField(null = True)

    Eating = models.BinaryField(null = True)

    Foraging = models.BinaryField(null = True)

    Other_Activities = models.TextField(blank = True)

    Kuks = models.BinaryField(null = True)

    Quaas = models.BinaryField(null = True)

    Moans = models.BinaryField(
                    default = False,
                    null = True,
    )

    Tail_flags = models.BinaryField(null = True)

    Tail_twitches = models.BinaryField(null = True)

    Approaches = models.BinaryField(null = True)

    Indifferent = models.BinaryField(null = True)

    Runs_from = models.BinaryField(null = True)
