# Generated by Django 2.2.3 on 2019-08-05 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_news_code2'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='photo2',
            field=models.ImageField(blank=True, default='', upload_to='app/photos', verbose_name='Дополнительная фотография 1'),
        ),
        migrations.AddField(
            model_name='news',
            name='photo3',
            field=models.ImageField(blank=True, default='', upload_to='app/photos', verbose_name='Дополнительная фотография 2'),
        ),
    ]
