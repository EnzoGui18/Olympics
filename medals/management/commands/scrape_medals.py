from django.core.management.base import BaseCommand
from medals.scraper import scrape_medals

class Command(BaseCommand):
    help = 'Scrape Olympic medals data and populate the database'

    def handle(self, *args, **kwargs):
        scrape_medals()
        self.stdout.write(self.style.SUCCESS('Successfully scraped data and populated the database'))
