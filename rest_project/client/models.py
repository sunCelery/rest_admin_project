from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser



def client_dir_path(instance, filename):
    """file will be uploaded to MEDIA_ROOT /client_<id>/<filename>"""
    return f'uploads/'
    # {instance.user.id}    {filename}


class CustomUser(AbstractUser):
    username = models.CharField(max_length=64, blank=True, null=True)
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)


class Client(models.Model):
    """Client db"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='profile')
    SEX_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('U', 'Prefer not to disclose'),
    )
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        default='U',
        blank='NULL',
        )
    birth_date = models.DateField(blank=True)
    photo = models.ImageField(
        upload_to='uploads/',
        blank=True,
    )



# class Photo(models.Model):
#     '''Separate db for photos'''
#     photo = models.ImageField(upload_to=client_dir_path)