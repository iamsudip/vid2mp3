#!/usr/bin/env python
'''
Commandline tool to download youtube flash videos as mp3.
It communicates with listentoyoutube.com for this purpose.
Vimeo.com, dailymotion.com, metacafe.com are also supported by this tool.
'''

import requests
import sys, os
from bs4 import BeautifulSoup
import time

def copyfileobj(fsrc, fdst, size, length=16*1024):
    """copy data from file-like object fsrc to file-like object fdst"""
    while True:
        buf = fsrc.read(length)
        if not buf:
            break
        fdst.write(buf)
#        sys.exit(0)

def download(data):
    try:
        with open("%s" %data[1], "wb") as fobj:
            print "File size: " + data[2]
            response = requests.get(data[0], stream=True)
            copyfileobj(response.raw, fobj, response.headers.get("content-length"))
    except IOError:
        data[1] = "Rename_manually.mp3"
        download(data)

def process_url(s_url, sleep_time = 10):
    try:
        s_url_soup = BeautifulSoup(requests.get(s_url).text, "xml")
        data = [str(s_url_soup.downloadurl.contents[0]),
            str(s_url_soup.file.contents[0]),
            str(s_url_soup.filesize.contents[0])
        ]
        if not data[0]:
            raise AttributeError
        print "Downloading: %s" % data[1]
        print "Fetching data from: %s" % data[0]
        return data
    except AttributeError:
        time.sleep(sleep_time)
        sleep_time += 10
        process_url(s_url, sleep_time)

def make_url(url):
    response = requests.post("http://www.listentoyoutube.com/cc/conversioncloud.php", data={"mediaurl": url})
    s_url = eval(response.text)['statusurl'].replace('\/', '/')
    data = process_url(s_url)
    download(data)

if __name__ == '__main__':
    make_url(sys.argv[1])

# http://www.listentoyoutube.com/process.php?url=http://www.youtube.com/watch?v=abcdef
