import scrapy
from datetime import datetime

now = datetime.now()
date_time = now.year, now.month, now.day, now.hour, now.minute

class MyrecordscrawlerSpider(scrapy.Spider):
    name = 'myrecordscrawler'
    allowed_domains = ['steamcharts.com']
    start_urls = ['https://steamcharts.com/']

    custom_settings = {
        'FEEDS': {'steamcrawl/data/record_games.csv': {'format': 'csv', "overwrite": True}}
    }

    def parse(self, response):
        yield response.follow("https://steamcharts.com/", callback=self.top_records, dont_filter=True)
    
    def top_records(self, response):
        top_records = response.xpath('//*[@id="toppeaks"]/tbody/tr/td/a//text()').getall()
        top_records_list = []

        for x in top_records:
            clean_records = x.strip()
            top_records_list.append(clean_records)

        record_peak = response.xpath('//*[@id="toppeaks"]/tbody/tr/td[2]//text()').getall()  
        record_peak_list = []

        for x in record_peak:
            record_peak_list.append(x)

        record_date = response.xpath('//*[@id="toppeaks"]/tbody/tr/td[3]//text()').getall()
        record_date_list = []

        for x in record_date:
            clean_record_date = x.strip('T00:00:00Z')
            record_date_list.append(clean_record_date)

        for x in range(len(top_records_list)):
            yield {
                "record_name": top_records_list[x],
                "record_peak_players": record_peak_list[x],
                "Date_acheived": record_date_list[x]
            }
