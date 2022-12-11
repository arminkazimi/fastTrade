from django.apps import AppConfig


class DataproviderConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "dataProvider"

    def ready(self):
        from .backgroundJobs import scheduler
        scheduler.start()

