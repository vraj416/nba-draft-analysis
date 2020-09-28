import requests
import pandas as pd
import pickle

head = {'Host': 'stats.nba.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
'Accept': 'application/json, text/plain, /',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'x-nba-stats-origin': 'stats',
'x-nba-stats-token': 'true',
'Connection': 'keep-alive',
'Referer': 'https://stats.nba.com/',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache'}

url = 'https://stats.nba.com/stats/leaguedashplayerbiostats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&Season=2019-20&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='
response = requests.get(url, headers=head, timeout=5)

print("hello")

headers = response.json()['resultSets'][0]['headers']
rows = response.json()['resultSets'][0]['rowSet']

df_player_info = pd.DataFrame(rows, columns=headers)

df_player_info.to_pickle("player_info.pickle")

