# this file scrapes the data from all past auctions/sales on the building Detroit website

import csv
import requests
import json
from BeautifulSoup import BeautifulSoup

page = 1
while page <=141: #141 total pages as of 5/23
    url = 'https://buildingdetroit.org/properties/pastlistings?location=&listingtype=list&category=&district=&bedrooms=&bathrooms=&minsqft=&maxsqft=&fromsaledate=&tosaledate=&page={}'.format(page)
    page = page + 1
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html)
    dataset = soup.find('script', attrs={'class': 'left resultscontainer'})


