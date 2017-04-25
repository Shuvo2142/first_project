# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellingcarts', '0003_sellingcart_items'),
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
    ]
