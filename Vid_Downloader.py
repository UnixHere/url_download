import requests
import m3u8
import subprocess
import time
import random
import tkinter as tk
from tkinter import filedialog

proxies = {
    "http": "http://121.136.189.231:60001",
    "https": "http://121.136.189.231:60001",
}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0'}
user_agents =[
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15']
headers = {'User-Agent': random.choice(user_agents)}
def open_m3u8():
    root = tk.Tk()

    return filedialog.askopenfilename(title="Select a file", filetypes=[("M3U8 Files", "*.m3u8"), ("All Files", "*.*")])
def download_from_m3u8(master):
    playlist_url = master.data['playlists'][0]['uri'] #certain video segments file
    r = requests.get(playlist_url,headers=headers)
    playlist = m3u8.loads(r.text)
    file_name = input(f"Video Name(format 'name.ts'): ")
    with open(file_name, 'wb') as f:
        for segment in playlist.data['segments']:
            print(segment['uri'])
            url = segment['uri']
            r = requests.get("https://n11.stv.livebox.sk" + url, headers=headers) # GOTTA CHANGE MAIN URL BEFORE USE
            f.write(r.content)
            #time.sleep(1)
    print('finished')
while True:
    a =input(f"this is a file downloader using m3u8 files mainly this is made for rtvs archiv web\nSelect m3u8 file F open directory U paste url(F/U): ")
    if a.lower() == 'f':
        m3u8_master_file_path = open_m3u8()
        print(m3u8_master_file_path)
        with open(m3u8_master_file_path, "r") as f:
            content = f.read()
        m3u8_master = m3u8.loads(content)
        print(m3u8_master)
        download_from_m3u8(m3u8_master)
    elif a.lower() == 'u':
        url = input(f"url: ")
        r = requests.get(url,headers=headers)
        m3u8_master = m3u8.loads(r.text)
        download_from_m3u8(m3u8_master)
    else:
        print('Wrong Input')
        continue
    a = input(f" Do you want to continue?(y/n)")
    if a.lower() == 'y':
        continue
    elif a.lower() == 'n':
        break
