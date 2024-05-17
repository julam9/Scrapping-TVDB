from dotenv import load_dotenv 
import tvdb_v4_official 
import pandas as pd
import os

load_dotenv()

# api key 
my_APIKEY = os.getenv("API_KEY")
tvdb = tvdb_v4_official.TVDB(my_APIKEY)

series1 = tvdb.get_series(121361)
print(pd.json_normalize(series1).T)