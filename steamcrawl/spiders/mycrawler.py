import scrapy
from datetime import datetime


now = datetime.now()
date_time = now.year, now.month, now.day, now.hour, now.minute

class MycrawlerSpider(scrapy.Spider):
    name = 'mycrawler'
    allowed_domains = ['steamcharts.com']
    start_urls = ['https://steamcharts.com/']

    custom_settings = {
        'FEEDS': {'steamcrawl/data/top_games.csv': {'format': 'csv', "overwrite": True}}
    }
    

    def parse(self, response):
        top_link = response.css('h2 a::attr(href)').get()
        full_link = f'https://steamcharts.com{top_link}'
       
        yield response.follow(full_link, callback=self.parse_top_games, dont_filter=True) 

    def parse_top_games(self, response):
        game_names = response.css('table.common-table a::text').getall()
        game_names_list = []
        
        for x in game_names:
            game_names_list.append(x.strip())

        current_players = response.css('table.common-table .num').getall()
        current_players_list = []
        
        for x in current_players:
            if '<td class="num">' in x:
                clean_players = x.strip('<td class="num"> </td>')
                current_players_list.append(clean_players)

        peak_players = response.css('table.common-table .peak-concurrent').getall()
        peak_players_list = []

        for x in peak_players:
            clean_peak = x.strip('<td class="num period-col peak-concurrent"> </td>')
            peak_players_list.append(clean_peak)
        
        hours = response.css('table.common-table .player-hours').getall()
        hours_list = []

        for x in hours:
            clean_hours = x.strip('<td class="num period-col player-hours"> </td>')
            hours_list.append(clean_hours)
        
        # yield gathered data into a dictionary
        for x in range(len(game_names_list)):
            yield {
                "name": game_names_list[x],
                "current_players": current_players_list[x],
                "peak_players": peak_players_list[x],
                "hours_played": hours_list[x],
                "date_time": now
            }

    
            
