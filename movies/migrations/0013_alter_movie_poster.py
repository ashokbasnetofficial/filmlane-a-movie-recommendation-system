# Generated by Django 4.0 on 2022-01-25 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_remove_movie_language_remove_movie_origincountry_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.CharField(max_length=500),
        ),
    ]
