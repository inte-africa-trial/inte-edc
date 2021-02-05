# Generated by Django 3.0.6 on 2020-07-01 00:04

import edc_model.models.fields.other_charfield
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inte_lists", "0005_auto_20200701_0041"),
        ("inte_subject", "0012_auto_20200630_0649"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="reasonforvisit",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
                "verbose_name": "Reason for Visit",
                "verbose_name_plural": "Reason for Visits",
            },
        ),
        migrations.RemoveField(
            model_name="historicalreasonforvisit",
            name="diabetes_services_other",
        ),
        migrations.RemoveField(
            model_name="historicalreasonforvisit",
            name="hiv_services_other",
        ),
        migrations.RemoveField(
            model_name="historicalreasonforvisit",
            name="hypertension_services_other",
        ),
        migrations.RemoveField(
            model_name="reasonforvisit",
            name="diabetes_services",
        ),
        migrations.RemoveField(
            model_name="reasonforvisit",
            name="diabetes_services_other",
        ),
        migrations.RemoveField(
            model_name="reasonforvisit",
            name="hiv_services",
        ),
        migrations.RemoveField(
            model_name="reasonforvisit",
            name="hiv_services_other",
        ),
        migrations.RemoveField(
            model_name="reasonforvisit",
            name="hypertension_services",
        ),
        migrations.RemoveField(
            model_name="reasonforvisit",
            name="hypertension_services_other",
        ),
        migrations.AddField(
            model_name="historicalreasonforvisit",
            name="clinic_services_other",
            field=edc_model.models.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
        migrations.AddField(
            model_name="historicalreasonforvisit",
            name="refill_diabetes",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                default="N/A",
                max_length=25,
                verbose_name="Is the patient refilling Diabetes medications?",
            ),
        ),
        migrations.AddField(
            model_name="historicalreasonforvisit",
            name="refill_hiv",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                default="N/A",
                max_length=25,
                verbose_name="Is the patient refilling HIV medications?",
            ),
        ),
        migrations.AddField(
            model_name="historicalreasonforvisit",
            name="refill_hypertension",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                default="N/A",
                max_length=25,
                verbose_name="Is the patient refilling Hypertension medications?",
            ),
        ),
        migrations.AddField(
            model_name="reasonforvisit",
            name="clinic_services",
            field=models.ManyToManyField(
                blank=True,
                related_name="clinic_services",
                to="inte_lists.ClinicServices",
                verbose_name="Why is the patient at the clinic?",
            ),
        ),
        migrations.AddField(
            model_name="reasonforvisit",
            name="clinic_services_other",
            field=edc_model.models.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
        migrations.AddField(
            model_name="reasonforvisit",
            name="refill_diabetes",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                default="N/A",
                max_length=25,
                verbose_name="Is the patient refilling Diabetes medications?",
            ),
        ),
        migrations.AddField(
            model_name="reasonforvisit",
            name="refill_hiv",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                default="N/A",
                max_length=25,
                verbose_name="Is the patient refilling HIV medications?",
            ),
        ),
        migrations.AddField(
            model_name="reasonforvisit",
            name="refill_hypertension",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                default="N/A",
                max_length=25,
                verbose_name="Is the patient refilling Hypertension medications?",
            ),
        ),
    ]
