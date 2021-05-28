import sys

from django.db import migrations
from respond_models.utils import calculate_dx_date_if_estimated
from tqdm import tqdm


def refresh_review_models(apps, schema_editor):
    for prefix in ["hiv", "htn", "dm"]:
        sys.stdout.write(f"\nUpdating {prefix} review models.\n")
        model_cls = apps.get_model(f"inte_subject.{prefix}initialreview")
        qs = model_cls.objects.all()
        total = qs.count()
        for obj in tqdm(qs, total=total):
            obj.dx_estimated_date, obj.dx_date_estimated = calculate_dx_date_if_estimated(
                obj.dx_date,
                obj.dx_ago,
                obj.report_datetime,
            )
            obj.save_base(update_fields=["dx_estimated_date", "dx_date_estimated"])
    sys.stdout.write(f"\n - Done.                                           \n")


class Migration(migrations.Migration):

    dependencies = [
        ("inte_subject", "0085_alter_arvregimens_options"),
    ]
    operations = [migrations.RunPython(refresh_review_models)]
