import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20190908',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')


musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')


#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis

#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis

#tr_1 = trs[0].select_one('td.info > a.title.ellipsis')

rank = 1
for music in musics:
    a = music.select_one('td.info > a.title.ellipsis')
    if not a == None:
        title = a.text
        singer = music.select_one('td.info > a.artist.ellipsis').text
        print(rank, title.strip(), '-', singer)
        rank =rank + 1