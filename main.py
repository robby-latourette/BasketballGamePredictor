import pandas as pd
#import sportsreference.nba as nba
#from sportsreference.nba import boxscore
#from sportsreference.nba.boxscore import Boxscore
#from datetime import datetime
import requests
import os
import shutil
years = list(range(1991,2022))
url_start = "https://www.basketball-reference.com/awards/awards_{}.html"

for year in years:
    url = url_start.format(year)
    
    data = requests.get(url)
    
    with open("mvp/{}.html".format(year), "w+") as f:
        f.write(data.text)
from bs4 import BeautifulSoup
with open("mvp/1991.html") as f:
    page = f.read()
    
soup = BeautifulSoup(page, 'html.parser')
soup.find('tr', class_="over_header").decompose()
mvp_table = soup.find_all(id="mvp")[0]

mvp_1991 = pd.read_html(str(mvp_table))[0]
mvp_1991.head(1)
mvp_1991["Year"] = 1991
mvp_1991.head()

