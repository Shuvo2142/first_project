# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20170423_0913'),
        ('sellingcarts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellingCartItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('quantity', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='sellingcart',
            name='items',
        ),
        migrations.RemoveField(
            model_name='sellingcart',
            name='quantity',
        ),
        migrations.AddField(
            model_name='sellingcartitem',
            name='cart',
            field=models.ForeignKey(to='sellingcarts.SellingCart'),
        ),
        migrations.AddField(
            model_name='sellingcartitem',
            name='item',
            field=models.ForeignKey(to='products.Product'),
        ),
    ]
