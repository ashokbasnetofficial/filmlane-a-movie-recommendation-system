# Generated by Django 4.0 on 2021-12-13 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movie_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.CharField(max_length=2),
        ),
    ]
