# Generated by Django 2.2.3 on 2019-08-09 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes_total',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]