# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20170423_0913'),
        ('sellingcarts', '0006_auto_20170424_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellingcart',
            name='items',
            field=models.ManyToManyField(through='sellingcarts.SellingCartItem', to='products.Product'),
        ),
        migrations.AddField(
            model_name='sellingcartitem',
            name='cart',
            field=models.ForeignKey(to='sellingcarts.SellingCart', default=1),
            preserve_default=False,
        ),
    ]
