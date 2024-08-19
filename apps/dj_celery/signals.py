from django.db.models import signals
from django.dispatch import receiver
from .models import Labour
from .tasks import my_task

@receiver(signals.post_save, sender=Labour)
def new_labour_created(sender, instance, created, **kwargs):
    print('inside the django signals... calling celery task..')
    my_task.delay(5, 50)