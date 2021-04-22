# Generated by Django 3.1.6 on 2021-02-09 12:09

from django.db import migrations, models
import edc_model.models.validators.date


class Migration(migrations.Migration):

    dependencies = [
        ('inte_subject', '0077_auto_20210203_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalhivinitialreview',
            name='arv_initiation_actual_date',
            field=models.DateField(help_text='If possible, provide the exact date here instead of estimating above.', null=True, validators=[edc_model.models.validators.date.date_not_future], verbose_name='Date started antiretroviral therapy (ART)'),
        ),
        migrations.AlterField(
            model_name='hivinitialreview',
            name='arv_initiation_actual_date',
            field=models.DateField(help_text='If possible, provide the exact date here instead of estimating above.', null=True, validators=[edc_model.models.validators.date.date_not_future], verbose_name='Date started antiretroviral therapy (ART)'),
        ),
    ]