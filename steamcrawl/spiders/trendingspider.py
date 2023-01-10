import scrapy
from datetime import datetime

now = datetime.now()
date_time = now.year, now.month, now.day, now.hour, now.minute


class TrendingspiderSpider(scrapy.Spider):
    name = 'trendingspider'
    allowed_domains = ['steamcharts.com']
    start_urls = ['https://steamcharts.com/']

    custom_settings = {
        'FEEDS': {'steamcrawl/data/trending_games.csv': {'format': 'csv', "overwrite": True}}
    }

    def parse(self, response):
        yield response.follow("https://steamcharts.com/", callback=self.parse_trending, dont_filter=True)

     # Gather data from top 5 trending games on steam
    def parse_trending(self, response):

        # get trending titles, strip html and add to list.
        trending_name = response.css('table.trending a::text').getall() 
        trending_name_list = []
        
        for x in trending_name:
            clean_trending = x.strip()
            trending_name_list.append(clean_trending)
        
        # get user change percentage and append to a list
        day_change = response.css('table.trending .gain ::text').getall()
        day_change_list = []
        
        for x in day_change:
            day_change_list.append(x)
        
        # get current players and append to list.
        current_tranding_players = response.css('table.trending .num ::text').getall()
        trending_players_list = []

        for x in current_tranding_players:
            trending_players_list.append(x)
        
        dict_list_trend = []

        # yield gathered data into a dictionary
        for x in range(len(trending_name_list)):
            trending = yield {
                "trending_name": trending_name_list[x],
                "24_hour_change": day_change_list[x],
                "current_players(trending)": trending_players_list[x],
                "date_time(trending)": now
            }
