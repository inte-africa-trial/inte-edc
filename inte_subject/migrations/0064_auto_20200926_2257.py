# Generated by Django 3.0.9 on 2020-09-26 19:57

from django.db import migrations, models
import edc_model.models.fields.other_charfield


class Migration(migrations.Migration):

    dependencies = [
        ("inte_lists", "0007_auto_20200910_1742"),
        ("inte_subject", "0063_auto_20200926_1639"),
    ]

    operations = [
        migrations.AddField(
            model_name="healtheconomicsrevised",
            name="rx_dm_paid_month_other",
            field=edc_model.models.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
        migrations.AddField(
            model_name="healtheconomicsrevised",
            name="rx_hiv_paid_month_other",
            field=edc_model.models.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
        migrations.AddField(
            model_name="healtheconomicsrevised",
            name="rx_htn_paid_month_other",
            field=edc_model.models.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
        migrations.AddField(
            model_name="historicalhealtheconomicsrevised",
            name="rx_dm_paid_month_other",
            field=edc_model.models.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
        migrations.AddField(
            model_name="historicalhealtheconomicsrevised",
            name="rx_hiv_paid_month_other",
            field=edc_model.models.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
        migrations.AddField(
            model_name="historicalhealtheconomicsrevised",
            name="rx_htn_paid_month_other",
            field=edc_model.models.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
        migrations.AlterField(
            model_name="healtheconomicsrevised",
            name="transport",
            field=models.ManyToManyField(
                max_length=25,
                to="inte_lists.TransportChoices",
                verbose_name="Which form of transport did you take to get to the hospital today?",
            ),
        ),
    ]