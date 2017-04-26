# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellingcarts', '0007_auto_20170424_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellingcartitem',
            name='line_item_total',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=20),
            preserve_default=False,
        ),
    ]
