# Generated by Django 4.0 on 2022-01-31 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0015_remove_movie_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='certificate',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='poster',
        ),
        migrations.AddField(
            model_name='movie',
            name='org_language',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tags',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
