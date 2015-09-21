# -*- coding: utf-8 -*-
import time
from bs4 import BeautifulSoup
import requests

class Scrap(object):

    def __init__(self, url):
        self.url = url
        self.run_scrap()

    def run_scrap(self):
        req = requests.get(self.url)
        if req.status_code == 200:

            html = BeautifulSoup(req.text, 'lxml')
            elements = html.find_all('tr',{'class':'listado'})

            for item in elements:
                cols = item.find_all('td', recursive=False)  # direct children

                line = cols[0].getText('', strip=True).encode('utf-8')
                fly_number = int(cols[1].getText('', strip=True))
                origin = cols[2].getText('', strip=True).encode('utf-8')
                string_hour = cols[3].getText('', strip=True).encode('utf-8')
                try:
                    hour = time.strptime(string_hour, '%I:%M %p')
                except:
                    hour = time.strptime(string_hour, '%H:%M %p')

                status = cols[4].getText('', strip=True).encode('utf-8')

                print '-----------'*5
                print line, fly_number, origin, hour, status


        else:
            print "Status Code %d" % req.status_code
