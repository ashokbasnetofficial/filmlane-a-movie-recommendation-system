# Generated by Django 4.0 on 2021-12-10 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('trailer', models.URLField(null=True)),
                ('rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1)),
                ('genre', models.CharField(choices=[('action', 'action'), ('comedy', 'comedy'), ('drama', 'drama'), ('thriller', 'thriller'), ('adventure', 'adventure')], max_length=30)),
            ],
        ),
    ]
