# Generated by Django 3.1.6 on 2021-05-09 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inte_screening", "0015_auto_20210509_2052"),
    ]

    operations = [
        migrations.AddField(
            model_name="dailyclosinglog",
            name="clinic_end_time",
            field=models.TimeField(null=True, verbose_name="Clinic End time"),
        ),
        migrations.AddField(
            model_name="dailyclosinglog",
            name="clinic_start_time",
            field=models.TimeField(null=True, verbose_name="Clinic start time"),
        ),
        migrations.AddField(
            model_name="historicaldailyclosinglog",
            name="clinic_end_time",
            field=models.TimeField(null=True, verbose_name="Clinic End time"),
        ),
        migrations.AddField(
            model_name="historicaldailyclosinglog",
            name="clinic_start_time",
            field=models.TimeField(null=True, verbose_name="Clinic start time"),
        ),
    ]