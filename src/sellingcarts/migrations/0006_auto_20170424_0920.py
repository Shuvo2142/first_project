# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellingcarts', '0005_auto_20170424_0900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellingcart',
            name='items',
        ),
        migrations.RemoveField(
            model_name='sellingcartitem',
            name='cart',
        ),
        migrations.AlterField(
            model_name='sellingcart',
            name='seller',
            field=models.ForeignKey(to='sellers.SellerAccount', blank=True, null=True),
        ),
    ]
