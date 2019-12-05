# Generated by Django 2.2.7 on 2019-12-05 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0008_auto_20191205_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Approaches',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Chasing',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Climbing',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Eating',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Foraging',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Indifferent',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Kuks',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Moans',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Other_Activities',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Quaas',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Running',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Runs_from',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Tail_flags',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Tail_twitches',
            field=models.BooleanField(default=True),
        ),
    ]
