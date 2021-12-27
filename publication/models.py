from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Publication(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='publication/', blank=True)
    upload_book = models.FileField(upload_to='publication/', blank=True)
    previous_library = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_library = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title


    def get_update_url(self):
        return reverse('publication-update', kwargs={
            'id': self.id
        })

    def get_delete_url(self):
        return reverse('publication-delete', kwargs={
            'id': self.id
        })  

    
    def get_absolute_url(self):
        return reverse('publication-detail', kwargs={
            'id': self.id
        })


      
