from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField


class CustomUser(AbstractUser):
    """
    Model of client-customuser DB table.

    This model needs for custom authentication.
    """
    username = models.CharField(max_length=64, blank=True, null=True)
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)


class Client(models.Model):
    """
    Model of client-client DB table.

    user_id (user class attribute) field here
    is pk of client-customuser DB table.
    """
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
    photo = ResizedImageField(
        upload_to='uploads/',
        blank=True,
        size=[600, 600],
    )
