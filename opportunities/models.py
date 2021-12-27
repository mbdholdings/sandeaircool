from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
from tinymce.models import HTMLField
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Opportunity(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    video = EmbedVideoField(blank=True, null=True)  # same like models.URLField()
    image = models.ImageField(blank=True, null=True)
    previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
    

    class Meta:
        verbose_name = 'opportunity'
        verbose_name_plural = 'opportunities'


    def __str__(self):
        return self.title


    def get_update_url(self):
        return reverse('opportunity-update', kwargs={
            'id': self.id
        })

    def get_delete_url(self):
        return reverse('opportunity-delete', kwargs={
            'id': self.id
        })    

    def get_absolute_url(self):
        return reverse('opportunity-detail', kwargs={
            'id': self.id
        })









