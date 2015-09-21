# -*- coding: utf-8 -*-
from django.db import models



class Website(models.Model):
    """
    """
    name = models.CharField(max_length=200)
    url = models.URLField()

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
    website = models.ForeignKey(Website)

class Item(models.Model):
    """
    """
    fly = models.ForeignKey(Fly)
    line = models.CharField(max_length=50)
    fly_number = models.IntegerField()
    origin = models.CharField(max_length=50)
    hour = models.TimeField()
    status = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Fly'
        verbose_name_plural = 'Flys'

    def __unicode__(self):
        return self.line

    def __str__(self):
        return "%s" % self.__unicode__()
