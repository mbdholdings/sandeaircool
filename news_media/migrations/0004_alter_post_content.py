# Generated by Django 3.2.10 on 2021-12-24 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_media', '0003_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
    ]
