# Generated by Django 3.0 on 2020-03-11 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inte_prn", "0002_auto_20200220_2308"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicallosstofollowup",
            name="loss_category",
            field=models.CharField(
                choices=[], max_length=25, verbose_name="Category of loss to follow up"
            ),
        ),
        migrations.AlterField(
            model_name="losstofollowup",
            name="loss_category",
            field=models.CharField(
                choices=[], max_length=25, verbose_name="Category of loss to follow up"
            ),
        ),
    ]