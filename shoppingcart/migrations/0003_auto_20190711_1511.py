# Generated by Django 2.2.3 on 2019-07-11 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0002_billingaddress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billingaddress',
            old_name='zip',
            new_name='zip_code',
        ),
        migrations.AddField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shoppingcart.BillingAddress'),
        ),
    ]