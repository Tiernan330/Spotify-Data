import pyodbc
import pandas as pd

'''
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This file contains functions to work with the Microsoft SQL Server to slim down the amount of code in other folders
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''


def ConnectServer():
    SERVER = '' #Note: name deleted for personal use
    DATABASE = 'Spotify Statistics'
    return pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', host=SERVER, database=DATABASE, trusted_connection="yes")

def Insert(cnxn, values):
    cursor = cnxn.cursor()
    insert_query = '''INSERT INTO SpotifyStats (SongID, Song, ArtistID, Artist, AlbumID, Album, AlbumArt, Duration, Date, Time, Popularity)
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'''
    cursor.execute(insert_query, values)
    cnxn.commit()

def GetData(cnxn):
    insert_query = '''SELECT * FROM SpotifyStats'''
    results = pd.read_sql_query(insert_query, cnxn)
    results.to_csv("..\Spotify Statistics\SQL_Server\Data\stats.csv", index=False) 

cnxn = ConnectServer()
GetData(cnxn)





    
    



