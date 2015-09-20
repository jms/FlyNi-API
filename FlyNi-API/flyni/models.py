# -*- coding: utf-8 -*-
from django.db import models
from dynamic_scraper.models import Scraper, SchedulerRuntime
from scrapy_djangoitem import DjangoItem


class Website(models.Model):
    """
    """
    name = models.CharField(max_length=200)
    url = models.URLField()
    scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)
    scraper_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Website'
        verbose_name_plural = 'Websites'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return "%s" % self.__unicode__()


class Fly(models.Model):
    """
    """
    create_date = models.DateField()

class Item(models.Model):
    """
    """
    website = models.ForeignKey(Website)
    fly = models.ForeignKey(Fly)
    line = models.CharField(max_length=50)
    fly_number = models.IntegerField()
    origin = models.CharField(max_length=50)
    hour = models.TimeField()
    status = models.CharField(max_length=50)
    checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Fly'
        verbose_name_plural = 'Flys'

    def __unicode__(self):
        return self.line

    def __str__(self):
        return "%s" % self.__unicode__()


class ArticleItem(DjangoItem):
    django_model = Fly
    