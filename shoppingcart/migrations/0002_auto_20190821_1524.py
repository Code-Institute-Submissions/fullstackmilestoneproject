# Generated by Django 2.2.4 on 2019-08-21 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='use_default_billing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='use_default_shipping',
            field=models.BooleanField(default=False),
        ),
    ]
