# Generated by Django 5.1.2 on 2024-10-23 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chairsapp', '0004_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.AddField(
            model_name='order',
            name='card_number',
            field=models.CharField(default='0000000000000000', max_length=16),
        ),
        migrations.AddField(
            model_name='order',
            name='customer_name',
            field=models.CharField(default='Unknown Customer', max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.TextField(default='Unknown Address'),
        ),
    ]
