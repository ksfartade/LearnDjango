from django.db.models import signals
from django.dispatch import receiver
from datetime import datetime
from .models import Student

@receiver(signals.pre_save, sender=Student)
def before_saving_instance(sender, instance, **kwargs):
    print("About to save:", instance)

@receiver(signals.post_save, sender=Student)
def after_saving_instance(sender, instance, created, **kwargs):
    if created:
        print("A new instance was created:", instance)
    else:
        print("An instance was updated:", instance)

@receiver(signals.pre_delete, sender=Student)
def before_deleting_instance(sender, instance, **kwargs):
    print("About to delete:", instance)

@receiver(signals.post_delete, sender=Student)
def after_deleting_instance(sender, instance, **kwargs):
    print("Instance deleted:", instance)

# @receiver(signals.pre_init, sender=Student)
# def before_instance_init(sender, *args, **kwargs):
#     print("Before Student instance initialization")

# @receiver(signals.post_init, sender=Student)
# def after_instance_init(sender, instance, **kwargs):
#     print("After Student instance initialization:", instance)
