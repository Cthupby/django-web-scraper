import hashlib
import json
import re
import scrapy
import time
import datetime

from models import ExtractedNews


class WebScraperSpider(scrapy.Spider):
    name = 'web_scraper'

    def start_requests(self):
        yield scrapy.Request(
            url="https://78.ru/news",
            callback=self.parse,
            meta={"playwright": True},
        )

    def parse(self, response):
        urls = [response.xpath('//a[contains(@class, "news-feed-timeline-item")]/@href').get()]
        for path in urls:
            url = f"https://78.ru/{path}"
            news = ExtractedNews.objects.filter(url=url)
            if not news:
                yield scrapy.Request(
                    url=url,
                    callback=self.parse_subpage,
                    meta={"playwright": True},
                )
        return {"url": response.url}

    def parse_subpage(self, response):
        url = str(response.url)
        title = response.xpath('//h1[contains(@class, "heading")]/text()').get()
        agregate_date = re.search('news/(.*)/', url).group(1)
        create = time.mktime(datetime.datetime.strptime(agregate_date, "%Y-%m-%d").timetuple())
        text = response.xpath('//div[contains(@class, "news__inner")]').get()
        news_id = hashlib.md5(url.encode())
        news = ExtractedNews.objects.create(
            news_id=str(news_id),
            url=url,
            title=title,
            created_date=str(create),
            text=text,
        )
        return {"url": response.url}
