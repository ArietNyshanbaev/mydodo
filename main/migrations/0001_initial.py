# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f')),
                ('icon', models.ImageField(upload_to=b'', null=True, verbose_name=b'\xd0\xb8\xd0\xba\xd0\xbe\xd0\xbd\xd0\xba\xd0\xb0', blank=True)),
            ],
            options={
                'verbose_name': '\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xd0\xb8\xd0\xbc\xd1\x8f \xd0\xbe\xd1\x82\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8f')),
                ('email', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xd1\x82\xd0\xb5\xd0\xbc\xd0\xb0')),
                ('body', models.CharField(max_length=1000, verbose_name=b'\xd1\x81\xd0\xbe\xd0\xbe\xd0\xb1\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd1\x82\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
            ],
            options={
                'verbose_name': '\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xd0\xb8\xd0\xbc\xd1\x8f \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd1\x87\xd0\xb8\xd0\xba\xd0\xb0')),
                ('telephone', models.CharField(max_length=100, verbose_name=b'\xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd\xd0\xb0')),
                ('date_of_order', models.CharField(default=b'\xd0\xbd\xd0\xb5 \xd1\x83\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0\xd0\xbd', max_length=200, verbose_name=b'\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb8 \xd0\xb2\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xb8\xd1\x81\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0')),
                ('job_description', models.TextField(default=b'\xd0\xbd\xd0\xb5 \xd1\x83\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0\xd0\xbd', verbose_name=b'\xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0')),
                ('address', models.CharField(default=b'\xd0\xbd\xd0\xb5 \xd1\x83\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0\xd0\xbd', max_length=400, verbose_name=b'\xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd\xd0\xb0')),
                ('date_of_submition', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb8 \xd0\xb2\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xbf\xd0\xbe\xd1\x81\xd1\x82\xd1\x83\xd0\xbf\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xb7\xd0\xb0\xd1\x8f\xd0\xb2\xd0\xba\xd0\xb8')),
                ('category', models.ForeignKey(verbose_name=b'\xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', to='main.Category')),
            ],
            options={
                'verbose_name': '\u0437\u0430\u044f\u0432\u043a\u0430',
                'verbose_name_plural': '\u0437\u0430\u044f\u0432\u043a\u0438',
            },
            bases=(models.Model,),
        ),
    ]
