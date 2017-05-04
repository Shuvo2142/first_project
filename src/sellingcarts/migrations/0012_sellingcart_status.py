# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellingcarts', '0011_auto_20170426_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellingcart',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
