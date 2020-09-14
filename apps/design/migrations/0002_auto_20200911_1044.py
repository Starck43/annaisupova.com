# Generated by Django 3.1 on 2020-09-11 10:44

import design.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Ярлык'),
        ),
        migrations.AlterField(
            model_name='project',
            name='cover',
            field=models.ImageField(storage=design.models.MediaFileStorage(), upload_to='portfolio/', verbose_name='Обложка'),
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(max_length=150, unique=True, verbose_name='Ярлык'),
        ),
    ]
