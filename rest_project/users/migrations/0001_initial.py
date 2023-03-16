# Generated by Django 4.1.7 on 2023-03-16 17:26

from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=users.models.user_dir_path)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=64)),
                ('sex', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('U', 'Prefer not to disclose')], max_length=1)),
                ('birth_date', models.DateField()),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.photo')),
            ],
        ),
    ]