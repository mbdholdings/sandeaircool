# Generated by Django 3.2.10 on 2021-12-26 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_products', '0004_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicefour',
            name='description',
        ),
        migrations.RemoveField(
            model_name='servicethree',
            name='description',
        ),
    ]
