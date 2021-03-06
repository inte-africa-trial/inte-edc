# Generated by Django 3.0.6 on 2020-06-30 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inte_consent", "0002_auto_20200623_0122"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalsubjectconsent",
            name="clinic_type",
            field=models.CharField(
                choices=[
                    ("hiv_clinic", "HIV Clinic"),
                    ("ncd_clinic", "NCD Clinic (Joint Diabetes/Hypertension)"),
                    ("diabetes_clinic", "Diabetes Clinic"),
                    ("hypertension_clinic", "Hypertension Clinic"),
                ],
                help_text="Should match that reported on the Screening form.",
                max_length=25,
                verbose_name="From which type of clinic was the patient selected?",
            ),
        ),
        migrations.AlterField(
            model_name="subjectconsent",
            name="clinic_type",
            field=models.CharField(
                choices=[
                    ("hiv_clinic", "HIV Clinic"),
                    ("ncd_clinic", "NCD Clinic (Joint Diabetes/Hypertension)"),
                    ("diabetes_clinic", "Diabetes Clinic"),
                    ("hypertension_clinic", "Hypertension Clinic"),
                ],
                help_text="Should match that reported on the Screening form.",
                max_length=25,
                verbose_name="From which type of clinic was the patient selected?",
            ),
        ),
    ]
