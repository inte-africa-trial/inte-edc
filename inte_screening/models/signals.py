from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .subject_screening import SubjectScreening
from .subject_refusal import SubjectRefusal


@receiver(
    post_save,
    weak=False,
    sender=SubjectRefusal,
    dispatch_uid="subject_refusal_on_post_save",
)
def subject_refusal_on_post_save(sender, instance, raw, created, **kwargs):
    """Updates `refused` field on SUbjectScreening
    """
    if not raw:
        try:
            obj = SubjectScreening.objects.get(
                screening_identifier=instance.screening_identifier
            )
        except ObjectDoesNotExist:
            pass
        else:
            obj.refused = True
            obj.save(update_fields=["refused"])


@receiver(
    post_delete,
    weak=False,
    sender=SubjectRefusal,
    dispatch_uid="subject_refusal_on_post_delete",
)
def subject_refusal_on_post_delete(sender, instance, using, **kwargs):
    """Updates/Resets subject screening.
    """
    try:
        obj = SubjectScreening.objects.get(
            screening_identifier=instance.screening_identifier
        )
    except ObjectDoesNotExist:
        pass
    else:
        obj.refused = False
        obj.save(update_fields=["refused"])
