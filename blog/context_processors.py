from .models import SiteSettings, MenuItem

def site_context(request):
    settings = SiteSettings.objects.first()
    menu = MenuItem.objects.all()
    return {
        'site_settings': settings,
        'menu_items': menu
    }
