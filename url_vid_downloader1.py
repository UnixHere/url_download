"""
This File Was used for testing new features might not work
"""

import requests
import m3u8
import subprocess
#import os
#dir_path = os.path.dirname(os.path.realpath(__file__))

import tkinter as tk
from tkinter import filedialog
def open_m3u8():
    root = tk.Tk()

    return filedialog.askopenfilename(title="Select a file", filetypes=[("M3U8 Files", "*.m3u8"), ("All Files", "*.*")])
def download_from_m3u8(master):
    playlist_url = master.data['playlists'][0]['uri'] #certain video segments file
    r = requests.get(playlist_url)
    playlist = m3u8.loads(r.text)
    file_name = input(f"Video Name(format 'name.ts'): ")
    with open(file_name, 'wb') as f:
        for segment in playlist.data['segments']:
            url = segment['uri']
            r = requests.get("https://n12.stv.livebox.sk" + url) 
            f.write(r.content)
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
        r = requests.get(url)
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
'''
root = tk.Tk()
root.withdraw() 
file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("M3U8 Files", "*.m3u8"), ("All Files", "*.*")])

# Print the selected file path
if file_path:
    print("You selected:", file_path)
else:
    print("No file selected")
"""
chunk_size = 256
url = "Enter Your url"
url = "Enter Your url""
r = requests.get(url, stream=True)
with open("cestou.mp4", "wb") as f:
    for chunk in r.iter_content(chunk_size=chunk_size):
        f.write(chunk)
"""

url = "Enter Your url"
r = requests.get(url)
print(r.text)

m3u8_master = m3u8.loads(r.text)
print('all\n',m3u8_master.data)
print('lists\n',m3u8_master.data['playlists'])
print('first\n',m3u8_master.data['playlists'][0])
print('url\n',m3u8_master.data['playlists'][0]['uri'])
playlist_url = m3u8_master.data['playlists'][0]['uri']

r = requests.get(playlist_url)
playlist = m3u8.loads(r.text)

print('all\n',playlist.data)
print('segments\n',playlist.data['segments'])
print('first\n',playlist.data['segments'][0])
print('url\n',playlist.data['segments'][0]['uri'])
r = requests.get(("domain url" + playlist.data['segments'][0]['uri']))

with open("video.ts", 'wb') as f:
    for segment in playlist.data['segments']:
        url = segment['uri']
        r = requests.get("domain url" + url) 
        f.write(r.content)

#subprocess.check_call(['ffmpeg', '-i', 'video.ts', 'video.mp4'], cwd=dir_path)       # you can use ffmpeg to convert .ts to .mp4 format
#subprocess.run(['ffmpeg', '-i', 'video.ts', 'video.mp4'])
print('finished')
'''
