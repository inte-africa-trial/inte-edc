# Generated by Django 3.0.9 on 2020-10-02 17:42

import edc_model.models.fields.other_charfield
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("inte_screening", "0013_auto_20200812_0317"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalsubjectrefusal",
            name="other_reason",
            field=edc_model.models.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
        migrations.AlterField(
            model_name="subjectrefusal",
            name="other_reason",
            field=edc_model.models.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
    ]
