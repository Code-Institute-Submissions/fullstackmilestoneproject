# Generated by Django 2.2.3 on 2019-08-10 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0004_auto_20190810_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shoppingcart.UserCoupon'),
        ),
    ]