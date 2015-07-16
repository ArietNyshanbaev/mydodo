# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_mail_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='category',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'\xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f'),
            preserve_default=True,
        ),
    ]
