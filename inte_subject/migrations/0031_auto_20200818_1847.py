# Generated by Django 3.0.9 on 2020-08-18 15:47

import _socket
from django.conf import settings
import django.contrib.sites.managers
from django.db import migrations, models
import django.db.models.deletion
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_revision.revision_field
import edc_model.models.fields.height
import edc_model.models.fields.weight
import edc_model.models.validators.date
import edc_protocol.validators
import edc_utils.date
import edc_visit_tracking.managers
import simple_history.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("sites", "0002_alter_domain_unique"),
        ("inte_subject", "0030_auto_20200813_1825"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalindicators",
            name="height",
            field=edc_model.models.fields.height.HeightField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="historicalindicators",
            name="weight",
            field=edc_model.models.fields.weight.WeightField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="indicators",
            name="height",
            field=edc_model.models.fields.height.HeightField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="indicators",
            name="weight",
            field=edc_model.models.fields.weight.WeightField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name="HistoricalFamilyHistory",
            fields=[
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True,
                        default=django_audit_fields.models.audit_model_mixin.utcnow,
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True,
                        default=django_audit_fields.models.audit_model_mixin.utcnow,
                    ),
                ),
                (
                    "user_created",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        db_index=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                    ),
                ),
                (
                    "report_datetime",
                    models.DateTimeField(
                        default=edc_utils.date.get_utcnow,
                        help_text="If reporting today, use today's date/time, otherwise use the date/time this information was reported.",
                        validators=[
                            edc_protocol.validators.datetime_not_before_study_start,
                            edc_model.models.validators.date.datetime_not_future,
                        ],
                        verbose_name="Report Date",
                    ),
                ),
                (
                    "consent_model",
                    models.CharField(editable=False, max_length=50, null=True),
                ),
                (
                    "consent_version",
                    models.CharField(editable=False, max_length=10, null=True),
                ),
                (
                    "crf_status",
                    models.CharField(
                        choices=[
                            ("INCOMPLETE", "Incomplete (some data pending)"),
                            ("COMPLETE", "Complete"),
                        ],
                        default="INCOMPLETE",
                        help_text="If some data is still pending, flag this CRF as incomplete",
                        max_length=25,
                        verbose_name="CRF status",
                    ),
                ),
                (
                    "crf_status_comments",
                    models.TextField(
                        blank=True,
                        help_text="for example, why some data is still pending",
                        null=True,
                        verbose_name="Any comments related to status of this CRF",
                    ),
                ),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "hypertension_in_household",
                    models.CharField(
                        choices=[
                            ("No", "No"),
                            ("yes_spouse", "Yes, my spouse"),
                            ("yes_parents", "Yes, one of my parents living with me"),
                            ("yes_relative", "Yes, another relative living with me"),
                        ],
                        max_length=25,
                        verbose_name="Do you know if anyone else in your household has <ul>high blood pressure</ul?",
                    ),
                ),
                (
                    "diabetes_in_household",
                    models.CharField(
                        choices=[
                            ("No", "No"),
                            ("yes_spouse", "Yes, my spouse"),
                            ("yes_parents", "Yes, one of my parents living with me"),
                            ("yes_relative", "Yes, another relative living with me"),
                        ],
                        max_length=25,
                        verbose_name="Do you know if anyone else in your household has <ul>diabetes</ul?",
                    ),
                ),
                (
                    "hiv_in_household",
                    models.CharField(
                        choices=[
                            ("No", "No"),
                            ("yes_spouse", "Yes, my spouse"),
                            ("yes_parents", "Yes, one of my parents living with me"),
                            ("yes_relative", "Yes, another relative living with me"),
                        ],
                        max_length=25,
                        verbose_name="Do you know if anyone else in your household has <ul>HIV</ul?",
                    ),
                ),
                (
                    "high_bp_bs_tf",
                    models.CharField(
                        choices=[
                            ("true", "True"),
                            ("false", "False"),
                            ("dont_know", "Don't know"),
                        ],
                        max_length=25,
                        verbose_name="High blood pressure and high blood sugar can cause many illnesses like heart attacks, stroke, kidney failure",
                    ),
                ),
                (
                    "overweight_tf",
                    models.CharField(
                        choices=[
                            ("true", "True"),
                            ("false", "False"),
                            ("dont_know", "Don't know"),
                        ],
                        max_length=25,
                        verbose_name="Being overweight protects from high blood pressure and high blood sugar",
                    ),
                ),
                (
                    "salty_foods_tf",
                    models.CharField(
                        choices=[
                            ("true", "True"),
                            ("false", "False"),
                            ("dont_know", "Don't know"),
                        ],
                        max_length=25,
                        verbose_name="Salty food protects from high blood sugar",
                    ),
                ),
                (
                    "excercise_tf",
                    models.CharField(
                        choices=[
                            ("true", "True"),
                            ("false", "False"),
                            ("dont_know", "Don't know"),
                        ],
                        max_length=25,
                        verbose_name="Regular exercise is important for people with <ul>high blood pressure</ul> or <ul>high blood sugar</ul> even if they are taking medicines for these conditions.",
                    ),
                ),
                (
                    "take_medicine_tf",
                    models.CharField(
                        choices=[
                            ("true", "True"),
                            ("false", "False"),
                            ("dont_know", "Don't know"),
                        ],
                        max_length=25,
                        verbose_name="Drugs for <ul>blood sugar</ul> and <ul>blood pressure</ul> can make you unwell",
                    ),
                ),
                (
                    "stop_hypertension_meds_tf",
                    models.CharField(
                        choices=[
                            ("true", "True"),
                            ("false", "False"),
                            ("dont_know", "Don't know"),
                        ],
                        max_length=25,
                        verbose_name="It is best to stop taking <ul>blood pressure</ul> pills when you feel better and start pill taking again when you feel sick",
                    ),
                ),
                (
                    "traditional_hypertension_tf",
                    models.CharField(
                        choices=[
                            ("true", "True"),
                            ("false", "False"),
                            ("dont_know", "Don't know"),
                        ],
                        max_length=25,
                        verbose_name="Herbs and traditional medicine are better for managing <ul>blood pressure</ul> than pills and medicines",
                    ),
                ),
                (
                    "stop_diabetes_meds_tf",
                    models.CharField(
                        choices=[
                            ("true", "True"),
                            ("false", "False"),
                            ("dont_know", "Don't know"),
                        ],
                        max_length=25,
                        verbose_name="It is best to stop taking <ul>blood sugar</ul> medicines when you feel better and start pill taking again when you feel sick",
                    ),
                ),
                (
                    "traditional_diabetes_tf",
                    models.CharField(
                        choices=[
                            ("true", "True"),
                            ("false", "False"),
                            ("dont_know", "Don't know"),
                        ],
                        max_length=25,
                        verbose_name="Herbs and traditional medicine are better for managing <ul>diabetes</ul> than pills and medicines",
                    ),
                ),
                (
                    "diabetes_cause_tf",
                    models.CharField(
                        choices=[
                            ("true", "True"),
                            ("false", "False"),
                            ("dont_know", "Don't know"),
                        ],
                        max_length=25,
                        verbose_name="Having drinks with sugar (e.g. tea/coffee) causes diabetes",
                    ),
                ),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="sites.Site",
                    ),
                ),
                (
                    "subject_visit",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="inte_subject.SubjectVisit",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Family History and Knowledge",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="FamilyHistory",
            fields=[
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True,
                        default=django_audit_fields.models.audit_model_mixin.utcnow,
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True,
                        default=django_audit_fields.models.audit_model_mixin.utcnow,
                    ),
                ),
                (
                    "user_created",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "report_datetime",
                    models.DateTimeField(
                        default=edc_utils.date.get_utcnow,
                        help_text="If reporting today, use today's date/time, otherwise use the date/time this information was reported.",
                        validators=[
                            edc_protocol.validators.datetime_not_before_study_start,
                            edc_model.models.validators.date.datetime_not_future,
                        ],
                        verbose_name="Report Date",
                    ),
                ),
                (
                    "consent_model",
                    models.CharField(editable=False, max_length=50, null=True),
                ),
                (
                    "consent_version",
                    models.CharField(editable=False, max_length=10, null=True),
                ),
                (
                    "crf_status",
                    models.CharField(
                        choices=[
                            ("INCOMPLETE", "Incomplete (some data pending)"),
                            ("COMPLETE", "Complete"),
                        ],
                        default="INCOMPLETE",
                        help_text="If some data is still pending, flag this CRF as incomplete",
                        max_length=25,
                        verbose_name="CRF status",
                    ),
                ),
                (
                    "crf_status_comments",
                    models.TextField(
                        blank=True,
                        help_text="for example, why some data is still pending",
                        null=True,
                        verbose_name="Any comments related to status of this CRF",
                    ),
                ),
                (
                    "hypertension_in_household",
                    models.CharField(
                        choices=[
                            ("No", "No"),
                            ("yes_spouse", "Yes, my spouse"),
                            ("yes_parents", "Yes, one of my parents living with me"),
                            ("yes_relative", "Yes, another relative living with me"),
                        ],
                        max_length=25,
                        verbose_name="Do you know if anyone else in your household has <ul>high blood pressure</ul?",
                    ),
                ),
                (
                    "diabetes_in_household",
                    models.CharField(
                        choices=[
                            ("No", "No"),
                            ("yes_spouse", "Yes, my spouse"),
                            ("yes_parents", "Yes, one of my parents living with me"),
                            ("yes_relative", "Yes, another relative living with me"),
                        ],
                        max_length=25,
                        verbose_name="Do you know if anyone else in your household has <ul>diabetes</ul?",
                    ),
                ),
                (
                    "hiv_in_household",
                    models.CharField(
                        choices=[
                            ("No", "No"),
                            ("yes_spouse", "Yes, my spouse"),
                            ("yes_parents", "Yes, one of my parents living with me"),
                            ("yes_relative", "Yes, another relative living with me"),
                        ],
                        max_length=25,
                        verbose_name="Do you know if anyone else in your household has <ul>HIV</ul?",
                    ),
                ),
                (
                    "high_bp_bs_tf",
                    models.CharField(
                        choices=[
                            ("true", "True"),
                            ("false", "False"),
                            ("dont_know", "Don't know"),
                        ],
                        max_length=25,
                        verbose_name="High blood pressure and high blood sugar can cause many illnesses like heart attacks, stroke, kidney failure",
                    ),
                ),
                (
                    "overweight_tf",
                    models.CharField(
                        choices=[
                            ("true", "True"),
                            ("false", "False"),
                            ("dont_know", "Don't know"),
                        ],
                        max_length=25,
                        verbose_name="Being overweight protects from high blood pressure and high blood sugar",
                    ),
                ),
                (
                    "salty_foods_tf",
                    models.CharField(
                        choices=[
                            ("true", "True"),
                            ("false", "False"),
                            ("dont_know", "Don't know"),
                        ],
                        max_length=25,
                        verbose_name="Salty food protects from high blood sugar",
                    ),
                ),
                (
                    "excercise_tf",
                    models.CharField(
                        choices=[
                            ("true", "True"),
                            ("false", "False"),
                            ("dont_know", "Don't know"),
                        ],
                        max_length=25,
                        verbose_name="Regular exercise is important for people with <ul>high blood pressure</ul> or <ul>high blood sugar</ul> even if they are taking medicines for these conditions.",
                    ),
                ),
                (
                    "take_medicine_tf",
                    models.CharField(
                        choices=[
                            ("true", "True"),
                            ("false", "False"),
                            ("dont_know", "Don't know"),
                        ],
                        max_length=25,
                        verbose_name="Drugs for <ul>blood sugar</ul> and <ul>blood pressure</ul> can make you unwell",
                    ),
                ),
                (
                    "stop_hypertension_meds_tf",
                    models.CharField(
                        choices=[
                            ("true", "True"),
                            ("false", "False"),
                            ("dont_know", "Don't know"),
                        ],
                        max_length=25,
                        verbose_name="It is best to stop taking <ul>blood pressure</ul> pills when you feel better and start pill taking again when you feel sick",
                    ),
                ),
                (
                    "traditional_hypertension_tf",
                    models.CharField(
                        choices=[
                            ("true", "True"),
                            ("false", "False"),
                            ("dont_know", "Don't know"),
                        ],
                        max_length=25,
                        verbose_name="Herbs and traditional medicine are better for managing <ul>blood pressure</ul> than pills and medicines",
                    ),
                ),
                (
                    "stop_diabetes_meds_tf",
                    models.CharField(
                        choices=[
                            ("true", "True"),
                            ("false", "False"),
                            ("dont_know", "Don't know"),
                        ],
                        max_length=25,
                        verbose_name="It is best to stop taking <ul>blood sugar</ul> medicines when you feel better and start pill taking again when you feel sick",
                    ),
                ),
                (
                    "traditional_diabetes_tf",
                    models.CharField(
                        choices=[
                            ("true", "True"),
                            ("false", "False"),
                            ("dont_know", "Don't know"),
                        ],
                        max_length=25,
                        verbose_name="Herbs and traditional medicine are better for managing <ul>diabetes</ul> than pills and medicines",
                    ),
                ),
                (
                    "diabetes_cause_tf",
                    models.CharField(
                        choices=[
                            ("true", "True"),
                            ("false", "False"),
                            ("dont_know", "Don't know"),
                        ],
                        max_length=25,
                        verbose_name="Having drinks with sugar (e.g. tea/coffee) causes diabetes",
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="sites.Site",
                    ),
                ),
                (
                    "subject_visit",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="inte_subject.SubjectVisit",
                    ),
                ),
            ],
            options={
                "verbose_name": "Family History and Knowledge",
                "verbose_name_plural": "Family History and Knowledge",
                "ordering": ("-modified", "-created"),
                "get_latest_by": "modified",
                "abstract": False,
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
            },
            managers=[
                ("on_site", django.contrib.sites.managers.CurrentSiteManager()),
                ("objects", edc_visit_tracking.managers.CrfModelManager()),
            ],
        ),
        migrations.AddIndex(
            model_name="familyhistory",
            index=models.Index(
                fields=["subject_visit", "site", "id"],
                name="inte_subjec_subject_2e330e_idx",
            ),
        ),
    ]
