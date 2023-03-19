from django.db import models
from django.conf import settings
from django.contrib.auth.models import User



# def client_dir_path(instance, filename):
#     """file will be uploaded to MEDIA_ROOT / client_<id>/<filename>"""
#     return f'client_{instance.client.id}/{filename}'



class Client(models.Model):
    """Client db"""
    name = models.CharField(max_length=32, blank=True)
    surname = models.CharField(max_length=64, blank=True)
    SEX_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('U', 'Prefer not to disclose'),
    )
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        default='U',
        blank=True,
        )
    birth_date = models.DateField(blank=True)
    # photo = models.ForeignKey(
    #     to='Photo',
    #     on_delete=models.PROTECT,
    #     blank=True,
    #     null=True,
    # )

    def __str__(self):
        return self.name

# class Photo(models.Model):
#     '''Separate db for photos'''
#     photo = models.ImageField(upload_to=client_dir_path)