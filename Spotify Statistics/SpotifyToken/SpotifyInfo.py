import requests

'''
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This file contains a class to be used to get a JSON file from the Spotify API that gives information of the current song playing in my spotify
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

Error = \
    {
        "id": "error",
        "name": "error",
        "ArtistID": "error",
        "artists": "error",
        "AlbumID": "error",
        "AlbumName": "error",
        "album art": "error",
        "length": "error",
        "pop": "error",
        "link": "error"
    }

class TrackInfo:
    def __init__(self):
        self.token = None
        self.Spotify_Get_Playback_State = 'https://api.spotify.com/v1/me/player'

    def setToken(self, x):
        self.token = x

    def getToken(self):
        return self.token

    def getPS(self):
        return self.Spotify_Get_Playback_State


    def getInfo(self):
        Spotify_Get_Playback_State = self.getPS()

        Spotify_Access_Token = self.getToken()

        response = requests.get(Spotify_Get_Playback_State,
                            headers={"Content-Type": "application/json",
                                     "Authorization": "Bearer {}".format(Spotify_Access_Token)})
        try:
            json_resp = response.json()
        except ValueError:
            print("\n Value Error!\n")
            return Error

        try:
            track_id = json_resp['item']['id']
        except KeyError:
            print("\n Value Error!\n")
            return Error
        track_name = json_resp['item']['name']
        artists = [artist for artist in json_resp['item']['artists']]
        artists_ID = ', '.join([artist['id'] for artist in artists])
        artists_names = ', '.join([artist['name'] for artist in artists])
        Album_ID = json_resp['item']['album']['id']
        AlbumName = json_resp['item']['album']['name']
        get_art = [image for image in json_resp['item']['album']['images'][0]['url']]
        art = ''.join([str(item) for item in get_art])
        length = json_resp["item"]["duration_ms"]
        popularity = json_resp["item"]["popularity"]
        link = json_resp['item']['external_urls']['spotify']

        current_track_info = \
            {
                "id": track_id,
                "name": track_name,
                "ArtistID": artists_ID,
                "artists": artists_names,
                "AlbumID": Album_ID,
                "AlbumName": AlbumName,
                "album art": art,
                "length": length,
                "pop": popularity,
                "link": link
            }
        return current_track_info
