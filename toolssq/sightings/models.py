from django.db import models

class Squirrel_attr(models.Model):

    Lattitude = models.IntegerField(
    #max_value=,
    #min_value=,
    help_text=_('Latitude of Squirrel'),
    )

    Longitude = models.IntegerField(
    #max_value=,
    #min_value=,
    help_text=_('Longitude of Squirrel'),
    )

    Squirrel_ID = models.CharField(
    max_length = 13,
    ) #not completed yet!!!!

    AM = 'AM'
    PM = 'PM'
    Shift_CHOICES = (
            (AM,'AM'),
            (PM, 'PM'),
    )
    Shift = models.CharField(
                max_length = 4,
                choices= Shift_CHOICES,
                default = AM
    )

    Date = models.DateField(
                help_text=_('Date spotted'),
                )  #How to convert to existing dataform

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    BLANK = ' '
    UNKNOWN = '?'
    Age_CHOICES =(
            (ADULT,'Adult'),
            (JUVENILE,'Juvenile'),
            (BLANK,' '),
            (UNKNOWN,'?'), #how to deal with blank and ?
    )
    Age = models.CharField(
                max_length = 16,
                choices= Age_CHOICES,
                default = BLANK
    )

    BLACK ='Black'
    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLANK = ' '
    Primary_Fur_Color_CHOICES =(
        (BLACK,'Black'),
        (GRAY,'Gray'),
        (CINNAMON,'Cinnamon'),
        (BLANK,' '), #how to deal with blank and ?
    )
    Primary_Fur_Color = models.CharField(
                max_length = 16,
                choices= Primary_Fur_Color_CHOICES,
                default = BLANK
    )

    ABOVE = 'Above Ground'
    PLANE = 'Ground Plane'
    BLANK = ' '
    Location_CHOICES =(
        (ABOVE,'Above Ground'),
        (PLANE,'Ground Plane'),
        (BLANK,' '),#how to deal with blank and ?
    )
    Location = models.CharField(
                max_length = 20,
                choices= Location_CHOICES,
                default = BLANK
    )

    Specific_Location = models.TextField(blank = True)
    #is this the right way?
    Running = models.BinaryField()

    Chasing = models.BinaryField()

    Climbing = models.BinaryField()

    Eating = models.BinaryField()

    Foraging = models.BinaryField()

    Other_Activities = models.TextField(blank = True)

    Kuks = models.BinaryField()

    Quaas = models.BinaryField()

    Moans = models.BinaryField(
                default = False
    )

    Tail_flags = models.BinaryField()

    Tail_twitches = models.BinaryField()

    Approaches = models.BinaryField()

    Indifferent = models.BinaryField()

    Runs_from = models.BinaryField()
