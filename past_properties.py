# this file scrapes the data from all past auctions/sales on the building Detroit website

import os
import csv
from googlesearch import search
from urllib import urljoin
import requests
from BeautifulSoup import BeautifulSoup

# https://cse.google.com/cse/publicurl?cx=007401815838453618094:ek-abrltudo
# https://www.googleapis.com/customsearch/v1/siterestrict?[parameters]
# search engine ID : 007401815838453618094:ek-abrltudo

# https://buildingdetroit.org/properties/pastlistings?location=&listingtype=list&category=&district=&bedrooms=&bathrooms=&minsqft=&maxsqft=&fromsaledate=&tosaledate=&page=
# 151 pages as of 7/26

# Step 1. build a list with all of the property urls

cwd = os.getcwd()
pathName = os.path.join(cwd, "DLBA_Auctions_Closed.csv")

property_list = []

page = 1
while page <= 151:
    # Progress tracking
    print "Scraping " + " Page" + " " + str(page)

    # Set up URL pattern

    base_url = 'https://buildingdetroit.org/properties/'
    mid_url = 'pastlistings?location=&listingtype=list&category=&district=&bedrooms=&bathrooms=&minsqft=&maxsqft='
    url = urljoin(base_url, mid_url, '&fromsaledate=&tosaledate=&page={}'.format(page))
    print(url)

    response = requests.get(url)
    html = response.content

    # FIX STARTING HERE
    soup = BeautifulSoup(html)
    dataset = soup.find('div', attrs={'class': 'left resultscontainer'})
    page = page + 1

    for propName in dataset.findAll('div', attrs={'class': 'propName'}):
        name = str(propName.find('a').text.replace('&nbsp;', ''))  # type: str
        name = name.replace(' ,', "-,")
        name = name.replace('  ', ', ')
        name = name.replace('$', ', $')
        name = name.replace(' Acres', '')
        commaCount = 5 - name.count(', ')
        if commaCount > 0:
            name = name + (', '*commaCount)
        href = propName.find('a')['href']
        propId = href[-9:].replace('/','')
        propId = propId.replace('d','')
        name = name + ", " + href + ", " + propId

        with open('./detroit_pastlistings.csv', 'wb') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(["Size (Acres)", "City", "County", "State", "Price", "Notes", "Link", "Property ID"])
            writer.writerows(property_list)

# step 2. crawl through list to extract data
# use the list of URLs collected in step 1


"""
#old idea - google search each of the properties. issue was that i was sending too many queries and google got mad
full_doc = []
with open('DLBA_Auctions_Closed.csv', 'rb') as csvfile:
    csvfile = csv.reader(csvfile)
    for row in csvfile:
        property_list.append(row[0])
print(property_list)

row_count = -1
prop_list = iter(property_list)
next(prop_list)
for x in prop_list:
    query = x + " " + "buildingdetroit.org/properties"
    for j in search(query, tld='com', num=1,stop=1,pause=4):
        full_doc.append(x + j)
        print(x + j)
"""