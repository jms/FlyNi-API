# -*- coding: utf-8 -*-
from celery.task import task

from dynamic_scraper.utils.task_utils import TaskUtils
from .models import Website, Item

@task()
def run_spiders():
    t = TaskUtils()
    t.run_spiders(Website, 'scraper', 'scraper_runtime', 'fly_spider')
    
@task()
def run_checkers():
    t = TaskUtils()
    t.run_checkers(Item, 'news_website__scraper', 'checker_runtime', 'fly_checker')