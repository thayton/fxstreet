#!/usr/bin/env python

import re
import sys
import csv
import requests

from bs4 import BeautifulSoup
from datetime import datetime

class Scraper(object):
    def __init__(self):
        self.url = 'http://calendar.fxstreet.com/InterestRatesWidget/GetMain?culture=en-US&timezone=UTC'
        self.headers = {
            'Referer': 'http://www.fxstreet.com/economic-calendar/world-interest-rates/'
        }

    def scrape(self):
        r = requests.get(self.url, headers=self.headers)
        s = BeautifulSoup(r.text, 'html.parser')
        t = s.find('table', id='banksTable')

        writer = csv.writer(sys.stdout)

        def SQL_date_fmt(datestr):
            if not re.search(r'^\d+-\d+-\d+ ', datestr):
                return datestr

            x = datestr
            x = x.split(' - ')
            t = datetime.strptime(x[0], '%m-%d-%Y')
            x[0] = datetime.strftime(t, '%Y-%m-%d')

            return ' - '.join(x)
            
        for tr in t.tbody.findAll('tr'):
            td = [ '%s' % td.text for td in tr.findAll('td') ]

            # Chomp %
            x = td[1].split(' %')
            x = x[0]

            td[1] = x

            # Fix Next Meeting & Last Change dates to SQL format (YYYY-MM-DD)
            td[-2] = SQL_date_fmt(td[-2])
            td[-1] = SQL_date_fmt(td[-1])

            writer.writerow(td)


if __name__ == '__main__':
    scraper = Scraper()
    scraper.scrape()
