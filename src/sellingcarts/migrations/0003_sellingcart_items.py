# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20170423_0913'),
        ('sellingcarts', '0002_auto_20170424_0655'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellingcart',
            name='items',
            field=models.ManyToManyField(through='sellingcarts.SellingCartItem', to='products.Product'),
        ),
    ]
