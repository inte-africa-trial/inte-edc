# Generated by Django 3.1.6 on 2021-05-12 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inte_screening', '0017_dailyclosinglogrevised'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyclosinglog',
            name='clinic_end_time',
            field=models.TimeField(help_text='Use 24HRS format. For example 07:00', null=True, verbose_name='Clinic End time'),
        ),
        migrations.AlterField(
            model_name='dailyclosinglog',
            name='clinic_start_time',
            field=models.TimeField(help_text='Use 24HRS format. For example 07:00', null=True, verbose_name='Clinic start time'),
        ),
        migrations.AlterField(
            model_name='historicaldailyclosinglog',
            name='clinic_end_time',
            field=models.TimeField(help_text='Use 24HRS format. For example 07:00', null=True, verbose_name='Clinic End time'),
        ),
        migrations.AlterField(
            model_name='historicaldailyclosinglog',
            name='clinic_start_time',
            field=models.TimeField(help_text='Use 24HRS format. For example 07:00', null=True, verbose_name='Clinic start time'),
        ),
    ]
