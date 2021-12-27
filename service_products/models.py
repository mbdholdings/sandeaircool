from tinymce.models import HTMLField
from django.db import models

class Sliding(models.Model):
    description_big = models.CharField(max_length=100, blank=True)
    description_small = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='home_page/')

    class Meta:
        verbose_name = 'slider'
        verbose_name_plural = 'sliders'

    def __str__(self):
        return self.description_big


class Preview(models.Model): 
    description = models.CharField(max_length=100, blank=True)
    content = models.TextField(max_length=500, blank=True)


    class Meta:
        verbose_name = 'preview'
        verbose_name_plural = 'preview'

    def __str__(self):
        return self.description

class Impression(models.Model): 
    description = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='home_page/')

    class Meta:
        verbose_name = 'impression'
        verbose_name_plural = 'impression'

    def __str__(self):
        return self.description


class ServiceOne(models.Model): 
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    content = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='service_products/')
    

    class Meta:
        verbose_name = 'service one'
        verbose_name_plural = 'service one'

    def __str__(self):
        return self.title

class ServiceTwo(models.Model): 
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='service_products/')
    

    class Meta:
        verbose_name = 'service two'
        verbose_name_plural = 'service two'

    def __str__(self):
        return self.title


class ServiceThree(models.Model): 
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='service_products/')
    

    class Meta:
        verbose_name = 'service three'
        verbose_name_plural = 'service three'

    def __str__(self):
        return self.title


class Title(models.Model): 
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, blank=True)
    

    class Meta:
        verbose_name = 'title'
        verbose_name_plural = 'title'

    def __str__(self):
        return self.title


class ServiceFour(models.Model): 
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='service_products/')
    

    class Meta:
        verbose_name = 'service four'
        verbose_name_plural = 'service four'

    def __str__(self):
        return self.title

class ServiceFive(models.Model): 
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, blank=True)
    content = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='service_products/')
    

    class Meta:
        verbose_name = 'service five'
        verbose_name_plural = 'service five'

    def __str__(self):
        return self.title

class ServiceSix(models.Model): 
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, blank=True)
    content = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='service_products/')
    

    class Meta:
        verbose_name = 'service six'
        verbose_name_plural = 'service six'

    def __str__(self):
        return self.title       


class TitleTwo(models.Model): 
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, blank=True)

    class Meta:
        verbose_name = 'title two'
        verbose_name_plural = 'title two'

    def __str__(self):
        return self.title


class ServiceSeven(models.Model): 
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='service_products/')
    

    class Meta:
        verbose_name = 'service seven'
        verbose_name_plural = 'service seven'

    def __str__(self):
        return self.title  