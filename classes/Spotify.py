import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv('./.env')
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

class Spotify:
    def __init__(self,song_name : str) -> None:
        self.song_name = song_name
        self.search = sp.search(song_name)
        self.__items = self.search['tracks']['items']

    def get_artist_name (self):
        try:
            items = self.__items[0]
        except IndexError:
            print(f"Couldn't find {self.song_name}")
            return None
        for item in items['artists']:
            return item['name']


    def get_album_release_date (self):
        try:
            items = self.__items[0]
        except IndexError:
            print(f"Couldn't find {self.song_name}")
            return None
        release_date : str =  items['album']['release_date']
        year = int(release_date.split('-')[0])
        div = divmod(year,100)
        century = div[0]
        decade = div[1]
        if century == 19:
            return str(decade)[0] + '0'
        elif century == 20:
            return str(century) + str(decade)[0] + '0'
        else:
            return 'Too fucking old'
