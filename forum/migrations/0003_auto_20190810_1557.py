# Generated by Django 2.2.3 on 2019-08-10 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_post_likes_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes_total',
            field=models.IntegerField(default=0),
        ),
    ]