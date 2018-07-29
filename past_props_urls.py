# this file scrapes the data from all past auctions/sales on the building Detroit website

import os
import requests
import csv
from BeautifulSoup import BeautifulSoup

# https://buildingdetroit.org/properties/pastlistings?location=&listingtype=list&category=&district=&bedrooms=&bathrooms=&minsqft=&maxsqft=&fromsaledate=&tosaledate=&page=
# 151 pages as of 7/26

# Step 1. build a list with all of the property urls

cwd = os.getcwd()
pathName = os.path.join(cwd, "DLBA_Auctions_Closed.csv")

property_list = []

page = 1
while page <= 151:
    # Progress tracking
    print "Scraping " + "Page" + " " + str(page)

    # Set up URL pattern
    base_url = 'https://buildingdetroit.org/properties/'
    mid_url = 'pastlistings?location=&listingtype=list&category=&district=&bedrooms=&bathrooms=&minsqft=&maxsqft='
    url = base_url + mid_url + '&fromsaledate=&tosaledate=&page={}'.format(page)
    print(url)
    page = page + 1

    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    text = soup.findAll(type="text/javascript")[20].string
    text = text.split('[',1)[1]
    parsed_text = text.split('},')
    s_count = 1
    prop_count = len(parsed_text)
    props = []
    for s in parsed_text:
        if s_count <len(parsed_text):
            s_list = str(s.split(':'))
            s_list = s_list.split(",")
            #print "Prop " + str(s_count) + ". " + str(s_list)
            address = str(s_list[1]).strip()
            #print(address)
            identifier = str(s_list[27]).strip()
            pid = str(s_list[3]).strip()
            url1 = "buildingdetroit.org/properties/" + identifier + "-" + pid
            url2 = "buildingdetroit.org/properties/" + identifier
            line = address + ", " + identifier + ", " + pid + ", " + url1 + ", " + url2
            line = line.replace('"', '')
            line = line.replace('u\'', '')
            props.append(line)
            s_count = s_count + 1
    # Split list into matrix
    for row in props:
        splitRow = row.split(', ')
        property_list.append(splitRow)


with open('./detroit_pastlistings.csv', 'wb') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Address", "Identifier", "PID", "URL1", "URL2"])
    writer.writerows(property_list)

# step 2. crawl through list to extract data
# use the list of URLs collected in step 1 - try URL1, if doesn't exist, try URL2


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