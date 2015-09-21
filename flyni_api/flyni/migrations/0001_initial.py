# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fly',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('line', models.CharField(max_length=50)),
                ('fly_number', models.IntegerField()),
                ('origin', models.CharField(max_length=50)),
                ('hour', models.TimeField()),
                ('status', models.CharField(max_length=50)),
                ('fly', models.ForeignKey(to='flyni.Fly')),
            ],
            options={
                'verbose_name': 'Fly',
                'verbose_name_plural': 'Flys',
            },
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name': 'Website',
                'verbose_name_plural': 'Websites',
            },
        ),
        migrations.AddField(
            model_name='fly',
            name='website',
            field=models.ForeignKey(to='flyni.Website'),
        ),
    ]
