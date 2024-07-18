from django.apps import AppConfig


class DjCeleryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.dj_celery'
    def ready(self):
        import apps.dj_celery.signals
