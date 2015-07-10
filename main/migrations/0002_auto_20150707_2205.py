# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='category',
        ),
        migrations.RemoveField(
            model_name='order',
            name='job_description',
        ),
        migrations.AddField(
            model_name='order',
            name='value',
            field=models.CharField(default=b'\xd0\xbd\xd0\xb5 \xd1\x83\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0\xd0\xbd', max_length=400, verbose_name=b'\xd0\xbf\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default=b'\xd0\xbd\xd0\xb5 \xd1\x83\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0\xd0\xbd', max_length=400, verbose_name=b'\xd0\xb0\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81'),
            preserve_default=True,
        ),
    ]
