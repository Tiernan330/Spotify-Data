from SQL_Server.ServerConnect import ConnectServer, Insert
from SpotifyToken.RefreshToken import call_refresh
from SpotifyToken.SpotifyInfo import TrackInfo
from SQL_Server.Tools.Tools import currentDate, currentTime
import requests
import time

'''
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Running this file connects to the Microsoft SQL Server and the Spotify API to get data from Spotify to insert into a Table
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

 
cnxn = ConnectServer()
print("connected to server")
AccessToken = call_refresh()
CurrentTrack_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
get_current_track = TrackInfo()
current_track_id = None
Timer = 3550

def TrackPlaying(access_token):
    response = requests.get(CurrentTrack_URL, headers={"Authorization": f"Bearer {access_token}"})
    json_resp = response.json()
    is_Playing = json_resp['is_playing']
    return is_Playing

while True:
    if Timer == 0:
        Timer = 3500
        print("Refreshing Token")
        AccessToken = call_refresh()

    previousSong = current_track_id
    get_current_track.setToken(AccessToken)
    try:
        current_track_info = get_current_track.getInfo()
    except KeyError:
        Timer = 3550
        AccessToken = call_refresh()
        print("\nKeyError Refresh\n")
        get_current_track.setToken(AccessToken)
        current_track_info = get_current_track.getInfo()


    if current_track_info['id'] != current_track_id and TrackPlaying(AccessToken) is True:
        if current_track_info['id'] != "error":
            current_track_id = current_track_info['id']
            print('Playing: ' + current_track_info['name'])
            Date = currentDate()
            Time = currentTime()
            values = [current_track_info['id'], current_track_info['name'], current_track_info['ArtistID'],
                    current_track_info['artists'], current_track_info['AlbumID'], current_track_info['AlbumName'],
                    current_track_info['album art'], current_track_info['length'], Date,
                    Time, current_track_info['pop']]
            Insert(cnxn, values)
    
    Timer -= 1
    time.sleep(1)


