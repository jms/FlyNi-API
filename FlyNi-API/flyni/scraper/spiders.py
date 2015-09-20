# -*- coding: utf-8 -*-
from dynamic_scraper.spiders.django_spider import DjangoSpider
from .models import Website, Fly, Item, ArticleItem


class ArticleSpider(DjangoSpider):
    
    name = 'fly_spider'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(NewsWebsite, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = Item
        self.scraped_obj_item_class = ArticleItem
        super(ArticleSpider, self).__init__(self, *args, **kwargs)