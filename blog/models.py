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
        

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, default="Blog Sitesi")
    site_description = models.TextField(blank=True)
    site_keywords = models.CharField(max_length=255, blank=True)
    contact_email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    footer_text = models.CharField(max_length=255, blank=True)
    header_image = models.ImageField(upload_to='headers/', blank=True, null=True)

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = "Site Ayarı"
        verbose_name_plural = "Site Ayarları"


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class StaticPage(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    content = RichTextUploadingField()  # CKEditor desteği varsa
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('static_page', kwargs={'slug': self.slug})
