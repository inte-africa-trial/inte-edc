# Generated by Django 3.0.6 on 2020-06-24 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("inte_subject", "0004_auto_20200624_0322"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="historicalhivinitialreview", name="clinic_next_appt_date",
        ),
        migrations.RemoveField(
            model_name="hivinitialreview", name="clinic_next_appt_date",
        ),
    ]
