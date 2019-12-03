# Generated by Django 2.2.7 on 2019-12-03 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Approaches',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Chasing',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Climbing',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Eating',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Foraging',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Indifferent',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Kuks',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Moans',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Other_Activities',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Quaas',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Running',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Runs_from',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Tail_flags',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel_attr',
            name='Tail_twitches',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=40, null=True),
        ),
    ]
