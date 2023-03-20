# Generated by Django 4.1.7 on 2023-03-20 18:11

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_alter_client_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=-1, scale=None, size=[600, 600], upload_to='uploads/'),
        ),
    ]
