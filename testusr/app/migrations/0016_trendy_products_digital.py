# Generated by Django 4.2 on 2023-06-12 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_customer_order_orderitem_shippngaddress_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trendy_products',
            name='digital',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
