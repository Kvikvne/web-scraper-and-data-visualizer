import plotly.express as px
import pandas as pd
from run_spiders import RunSpiders as scrape

def steamapp(): 
    scrape.main()

    top_file = 'steamcrawl/data/top_games.csv'
    trending_file = 'steamcrawl/data/trending_games.csv'
    record_file = 'steamcrawl/data/record_games.csv'

    # create dataframe
    df_top = pd.read_csv(top_file)
    df_trending = pd.read_csv(trending_file)
    df_record = pd.read_csv(record_file)

    # gen graph
    top_games_plot = px.bar(df_top, 
    x="name", 
    y="current_players", 
    title="Top Games (current players)", 
    text='current_players', 
    color="hours_played", 
    labels={'hours_played': 'Hours played all time', 'current_players':'Players Online', 'name':'Game'})

    top_games_plot.show()

    trending_plot = px.bar(df_trending, 
    x="trending_name", 
    y="current_players(trending)", 
    title="Trending Games", 
    text='24_hour_change', 
    color="24_hour_change", 
    labels={'24_hour_change': 'Percent change', 'trending_name':'Game', 'current_players(trending)':'Players Online'})

    trending_plot.show()

    record_plot = px.bar(df_record, 
    x="record_name", 
    y="record_peak_players", 
    title="Peak Player Records", 
    text='record_peak_players', 
    color='Date_acheived', 
    labels={'record_name':'Game', 'record_peak_players': 'Total peak players', 'Date_acheived':'Date acheived'})

    record_plot.show()
steamapp()