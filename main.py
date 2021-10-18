from classes.Excel import Excel
from classes.Song import Song
from classes.Spotify import Spotify
from classes.Parser import Parser
from sys import argv
from os import listdir

if len(argv) < 2:
    files = listdir('.')
    candidate = ''
    for file in files:
        if file.__contains__('.xlsx'):
            candidate = file

    if candidate != '':
        print(f"You didn't specify any xlsx file, do you want to open {candidate}?")
    else:
        print("You didn't specify any file, usage= python main.py <excel file>")

p = Parser(argv[1])
songs = p.get_songs()
artists = p.get_artists()
songs_data = []
#pprint(songs)

for (song,artist) in zip(songs,artists):
    sp = Spotify(song)  
    release_date = sp.get_album_release_date()
    _artist = artist if isinstance(artist,str) else sp.get_artist_name()
    print(_artist,song,release_date)
    if release_date and _artist:
        songs_data.append(Song(song,_artist,release_date))
    else:
        songs_data.append(Song('Couldnt','Find',song))


e = Excel('dump.xlsx')
e.insert_songs(songs_data)



    