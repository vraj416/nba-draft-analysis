import pickle
import pandas as pd 

df_player_info = pd.read_pickle('player_info.pickle')
print(df_player_info.head())
df_player_info= df_player_info[["PLAYER_ID", "PLAYER_NAME", "TEAM_ID", "TEAM_ABBREVIATION", "DRAFT_YEAR", "DRAFT_ROUND", "DRAFT_NUMBER"]]

df_player_info['DRAFT_NUMBER'].replace(['Undrafted'], "61", inplace=True)
df_player_info['DRAFT_ROUND'].replace(['Undrafted'], "3", inplace=True)
df_player_info.to_csv("player_info.csv")