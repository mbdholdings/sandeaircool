from tinymce.models import HTMLField
from django.db import models
from embed_video.fields import EmbedVideoField


class Ceo(models.Model):
    title = models.CharField(max_length=50)
    content_one = models.TextField(max_length=400, blank=True)
    content_two = models.TextField(max_length=400, blank=True)
    content_three = models.TextField(max_length=400, blank=True)
    content_four = models.TextField(max_length=400, blank=True)

    image = models.ImageField(upload_to='about/')


    class Meta:
        verbose_name = 'ceo'
        verbose_name_plural = 'ceo'

    def __str__(self):
        return self.title

class AboutUs(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    class Meta:
        verbose_name = 'about us'
        verbose_name_plural = 'about us'

    def __str__(self):
        return self.title


class Media(models.Model): 
    heading = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    

    class Meta:
        verbose_name = 'text'
        verbose_name_plural = 'text'

    def __str__(self):
        return self.heading

class Team(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    bio = models.TextField()
    image = models.ImageField(upload_to='about/')


    class Meta:
        verbose_name = 'team'
        verbose_name_plural = 'team'

    def __str__(self):
        return self.name

