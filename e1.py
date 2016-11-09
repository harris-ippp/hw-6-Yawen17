#!/usr/bin/env python

import urllib.request
from bs4 import BeautifulSoup

ELECTION_URL = \
    "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2015/office_id:1/stage:General"

page = urllib.request.urlopen(ELECTION_URL)
soup = BeautifulSoup(page, 'html.parser')
elections_ids = []
with open("ELECTION_ID", "w+") as f:
    for item in soup.find_all('tr', 'election_item'):
        _, _, id = item['id'].split('-')
        year = item.find('td', 'year first').string
        f.write("%s %s\n" % (year, id))

