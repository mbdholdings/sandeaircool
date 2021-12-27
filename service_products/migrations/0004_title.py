# Generated by Django 3.2.10 on 2021-12-26 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_products', '0003_auto_20211226_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'title',
                'verbose_name_plural': 'title',
            },
        ),
    ]
