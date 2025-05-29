import nba_history
import pandas 

from nba_history import player_data, team_data 

#def scrape_draft_data():
#
#def scrape_player_salaries():
#
#def scrape_player_total_stats():
#
#def scrape_player_per_game_stats():
#
#def scrape_player_shooting_stats():
#
#def scrape_all_stars():
#
#def scrape_nba_team_records():

# scrape 2013 NBA draft picks
df = player_data.scrape_draft_data(start_year = 2013,
	end_year = 2013,
	export = False)
	
print(df.head())
