# Generated by Django 3.2.9 on 2021-12-13 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Impression',
            new_name='Intro',
        ),
        migrations.AlterModelOptions(
            name='intro',
            options={'verbose_name': 'Intro', 'verbose_name_plural': 'Intro'},
        ),
    ]
