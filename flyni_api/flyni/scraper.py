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
                line = item.find('td').getText().encode('utf-8').strip()
                fly_number = int(item.find('td').next_sibling.next_sibling.getText())
                origin = item.find('td').next_sibling.next_sibling.next_sibling.next_sibling.getText().encode('utf-8').strip()
                string_hour = item.find('td').next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.getText().encode('utf-8').strip()
                
                try:
                    hour = time.strptime(string_hour, '%I:%M %p')
                except:
                    hour = time.strptime(string_hour, '%H:%M %p')

                status = item.find('td').next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.getText().encode('utf-8').strip()

                print '-----------'*5
                print line, fly_number, origin, hour, status


        else:
            print "Status Code %d" % req.status_code



