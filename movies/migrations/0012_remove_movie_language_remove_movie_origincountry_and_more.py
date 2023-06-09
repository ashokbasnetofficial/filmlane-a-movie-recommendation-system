# Generated by Django 4.0 on 2022-01-25 09:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_movie_cast_movie_director_movie_duration_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='language',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='origincountry',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='writer',
        ),
        migrations.AddField(
            model_name='movie',
            name='certificate',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='tags',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='cast',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='releasedDate',
            field=models.IntegerField(default=2000, validators=[django.core.validators.MaxValueValidator(2021), django.core.validators.MinValueValidator(1950)]),
        ),
    ]
