#!/usr/bin/env python
'''
Commandline tool to download youtube flash videos as mp3.
It communicates with listentoyoutube.com for this purpose.
Vimeo.com, dailymotion.com, metacafe.com are also supported by this tool.
'''

import requests
import sys
from bs4 import BeautifulSoup
import shutil

def process_url(url):
    response = requests.post("http://www.listentoyoutube.com/cc/conversioncloud.php", data={"mediaurl": url})
    s_url = eval(response.text)['statusurl'].replace('\/', '/')
    s_url_soup = BeautifulSoup(requests.get(s_url).text, "xml")
    data = { "url" : str(s_url_soup.downloadurl.contents[0]),
        "name" : str(s_url_soup.file.contents[0]),
        "size" : str(s_url_soup.filesize.contents[0])
    }
    return data

def download(data):
    with open("%s" %data["name"], "wb") as fobj:
        print "Downloading: %s" % data["name"]
        print "File size: " + data["size"]
        response = requests.get(data["url"], stream=True)
        shutil.copytree(response.raw, fobj)

if __name__ == '__main__':
    data = process_url(sys.argv[1])
    download(data)
