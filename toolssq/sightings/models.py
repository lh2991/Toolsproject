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
    TRUE = 'True'
    FALSE = 'False'
    TF_CHOICES = (
        (TRUE,'True'),
        (FALSE,'False'),
    )
    Running = models.CharField(
                max_length = 40,
                choices= TF_CHOICES,
                null = True,
    )

    Chasing = models.CharField(
                max_length = 40,
                choices= TF_CHOICES,
                null = True,
    )


    Climbing = models.CharField(
                max_length = 40,
                choices= TF_CHOICES,
                null = True,
    )


    Eating = models.CharField(
                max_length = 40,
                choices= TF_CHOICES,
                null = True,
    )


    Foraging = models.CharField(
                max_length = 40,
                choices= TF_CHOICES,
                null = True,
    )


    Other_Activities = models.CharField(
                max_length = 40,
                choices= TF_CHOICES,
                null = True,
    )


    Kuks = models.CharField(
                max_length = 40,
                choices= TF_CHOICES,
                null = True,
    )


    Quaas = models.CharField(
                max_length = 40,
                choices= TF_CHOICES,
                null = True,
    )


    Moans = models.CharField(
                max_length = 40,
                choices= TF_CHOICES,
                null = True,
    )


    Tail_flags = models.CharField(
                max_length = 40,
                choices= TF_CHOICES,
                null = True,
    )


    Tail_twitches = models.CharField(
                max_length = 40,
                choices= TF_CHOICES,
                null = True,
    )


    Approaches = models.CharField(
                max_length = 40,
                choices= TF_CHOICES,
                null = True,
    )


    Indifferent = models.CharField(
                max_length = 40,
                choices= TF_CHOICES,
                null = True,
    )


    Runs_from = models.CharField(
                max_length = 40,
                choices= TF_CHOICES,
                null = True,
    )
