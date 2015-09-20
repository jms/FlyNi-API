# -*- coding: utf-8 -*-
from dynamic_scraper.spiders.django_checker import DjangoChecker
from .models import Item


class ArticleChecker(DjangoChecker):
    
    name = 'fly_checker'
    
    def __init__(self, *args, **kwargs):
        self._set_ref_object(Article, **kwargs)
        self.scraper = self.ref_object.news_website.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.checker_runtime
        super(ArticleChecker, self).__init__(self, *args, **kwargs)