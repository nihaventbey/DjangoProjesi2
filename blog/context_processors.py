from .models import SiteSettings, MenuItem

def site_context(request):
    return {
        'site_settings': SiteSettings.objects.first(),
        'menu_items': MenuItem.objects.all().order_by('order')
    }
