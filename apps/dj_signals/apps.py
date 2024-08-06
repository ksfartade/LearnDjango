from django.apps import AppConfig


class DjSignalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.dj_signals'
    def ready(self):
        import apps.dj_signals.signals
