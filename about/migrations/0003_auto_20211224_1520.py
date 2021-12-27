# Generated by Django 3.2.10 on 2021-12-24 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20211224_1428'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ceo',
            options={'verbose_name': 'ceo', 'verbose_name_plural': 'ceo'},
        ),
        migrations.RemoveField(
            model_name='ceo',
            name='content',
        ),
        migrations.AddField(
            model_name='ceo',
            name='content_one',
            field=models.TextField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='ceo',
            name='content_three',
            field=models.TextField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='ceo',
            name='content_two',
            field=models.TextField(blank=True, max_length=400),
        ),
    ]