from tinymce.models import HTMLField
from django.db import models


class HeadingOne(models.Model):
    heading = models.CharField(max_length=100)
    description = models.TextField()


    class Meta:
        verbose_name = 'Heading_one'
        verbose_name_plural = 'Heading_one'

    def __str__(self):
        return self.heading 

class MidImage(models.Model):
    heading = models.CharField(max_length=100)
    content_one = models.TextField(max_length=400, blank=True)
    image = models.ImageField(upload_to='home_page/', blank=True)

    class Meta:
        verbose_name = 'Mid_image'
        verbose_name_plural = 'Mid_image'

    def __str__(self):
        return self.heading  


class HeadingTwo(models.Model):
    heading = models.CharField(max_length=100)
    description = models.TextField(max_length=400, blank=True)
    image = models.ImageField(upload_to='home_page/', blank=True)


    class Meta:
        verbose_name = 'Heading_two'
        verbose_name_plural = 'Heading_two'

    def __str__(self):
        return self.heading         

class HeadingThree(models.Model):
    customer_name = models.CharField(max_length=100)
    testimony = models.TextField(max_length=400, blank=True)

    class Meta:
        verbose_name = 'Heading_three'
        verbose_name_plural = 'Heading_three'

    def __str__(self):
        return self.customer_name

class Slider(models.Model):
    description = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='home_page/')
    text_one = models.TextField(max_length=200, blank=True)
    text_two = models.TextField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'slider'
        verbose_name_plural = 'sliders'

    def __str__(self):
        return self.description

class Intro(models.Model): 
    description = models.CharField(max_length=100)
    content_one = models.TextField(max_length=400, blank=True)
    content_two = models.TextField(max_length=400, blank=True)
    content_three = models.TextField(max_length=400, blank=True)
    image_one = models.ImageField(upload_to='home_page/', blank=True)
    image_two = models.ImageField(upload_to='home_page/', blank=True)


    class Meta:
        verbose_name = 'Intro'
        verbose_name_plural = 'Intro'

    def __str__(self):
        return self.description

class WelcomeWords(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='home_page/')

    class Meta:
        verbose_name = 'welcome word'
        verbose_name_plural = 'welcome words'

    def __str__(self):
        return self.title


class MissionVision(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='home_page/', blank=True)


    class Meta:
        verbose_name = 'mission vision'
        verbose_name_plural = 'mission vision'

    def __str__(self):
        return self.title       







