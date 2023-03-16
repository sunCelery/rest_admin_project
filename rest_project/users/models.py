from django.db import models


def user_dir_path(instance, filename):
    '''file will be uploaded to MEDIA_ROOT / user_<id>/<filename>'''
    return f'user_{instance.user.id}/{filename}'


class User(models.Model):
    '''User class db'''
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=64)
    SEX_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('U', 'Prefer not to disclose'),
    )
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        )
    birth_date = models.DateField()
    photo = models.ForeignKey(
        to='Photo',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

class Photo(models.Model):
    '''Separate db for photos'''
    photo = models.ImageField(upload_to=user_dir_path)