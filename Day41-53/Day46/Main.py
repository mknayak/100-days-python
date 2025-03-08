import json
import os

import requests
import bs4 as bs
import base64
import datetime

user_input = input("which year do you want to travel to? type the date in this format yyyy-mm-dd:")
URL="https://www.billboard.com/charts/hot-100"

def get_song_list():
    song_list = []
    content=requests.get(f"{URL}/{user_input}/", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}).text
    webdata= bs.BeautifulSoup(content, "html.parser")
    song_divs= webdata.find_all("div", {"class":"o-chart-results-list-row-container"})
    for song_div in song_divs:
        song = song_div.select_one("li.lrv-u-width-100p ul li.o-chart-results-list__item")
        title= song.select_one("h3").text
        album= song.select_one("span").text
        song_list.append({"title":title.strip(), "album":album.strip()})
    return song_list

#print(get_song_list())

def create_spotify_playlist():
    client_id="183aa24d22e744c0819ebb89e0f5736e"
    client_secret="24df953508c745a99997d6ab123f91fa"
    api="https://api.spotify.com"
    auth_token=try_get_authtoken(client_id,client_secret)
    print(auth_token)

def try_get_authtoken(client_id, client_secret):
    file_name="client_credentials.json"
    access_token_data=""
    get_new_token=False
    if os.path.isfile(file_name):
        with open(file_name, "r") as f:
            client_credentials = json.load(f)
            if client_credentials["expiry"]-datetime.timedelta(minutes=5) < datetime.datetime.now() :
                get_new_token=True
            else:
                access_token_data= client_credentials["access_token"]
    else:
        get_new_token=True
    if get_new_token:
        auth_token = create_spotify_token(client_id, client_secret)
        access_token_data = auth_token["access_token"]
        expiry = datetime.datetime.now() + datetime.timedelta(seconds=auth_token["expires_in"])
        with open(file_name, "w") as f2:
            content_to_write="{'access_token':'"+access_token_data+"','expiry':'"+expiry.strftime("%m/%d/%Y, %H:%M:%S")+"'}"
            f2.write(content_to_write)
    return access_token_data

def create_spotify_token(client_id, client_secret):
    api="https://api.spotify.com"
    auth_token=base64.b64encode(f"{client_id}:{client_secret}".encode("utf-8")).decode("utf-8")
    clinet_credential= requests.post("https://accounts.spotify.com/api/token", headers={
        "Authorization": f"Basic {auth_token}"
    }, data={"grant_type": "client_credentials"}).json()
    return clinet_credential

create_spotify_playlist()