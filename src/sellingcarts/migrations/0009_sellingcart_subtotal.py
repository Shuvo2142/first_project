# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellingcarts', '0008_sellingcartitem_line_item_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellingcart',
            name='subtotal',
            field=models.DecimalField(default=0.0, decimal_places=2, max_digits=20),
            preserve_default=False,
        ),
    ]
