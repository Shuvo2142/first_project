# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0001_initial'),
        ('products', '0006_auto_20170423_0913'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('items', models.ForeignKey(to='products.Product')),
                ('seller', models.ForeignKey(to='sellers.SellerAccount')),
            ],
        ),
    ]
