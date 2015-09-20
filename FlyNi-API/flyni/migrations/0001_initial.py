# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_scraper', '0008_auto_20150920_0254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fly',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('create_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('line', models.CharField(max_length=50)),
                ('fly_number', models.IntegerField()),
                ('origin', models.CharField(max_length=50)),
                ('hour', models.TimeField()),
                ('status', models.CharField(max_length=50)),
                ('checker_runtime', models.ForeignKey(null=True, blank=True, to='dynamic_scraper.SchedulerRuntime', on_delete=django.db.models.deletion.SET_NULL)),
                ('fly', models.ForeignKey(to='flyni.Fly')),
            ],
            options={
                'verbose_name_plural': 'Flys',
                'verbose_name': 'Fly',
            },
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('scraper', models.ForeignKey(null=True, blank=True, to='dynamic_scraper.Scraper', on_delete=django.db.models.deletion.SET_NULL)),
                ('scraper_runtime', models.ForeignKey(null=True, blank=True, to='dynamic_scraper.SchedulerRuntime', on_delete=django.db.models.deletion.SET_NULL)),
            ],
            options={
                'verbose_name_plural': 'Websites',
                'verbose_name': 'Website',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='website',
            field=models.ForeignKey(to='flyni.Website'),
        ),
    ]
