# Generated by Django 3.1.7 on 2021-05-04 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_cartoonpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelpost',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='Anime_img'),
        ),
    ]
