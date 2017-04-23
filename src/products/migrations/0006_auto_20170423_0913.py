# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='default',
        ),
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ForeignKey(to='products.Category', default=1),
            preserve_default=False,
        ),
    ]
