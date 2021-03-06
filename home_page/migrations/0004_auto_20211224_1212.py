# Generated by Django 3.2.10 on 2021-12-24 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0003_auto_20211213_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='MidPageImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('content_one', models.TextField(blank=True, max_length=400)),
                ('image', models.ImageField(blank=True, upload_to='home_page/')),
            ],
            options={
                'verbose_name': 'Mid_page_image',
                'verbose_name_plural': 'Mid_page_image',
            },
        ),
        migrations.RenameField(
            model_name='headingthree',
            old_name='heading',
            new_name='Customer_name',
        ),
        migrations.RemoveField(
            model_name='headingthree',
            name='description',
        ),
        migrations.AddField(
            model_name='headingthree',
            name='testimony',
            field=models.TextField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='headingtwo',
            name='image',
            field=models.ImageField(blank=True, upload_to='home_page/'),
        ),
        migrations.AlterField(
            model_name='headingtwo',
            name='description',
            field=models.TextField(blank=True, max_length=400),
        ),
    ]
