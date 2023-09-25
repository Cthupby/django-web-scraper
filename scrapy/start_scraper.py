from web_scraper.spiders.web_scraper import WebScraperSpider
from scrapy.crawler import CrawlProcess


def main():
    process = CrawlerProcess()
    process.crawl(WebScraperSpider)
    process.start()


if __name__ == "__main__":
    main()
