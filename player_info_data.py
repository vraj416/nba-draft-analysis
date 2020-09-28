import pickle
import pandas as pd 

df = pd.read_pickle('player_info.pickle')

print(df.columns)