from django.db import models
from django.utils.html import mark_safe
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to='post_images/', 
        null=True, 
        blank=True,
        verbose_name="Post Görseli"
    )
    def image_tag(self):
        if self.image:
            return mark_safe(f'''
                <div style="display: flex; align-items: center; gap: 1rem;">
                  <label for="hidden_image_input" style="cursor:pointer;">
                    <img src="{self.image.url}" style="height:150px; border-radius:8px;" />
                  </label>
                  <span style="white-space: nowrap;">
                    <input type="checkbox" name="image-clear" id="image-clear-id" />
                    <label for="image-clear-id">Temizle</label>
                  </span>
                </div>
            ''')
        return "Görsel yok"


        image_tag.short_description = "Önizleme"
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])