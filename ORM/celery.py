from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ORM.settings')

app = Celery('ORM')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


# path/to/your/proj/src/cfehome/celery.py

from celery.schedules import crontab

# Below is for illustration purposes. We 
# configured so we can adjust scheduling 
# in the Django admin to manage all 
# Periodic Tasks like below
# app.conf.beat_schedule = {
#     'multiply-task-crontab': {
#         'task': 'multiply_two_numbers',
#         'schedule': crontab(hour=5, minute=20, day_of_week='*'),
#         'args': (16, 16),
#     },
#     'multiply-every-30-seconds': {
#         'task': 'multiply_two_numbers',
#         'schedule': 30.0,
#         'args': (16, 16)
#     },
#     'add-every-1-seconds': {
#         'task': 'apps.dj_celery.tasks.add',
#         'schedule': 60.0,
#         'args': (16, 16)
#     },
# }
