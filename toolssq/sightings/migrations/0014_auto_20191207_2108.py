# Generated by Django 2.2.7 on 2019-12-07 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0013_auto_20191206_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Date',
            field=models.DateField(help_text='Format:yyyy-mm-dd'),
        ),
    ]