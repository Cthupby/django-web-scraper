import time
from loguru import logger

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

#from web.lib.scraper import get_data


class Command(BaseCommand):
    help = "Start web scraper!"

    def handle(self, *args, **options):
        #get_data()
        logger.info("Web scraper was started!")
