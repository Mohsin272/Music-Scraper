import requests
from bs4 import BeautifulSoup
import pandas as pd

#Getting HTML
url='https://www.billboard.com/charts/hot-100'
response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')

song_name=[]
artist=[]
position=[]

#Getting DATA
song_data=soup.findAll('li',attrs={'class':'chart-list__element display--flex'})

for i in song_data:
    name=i.find('span',class_='chart-element__information__song text--truncate color--primary').text.replace('\n','')
    song_name.append(name)

    song_artist=i.find('span',class_='chart-element__information__artist text--truncate color--secondary').text.replace('\n','')
    artist.append(song_artist)

    pos=i.find('span',class_='chart-element__rank__number').text.replace('\n','')
    position.append(pos)

SongDF=pd.DataFrame({'Title':song_name,'Artist':artist,'Position':position})
SongDF.to_csv('C:/Users/Mohsin Tahir/Desktop/Scraping Python/Music Scrape/Top 100 music charts.csv',index=False,encoding='UTF-8')


