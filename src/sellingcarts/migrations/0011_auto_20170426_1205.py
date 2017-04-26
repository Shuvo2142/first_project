# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellingcarts', '0010_auto_20170426_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellingcartitem',
            name='line_item_total',
            field=models.DecimalField(decimal_places=2, null=True, max_digits=20),
        ),
    ]
