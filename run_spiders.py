from steamcrawl.spiders.mycrawler import MycrawlerSpider as top
from steamcrawl.spiders.myrecordscrawler import MyrecordscrawlerSpider as records
from steamcrawl.spiders.trendingspider import TrendingspiderSpider as trending
from scrapy.crawler import CrawlerProcess

class RunSpiders():
    def __init__(self) -> None:
        pass
    def main():
        process = CrawlerProcess()
        process.crawl(top)
        process.crawl(trending)
        process.crawl(records)
        process.start()

    
