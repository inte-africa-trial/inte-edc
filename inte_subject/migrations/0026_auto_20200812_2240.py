# Generated by Django 3.0.6 on 2020-08-12 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inte_lists", "0006_auto_20200812_0317"),
        ("inte_subject", "0025_auto_20200812_2228"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="healtheconomicsrevised", name="rx_arv_recv_today",
        ),
        migrations.RemoveField(
            model_name="healtheconomicsrevised", name="rx_diabetes_recv_today",
        ),
        migrations.RemoveField(
            model_name="healtheconomicsrevised", name="rx_hypertension_recv_today",
        ),
        migrations.RemoveField(
            model_name="healtheconomicsrevised", name="rx_other_recv_today",
        ),
        migrations.AddField(
            model_name="healtheconomicsrevised",
            name="rx_diabetes_paid_today",
            field=models.ManyToManyField(
                blank=True,
                related_name="_healtheconomicsrevised_rx_diabetes_paid_today_+",
                to="inte_lists.DrugPaySources",
                verbose_name="If YES, received raised blood sugar (diabetes) drugs, how were these paid for?",
            ),
        ),
        migrations.AddField(
            model_name="healtheconomicsrevised",
            name="rx_diabetes_today",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                default="Yes",
                max_length=15,
                verbose_name="Did you receive raised blood sugar (diabetes) drugs today?",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="healtheconomicsrevised",
            name="rx_hiv_paid_today",
            field=models.ManyToManyField(
                blank=True,
                max_length=25,
                related_name="_healtheconomicsrevised_rx_hiv_paid_today_+",
                to="inte_lists.DrugPaySources",
                verbose_name="If YES, received ARV (HIV) drugs, how were these paid for?",
            ),
        ),
        migrations.AddField(
            model_name="healtheconomicsrevised",
            name="rx_hiv_today",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                default="Yes",
                max_length=15,
                verbose_name="Did you receive ARVs (HIV) today?",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="healtheconomicsrevised",
            name="rx_hypertension_paid_today",
            field=models.ManyToManyField(
                blank=True,
                related_name="_healtheconomicsrevised_rx_hypertension_paid_today_+",
                to="inte_lists.DrugPaySources",
                verbose_name="If YES, received high blood pressure (Hypertension) drugs, how were these paid for?",
            ),
        ),
        migrations.AddField(
            model_name="healtheconomicsrevised",
            name="rx_hypertension_today",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                default="Yes",
                max_length=15,
                verbose_name="Did you receive raised blood pressure (hypertension) drugs today?",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="healtheconomicsrevised",
            name="rx_other_paid_today",
            field=models.ManyToManyField(
                blank=True,
                related_name="_healtheconomicsrevised_rx_other_paid_today_+",
                to="inte_lists.DrugPaySources",
                verbose_name="If YES, received 'other' drugs, how were these paid for?",
            ),
        ),
        migrations.AddField(
            model_name="healtheconomicsrevised",
            name="rx_other_today",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                default="Yes",
                max_length=15,
                verbose_name="Did you receive 'other' drugs today?",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="historicalhealtheconomicsrevised",
            name="rx_diabetes_today",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                default="Yes",
                max_length=15,
                verbose_name="Did you receive raised blood sugar (diabetes) drugs today?",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="historicalhealtheconomicsrevised",
            name="rx_hiv_today",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                default="Yes",
                max_length=15,
                verbose_name="Did you receive ARVs (HIV) today?",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="historicalhealtheconomicsrevised",
            name="rx_hypertension_today",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                default="Yes",
                max_length=15,
                verbose_name="Did you receive raised blood pressure (hypertension) drugs today?",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="historicalhealtheconomicsrevised",
            name="rx_other_today",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                default="Yes",
                max_length=15,
                verbose_name="Did you receive 'other' drugs today?",
            ),
            preserve_default=False,
        ),
    ]