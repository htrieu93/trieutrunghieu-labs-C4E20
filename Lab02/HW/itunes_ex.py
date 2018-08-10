from urllib.request import urlopen
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL
import pyexcel


#Part 1:
url = "https://www.apple.com/itunes/charts/songs/"

# Running once to open and read url
conn = urlopen(url)

content =  conn.read().decode('utf-8')

soup = BeautifulSoup(content, 'html.parser')

div_list = soup.find_all(name = 'div', attrs= {'section-content'})

ul = div_list[1].ul
song_list = ul.find_all('li')

song_dic = []

for song in song_list:
    name = song.h3.a.string
    artist = song.h4.a.string
    dic = {}
    dic['name'] = name
    dic['artist'] = artist
    song_dic.append(dic)

pyexcel.save_as(records = song_dic, dest_file_name = 'List_of_songs.xlsx')

#Part 2:

for song in song_dic:
    options = {
    'format' : 'bestaudio/audio',
    'default_search' : 'ytsearch',
    'max_downloads' : 1
}

    dl = YoutubeDL(options)
    dl.download([song['name'] + ' ' + song['artist']])

