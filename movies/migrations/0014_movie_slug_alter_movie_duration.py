# Generated by Django 4.0 on 2022-01-27 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0013_alter_movie_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.CharField(max_length=200),
        ),
    ]
