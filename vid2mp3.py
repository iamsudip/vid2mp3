#!/usr/bin/env python
'''
Commandline tool to download youtube flash videos as mp3.
It communicates with listentoyoutube.com for this purpose.
Vimeo.com, dailymotion.com, metacafe.com are also supported by this tool.
'''

import requests
import sys
from bs4 import BeautifulSoup
import time

sleep_time = 0

def abc(s_url):
    try:
        s_url_soup = BeautifulSoup(requests.get(s_url).text, "xml")
        data = { "url" : str(s_url_soup.downloadurl.contents[0]),
            "name" : str(s_url_soup.file.contents[0]),
            "size" : str(s_url_soup.filesize.contents[0])
        }
        return data
    except AttributeError:
        sleep_time += 10
        time.sleep(sleep_time)
        abc(s_url)

def copyfileobj(fsrc, fdst, length=16*1024):
    """copy data from file-like object fsrc to file-like object fdst"""
    while 1:
        buf = fsrc.read(length)
        if not buf:
            break
        fdst.write(buf)

def process_url(url):
    response = requests.post("http://www.listentoyoutube.com/cc/conversioncloud.php", data={"mediaurl": url})
    s_url = eval(response.text)['statusurl'].replace('\/', '/')
    download(abc(s_url))

def download(data):
    try:
        with open("%s" %data["name"], "wb") as fobj:
            print "Downloading: %s" % data["name"]
            print "File size: " + data["size"]
            response = requests.get(data["url"], stream=True)
            copyfileobj(response.raw, fobj)
    except IOError:
        data["name"] = "Rename_manually.mp3"
        download(data)

if __name__ == '__main__':
    data = process_url(sys.argv[1])
    download(data)
