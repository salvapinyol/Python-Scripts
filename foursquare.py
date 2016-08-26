#https://foursquare.com/v/salut-i-benzina/4fa65d0ce4b05483078fd4cd
#http://maps.google.com/?q=<lat>,<lng>
#https://googledrive.github.io/PyDrive/docs/_build/html/filemanagement.html
#https://github.com/gboeing/data-visualization/blob/master/location-history/foursquare-location-history.ipynb
#https://pypi.python.org/pypi/pyshorteners

import pandas as pd, numpy as np
import requests, json
from datetime import datetime as dt
# from pydrive.drive import GoogleDrive
# from pydrive.auth import GoogleAuth
# from mpl_toolkits.basemap import Basemap
from keys import foursquare_oauth_token 


# the json file will contain the entire downloaded check-ins data set
json_file = 'data/foursqure-checkins.json'

# the csv file will contain the cleaned data used for subsequent analysis
csv_file = 'data/foursquare-location-history.csv'

excel_file = 'data/foursquare-location-history.xlsx'
excel_file2 = 'data/foursquare-location-history-unique.xls'

# api endpoint to download your checkin history
url_template = 'https://api.foursquare.com/v2/users/self/checkins?limit=250&v=20160104&offset={}&oauth_token={}'

# you can only pull 250 records at a time from the api, so use offset to increment by 250 in a loop
offset = 0
data = []
while True:
    #print(offset, end=' ')
    response = requests.get(url_template.format(offset, foursquare_oauth_token))
    if len(response.json()['response']['checkins']['items']) == 0:
        break #whenever api returns no rows, offset value has exceeded total records so we're done
    data.append(response.json())
    offset += 250
# save the entire raw downloaded check-ins data set as json
with open(json_file, 'w') as f:
    f.write(json.dumps(data, indent=2))

# location_components is the list of pieces we're interested in pulling out of the dataset
location_components = ['city', 'state', 'country']
rows = []
for response in data:
    for item in response['response']['checkins']['items']:
        try:
            checkin = {}
            checkin['venue_name'] = item['venue']['name']
            checkin['created_at'] = item['createdAt']
            checkin['gmap'] = 'http://maps.google.com/?q={},{}' .format(item['venue']['location']['lat'],item['venue']['location']['lng'])
            
            if len(item['venue']['categories']) > 0:
                checkin['category'] = item['venue']['categories'][0]['name']
                
            for component in location_components:
                if component in item['venue']['location']:
                    checkin[component] = item['venue']['location'][component]
                else:
                    checkin[component] = np.nan
            checkin['shout'] = item.get('shout', np.nan)
            rows.append(checkin)
        except:
            print "error: ", checkin
       
df_full = pd.DataFrame(rows)

# convert unix timestamp to date and time, then drop the timestamp column
df_full['datetime'] = df_full['created_at'].map(lambda x: dt.fromtimestamp(x).strftime('%d/%m/%Y %H:%M'))
df_full = df_full.drop('created_at', axis=1)

#Ordeno las columnas del dataframe
df_full = df_full[['datetime', 'venue_name', 'shout', 'category', 'city', 'state', 'country', 'gmap']]

writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
                        
df_full.to_csv(csv_file, index=False, encoding='utf-8', sep=",")
df_full.to_excel(writer,sheet_name='todos',index=False, encoding='utf-8')

# remove multiple check-ins at the same location
df_unique = df_full.drop_duplicates(subset=['venue_name',], keep='last').copy()
df_unique.to_excel(writer,sheet_name='unicos',index=False, encoding='utf-8')

writer.save()

# gauth = GoogleAuth()
# gauth.LocalWebserverAuth()
# drive = GoogleDrive(gauth)
# fileg = drive.CreateFile()
# fileg.SetContentFile(excel_file)
# fileg.Upload() # Upload the file.
# print('title: %s, mimeType: %s' % (fileg['title'], fileg['mimeType']))

