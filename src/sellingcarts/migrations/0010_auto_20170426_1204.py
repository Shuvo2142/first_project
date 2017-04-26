# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellingcarts', '0009_sellingcart_subtotal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellingcart',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, null=True, max_digits=20),
        ),
    ]
