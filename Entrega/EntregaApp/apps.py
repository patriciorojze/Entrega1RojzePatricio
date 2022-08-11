from django.apps import AppConfig

from Entrega.settings import LANGUAGE_CODE


class EntregaappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'EntregaApp'
    LANGUAGE_CODE = 'en-us'
