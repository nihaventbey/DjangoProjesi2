from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    
    # ready() metodu ve model tanımları KESİNLİKLE OLMAMALI