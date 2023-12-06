from django.apps import AppConfig


class RecordConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'record'
    
    def ready(self):
        from . import signals