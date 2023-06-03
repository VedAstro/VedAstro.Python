#Generate Horoscope details by scraping astrosage and pass in person details to astroved API to generate planet attributes
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time

#segments = {'Businessman':4, 'Politician':1,'Cricket':1,'Hollywood':1, 'Bollywood':1, 'Musician':1, 'Literature':1, 'Sports':1, 'Criminal':1, 'Astrologer':1, 'Singer':1, 'Scientist':1, 'Football':1, 'Hockey':1}
segments = {'Businessman':1}

names_url = {}

for i in segments:
    names_href =[]
    for j in range(segments[i]):
        url = 'http://www.astrosage.com/celebrity-horoscope/default.asp?page='+str(j+1)+"&category="+str(i)
        print(url)
        response = requests.get(url)
        print(response)
        soup = BeautifulSoup(response.content,"html.parser")
        for row in soup.find_all(class_='ui-img-container'):
            names_href.append(row.a['href'])
        names_url[str(i)] = names_href

person_details_dict ={
    "Date of Birth":[],
    "Time of Birth": [],
    "Place of Birth": [],
    "Name":[],
    "Information Source":[],
    "Segment":[]
}

for l in names_url:
    for j in names_url[str(l)]:
        url="http://www.astrosage.com/celebrity-horoscope/"+str(j)
        response = requests.get(url)
        soup=BeautifulSoup(response.content,"html.parser")
        for row in soup.find_all(class_='celebcont', limit=8):
            try:
                person_details_dict[str(row.b.contents[0].strip(":"))].append(str(row.contents[2]).strip())
            except:
                continue
        person_details_dict['Segment'].append(str(l))

#Put this into a dataframe and write to csv
m = pd.DataFrame.from_dict(person_details_dict, orient='index')
m=m.transpose()
#Convert date to right format
m['Date of Birth'] = pd.to_datetime(m["Date of Birth"], format="%A, %B %d, %Y").dt.strftime('%d/%m/%Y') 
m.to_csv("horoscope.csv", index=False, encoding='utf-8')

#TODO: Send to API to get Planet Attributes
# horoscopeDict = m.to_dict()

# for k in horoscopeDict:

#     url = 'https://api.vedastro.org/Location/{0}}/Time/{1}}/{2}}/Planet/All'.format(horoscopeDict['Place of Birth'], horoscopeDict['Time of Birth'], horoscopeDict['Date of Birth'])
#     resp = requests.get(url)
#     if resp.status_code ==200:
#         data = resp.json()
#         data = data['Payload']
#         df = pd.json_normalize(data)
#         print(df)
#     df.to_csv("temp-"+k+".csv", index=None)
