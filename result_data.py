import requests
from bs4 import BeautifulSoup

# URL of the webpage containing the element you want to scrape
url = "https://www.espncricinfo.com/series/indian-premier-league-2007-08-313494/match-schedule-fixtures-and-results"


# Send a GET request to the webpage
response = requests.get(url)

# Parse the HTML content of the webpage
soup = BeautifulSoup(response.text, 'html.parser')

data = soup.find('div', class_="ds-mb-4")

team1_div = data.find('div', class_="ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-my-1")

team1_div_nested = data.find('div', class_="ds-flex ds-items-center ds-min-w-0 ds-mr-1")
team_1_title = team1_div_nested.get('title')
team_1_score_div = data.find('div', class_="ds-text-compact-s ds-text-typo ds-text-right ds-whitespace-nowrap")
team_1_score = team_1_score_div.find('strong').text.split('/')[0]
print('team1_title', team_1_title)
print('team1_score', team_1_score)

team_2_div = data.find('div', class_="ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-opacity-50 ds-my-1")
team2_div_nested = team_2_div.find('div', class_="ds-flex ds-items-center ds-min-w-0 ds-mr-1")
team_2_title = team2_div_nested.get('title')
team_2_score = team_2_div.find('strong').text
print('title', team_2_title)
print('score', team_2_score)


