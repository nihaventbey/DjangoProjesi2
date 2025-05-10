from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'image_tag')
    readonly_fields = ('image_tag',)

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="150" />'
        return "Görsel Yok"
    image_preview.short_description = "Önizleme"
    image_preview.allow_tags = True

admin.site.register(Post, PostAdmin)

from django.contrib import admin
from .models import Post
from django.utils.safestring import mark_safe
from django import forms

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'style': 'display:none;', 'id': 'hidden_image_input'})
        }

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    readonly_fields = ('image_tag',)

    class Media:
        js = ('blog/js/admin_image_toggle.js',)
