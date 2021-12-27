from django.db import models

class GallerySlider(models.Model): 
    description = models.CharField(max_length=100, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    image_gallery = models.ImageField(upload_to='gallery/')


    class Meta:
        verbose_name = 'gallery_slider'
        verbose_name_plural = 'gallery_sliders'

    def __str__(self):
        return self.description


class Gallery(models.Model): 
    description = models.CharField(max_length=100, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    image_gallery = models.ImageField(upload_to='gallery/')


    class Meta:
        verbose_name = 'gallery'
        verbose_name_plural = 'galleries'

    def __str__(self):
        return self.description

class GalleryExtra(models.Model): 
    description = models.CharField(max_length=100, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    image_gallery = models.ImageField(upload_to='gallery/')


    class Meta:
        verbose_name = 'gallery_extra'
        verbose_name_plural = 'gallery_extra'

    def __str__(self):
        return self.description