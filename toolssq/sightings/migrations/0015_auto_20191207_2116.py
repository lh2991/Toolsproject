# Generated by Django 2.2.7 on 2019-12-07 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0014_auto_20191207_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Squirrel_ID',
            field=models.CharField(help_text='Enter in form hectare_ID-shift-HHMM-number', max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
