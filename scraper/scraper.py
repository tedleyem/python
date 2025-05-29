#!/bin/python3 
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# source links
url = 'https://www.basketball-reference.com/players/j/jamesle01.html'
browser = webdriver.Firefox()
browser.get(url)

player_comp_source = 'https://www.landofbasketball.com/player_comparison.htm'
player_top_pts_source = 'https://www.landofbasketball.com/nba_players_stats/top_pts/lebron_james.htm'
year_by_year_source = 'https://www.landofbasketball.com/yearbyyear/2023_2024_teams.htm'


# fetch html data
page = requests.get(url)

# create object
soup = BeautifulSoup(page.content)

# grab all table cells with td tag
cells = soup.findAll('td')

rows = soup.findAll('tf')
nrows = len(rows)
for i in range(1,nrows):
        # skip the first row which wont have datat (header)
        row_cells = rows[i].findAll('td')
        # create start time
        start_time = row_cells[0].get_text()
        # if I want the home team, I access the second cell
        home_team = row_cells[1].get_text()

# selenium browser find element by string
player_link = browser.find_element_by_link_text('Lebron James')
player_link.click()

def scraper_test():
    soup = BeautifulSoup(broswer.page_source, 'html')
    rows = soup.findAll('tr',{'class':"Table_TR Table_TR--sm Tables_even"})
    pars = rows[0].findAll('span',{'class':'Scorecard_Score br-1'})
    scores = rows[0].findAll('td',{'class':'Table_TD'})
    pars_we_want = [cells.get_text() for cells in pars]
    scores_we_want = [cells.get_text() for cells in scores]

def main():
    scraper_test()

if __name__ == '__main__':
    main()