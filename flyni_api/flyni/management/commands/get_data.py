# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError

from optparse import make_option

from ...scraper import Scrap


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (make_option(
        '--url',
        action='store',
        dest='url',
        help='Subject of the email'),)

    def handle(self, *args, **options):
        #try:
    	Scrap(options.get('url'))
        #except:
        	# raise CommandError('Broken does not exist')
