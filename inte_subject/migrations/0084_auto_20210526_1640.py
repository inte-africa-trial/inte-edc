# Generated by Django 3.2.3 on 2021-05-26 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("inte_lists", "0011_auto_20210524_1533"),
        ("inte_subject", "0083_auto_20210526_0406"),
    ]

    operations = [
        migrations.CreateModel(
            name="ArvRegimens",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("inte_lists.arvregimens",),
        ),
        migrations.AlterField(
            model_name="drugrefillhiv",
            name="rx",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="inte_subject.arvregimens",
                verbose_name="Which medicine did the patient receive today?",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldrugrefillhiv",
            name="rx",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="inte_subject.arvregimens",
                verbose_name="Which medicine did the patient receive today?",
            ),
        ),
    ]
