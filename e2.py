#!/usr/bin/env python

import urllib.request
from bs4 import BeautifulSoup

for line in open('ELECTION_ID'):
    year, id = line.strip().split()
    url = \
        "http://historical.elections.virginia.gov/elections/download/%s/precincts_include:0/" \
        % id
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    with open("%s.csv" % year, "w+") as f:
        f.write(str(soup))
