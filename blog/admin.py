from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="150" />'
        return "Görsel Yok"
    image_preview.short_description = "Önizleme"
    image_preview.allow_tags = True

admin.site.register(Post, PostAdmin)