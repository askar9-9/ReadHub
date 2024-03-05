from django.apps import AppConfig


class CatalogConfig(AppConfig):
    verbose_name = "Управление книгами"
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'