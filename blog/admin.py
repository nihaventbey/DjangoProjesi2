from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from .models import Post, SiteSettings, MenuItem, StaticPage

# ------------ PostAdmin ------------
class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'style': 'display:none;', 'id': 'hidden_image_input'})
        }

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'created_at', 'image_tag')
    readonly_fields = ('image_tag',)

    class Media:
        js = ('blog/js/admin_image_toggle.js',)


# ------------ SiteSettingsAdmin ------------
@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'contact_email', 'phone_number')

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()  # Sadece 1 tane eklenebilsin


# ------------ MenuItemAdmin ------------
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'order')


# ------------ StaticPageAdmin ------------
@admin.register(StaticPage)
class StaticPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


# ------------ Post kayıt ------------
admin.site.register(Post, PostAdmin)
